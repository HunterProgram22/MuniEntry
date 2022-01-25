"""
Copyright 2021 Justin Kudela

The main application entry point.

The main window contains options for selecting the judicial officer and templates.
"""
import multiprocessing
import sys
import pathlib
from multiprocessing import Process, freeze_support

from PyQt5.QtGui import QPixmap
from PyQt5.QtSql import QSqlDatabase
from loguru import logger
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QSplashScreen
from PyQt5.QtCore import QTimer, Qt
from PyQt5 import QtGui

from resources.db.create_data_lists import create_arraignment_cases_list, create_slated_cases_list, \
    create_final_pretrial_cases_list
from models.party_types import JudicialOfficer
from models.data_loader import CriminalCaseSQLRetriever
from models.case_information import CriminalCaseInformation
from views.custom_widgets import RequiredBox
from views.main_window_ui import Ui_MainWindow
from controllers.sentencing_dialogs import JailCCPleaDialog, NoJailPleaDialog
from controllers.leap_plea_dialogs import LeapPleaLongDialog, LeapPleaShortDialog
from controllers.fta_bond_dialogs import FTABondDialog
from controllers.not_guilty_bond_dialogs import NotGuiltyBondDialog
from settings import create_arraignments_database_connection, create_final_pretrial_database_connection
from settings import create_slated_database_connection

PATH = str(pathlib.Path().absolute())

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

    def __init__(self, arraignment_database, slated_database, final_pretrial_database, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # The self argument that is called is MainWindow
        self.setWindowIcon(QtGui.QIcon(PATH + '/resources/icons/gavel.ico'))
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
            self.JailCCButton: JailCCPleaDialog,
            self.LeapPleaLongButton: LeapPleaLongDialog,
            self.LeapPleaShortButton: LeapPleaShortDialog,
            self.FTABondButton: FTABondDialog,
            self.NotGuiltyBondButton: NotGuiltyBondDialog,
        }
        self.arraignment_database = arraignment_database
        self.slated_database = slated_database
        self.final_pretrial_database = final_pretrial_database
        self.daily_case_list_buttons = {
            self.arraignments_radioButton: self.arraignment_database,
            self.slated_radioButton: self.slated_database,
            self.final_pretrial_radioButton: self.final_pretrial_database,
        }
        self.connect_daily_case_list_buttons()
        self.load_judicial_officers()
        self.connect_entry_buttons()
        self.load_case_lists()

    def connect_menu_signal_slots(self):
        """This is for connecting top level MainWindow menu options to slots/functions."""
        self.menu_file_exit.triggered.connect(self.close)
        self.arraignments_radioButton.toggled.connect(lambda: self.btnstate(self.arraignments_radioButton))
        self.slated_radioButton.toggled.connect(lambda: self.btnstate(self.slated_radioButton))
        self.final_pretrial_radioButton.toggled.connect(lambda: self.btnstate(self.final_pretrial_radioButton))

    def btnstate(self, button):
        if button.text() == "Arraignments":
            if button.isChecked():
                self.arraignment_cases_box.setEnabled(True)
                self.slated_cases_box.setCurrentText("")
                self.slated_cases_box.setEnabled(False)
                self.final_pretrial_cases_box.setCurrentText("")
                self.final_pretrial_cases_box.setEnabled(False)
        if button.text() == "Slated":
            if button.isChecked():
                self.arraignment_cases_box.setCurrentText("")
                self.arraignment_cases_box.setEnabled(False)
                self.slated_cases_box.setEnabled(True)
                self.final_pretrial_cases_box.setCurrentText("")
                self.final_pretrial_cases_box.setEnabled(False)
        if button.text() == "Final Pre-trials":
            if button.isChecked():
                self.arraignment_cases_box.setCurrentText("")
                self.arraignment_cases_box.setEnabled(False)
                self.slated_cases_box.setCurrentText("")
                self.slated_cases_box.setEnabled(False)
                self.final_pretrial_cases_box.setEnabled(True)

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

    def connect_daily_case_list_buttons(self):
        for key in self.daily_case_list_buttons:
            key.clicked.connect(self.set_case_list)

    def set_case_list(self):
        for key, value in self.daily_case_list_buttons.items():
            if key.isChecked():
                self.case_list_to_load = value

    def connect_entry_buttons(self):
        """Connects the starting dialog that will be launched upon button press."""
        for key in self.dialog_dict:
            key.pressed.connect(self.start_dialog_from_entry_button)

    def load_case_lists(self):
        """Loads the cms_case numbers of all the cases that are in the daily_case_list databases. This
        does not load the cms_case data for each cms_case."""
        self.arraignment_cases_box.addItems(create_arraignment_cases_list())
        self.slated_cases_box.addItems(create_slated_cases_list())
        self.final_pretrial_cases_box.addItems(create_final_pretrial_cases_list())

    @logger.catch
    def start_dialog_from_entry_button(self):
        """ Launches the dialog that is connected to each button."""
        if self.judicial_officer is None:
            message = RequiredBox("You must select a judicial officer.")
            message.exec()
        else:
            database_list = [
                (self.arraignment_database, self.arraignment_cases_box),
                (self.slated_database, self.slated_cases_box),
                (self.final_pretrial_database, self.final_pretrial_cases_box),
            ]
            if any(key.isChecked() for key in self.daily_case_list_buttons.keys()):
                database = self.case_list_to_load
                for item in database_list:
                    if database is item[0]:
                        database.open()
                        if item[1].currentText() == "":
                            self.case_to_load = CriminalCaseInformation()
                            dialog = self.dialog_dict[self.sender()](self.judicial_officer, self.case_to_load)
                        else:
                            """The case_number splits the selected case to extract the case number, then
                            it takes the returned list and puts the case number (index 1 of the case number list)
                            into the CriminalCaseSqlRetriever."""
                            case_number = item[1].currentText().split("- ")
                            self.case_to_load = CriminalCaseSQLRetriever(case_number[1], database).load_case()
                            dialog = self.dialog_dict[self.sender()](self.judicial_officer, self.case_to_load)
                dialog.exec()
            else:
                message = RequiredBox("You must select a case list to load. If loading a "
                        "blank template choose any case list and leave dropdown menu blank.")
                message.exec()


@logger.catch
def main():
    """The main loop of the application. The arraignments/slated/final_pretrial databases are created each time the
    application is loaded after any existing prior version is deleted."""
    # TODO: There should be a better way create daily_case_lists instead of importing
    from resources.db import create_daily_case_lists
    app = QApplication(sys.argv)
    splash = QSplashScreen(QPixmap(PATH + '/resources/icons/gavel.png'))
    splash.show()
    print("Loading")
    QTimer.singleShot(2000, splash.close)
    arraignment_database = create_arraignments_database_connection()
    slated_database = create_slated_database_connection()
    final_pretrial_database = create_final_pretrial_database_connection()
    win = Window(arraignment_database, slated_database, final_pretrial_database)
    win.show()
    print(QSqlDatabase.connectionNames())
    sys.exit(app.exec())


if __name__ == "__main__":
    # __spec__ = None # Used to get Python Debugger to work - may have other ramifications(?)
    multiprocessing.freeze_support()
    # Process(target=main).start()
    main()
