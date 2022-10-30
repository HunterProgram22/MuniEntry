"""Module for setting up logging for the application."""
import sys
import traceback
from datetime import datetime
from functools import partialmethod

from loguru import logger
from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import QApplication, QMessageBox

from munientry.paths import LOG_PATH, ICON_PATH
from munientry.settings import SOCKET_NAME


# Logging Settings
NOW = datetime.now()
NOW_STRING = NOW.strftime('%m_%d_%Y__%H_%M_%S')
LOG_TIME = f'{NOW_STRING}'

FULL_LOG_NAME = f'Full_Log_{SOCKET_NAME}_{LOG_TIME}.log'
USER_LOG_NAME = f'{SOCKET_NAME}_User_Log_{LOG_TIME}.log'

APP_LOGGING_LEVEL = 20

IMPORT_LOGLEVEL = 18
DATABASE_LOGLEVEL = 21
DIALOG_LOGLEVEL = 22
BUTTON_LOGLEVEL = 24
ACTION_LOGLEVEL = 25
CHOICE_LOGLEVEL = 26
CHECKFAIL_LOGLEVEL = 27
REQUIRED_LOGLEVEL = 28


class CriticalErrorBox(QMessageBox):
    """Catchall Message Box for showing any uncaught exceptions."""

    def __init__(self, message=None, title='Critical Error', parent=None):
        super().__init__(parent)
        self.message = message
        self.title = title
        self.set_up_widget()
        logger.critical(self.title)

    def set_up_widget(self):
        self.setWindowIcon(QtGui.QIcon(f'{ICON_PATH}gavel.ico'))
        self.setIcon(QMessageBox.Icon.Critical)
        self.setWindowTitle(self.title)
        self.setText(self.message)
        self.setStandardButtons(QMessageBox.StandardButton.Ok)


FMT = '{time:YYYY-MM-DD HH:mm:ss:SSS} | {level: <10} | {message: <75} | {function}:{name}:{line}'

logger.add(f'{LOG_PATH}{USER_LOG_NAME}', format=FMT, level=APP_LOGGING_LEVEL)

logger.level('IMPORT', no=IMPORT_LOGLEVEL, color='<white>')

logger.level('DATABASE', no=DATABASE_LOGLEVEL, color='<green>')
logger.__class__.database = partialmethod(logger.__class__.log, 'DATABASE')

logger.level('DIALOG', no=DIALOG_LOGLEVEL, color='<green>')
logger.__class__.dialog = partialmethod(logger.__class__.log, 'DIALOG')

logger.level('BUTTON', no=BUTTON_LOGLEVEL, color='<cyan>')
logger.__class__.button = partialmethod(logger.__class__.log, 'BUTTON')

logger.level('ACTION', no=ACTION_LOGLEVEL, color='<cyan>')
logger.__class__.action = partialmethod(logger.__class__.log, 'ACTION')

logger.level('CHOICE', no=CHOICE_LOGLEVEL, color='<cyan>')
logger.__class__.choice = partialmethod(logger.__class__.log, 'CHOICE')

logger.level('CHECKFAIL', no=CHECKFAIL_LOGLEVEL, color='<magenta>')
logger.__class__.checkfail = partialmethod(logger.__class__.log, 'CHECKFAIL')

logger.level('REQUIRED', no=REQUIRED_LOGLEVEL, color='<magenta>')
logger.__class__.required = partialmethod(logger.__class__.log, 'REQUIRED')


def show_exception_box(log_msg):
    """Checks if a QApplication instance is available and shows a messagebox with exception message.

    If unavailable (non-console application), log an additional notice.
    """
    if QApplication.instance() is not None:
        errorbox = CriticalErrorBox()
        errorbox.setText(
            'An unexpected error occured. Please alert Justin as soon as possible.'
            + ' Depending on the error, you may continue to use the application by clicking'
            + ' OK, but must choose an option other than the one the caused this error message.'
            + f' The error is:\n\n\n{log_msg}',
        )
        errorbox.exec()
    else:
        logger.debug('No QApplication instance available.')


class UncaughtHook(QtCore.QObject):
    """Catchall Class for any exceptions not specifically addressed in code.

    Source: https://timlehr.com/python-exception-hooks-with-qt-message-box/
    """

    _exception_caught = QtCore.pyqtSignal(object)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # this registers the exception_hook() function as hook with the Python interpreter
        sys.excepthook = self.exception_hook

        # connect signal to execute the message box function always on main thread
        self._exception_caught.connect(show_exception_box)

    def exception_hook(self, exc_type, exc_value, exc_traceback):
        """Function handling uncaught exceptions.

        It is triggered each time an uncaught exception occurs.
        """
        if issubclass(exc_type, KeyboardInterrupt):
            # ignore keyboard interrupt to support console applications
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
        else:
            exc_info = (exc_type, exc_value, exc_traceback)
            log_msg = '\n'.join(
                [
                    ''.join(traceback.format_tb(exc_traceback)),
                    f'{exc_type.__name__}: {exc_value}',
                ],
            )
            try:
                logger.critical(f'Uncaught exception:\n {log_msg}', exc_info=exc_info)
            except KeyError as error:
                logger.critical(error)

            # trigger message box show
            self._exception_caught.emit(log_msg)


# create a global instance of our class to register the hook
qt_exception_hook = UncaughtHook()
