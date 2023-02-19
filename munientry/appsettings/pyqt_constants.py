"""Module containting PyQt6 specific constants used throughout the application."""
from PyQt6.QtCore import QDate, QDateTime
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QMessageBox

from munientry.appsettings.paths import ICON_PATH

MAX_JAIL_TIME_VALIDATOR = QIntValidator(0, 1000)
TODAY = QDate.currentDate()
TIMENOW = QDateTime.currentDateTime()
YES_BUTTON_RESPONSE = QMessageBox.StandardButton.Yes
NO_BUTTON_RESPONSE = QMessageBox.StandardButton.No
CANCEL_BUTTON_RESPONSE = QMessageBox.StandardButton.Cancel
