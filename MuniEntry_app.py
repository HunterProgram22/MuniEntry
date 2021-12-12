"""
Copyright 2021 Justin Kudela

The main application entry point.

The main window contains options for selecting the judicial officer and templates.
"""
import sys

from loguru import logger
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from PyQt5 import QtGui

from resources.db.create_data_lists import create_cases_list
from models.party_types import JudicialOfficer
from models.data_loader import CriminalCaseSQLRetriever
from models.case_information import CriminalCaseInformation
from views.main_window_ui import Ui_MainWindow
from controllers.no_jail_plea_dialogs import NoJailPleaDialog
from controllers.leap_plea_dialogs import LeapPleaLongDialog, LeapPleaShortDialog
from controllers.fta_bond_dialogs import FTABondDialog
from controllers.not_guilty_bond_dialogs import NotGuiltyBondDialog
from controllers.juror_payment_dialogs import JurorPaymentDialog
from settings import create_arraignments_database_connection


logger.add("./resources/logs/Error_log_{time}.log")


class Window(QMainWindow, Ui_MainWindow):
    """The MainWindow of the application from which the judicial officer and template for creating
    an entry is selected.

    :judicial_officer_dict: - used to connect a radio button to a judicial officer. If a judicial
    officer is added to the view then add new judicial officer to dict (key:
    self.lastname_radioButton, value: "Lastname").The button will be connected to the slot for
    self.judicial_officer by the function connect_judicial_officer_buttons.

    :dialog_dict: - If a new entry button is added to the view then a new
    key:value pair needs to be added to dialog_dict (key: buttonName, value:
    dialogObject)."""

    def __init__(self, arraignments_database, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # The self argument that is called is MainWindow
        self.setWindowIcon(QtGui.QIcon('./resources/icons/gavel.jpg'))
        self.connect_menu_signal_slots()
        self.judicial_officer = None
        self.case_to_load = None
        self.judicial_officer_dict = {
            self.bunner_radioButton: JudicialOfficer("Amanda", "Bunner", "Magistrate"),
            self.pelanda_radioButton: JudicialOfficer("Kevin", "Pelanda", "Magistrate"),
            self.kudela_radioButton: JudicialOfficer("Justin", "Kudela", "Magistrate"),
            self.rohrer_radioButton: JudicialOfficer("Kyle", "Rohrer", "Judge"),
            self.hemmeter_radioButton: JudicialOfficer("Marianne", "Hemmeter", "Judge"),
        }
        self.dialog_dict = {
            self.NoJailPleaButton: NoJailPleaDialog,
            self.LeapPleaLongButton: LeapPleaLongDialog,
            self.LeapPleaShortButton: LeapPleaShortDialog,
            self.FTABondButton: FTABondDialog,
            self.NotGuiltyBondButton: NotGuiltyBondDialog,
            self.JurorPaymentButton: JurorPaymentDialog,
        }
        self.load_judicial_officers()
        self.connect_entry_buttons()
        self.load_arraignment_case_list()
        self.arraignments_database = arraignments_database

    def connect_menu_signal_slots(self):
        """This is for connecting top level MainWindow menu options to slots/functions."""
        self.menu_file_exit.triggered.connect(self.close)

    def load_judicial_officers(self):
        """Loads judicial officers and connects the radio button for each judicial officer to the
        radio button so that if it is selected when an entry dialog button is pressed to load the
        dialog, then the judicial officer that is selected will be passed to the dialog."""
        for key in self.judicial_officer_dict:
            key.clicked.connect(self.set_judicial_officer)

    def set_judicial_officer(self):
        """Checks the judicial officer radio buttons and then sets the judicial officer."""
        for key, value in self.judicial_officer_dict.items():
            if key.isChecked():
                self.judicial_officer = value

    def connect_entry_buttons(self):
        """Connects the starting dialog that will be launched upon button press."""
        for key in self.dialog_dict:
            key.pressed.connect(self.start_dialog_from_entry_button)

    def load_arraignment_case_list(self):
        """Loads the cms_case numbers of all the cases that are in the arraignments database. This
        does not load the cms_case data for each cms_case."""
        self.arraignment_cases_box.addItems(create_cases_list())

    @logger.catch
    def start_dialog_from_entry_button(self):
        """ Launches the dialog that is connected to each button."""
        if self.judicial_officer is None:
            message = QMessageBox()
            message.setIcon(QMessageBox.Warning)
            message.setWindowTitle("Required")
            message.setText("You must select a judicial officer.")
            message.setStandardButtons(QMessageBox.Ok)
            message.exec()
        else:
            self.arraignments_database.open()
            if self.arraignment_cases_box.currentText() == "":
                self.case_to_load = CriminalCaseInformation()
                dialog = self.dialog_dict[self.sender()](self.judicial_officer, self.case_to_load)
            else:
                database = self.arraignments_database
                case_number = self.arraignment_cases_box.currentText()
                self.case_to_load = CriminalCaseSQLRetriever(case_number, database).load_case()
                dialog = self.dialog_dict[self.sender()](self.judicial_officer, self.case_to_load)
            dialog.exec()


@logger.catch
def main():
    """The main loop of the application. The arraignments database is created each time the
    application is loaded after any existing prior version is deleted."""
    app = QApplication(sys.argv)
    arraignments_database = create_arraignments_database_connection()
    win = Window(arraignments_database)
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    from resources.db import create_arraignment_table
    main()
