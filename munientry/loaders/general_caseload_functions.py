"""Contains functions used for working with a daily case list or case search prior to loading."""
from __future__ import annotations

from munientry.appsettings.pyqt_constants import YES_BUTTON_RESPONSE
from munientry.data import sql_server_getters as sql_server
from munientry.models.cms_models import CmsCaseInformation
from munientry.widgets.message_boxes import WarningBox


def search_daily_case_list(daily_case_list, last_name: str) -> tuple:
    """Loops through all cases in daily case list to find matching last names.

    :daily_case_list: A DailyCaseListComboBox object.
    """
    case_match_count = 0
    matched_cases_list = []
    for case in daily_case_list.all_items():
        if case == '':
            continue
        checked_last_name, checked_case_number = case.split(' - ')
        if checked_last_name == last_name:
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


def check_for_companion_cases(daily_case_list) -> CmsCaseInformation:
    """Checks for matching last names to find potential companion cases to load.

    :daily_case_list: A DailyCaseListComboBox object.
    """
    last_name, case_number = daily_case_list.currentText().split(' - ')
    case_match_count, matched_cases_list = search_daily_case_list(daily_case_list, last_name)
    if case_match_count > 1:
        response = ask_if_cases_combined(last_name, matched_cases_list)
        if response == YES_BUTTON_RESPONSE:
            return load_multiple_cases(matched_cases_list)
    return load_single_case(case_number)


def set_case_to_load(daily_case_list) -> CmsCaseInformation:
    """Returns CmsCaseInformation object model for loading to the template.

    :daily_case_list: The DailyCaseListComboBox that is currently selected on the Main Window.
    """
    if daily_case_list.currentText() == '':
        return load_no_case()
    return check_for_companion_cases(daily_case_list)


def load_no_case() -> CmsCaseInformation:
    """Loads the CmsCaseInformation model with no data.

    Avoids unnecessary call to the database when there is no data to load.
    """
    return CmsCaseInformation()


def load_single_case(case_number: str) -> CmsCaseInformation:
    """Loads a single case into the CmsCaseInformation model."""
    return sql_server.CriminalCaseSQLServer(case_number).load_case()


def load_multiple_cases(matched_case_numbers: list) -> CmsCaseInformation:
    """Loads multiple cases into the CmsCaseInformation model."""
    return sql_server.MultipleCriminalCaseSQLServer(matched_case_numbers).load_case()
