"""Module containting PyQt6 specific constants used throughout the application."""
from PyQt6.QtCore import QDate, QDateTime
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QMessageBox

MAX_JAIL_TIME_VALIDATOR = QIntValidator(0, 1000)
YES_BUTTON_RESPONSE = QMessageBox.StandardButton.Yes
NO_BUTTON_RESPONSE = QMessageBox.StandardButton.No
CANCEL_BUTTON_RESPONSE = QMessageBox.StandardButton.Cancel
