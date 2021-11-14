"""
The main application entry point. The main window contains options for
selecting the judicial officer on the case and also different templates.
"""
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtSql import QSqlQuery
from loguru import logger
from dataclasses import dataclass

from resources.db import create_arraignment_table

from models.party_types import JudicialOfficer
from models.case_information import CaseLoadData
from views.main_window_ui import Ui_MainWindow
from controllers.minor_misdemeanor_dialogs import MinorMisdemeanorDialog
from controllers.leap_plea_dialogs import LeapPleaLongDialog, LeapPleaShortDialog
from controllers.fta_bond_dialogs import FTABondDialog
from settings import create_arraignments_database_connection
from resources.db.DatabaseCreation import create_cases_list

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

    def __init__(self, arraignments_database, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # The self argument that is called is MainWindow
        self.connect_menu_signal_slots()
        self.judicial_officer = None
        self.judicial_officer_type = None
        self.judicial_officer_dict = {
            self.bunner_radioButton: JudicialOfficer("Amanda", "Bunner", "Magistrate"),
            self.pelanda_radioButton: JudicialOfficer("Kevin", "Pelanda", "Magistrate"),
            self.kudela_radioButton: JudicialOfficer("Justin", "Kudela", "Magistrate"),
            self.rohrer_radioButton: JudicialOfficer("Kyle", "Rohrer", "Judge"),
            self.hemmeter_radioButton: JudicialOfficer("Marianne", "Hemmeter", "Judge"),
        }
        self.dialog_dict = {
            self.MinorMisdemeanorTrafficButton: MinorMisdemeanorDialog,
            self.LeapPleaLongButton: LeapPleaLongDialog,
            self.LeapPleaShortButton: LeapPleaShortDialog,
            self.FTABondButton: FTABondDialog,
        }
        self.connect_judicial_officer_buttons()
        self.connect_entry_buttons()
        self.arraignment_list = create_cases_list()
        self.load_arraignment_case_list()
        self.arraignments_database = arraignments_database


    def load_arraignment_case_list(self):
        self.arraignment_cases_box.addItems(self.arraignment_list)

    def connect_judicial_officer_buttons(self):
        """Connects the radio buttons for each judicial officer to their
        JudicialOfficer object."""
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
        """ Launches the dialog that is connected to each button.
        The judicial_officer argument must be passed to insure the creation
        of the proper template features."""
        try:
            if self.judicial_officer is None:
                raise AttributeError
            self.arraignments_database.open()
            case_to_load = self.get_case_to_load()
            dialog = self.dialog_dict[self.sender()](self.judicial_officer, case_to_load)
            dialog.exec()
        except AttributeError:
            message = QMessageBox()
            message.setIcon(QMessageBox.Warning)
            message.setWindowTitle("Required")
            message.setText("You must select a judicial officer.")
            message.setStandardButtons(QMessageBox.Ok)
            message.exec()

    @logger.catch
    def get_case_to_load(self):
        """Query arraignment_list based on case number to return the data to load for the
        dialog. Query.value(0) is id, then 1 is case_number, 2 is last_name, 3 is first_name.
        query.finish() is called to avoid memory leaks."""
        key = self.arraignment_cases_box.currentText()
        query = QSqlQuery(self.arraignments_database)
        query_string = "SELECT * FROM cases WHERE case_number=16TRC00001"
        print(query_string)
        query.prepare(query_string)
        #query.bindValue(":key", key)
        query.exec()
        charges_list = []
        while query.next():
            case_number = query.value(1)
            defendant_last_name = query.value(2)
            defendant_first_name = query.value(3)
            offense = query.value(4)
            statute = query.value(5)
            degree = query.value(6)
            new_charge = (offense, statute, degree)
            charges_list.append(new_charge)
            print(charges_list)
            fra_in_file = query.value(7)
            break #Eventually remove break statement to get multipe subcases/charges
        if self.arraignment_cases_box.currentText() == "":
            query.finish()
            return CaseLoadData()
        else:
            query.finish()
            return CaseLoadData(case_number, defendant_last_name, defendant_first_name, offense, statute, degree, fra_in_file)

@logger.catch
def main():
    """The main loop of the application. A logger is wrapped on the function
    but needs to be set up to properly log error files. It won't catch all
    errors from the application, only those causing a main loop error."""
    app = QApplication(sys.argv)
    arraignments_database = create_arraignments_database_connection()
    win = Window(arraignments_database)
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
