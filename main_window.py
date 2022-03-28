from loguru import logger
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow

from db.databases import create_daily_cases_list, CriminalCaseSQLRetriever
from package.controllers.information_checkers import (
    check_judicial_officer,
    check_case_list_selected,
)
from package.controllers.main_entry_dialogs import (
    DiversionPleaDialog,
    JailCCPleaDialog,
    FineOnlyPleaDialog,
    NotGuiltyBondDialog,
    ProbationViolationBondDialog,
    FailureToAppearDialog,
)
from package.models.case_information import CriminalCaseInformation
from package.models.party_types import JudicialOfficer
from package.views.custom_widgets import ExtendedComboBox
from package.views.main_window_ui import Ui_MainWindow
from settings import ICON_PATH


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, daily_case_list_database, parent=None):
        super().__init__(parent)
        self.daily_case_list_database = daily_case_list_database
        self.setupUi(self)  # The self argument that is called is MainWindow
        self.setWindowIcon(QtGui.QIcon(f"{ICON_PATH}gavel.ico"))
        self.create_main_window_dicts()
        self.set_daily_case_lists_type()
        self.connect_signals_to_slots()
        self.load_case_lists()
        self.button_state()  # This is called to set boxes all to hidden on load.
        self.judicial_officer = None
        self.case_to_load = None
        self.FailureToAppearButton.setHidden(False)
        self.ProbationViolationBondButton.setHidden(False)

    def create_main_window_dicts(self):
        """
        Dictionaries linking buttons on MainWindow to different objects.

        :judicial_officer_dict: - used to connect a radio button to a judicial officer. If a
        judicial officer is added to the view then add new judicial officer to dict (key:
        self.lastname_radioButton, value: "Lastname").The button will be connected to the slot for
        self.judicial_officer by the function connect_judicial_officer_buttons.

        :dialog_dict: - If a new entry button is added to the view then a new
        key:value pair needs to be added to dialog_dict (key: buttonName, value:
        dialogObject).
        """
        self.judicial_officer_dict = {
            self.bunner_radioButton: JudicialOfficer("Amanda", "Bunner", "Magistrate"),
            self.pelanda_radioButton: JudicialOfficer("Kevin", "Pelanda", "Magistrate"),
            self.kudela_radioButton: JudicialOfficer("Justin", "Kudela", "Magistrate"),
            self.rohrer_radioButton: JudicialOfficer("Kyle", "Rohrer", "Judge"),
            self.hemmeter_radioButton: JudicialOfficer("Marianne", "Hemmeter", "Judge"),
            self.kimbler_radioButton: JudicialOfficer("Guy", "Reece II", "Judge"),
        }
        self.dialog_dict = {
            self.FineOnlyPleaButton: FineOnlyPleaDialog,
            self.JailCCPleaButton: JailCCPleaDialog,
            self.DiversionButton: DiversionPleaDialog,
            self.NotGuiltyBondButton: NotGuiltyBondDialog,
            self.FailureToAppearButton: FailureToAppearDialog,
            self.ProbationViolationBondButton: ProbationViolationBondDialog,
        }
        self.daily_case_list_buttons = {
            self.arraignments_radioButton: "arraignments",
            self.slated_radioButton: "slated",
            self.final_pretrial_radioButton: "final_pretrials",
            self.pleas_radioButton: "pleas",
            self.trials_to_court_radioButton: "trials_to_court",
            self.pcvh_fcvh_radioButton: "pcvh_fcvh",
        }
        self.database_table_dict = {
            "arraignments": self.arraignment_cases_box,
            "slated": self.slated_cases_box,
            "final_pretrials": self.final_pretrial_cases_box,
            "pleas": self.pleas_cases_box,
            "trials_to_court": self.trials_to_court_cases_box,
            "pcvh_fcvh": self.pcvh_fcvh_cases_box,
        }
        self.button_state_dict = {
            self.arraignments_radioButton: self.arraignment_cases_box,
            self.slated_radioButton: self.slated_cases_box,
            self.final_pretrial_radioButton: self.final_pretrial_cases_box,
            self.pleas_radioButton: self.pleas_cases_box,
            self.trials_to_court_radioButton: self.trials_to_court_cases_box,
            self.pcvh_fcvh_radioButton: self.pcvh_fcvh_cases_box,
        }

    def set_daily_case_lists_type(self):
        """Sets the daily cases lists to the custom widget ExtendedComboBox. The ExtendedComboBox
        class allows for auto-completion filtering when typing in the box."""
        self.arraignment_cases_box.__class__ = ExtendedComboBox
        self.slated_cases_box.__class__ = ExtendedComboBox
        self.final_pretrial_cases_box.__class__ = ExtendedComboBox
        self.pleas_cases_box.__class__ = ExtendedComboBox
        self.trials_to_court_cases_box.__class__ = ExtendedComboBox
        self.pcvh_fcvh_cases_box.__class__ = ExtendedComboBox

    def connect_signals_to_slots(self):
        self.menu_file_exit.triggered.connect(self.close)
        self.connect_daily_case_list_buttons()
        for key in self.daily_case_list_buttons:
            key.clicked.connect(self.set_case_list_table)
        for key in self.dialog_dict:
            key.pressed.connect(self.start_dialog_from_entry_button)
        for key in self.judicial_officer_dict:
            key.clicked.connect(self.set_judicial_officer)

    def connect_daily_case_list_buttons(self):
        self.arraignments_radioButton.toggled.connect(
            lambda: self.button_state(self.arraignments_radioButton)
        )
        self.slated_radioButton.toggled.connect(lambda: self.button_state(self.slated_radioButton))
        self.final_pretrial_radioButton.toggled.connect(
            lambda: self.button_state(self.final_pretrial_radioButton)
        )
        self.pleas_radioButton.toggled.connect(lambda: self.button_state(self.pleas_radioButton))
        self.trials_to_court_radioButton.toggled.connect(
            lambda: self.button_state(self.trials_to_court_radioButton)
        )
        self.pcvh_fcvh_radioButton.toggled.connect(
            lambda: self.button_state(self.pcvh_fcvh_radioButton)
        )

    def set_case_list_table(self):
        self.case_table = self.daily_case_list_buttons.get(self.sender())

    def button_state(self, button=None):
        if button is None:
            selected_case_list = None
        else:
            selected_case_list = self.button_state_dict[button]
        for value in self.button_state_dict.values():
            if value == selected_case_list:
                value.setEnabled(True)
                value.setHidden(False)
                value.setFocus()
            else:
                value.setCurrentText("")
                value.setHidden(True)
                value.setEnabled(False)

    def set_judicial_officer(self):
        """Checks the judicial officer radio buttons and then sets the judicial officer to the
        one that is checked."""
        for key, value in self.judicial_officer_dict.items():
            if key.isChecked():
                self.judicial_officer = value

    def load_case_lists(self):
        """Loads the cms_case numbers of all the cases that are in the daily_case_list databases.
        This does not load the cms_case data for each cms_case."""
        self.arraignment_cases_box.addItems(
            create_daily_cases_list("daily_case_lists.sqlite", "arraignments")
        )
        self.slated_cases_box.addItems(create_daily_cases_list("daily_case_lists.sqlite", "slated"))
        self.final_pretrial_cases_box.addItems(
            create_daily_cases_list("daily_case_lists.sqlite", "final_pretrials")
        )
        self.pleas_cases_box.addItems(create_daily_cases_list("daily_case_lists.sqlite", "pleas"))
        self.trials_to_court_cases_box.addItems(
            create_daily_cases_list("daily_case_lists.sqlite", "trials_to_court")
        )
        self.pcvh_fcvh_cases_box.addItems(
            create_daily_cases_list("daily_case_lists.sqlite", "pcvh_fcvh")
        )

    @logger.catch
    @check_judicial_officer
    @check_case_list_selected
    def start_dialog_from_entry_button(self):
        self.daily_case_list_database.open()
        selected_case_list = self.database_table_dict.get(self.case_table)
        if selected_case_list.currentText() == "":
            self.case_to_load = CriminalCaseInformation()
        else:
            case_number = selected_case_list.currentText().split("- ")[1]
            self.case_to_load = CriminalCaseSQLRetriever(
                case_number, self.case_table, self.daily_case_list_database
            ).load_case()
        self.dialog = self.dialog_dict[self.sender()](
            self.judicial_officer, self.case_to_load, self.case_table
        )
        self.dialog.exec()
