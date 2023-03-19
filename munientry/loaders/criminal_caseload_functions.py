"""Functions used for working with a criminal case lists or criminal case search prior to loading.

**munientry/loaders/criminal_caseload_functions**

Functions:
    ask_if_cases_combined(last_name, matched_cases_list) -> object

    check_for_last_name_match(daily_case_list, last_name) -> tuple

    get_crim_case_number(mainwindow) -> Optional[str]

    get_crim_cms_case_data(mainwindow) -> CriminalCmsCaseInformation

    load_case_information(daily_case_list) -> CriminalCmsCaseInformation

    load_multiple_cases(matched_case_numbers) -> CriminalCmsCaseInformation

    load_no_case() -> CriminalCmsCaseInformation

    load_single_case(case_number) -> CriminalCmsCaseInformation

    set_case_loader(daily_case_list) -> CriminalCmsCaseInformation
"""
from typing import Optional

from loguru import logger

from munientry.settings.pyqt_constants import YES_BUTTON_RESPONSE
from munientry.sqlserver import crim_getters as sql_server
from munientry.models.cms_models import CriminalCmsCaseInformation
from munientry.widgets.combo_boxes import DailyCaseListComboBox
from munientry.widgets.message_boxes import WarningBox

CASE_LIST_TAB = 'case_list_tab'


def ask_if_cases_combined(last_name: str, matched_cases_list: list) -> WarningBox:
    """Asks user if they want to combine matched cases or just load single selected case.

    Args:
        last_name (str): The last name from the case current selected in the case list.

        matched_cases_list (list): All cases where the last name provided matches the last name \
        of a case in the selected daily case list.

    Returns:
        WarningBox: A custom widget message box asking for user input.
    """
    case_numbers = '\n'.join(matched_cases_list)
    case_count = len(matched_cases_list)
    message = (
        f'There are {case_count} cases with the last name {last_name}.\n\nThe matching '
        + f'cases are:\n{case_numbers}\n\nDo you want to combine them into a single entry?'
    )
    return WarningBox(message, 'Companion Cases').exec()


def check_for_last_name_match(daily_case_list: DailyCaseListComboBox, last_name: str) -> tuple:
    """Loops through all cases in selected daily case list to find any matching last names.

    Args:
        daily_case_list (DailyCaseListComboBox): The selected daily case list.

        last_name (str): The last name from the case current selected in the case list.

            Example: For a selection of '22TRD01944 - Conkey' the last name is 'Conkey.'

    Returns:
        tuple: (case_match_count, matched_cases_list)

            case_match_count (int):

            matched_cases_list (list): A list of all cases where the last name provided matches
            the last name of a case in the selected daily case list.
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


def get_crim_case_number(mainwindow) -> Optional[str]:
    """Returns the string case number of a case if selected or entered, otherwise returns None."""
    if mainwindow.cases_tab_widget.currentWidget().objectName() == CASE_LIST_TAB:
        try:
            _last_name, case_number = mainwindow.daily_case_list.currentText().split(' - ')
        except ValueError as err:
            logger.warning(err)
            return None
        return case_number
    return mainwindow.crim_case_search_box.text()


def get_crim_cms_case_data(mainwindow) -> CriminalCmsCaseInformation:
    """Returns a CriminalCmsCaseInformation object with case data."""
    if mainwindow.cases_tab_widget.currentWidget().objectName() == CASE_LIST_TAB:
        return load_crim_case_information(mainwindow.daily_case_list)
    case_number = mainwindow.crim_case_search_box.text()
    return load_single_crim_case(case_number)


def load_crim_case_information(daily_case_list: DailyCaseListComboBox) -> CriminalCmsCaseInformation:
    """Loads the CriminalCmsCaseInformation object model for loading to the template.

    Args:
        daily_case_list (DailyCaseListComboBox): The selected daily case list.

    Returns:
        CriminalCmsCaseInformation: An instance of a CmsCaseInformation object with or without data.
    """
    if daily_case_list.currentText() == '':
        return load_no_crim_case()
    return set_case_loader(daily_case_list)


def load_no_crim_case() -> CriminalCmsCaseInformation:
    """Loads the CriminalCmsCaseInformation model with no data.

    Avoids unnecessary call to the database when there is no data to load.

    Returns:
        CriminalCmsCaseInformation: An instance of a CmsCaseInformation object without data.
    """
    return CriminalCmsCaseInformation()


def load_multiple_crim_cases(matched_case_numbers: list) -> CriminalCmsCaseInformation:
    """Loads multiple cases into the CriminalCmsCaseInformation model.

    Args:
        matched_case_numbers (list): A list containing strings of all the case numbers to be loaded.

    Returns:
        CriminalCmsCaseInformation: An instance of a CmsCaseInformation object with data from a single case.
    """
    return sql_server.MultipleCrimCaseData(matched_case_numbers).load_case()


def load_single_crim_case(case_number: str) -> CriminalCmsCaseInformation:
    """Loads a single case into the CriminalCmsCaseInformation model.

    Args:
        case_number (str): A string of the case number to be loaded.

    Returns:
        CriminalCmsCaseInformation: An instance of a CmsCaseInformation object with data from a single case.
    """
    return sql_server.CrimCaseData(case_number).load_case()


def set_case_loader(daily_case_list: DailyCaseListComboBox) -> CriminalCmsCaseInformation:
    """Loads either a single case or multiple cases depending on user input.

    Args:
        daily_case_list (DailyCaseListComboBox): The selected daily case list.

    Returns:
        CriminalCmsCaseInformation: An instance of a CmsCaseInformation object with case data for a
        single case or mulitiple cases.
    """
    last_name, case_number = daily_case_list.currentText().split(' - ')
    case_match_count, matched_cases_list = check_for_last_name_match(daily_case_list, last_name)
    if case_match_count > 1:
        response = ask_if_cases_combined(last_name, matched_cases_list)
        if response == YES_BUTTON_RESPONSE:
            return load_multiple_crim_cases(matched_cases_list)
    return load_single_crim_case(case_number)


def set_case_table(mainwindow) -> Optional[str]:
    """Returns the string case table name if case list tab is selected, otherwise returns None."""
    if mainwindow.cases_tab_widget.currentWidget().objectName() == CASE_LIST_TAB:
        return mainwindow.daily_case_list.name
    return None
