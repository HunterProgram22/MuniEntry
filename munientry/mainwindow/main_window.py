"""Module containing the Main Window of the application."""
from loguru import logger
from PyQt5.QtWidgets import QInputDialog, QMainWindow, QMessageBox

from munientry.data.sql_lite_getters import (
    CriminalCaseSQLLite,
    MultipleCriminalCaseSQLLite,
)
from munientry.mainwindow import main_window_signalconnector, main_window_view
from munientry.mainwindow.main_window_slots import MainWindowSlotFunctionsMixin
from munientry.mainwindow.menu import MainWindowMenu
from munientry.models.cms_models import CmsCaseInformation
from munientry.models.party_types import JudicialOfficer
from munientry.views.main_window_ui import Ui_MainWindow
from munientry.widgets.message_boxes import WarningBox


def load_no_case() -> CmsCaseInformation:
    """Loads the CmsCaseInformation model with no data."""
    return CmsCaseInformation()


def load_single_case(case_number: str, case_table: str) -> CmsCaseInformation:
    """Loads a single case into the CmsCaseInformation model."""
    return CriminalCaseSQLLite(case_number, case_table).load_case()


def load_multiple_cases(matched_case_numbers: list, case_table: str) -> CmsCaseInformation:
    """Loads multiple cases into the CmsCaseInformation model."""
    return MultipleCriminalCaseSQLLite(matched_case_numbers, case_table).load_case()


def search_daily_case_list(daily_case_list: list, selected_last_name: str) -> tuple:
    """Loops through all cases in daily case list to find matching last names."""
    case_match_count = 0
    matched_cases_list = []
    for case in daily_case_list.all_items():
        if case == '':
            continue
        checked_last_name, checked_case_number = case.split(' - ')
        if checked_last_name == selected_last_name:
            case_match_count += 1
            matched_cases_list.append(checked_case_number)
    return case_match_count, matched_cases_list


def check_for_companion_cases(daily_case_list: object) -> CriminalCaseSQLLite:
    """Checks for matching last names to find potential companion cases to load."""
    last_name, case_number = daily_case_list.currentText().split(' - ')
    case_match_count, matched_cases_list = search_daily_case_list(daily_case_list, last_name)
    if case_match_count > 1:
        response = ask_if_cases_combined(last_name, matched_cases_list)
        if response == QMessageBox.Yes:
            return load_multiple_cases(matched_cases_list, daily_case_list.name)
    return load_single_case(case_number, daily_case_list.name)


def ask_if_cases_combined(last_name: str, matched_cases_list: list) -> WarningBox:
    """Asks user if they want to combine matched cases or just load single selected case."""
    case_numbers = '\n'.join(matched_cases_list)
    case_count = len(matched_cases_list)
    message = (
        f'There are {case_count} cases with the last name {last_name}.\n\nThe matching '
        + f'cases are:\n{case_numbers}\n\nDo you want to combine them into a single entry?'
    )
    return WarningBox(message, 'Companion Cases').exec()


class MainWindow(QMainWindow, Ui_MainWindow, MainWindowSlotFunctionsMixin):
    """The main window of the application that is the launching point for all dialogs."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.modify_view()
        self.connect_signals_to_slots()
        self.menu = MainWindowMenu(self)
        self.load_case_lists()
        self.show_hide_daily_case_lists()
        self.judicial_officer = None
        self.dialog = None
        self.daily_case_list = None

    def modify_view(self) -> None:
        main_window_view.MainWindowViewModifier(self)

    def connect_signals_to_slots(self) -> None:
        main_window_signalconnector.MainWindowSignalConnector(self)

    def set_visiting_judge(self):
        if self.visiting_judge_radioButton.isChecked():
            first_name, response_ok = QInputDialog.getText(
                self, 'Set Visiting Judge', 'Enter Judge First Name:',
            )
            last_name, response_ok = QInputDialog.getText(
                self, 'Set Visiting Judge', 'Enter Judge Last Name:',
            )
            if response_ok:
                update_dict = {
                    self.visiting_judge_radioButton: JudicialOfficer(
                        f'{first_name}', f'{last_name}', 'Judge',
                    ),
                }
                self.judicial_officer_buttons_dict.update(update_dict)
                self.visiting_judge_radioButton.setText(f'Judge {last_name}')

    def update_judicial_officer(self) -> None:
        self.judicial_officer = self.judicial_officer_buttons_dict.get(self.sender())
        judicial_officer = self.judicial_officer.last_name
        logger.action(f'Judicial Officer set to: {judicial_officer}')

    def set_case_to_load(self, daily_case_list: object) -> CmsCaseInformation:
        """Returns CmsCaseInformation object model for loading to the template.

        :daily_case_list: The daily case list table that is currently selected on the Main Window.
        """
        if daily_case_list.currentText() == '':
            return load_no_case()
        return check_for_companion_cases(daily_case_list)
