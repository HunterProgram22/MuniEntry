import sys
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot

from pyuifiles.main_window_ui import Ui_MainWindow
from Dialogs.CriminalDialogs import (
    OviDialog,
    SentencingDialog,
    FailureToAppearDialog,
    CaseInformationDialog,
)


# Code to update UI files to py files
# pyuic5 -o main_window_ui.py ui/MainWndow.ui


class Window(QMainWindow, Ui_MainWindow):
    DIALOG_DICT = {
        "FinalJudgmentEntryButton": CaseInformationDialog,
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
