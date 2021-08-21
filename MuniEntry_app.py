import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSlot

from views.main_window_ui import Ui_MainWindow
from controllers.CriminalDialogs import CaseInformationDialog
from controllers.NoJailTrafficDialogs import TrafficCaseInformationDialog


class Window(QMainWindow, Ui_MainWindow):
    DIALOG_DICT = {
        "FinalJudgmentEntryButton": CaseInformationDialog,
        "MinorMisdemeanorTrafficButton": TrafficCaseInformationDialog,
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
