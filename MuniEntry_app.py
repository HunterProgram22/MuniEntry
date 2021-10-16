"""
The main application entry point. The main window contains options for
selecting the judicial officer on the case and also different templates.
"""
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from loguru import logger

from models.party_types import JudicialOfficer
from views.main_window_ui import Ui_MainWindow
from controllers.minor_misdemeanor_dialogs import MinorMisdemeanorDialog

logger.add("./resources/logs/Error_log_{time}.log")


class Window(QMainWindow, Ui_MainWindow):
    """The MainWindow of the application.  If changes to the view
    (Ui_MainWindow) are made in QtDesigner then the command
    'pyuic5 -o views/main_window_ui.py resources/ui/MainWindow.ui' must be run
    to update changes to the view file.

    All slots and signals are connected after the view is created. Slots and
    signals can be linked in the view (using QtDesigner or directly in the view
    file after pyuic5 is run), however, connecting in MainWindow (class Window)
    is generally cleaner and allows ease of scalabilty.

    :judicial_officer_dict: - If a new judicial officer is added then
    they only need a radio button added to the view (key:
    self.lastname_radioButton, value: "Lastname").The button will be connected
    to the slot for self.judicial_officer by the function
    connect_judicial_officer_buttons.

    :dialog_dict: - If a new entry button is added to the view then a new
    key:value pair needs to be added to dialog_dict (key: buttonName, value:
    dialogObject).
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # The self argument that is called is MainWindow
        self.connect_menu_signal_slots()
        self.judicial_officer = None
        self.judicial_officer_type = None
        self.judicial_officer_dict = {
            self.bunner_radioButton: JudicialOfficer("Amanda", "Bunner", "Magistrate"),
            self.pelanda_radioButton: JudicialOfficer("Kevin", "Pelanda", "Magistrate"),
            self.rohrer_radioButton: JudicialOfficer("Kyle", "Rohrer", "Judge"),
            self.hemmeter_radioButton: JudicialOfficer("Marianne", "Hemmeter", "Judge"),
        }
        self.dialog_dict = {
            self.MinorMisdemeanorTrafficButton: MinorMisdemeanorDialog,
            self.GreenSheetButton: MinorMisdemeanorDialog,
        }
        self.connect_judicial_officer_buttons()
        self.connect_entry_buttons()

    def connect_judicial_officer_buttons(self):
        """Connects the radio buttons for each judicial officer to their
        JudicialOfficer object.

        'Clicked' is used instead of 'pressed' for connecting the
        judicial_officer buttons because 'pressed' was causing an
        inconsistent bug."""
        for key in self.judicial_officer_dict:
            key.clicked.connect(self.set_judicial_officer)

    def set_judicial_officer(self):
        """Sets the judicial officer for the main application that will be
        transferred to the entry that is selected."""
        for key, value in self.judicial_officer_dict.items():
            if key.isChecked():
                self.judicial_officer = value

    def connect_entry_buttons(self):
        """Cycles through all buttons that are listed in the dialog_dict and
        connects them to the slot for each button. Connects the starting dialog
        that will be launched upon button press."""
        for key in self.dialog_dict:
            key.pressed.connect(self.start_dialog_from_entry_button)

    def connect_menu_signal_slots(self):
        """Self explanatory."""
        self.menu_file_exit.triggered.connect(self.close)

    @logger.catch
    def start_dialog_from_entry_button(self):
        """
        Launches the dialog that is connected to each button.
        The judicial_officer argument must be passed to insure the creation
        of the proper template features.
        """
        try:
            if self.judicial_officer is None:
                raise AttributeError
            dialog = self.dialog_dict[self.sender()](self.judicial_officer)
            dialog.exec()
        except AttributeError:
            message = QMessageBox()
            message.setIcon(QMessageBox.Warning)
            message.setWindowTitle("Required")
            message.setText("You must select a judicial officer.")
            message.setStandardButtons(QMessageBox.Ok)
            message.exec()


@logger.catch
def main():
    """The main loop of the application. A logger is wrapped on the function
    but needs to be set up to properly log error files. It won't catch all
    errors from the application, only those causing a main loop error."""
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
