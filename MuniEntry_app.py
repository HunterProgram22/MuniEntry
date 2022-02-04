"""
Copyright 2021 Justin Kudela

The main application entry point.

The main window contains options for selecting the judicial officer and templates.
"""
import multiprocessing
import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtSql import QSqlDatabase
from loguru import logger
from PyQt5.QtWidgets import QApplication, QMainWindow, QSplashScreen
from PyQt5.QtCore import QTimer
from PyQt5 import QtGui

from package.models.party_types import JudicialOfficer
from db.databases import CriminalCaseSQLRetriever, create_daily_case_list_database_connection, create_daily_cases_list
from package.models.case_information import CriminalCaseInformation
from package.views.custom_widgets import RequiredBox, ExtendedComboBox
from package.views.main_window_ui import Ui_MainWindow
from package.controllers.sentencing_dialogs import JailCCPleaDialog, NoJailPleaDialog
from package.controllers.leap_plea_dialogs import LeapPleaLongDialog, LeapPleaShortDialog
from package.controllers.fta_bond_dialogs import FTABondDialog
from package.controllers.not_guilty_bond_dialogs import NotGuiltyBondDialog
from settings import ICON_PATH


logger.add("./resources/logs/Error_log_{time}.log")


class Window(QMainWindow, Ui_MainWindow):
    """:judicial_officer_dict: - used to connect a radio button to a judicial officer. If a judicial
    officer is added to the view then add new judicial officer to dict (key:
    self.lastname_radioButton, value: "Lastname").The button will be connected to the slot for
    self.judicial_officer by the function connect_judicial_officer_buttons.

    :dialog_dict: - If a new entry button is added to the view then a new
    key:value pair needs to be added to dialog_dict (key: buttonName, value:
    dialogObject)."""

    def __init__(self, daily_case_list_database, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # The self argument that is called is MainWindow
        self.setWindowIcon(QtGui.QIcon(ICON_PATH + 'gavel.ico'))
        self.connect_signals_to_slots()
        self.arraignment_cases_box.__class__ = ExtendedComboBox
        self.slated_cases_box.__class__ = ExtendedComboBox
        self.final_pretrial_cases_box.__class__ = ExtendedComboBox
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
        self.daily_case_list_database = daily_case_list_database
        self.daily_case_list_buttons = {
            self.arraignments_radioButton: "arraignments",
            self.slated_radioButton: "slated",
            self.final_pretrial_radioButton:"final_pretrials",
        }
        self.connect_daily_case_list_buttons()
        self.load_judicial_officers()
        self.connect_entry_buttons()
        self.load_case_lists()

    def connect_signals_to_slots(self):
        self.menu_file_exit.triggered.connect(self.close)
        self.arraignments_radioButton.toggled.connect(lambda: self.btnstate(self.arraignments_radioButton))
        self.slated_radioButton.toggled.connect(lambda: self.btnstate(self.slated_radioButton))
        self.final_pretrial_radioButton.toggled.connect(lambda: self.btnstate(self.final_pretrial_radioButton))

    def btnstate(self, button):
        if button.text() == "Arraignments":
            if button.isChecked():
                self.arraignment_cases_box.setEnabled(True)
                self.arraignment_cases_box.setFocus()
                self.slated_cases_box.setCurrentText("")
                self.slated_cases_box.setEnabled(False)
                self.final_pretrial_cases_box.setCurrentText("")
                self.final_pretrial_cases_box.setEnabled(False)
        if button.text() == "Slated":
            if button.isChecked():
                self.arraignment_cases_box.setCurrentText("")
                self.arraignment_cases_box.setEnabled(False)
                self.slated_cases_box.setEnabled(True)
                self.slated_cases_box.setFocus()
                self.final_pretrial_cases_box.setCurrentText("")
                self.final_pretrial_cases_box.setEnabled(False)
        if button.text() == "Final Pre-trials":
            if button.isChecked():
                self.arraignment_cases_box.setCurrentText("")
                self.arraignment_cases_box.setEnabled(False)
                self.slated_cases_box.setCurrentText("")
                self.slated_cases_box.setEnabled(False)
                self.final_pretrial_cases_box.setEnabled(True)
                self.final_pretrial_cases_box.setFocus()

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
            key.clicked.connect(self.set_case_list_table)

    def set_case_list_table(self):
        for button, table in self.daily_case_list_buttons.items():
            if button.isChecked():
                return table

    def connect_entry_buttons(self):
        """Connects the starting dialog that will be launched upon button press."""
        for key in self.dialog_dict:
            key.pressed.connect(self.start_dialog_from_entry_button)

    def load_case_lists(self):
        """Loads the cms_case numbers of all the cases that are in the daily_case_list databases. This
        does not load the cms_case data for each cms_case."""
        self.arraignment_cases_box.addItems(create_daily_cases_list("daily_case_lists.sqlite", "arraignments"))
        self.slated_cases_box.addItems(create_daily_cases_list("daily_case_lists.sqlite","slated"))
        self.final_pretrial_cases_box.addItems(create_daily_cases_list("daily_case_lists.sqlite","final_pretrials"))

    @logger.catch
    def start_dialog_from_entry_button(self):
        """ Launches the dialog that is connected to each button."""
        if self.judicial_officer is None:
            message = RequiredBox("You must select a judicial officer.")
            message.exec()
        else:
            database_table_dict = {
                "arraignments": self.arraignment_cases_box,
                "slated": self.slated_cases_box,
                "final_pretrials": self.final_pretrial_cases_box,
            }
            if any(key.isChecked() for key in self.daily_case_list_buttons.keys()):
                self.daily_case_list_database.open()
                case_table = self.set_case_list_table() # Set based on the radio button that is checked for the arr/slate/final
                # THIS is where the current issue is located - right now loops three times. Need to match up the button selected
                # to the table.
                selected_case_list = database_table_dict.get(case_table)
                if selected_case_list.currentText() == "":
                    self.case_to_load = CriminalCaseInformation()
                    dialog = self.dialog_dict[self.sender()](self.judicial_officer, self.case_to_load)
                    dialog.exec()
                else:
                    """The case_number splits the selected case to extract the case number, then
                    it takes the returned list and puts the case number (index 1 of the case number list)
                    into the CriminalCaseSqlRetriever."""
                    case_number = selected_case_list.currentText().split("- ")
                    self.case_to_load = \
                        CriminalCaseSQLRetriever(case_number[1], case_table, self.daily_case_list_database).load_case()
                    dialog = self.dialog_dict[self.sender()](self.judicial_officer, self.case_to_load)
                    dialog.exec()
            else:
                message = RequiredBox("You must select a case list to load. If loading a "
                                      "blank template choose any case list and leave dropdown menu blank.")
                message.exec()


@logger.catch
def main():
    app = QApplication(sys.argv)
    splash = QSplashScreen(QPixmap(ICON_PATH + 'gavel.png'))
    splash.show()
    print("Loading")
    QTimer.singleShot(2000, splash.close)
    daily_case_list_database = create_daily_case_list_database_connection()
    win = Window(daily_case_list_database)
    win.show()
    print(QSqlDatabase.connectionNames())
    sys.exit(app.exec())


if __name__ == "__main__":
    # __spec__ = None # Used to get Python Debugger to work - may have other ramifications(?)
    multiprocessing.freeze_support()
    # Process(target=main).start()
    main()
