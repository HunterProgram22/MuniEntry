"""Module containing custom widget Message Boxes.

If using QtDesigner for creation of the Ui file you must promote the widget to one of the custom
widgets that is used. The header file for this module must then be added in QtDesigner so that
when the file is converted using 'pyuic6 -o {python_view_file.py} {qt_ui_file.ui}' this
module will be imported as part of the python_view_file.py.
"""
from loguru import logger
from PyQt6 import QtGui
from PyQt6.QtWidgets import QMessageBox, QPushButton

from munientry.settings import GAVEL_PATH

FAIL = 'Fail'
PASS = 'Pass'
BLANK = ''


class RequiredBox(QMessageBox):
    """Custom QMessageBox used when a hard stop of the application is required.

    Provides user with the required information that is missing and returns control back to
    the UI after okay is clicked, but stops the process that was running.
    """

    def __init__(self, message, title='Required', parent=None):
        super().__init__(parent)
        self.message = message
        self.title = title
        self.set_up_widget()
        logger.required(self.title)

    def set_up_widget(self):
        self.setWindowIcon(QtGui.QIcon(GAVEL_PATH))
        self.setIcon(QMessageBox.Icon.Critical)
        self.setWindowTitle(self.title)
        self.setText(self.message)
        self.setStandardButtons(QMessageBox.StandardButton.Ok)


class InfoBox(QMessageBox):
    """Custom QMessage box used when information is needed to be provided to the user.

    Provides user with the information and then returns control back to the UI but continues
    with the process.
    """

    def __init__(self, message=None, title=None, parent=None):
        super().__init__(parent)
        self.message = message
        self.title = title
        self.set_up_widget()
        logger.info(self.title)

    def set_up_widget(self):
        self.setWindowIcon(QtGui.QIcon(GAVEL_PATH))
        self.setIcon(QMessageBox.Icon.Information)
        self.setWindowTitle(self.title)
        self.setText(self.message)
        self.setStandardButtons(QMessageBox.StandardButton.Ok)


class WarningBox(QMessageBox):
    """Custom QMessage box used when the user may choose whether to continue based on the info.

    Provides user with the information and returns control back to the UI. If the user chooses
    Yes the process continues running, if the user chooses No it stops the current process.
    """

    def __init__(self, message, title='Warning', parent=None):
        super().__init__(parent)
        self.message = message
        self.title = title
        self.set_up_widget()
        logger.choice(self.title)

    def set_up_widget(self):
        self.setWindowIcon(QtGui.QIcon(GAVEL_PATH))
        self.setIcon(QMessageBox.Icon.Warning)
        self.setWindowTitle(self.title)
        self.setText(self.message)
        self.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)


class TwoChoiceQuestionBox(QMessageBox):
    """Custom QMessage box used for providing two custom labeled choices for the user to choose.

    Provides user with the information and then uses a YesRole and NoRole Button. Control is
    returned to the UI and the process continues. Information in the view is changed based on the
    response of YesRole or NoRole.
    """

    def __init__(self, message, yes_choice, no_choice, title='Information Required', parent=None):
        super().__init__(parent)
        self.message = message
        self.title = title
        self.set_up_widget(yes_choice, no_choice)
        logger.choice(self.title)

    def set_up_widget(self, yes_choice, no_choice):
        self.setWindowIcon(QtGui.QIcon(GAVEL_PATH))
        self.setIcon(QMessageBox.Icon.Question)
        self.setWindowTitle(self.title)
        self.setText(self.message)
        self.addButton(QPushButton(yes_choice), QMessageBox.ButtonRole.YesRole)  # YesRole returns 5
        self.addButton(QPushButton(no_choice), QMessageBox.ButtonRole.NoRole)  # NoRole returns 6


class JailWarningBox(QMessageBox):
    """Custom QMessageBox used specifically to provide a warning about setting jail report date.

    Provides user with information about whether a report date should be set based on calculation
    of jail days set and jail time credit. The calculation is done elsewhere. The message box
    will set the report date checkbox and continue, or not set the checkbox and continue based
    on the user response.

    TODO: Cancel button acts like a 'No' response but should stop the process.
    """

    def __init__(self, message, title='Jail Warning', parent=None):
        super().__init__(parent)
        self.message = message
        self.title = title
        self.set_up_widget()
        logger.choice(self.title)

    def set_up_widget(self):
        self.setWindowIcon(QtGui.QIcon(GAVEL_PATH))
        self.setIcon(QMessageBox.Icon.Warning)
        self.setWindowTitle(self.title)
        self.setText(self.message)
        self.setStandardButtons(
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No
            | QMessageBox.StandardButton.Cancel,
        )
