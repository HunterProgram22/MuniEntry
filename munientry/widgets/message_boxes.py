"""Module containing custom widget Message Boxes."""
from loguru import logger
from PyQt6 import QtGui
from PyQt6.QtWidgets import QMessageBox, QPushButton

from munientry.settings.paths import GAVEL_PATH


class BaseBox(QMessageBox):
    """A Custom QMessageBox base class for interacting with the user."""

    def __init__(self, message, title=None, parent=None):
        super().__init__(parent)
        self.message = message
        self.title = title
        self.set_up_widget()
        logger.info(self.title)

    def set_up_widget(self):
        self.setWindowIcon(QtGui.QIcon(GAVEL_PATH))
        self.setIcon(QMessageBox.Icon.Critical)
        self.setWindowTitle(self.title)
        self.setText(self.message)
        self.set_buttons()


class RequiredBox(BaseBox):
    """Custom QMessageBox used when a hard stop of the application is required.

    Provides user with the required information that is missing and returns control back to
    the UI after okay is clicked, but stops the process that was running.
    """

    def set_buttons(self):
        self.setStandardButtons(QMessageBox.StandardButton.Ok)


class InfoBox(BaseBox):
    """Custom QMessage box used when information is needed to be provided to the user.

    Provides user with the information and then returns control back to the UI but continues
    with the process.
    """

    def set_buttons(self):
        self.setStandardButtons(QMessageBox.StandardButton.Ok)


class WarningBox(BaseBox):
    """Custom QMessage box used when the user may choose whether to continue based on the info.

    Provides user with the information and returns control back to the UI. If the user chooses
    Yes the process continues running, if the user chooses No it stops the current process.
    """

    def set_buttons(self):
        self.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)


class TwoChoiceQuestionBox(BaseBox):
    """Custom QMessage box used for providing two custom labeled choices for the user to choose.

    Provides user with the information and then uses a YesRole and NoRole Button. Control is
    returned to the UI and the process continues. Information in the view is changed based on the
    response of YesRole or NoRole.
    """

    def __init__(self, message, yes_choice, no_choice, title='Information Required', parent=None):
        super().__init__(parent)
        self.yes_choice = yes_choice
        self.no_choie = no_choice

    def set_buttons(self):
        self.addButton(QPushButton(self.yes_choice), QMessageBox.ButtonRole.YesRole)  # YesRole returns 5
        self.addButton(QPushButton(self.no_choice), QMessageBox.ButtonRole.NoRole)  # NoRole returns 6


class JailWarningBox(BaseBox):
    """Custom QMessageBox used specifically to provide a warning about setting jail report date.

    Provides user with information about whether a report date should be set based on calculation
    of jail days set and jail time credit. The calculation is done elsewhere. The message box
    will set the report date checkbox and continue, or not set the checkbox and continue based
    on the user response.
    """

    def set_buttons(self):
        self.setStandardButtons(
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No
            | QMessageBox.StandardButton.Cancel,
        )


class MinimumsQuestionBox(BaseBox):
    """Question box for setting OVI 1 minimums."""

    def set_buttons(self):
        self.min_dismiss_button = self.addButton('Yes - Dismiss Other Charges', QMessageBox.ButtonRole.ActionRole)
        self.min_no_dismiss_button = self.addButton('Yes - Do Not Dismiss Other Charges', QMessageBox.ButtonRole.ActionRole)
        self.no_mins_button = self.addButton('No', QMessageBox.ButtonRole.ActionRole)
