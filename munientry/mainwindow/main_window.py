"""Module containing the Main Window of the application."""
from loguru import logger
from PyQt5.QtWidgets import QComboBox, QInputDialog, QMainWindow, QMessageBox

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


def search_daily_case_list(all_cases: list, selected_last_name: str) -> tuple:
    """Loops through all cases in daily case list to find matching last names."""
    case_match_count = 0
    matched_cases_list = []
    for case in all_cases:
        if case == '':
            continue
        checked_last_name, checked_case_number = case.split(' - ')
        if checked_last_name == selected_last_name:
            case_match_count += 1
            matched_cases_list.append(checked_case_number)
    return case_match_count, matched_cases_list


def check_for_companion_cases(selected_case_table: object, case_table: str) -> CriminalCaseSQLLite:
    """Checks for matching last names to find potential companion cases to load."""
    selected_last_name, selected_case_number = selected_case_table.currentText().split(' - ')
    all_cases = [selected_case_table.itemText(case) for case in range(selected_case_table.count())]
    case_match_count, matched_cases_list = search_daily_case_list(all_cases, selected_last_name)
    if case_match_count > 1:
        return ask_if_cases_combined(selected_last_name, matched_cases_list, case_table)
    return load_single_case(selected_case_number, case_table)


def ask_if_cases_combined(selected_last_name: str, matched_cases_list: list, case_table) -> CriminalCaseSQLLite:
    """Asks user if they want to combine matched cases or just load single selected case."""
    case_numbers = '\n'.join(matched_cases_list)
    case_count = len(matched_cases_list)
    message = (
        f'There are {case_count} cases with the last name {selected_last_name}.\n\nThe matching '
        + f'cases are:\n{case_numbers}\n\nDo you want to combine them into a single entry?'
    )
    response = WarningBox(message, 'Companion Cases').exec()
    if response == QMessageBox.No:
        return load_single_case(selected_case_number, case_table)
    return load_multiple_cases(matched_cases_list, case_table)


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
        self.case_table = 'None'

    def modify_view(self) -> None:
        main_window_view.MainWindowViewModifier(self)

    def connect_signals_to_slots(self) -> None:
        main_window_signalconnector.MainWindowSignalConnector(self)

    def set_selected_case_list_table(self) -> None:
        self.case_table = self.sender().name

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

    def set_case_to_load(self, selected_case_table: QComboBox) -> CmsCaseInformation:
        """Returns CmsCaseInformation object model for loading to the template.

        :selected_case_table: The QComboBox object that is the daily case list table that is
            currently selected on the Main Window.

        TODO: Refactor selected_case_table and self.case_table to single variable.
        """
        logger.debug(selected_case_table)
        logger.debug(f'Self is {self.case_table}')
        if selected_case_table.currentText() == '':
            return load_no_case()
        return check_for_companion_cases(selected_case_table, self.case_table)
