import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5.QtCore import pyqtSlot

from views.main_window_ui import Ui_MainWindow
from controllers.MinorMisdemeanorDialogs import TrafficCaseInformationDialog

class Window(QMainWindow, Ui_MainWindow):
    """The MainWindow of the application loads the view that is created
    initially from QtDesigner. If changes to the view are made then the command
    'pyuic5 -o views/main_window_ui.py resources/ui/MainWindow.ui' must be
    run to update changes to the view.

    All slots and signals are connected after the view is created. Slots and signals
    can be linked in the view (using QtDesigner or directly in the view file after
    pyuic5 is run), however, connecting in MainWindow (class Window) is generally
    cleaner and allows ease of scalabilty.

    :judicial_officer_dict: - If a new judicial officer is added then
    they only need a radio button added to the view (key: self.lastname_radioButton,
    value: "Lastname").The button will be connected to the slot for self.judicial_officer by the function
    connect_judicial_officer_buttons.

    :dialog_dict: - If a new entry button is added to the view then a new key:value
    pair needs to be added to dialog_dict (key: buttonName, value: dialog-to-be-called).
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self) #The self argument that is called is MainWindow
        self.connect_signal_slots()
        self.judicial_officer_dict = {
            self.bunner_radioButton: "Bunner",
            self.pelanda_radioButton: "Pelanda",
            self.rohrer_radioButton: "Rohrer",
            self.hemmeter_radioButton: "Hemmeter",
        }
        self.dialog_dict = {
            self.MinorMisdemeanorTrafficButton: TrafficCaseInformationDialog,
            self.GreenSheetButton: TrafficCaseInformationDialog,
        }

        #Set View and Connect Signals
        self.bunner_radioButton.setChecked(True)
        self.judicial_officer = "Bunner"
        self.connect_judicial_officer_buttons()
        self.connect_entry_buttons()

    def connect_judicial_officer_buttons(self):
        for key in self.judicial_officer_dict:
            key.clicked.connect(self.check_judicial_officer)

    def check_judicial_officer(self):
        for key in self.judicial_officer_dict:
            if key.isChecked():
                self.judicial_officer = self.judicial_officer_dict[key]

    def connect_entry_buttons(self):
        for key in self.dialog_dict:
            key.clicked.connect(self.entry_button_dialog_start)

    def connect_signal_slots(self):
        """This function connects menubar options."""
        self.menu_file_exit.triggered.connect(self.close)

    def entry_button_dialog_start(self):
        dialog = self.dialog_dict[self.sender()](self.judicial_officer)
        dialog.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
