from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QLabel, QPushButton, QMessageBox, QComboBox, QLineEdit

class PleaComboBox(QComboBox):
    def __init__(self, parent = None):
        super().__init__()
        self.set_up_widget()

    def set_up_widget(self):
        self.setMinimumSize(QtCore.QSize(300, 0))
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setEditable(True)
        self.setObjectName("plea_choice_box")
        self.addItem("")
        self.addItem("Guilty")
        self.addItem("No Contest")
        self.addItem("Not Guilty")
        self.addItem("Dismissed")


class FindingComboBox(QComboBox):
    def __init__(self, parent = None):
        super().__init__()
        self.set_up_widget()

    def set_up_widget(self):
        self.setMinimumSize(QtCore.QSize(300, 0))
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setEditable(True)
        self.setObjectName("finding_choice_box")
        self.addItem("")
        self.addItem("Guilty")
        self.addItem("Not Guilty")
        self.addItem("Dismissed")
        self.addItem("Guilty - Allied Offense")
        self.addItem("Not Guilty - Allied Offense")
