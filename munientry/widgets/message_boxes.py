from PyQt6 import QtGui
from PyQt6.QtWidgets import QMessageBox, QPushButton
from loguru import logger
from munientry.settings import ICON_PATH

FAIL = 'Fail'
PASS = 'Pass'
BLANK = ''


class RequiredBox(QMessageBox):
    def __init__(self, message, title='Required', parent=None):
        super(QMessageBox, self).__init__(parent)
        self.message = message
        self.title = title
        self.set_up_widget()
        logger.required(self.title)

    def set_up_widget(self):
        self.setWindowIcon(QtGui.QIcon(ICON_PATH + 'gavel.ico'))
        self.setIcon(QMessageBox.Icon.Critical)
        self.setWindowTitle(self.title)
        self.setText(self.message)
        self.setStandardButtons(QMessageBox.StandardButton.Ok)


class InfoBox(QMessageBox):
    def __init__(self, message=None,title=None, parent=None):
        super(QMessageBox, self).__init__(parent)
        self.message = message
        self.title = title
        self.set_up_widget()
        logger.info(self.title)

    def set_up_widget(self):
        self.setWindowIcon(QtGui.QIcon(ICON_PATH + 'gavel.ico'))
        self.setIcon(QMessageBox.Icon.Information)
        self.setWindowTitle(self.title)
        self.setText(self.message)
        self.setStandardButtons(QMessageBox.StandardButton.Ok)


class WarningBox(QMessageBox):
    def __init__(self, message, title='Warning', parent=None):
        super(QMessageBox, self).__init__(parent)
        self.message = message
        self.title = title
        self.set_up_widget()
        logger.choice(self.title)

    def set_up_widget(self):
        self.setWindowIcon(QtGui.QIcon(ICON_PATH + 'gavel.ico'))
        self.setIcon(QMessageBox.Icon.Warning)
        self.setWindowTitle(self.title)
        self.setText(self.message)
        self.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)


class TwoChoiceQuestionBox(QMessageBox):
    def __init__(self, message, yes_choice, no_choice, title='Additional Information Required', parent=None):
        super(QMessageBox, self).__init__(parent)
        self.message = message
        self.title = title
        self.set_up_widget(yes_choice, no_choice)
        logger.choice(self.title)

    def set_up_widget(self, yes_choice, no_choice):
        self.setWindowIcon(QtGui.QIcon(ICON_PATH + 'gavel.ico'))
        self.setIcon(QMessageBox.Icon.Question)
        self.setWindowTitle(self.title)
        self.setText(self.message)
        self.addButton(QPushButton(yes_choice), QMessageBox.YesRole) # YesRole returns 5
        self.addButton(QPushButton(no_choice), QMessageBox.NoRole)  # NoRole returns 6


class JailWarningBox(QMessageBox):
    def __init__(self, message, title='Jail Warning', parent=None):
        super(QMessageBox, self).__init__(parent)
        self.message = message
        self.title = title
        self.set_up_widget()
        logger.choice(self.title)

    def set_up_widget(self):
        self.setWindowIcon(QtGui.QIcon(ICON_PATH + 'gavel.ico'))
        self.setIcon(QMessageBox.Icon.Warning)
        self.setWindowTitle(self.title)
        self.setText(self.message)
        self.setStandardButtons(QMessageBox.StandardButton.Yes |
                                QMessageBox.StandardButton.No |
                                QMessageBox.StandardButton.Cancel)