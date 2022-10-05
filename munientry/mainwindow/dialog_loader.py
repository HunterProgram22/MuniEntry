"""Module containing classes and functions for loading dialogs from the Main Window."""
from PyQt5.QtWidgets import QMessageBox, QDialog
from loguru import logger

from munientry.data import sql_server_getters as sql_server
from munientry.data import sql_lite_getters as sql_lite
from munientry.models.cms_models import CmsCaseInformation
from munientry.widgets.message_boxes import WarningBox, RequiredBox


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


def ask_if_cases_combined(last_name: str, matched_cases_list: list) -> object:
    """Asks user if they want to combine matched cases or just load single selected case."""
    case_numbers = '\n'.join(matched_cases_list)
    case_count = len(matched_cases_list)
    message = (
        f'There are {case_count} cases with the last name {last_name}.\n\nThe matching '
        + f'cases are:\n{case_numbers}\n\nDo you want to combine them into a single entry?'
    )
    return WarningBox(message, 'Companion Cases').exec()


def check_for_companion_cases(daily_case_list: object) -> object:
    """Checks for matching last names to find potential companion cases to load."""
    last_name, case_number = daily_case_list.currentText().split(' - ')
    case_match_count, matched_cases_list = search_daily_case_list(daily_case_list, last_name)
    if case_match_count > 1:
        response = ask_if_cases_combined(last_name, matched_cases_list)
        if response == QMessageBox.Yes:
            return load_multiple_cases(matched_cases_list)
    return load_single_case(case_number)


def set_case_to_load(daily_case_list: object) -> CmsCaseInformation:
    """Returns CmsCaseInformation object model for loading to the template.

    :daily_case_list: The daily case list table that is currently selected on the Main Window.
    """
    if daily_case_list.currentText() == '':
        return load_no_case()
    return check_for_companion_cases(daily_case_list)


def load_no_case() -> CmsCaseInformation:
    """Loads the CmsCaseInformation model with no data."""
    return CmsCaseInformation()


def load_single_case(case_number: str) -> CmsCaseInformation:
    """Loads a single case into the CmsCaseInformation model."""
    return sql_server.CriminalCaseSQLServer(case_number).load_case()


def load_single_driving_info_case(case_number: str) -> CmsCaseInformation:
    """Loads a single with Driving Info query into the CmsCaseInformation model."""
    return sql_server.DrivingInfoSQLServer(case_number).load_case()


def load_multiple_cases(matched_case_numbers: list) -> CmsCaseInformation:
    """Loads multiple cases into the CmsCaseInformation model."""
    return sql_server.MultipleCriminalCaseSQLServer(matched_case_numbers).load_case()


class DialogLoader(object):
    """Loads the Dialog that is selected from the Main Window UI."""

    def __init__(self, mainwindow):
        self.mainwindow = mainwindow

    def load_crimtraffic_entry(self):
        button_dict = self.mainwindow.crim_traffic_dialog_buttons_dict
        return self.load_dialog_process(button_dict)

    def load_scheduling_entry(self):
        button_dict = self.mainwindow.scheduling_dialog_buttons_dict
        return self.load_dialog_process(button_dict)

    def load_admin_entry(self):
        button_dict = self.mainwindow.admin_dialog_buttons_dict
        return self.load_admin_dialog_process(button_dict)

    def set_case_table(self):
        if self.mainwindow.search_tabWidget.currentWidget().objectName() == 'case_list_tab':
            if self.is_daily_case_list_selected():
                return self.mainwindow.daily_case_list.name
        return None

    def is_daily_case_list_selected(self):
        daily_case_lists = self.mainwindow.daily_case_lists
        if not any(case_list.radio_button.isChecked() for case_list in daily_case_lists):
            RequiredBox(
                'You must select a case list. If not loading a case in the case list '
                + 'leave the case list field blank.', 'Daily Case List Required',
            ).exec()
            return False
        return True

    def get_cms_case_data(self):
        if self.mainwindow.search_tabWidget.currentWidget().objectName() == 'case_list_tab':
            return set_case_to_load(self.mainwindow.daily_case_list)
        case_number = self.mainwindow.case_search_box.text()
        return load_single_case(case_number)

    def load_dialog_process(self, button_dict):
        case_table = self.set_case_table()
        judicial_officer = self.mainwindow.judicial_officer
        cms_case_data = self.get_cms_case_data()
        logger.info(f'CMS Case Data: {cms_case_data}')
        return button_dict.get(self.mainwindow.sender())(
            judicial_officer,
            cms_case = cms_case_data,
            case_table = case_table,
        )

    def get_case_number(self) -> str:
        if self.mainwindow.search_tabWidget.currentWidget().objectName() == 'case_list_tab':
            try:
                last_name, case_number = self.mainwindow.daily_case_list.currentText().split(' - ')
            except ValueError as err:
                logger.warning(err)
                return None
            return case_number
        return self.mainwindow.case_search_box.text()

    def load_admin_dialog_process(self, button_dict):
        """Used for driving privileges entry because case search query is unique."""
        case_table = None
        judicial_officer = self.mainwindow.judicial_officer
        case_number = self.get_case_number()
        cms_case_data = load_single_driving_info_case(case_number)
        logger.info(f'CMS Case Data: {cms_case_data}')
        return button_dict.get(self.mainwindow.sender())(
            judicial_officer,
            cms_case = cms_case_data,
            case_table = case_table,
        )


class DialogPreloadChecker(object):
    """Interface for performing checks to make sure necessary options selected prior to load."""

    def __init__(self, mainwindow):
        self.mainwindow = mainwindow

    def crimtraffic_checks(self):
        required_officers = [
            self.mainwindow.hemmeter_radioButton.isChecked(),
            self.mainwindow.rohrer_radioButton.isChecked(),
            self.mainwindow.bunner_radioButton.isChecked(),
            self.mainwindow.kudela_radioButton.isChecked(),
            self.mainwindow.visiting_judge_radioButton.isChecked(),
            self.mainwindow.pelanda_radioButton.isChecked(),
        ]
        if any(required_officers):
            return True
        RequiredBox('You must select judicial officer.', 'Judicial Officer Required').exec()
        return False

    def scheduling_checks(self):
        required_officers = [
            self.mainwindow.dattilo_radioButton.isChecked(),
            self.mainwindow.patterson_radioButton.isChecked(),
            self.mainwindow.none_radioButton.isChecked(),
        ]
        if any(required_officers):
            return True
        RequiredBox(
            'You must select an assignment commissioner.', 'Assignment Commissioner Required',
        ).exec()
        return False

    def admin_checks(self):
        required_officers = [
            self.mainwindow.assn_comm_dattilo_radioButton.isChecked(),
            self.mainwindow.assn_comm_patterson_radioButton.isChecked(),
            self.mainwindow.court_admin_kudela_radioButton.isChecked(),
            self.mainwindow.jury_comm_patterson_radioButton.isChecked(),
        ]
        if any(required_officers):
            return True
        RequiredBox(
            'You must select an administrative staff person.', 'Administrative Staff Required',
        ).exec()
        return False
