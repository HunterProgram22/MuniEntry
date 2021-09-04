import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSlot

from views.main_window_ui import Ui_MainWindow
from controllers.CriminalDialogs import CaseInformationDialog
from controllers.MinorMisdemeanorDialogs import TrafficCaseInformationDialog


class Window(QMainWindow, Ui_MainWindow):
    DIALOG_DICT = {
        "GreenSheetButton": CaseInformationDialog,
        "MinorMisdemeanorTrafficButton": TrafficCaseInformationDialog,
    }

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.bunner_radioButton.setChecked(True)
        self.bunner_radioButton.clicked.connect(self.check_judicial_officer)
        self.pelanda_radioButton.clicked.connect(self.check_judicial_officer)
        self.rohrer_radioButton.clicked.connect(self.check_judicial_officer)
        self.hemmeter_radioButton.clicked.connect(self.check_judicial_officer)

    def check_judicial_officer(self):
        if self.bunner_radioButton.isChecked():
            self.judicial_officer = "Bunner"
        elif self.pelanda_radioButton.isChecked():
            self.judicial_officer = "Pelanda"
        elif self.rohrer_radioButton.isChecked():
            self.judicial_officer = "Rohrer"
        elif self.hemmeter_radioButton.isChecked():
            self.judicial_officer = "Hemmeter"

    def connectSignalsSlots(self):
        pass

    def pushButtonDialog(self):
        sending_button = self.sender()
        dialog = Window.DIALOG_DICT[sending_button.objectName()](self.judicial_officer)
        dialog.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
