import sys
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot

from main_window_ui import Ui_MainWindow
from DialogModels import (
    MotionEntryDialog, JuryInstructionsDialog, TransferEntryDialog,
    VerdictFormDialog, YellowFormDialog, ExtraditionEntryDialog, OviEntryDialog,
    )

#Code to update UI
#pyuic5 -o main_window_ui.py ui/MainWndow.ui




class Window(QMainWindow, Ui_MainWindow):
    DIALOG_DICT = {
        "TransferEntryDialog":TransferEntryDialog,
        "JuryInstructionsDialog":JuryInstructionsDialog,
        "MotionEntryDialog":MotionEntryDialog,
        "VerdictFormDialog":VerdictFormDialog,
        "YellowFormDialog":YellowFormDialog,
        "ExtraditionEntryDialog":ExtraditionEntryDialog,
        "OviEntryDialog":OviEntryDialog,
        }

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        pass

    def pushButtonDialog(self):
        sending_button = self.sender()
        dialog = Window.DIALOG_DICT[sending_button.objectName()]()
        dialog.exec()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
