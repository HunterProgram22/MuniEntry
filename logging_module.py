import sys
import traceback

from loguru import logger
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox

from settings import LOG_NAME, ICON_PATH

fmt = '{time:YYYY-MM-DD HH:mm:ss:SSS} | {level: <10} | {message: <75} | {function}:{name}:{line}'
logger.add(f'./resources/logs/{LOG_NAME}', format=fmt)
logger.level('IMPORT', no=18, color='<white>')
logger.level('DIALOG', no=22, color='<green>')
logger.level('BUTTON', no=24, color='<cyan>')
logger.level('CHOICE', no=26, color='<cyan>')
logger.level('CHECKFAIL', no=27, color='<magenta>')
logger.level('REQUIRED', no=28, color='<magenta>')


class CriticalErrorBox(QMessageBox):
    def __init__(self, message=None, title='Critical Error', parent=None):
        super(QMessageBox, self).__init__(parent)
        self.message = message
        self.title = title
        self.set_up_widget()
        logger.critical(self.title)

    def set_up_widget(self):
        self.setWindowIcon(QtGui.QIcon(ICON_PATH + 'gavel.ico'))
        self.setIcon(QMessageBox.Critical)
        self.setWindowTitle(self.title)
        self.setText(self.message)
        self.setStandardButtons(QMessageBox.Ok)


def show_exception_box(log_msg):
    """Checks if a QApplication instance is available and shows a messagebox with the exception message.
    If unavailable (non-console application), log an additional notice.
    """
    if QtWidgets.QApplication.instance() is not None:
        errorbox = CriticalErrorBox()
        errorbox.setText(
            "An unexpected error occured. Please alert Justin as soon as possible."
            + " Depending on the error, you may continue to use the application by clicking"
            + " OK, but must choose an option other than the one the caused this error message."
            + " The error is:\n\n\n{0}".format(log_msg)
        )
        errorbox.exec_()
    else:
        logger.debug("No QApplication instance available.")


class UncaughtHook(QtCore.QObject):
    _exception_caught = QtCore.pyqtSignal(object)

    def __init__(self, *args, **kwargs):
        super(UncaughtHook, self).__init__(*args, **kwargs)

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
            log_msg = '\n'.join([''.join(traceback.format_tb(exc_traceback)),
                                 '{0}: {1}'.format(exc_type.__name__, exc_value)])
            logger.critical("Uncaught exception:\n {0}".format(log_msg), exc_info=exc_info)

            # trigger message box show
            self._exception_caught.emit(log_msg)


# create a global instance of our class to register the hook
qt_exception_hook = UncaughtHook()