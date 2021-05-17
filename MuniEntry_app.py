import sys
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot

from main_window_ui import Ui_MainWindow
from DialogModels import OmnibusMotionDialog, JuryInstructionsDialog

#Code to update UI
#pyuic5 -o main_window_ui.py ui/main_window.ui

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.actionOmnibus_Motion_Form.triggered.connect(self.OmnibusMotionForm)
        self.actionJury_Instructions.triggered.connect(self.JuryInstructionsForm)

    def OmnibusMotionForm(self):
        dialog = OmnibusMotionDialog(self)
        dialog.exec()

    def JuryInstructionsForm(self):
        dialog = JuryInstructionsDialog(self)
        dialog.exec()

    def pushButtonJury(self):
        dialog = JuryInstructionsDialog(self)
        dialog.exec()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
