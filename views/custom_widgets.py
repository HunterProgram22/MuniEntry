from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QLabel, QPushButton, QMessageBox, QComboBox, QLineEdit

class PleaComboBox(QComboBox):
    def __init__(self, parent=None):
        super(QComboBox, self).__init__(parent)
        self.set_up_widget()

    def set_up_widget(self):
        self.setMinimumSize(QtCore.QSize(300, 0))
        self.setMaximumSize(QtCore.QSize(300, 50))
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setEditable(True)
        self.setObjectName("plea_choice_box")
        self.addItem("")
        self.addItem("Guilty")
        self.addItem("No Contest")
        self.addItem("Not Guilty")
        self.addItem("Dismissed")

    def currentText(self):
        print("this method works")


class FindingComboBox(QComboBox):
    def __init__(self, parent=None):
        super(QComboBox, self).__init__(parent)
        self.set_up_widget()

    def set_up_widget(self):
        self.setMinimumSize(QtCore.QSize(300, 0))
        self.setMaximumSize(QtCore.QSize(300, 50))
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setEditable(True)
        self.setObjectName("finding_choice_box")
        self.addItem("")
        self.addItem("Guilty")
        self.addItem("Not Guilty")
        self.addItem("Dismissed")
        self.addItem("Guilty - Allied Offense")
        self.addItem("Not Guilty - Allied Offense")

class FineLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super(QLineEdit, self).__init__(parent)
        self.set_up_widget()

    def set_up_widget(self):
        self.setMinimumSize(QtCore.QSize(300, 0))
        self.setMaximumSize(QtCore.QSize(300, 50))
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setObjectName("fines_amount")

class FineSuspendedLineEdit(FineLineEdit):
    def __init__(self, parent=None):
        super(FineLineEdit, self).__init__(parent)
        self.setObjectName("fines_suspended")
