"""Module containing the Main Window of the application."""

from loguru import logger
from PyQt5.QtWidgets import QComboBox, QInputDialog, QMainWindow, QMessageBox

from munientry.data.sql_lite_getters import CriminalCaseSQLRetriever, MultipleCriminalCaseSQLRetriever
from munientry.mainwindow import main_window_signalconnector, main_window_view
from munientry.mainwindow.main_window_menu import connect_menu_functions
from munientry.mainwindow.main_window_slots import MainWindowSlotFunctionsMixin
from munientry.models.cms_models import CmsCaseInformation
from munientry.models.party_types import JudicialOfficer
from munientry.views.main_window_ui import Ui_MainWindow
from munientry.widgets.message_boxes import WarningBox


def load_blank_case_template() -> CmsCaseInformation:
    """Loads the CmsCaseInformation model with no data."""
    return CmsCaseInformation()


def load_case_from_case_list(selected_case_table, case_table) -> CriminalCaseSQLRetriever:
    """Loads the case data from a case table.

    Returns a CmsCaseInformation object via CriminalCaseSQLRetriever().load_case()
    that contains all data from the Cms daily case list reports.
    """
    case_number = selected_case_table.currentText().split(' - ')[1]
    last_name = selected_case_table.currentText().split(' - ')[0]
    all_cases = [selected_case_table.itemText(i) for i in range(selected_case_table.count())]
    case_match_count = 0
    matched_case_numbers_list = []
    for case in all_cases:
        if case.split(' - ')[0] == last_name:
            case_match_count += 1
            matched_case_number = case.split(' - ')[1]
            matched_case_numbers_list.append(matched_case_number)
    if case_match_count > 1:
        message = (
                f'There are {case_match_count} cases with the last name {last_name}.\n\nThe matching cases are: '
                + f'{matched_case_numbers_list}.\n\nDo you want to '
                + f'combine them into a single entry?'
        )
        msg_response = WarningBox(message, 'Companion Cases').exec()
        if msg_response == QMessageBox.No:
            return load_single_case_for_template(case_number, case_table)
        if msg_response == QMessageBox.Yes:
            joined_case_numbers = ', '.join(matched_case_numbers_list)
            return load_multiple_cases_for_template(matched_case_numbers_list, joined_case_numbers, case_table)
    return load_single_case_for_template(case_number, case_table)


def load_single_case_for_template(case_number, case_table):
    return CriminalCaseSQLRetriever(case_number, case_table).load_case()


def load_multiple_cases_for_template(matched_case_numbers_list, joined_case_numbers, case_table):
    return MultipleCriminalCaseSQLRetriever(matched_case_numbers_list, joined_case_numbers, case_table).load_case()


class MainWindow(QMainWindow, Ui_MainWindow, MainWindowSlotFunctionsMixin):
    """The main window of the application that is the launching point for all dialogs."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.modify_view()
        self.connect_signals_to_slots()
        connect_menu_functions(self)
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
        self.case_table = self.daily_case_list_buttons_dict.get(self.sender(), 'None')

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
        if selected_case_table.currentText() == '':
            return load_blank_case_template()
        else:
            return load_case_from_case_list(selected_case_table, self.case_table)

