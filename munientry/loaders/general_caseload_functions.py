"""Functions used for working with a daily case list or case search prior to loading.

**munientry/loaders/general_caseload_functions**

Functions:
    check_for_last_name_match(daily_case_list, last_name) -> tuple
    ask_if_cases_combined(last_name, matched_cases_list) -> object
    set_case_loader(daily_case_list) -> CmsCaseInformation
    load_case_information(daily_case_list) -> CmsCaseInformation
    load_no_case() -> CmsCaseInformation
    load_single_case(case_number) -> CmsCaseInformation
    load_multiple_cases(matched_case_numbers) -> CmsCaseInformation
"""

from munientry.appsettings.pyqt_constants import YES_BUTTON_RESPONSE
from munientry.data import sql_server_getters as sql_server
from munientry.models.cms_models import CmsCaseInformation
from munientry.widgets.message_boxes import WarningBox


def check_for_last_name_match(daily_case_list: object, last_name: str) -> tuple:
    """Loops through all cases in selected daily case list to find any matching last names.

    Args:
        daily_case_list: DailyCaseListCombobox
            The selected daily case list.

        last_name: str
            The last name from the case current selected in the case list.

            Example: 22TRD01944 - Conkey -> the last name is 'Conkey'

    Returns:
        tuple
            (case_match_count, matched_cases_list)

            case_match_count: int

            matched_cases_list: list
                A list of all cases where the last name provided matches the last name of a
                case in the selected daily case list.
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
    """Asks user if they want to combine matched cases or just load single selected case.

    Args:
        last_name: str
            The last name from the case current selected in the case list.

            Example: 22TRD01944 - Conkey -> the last name is 'Conkey'

    matched_cases_list: list
        A list of all cases where the last name provided matches the last name of a
        case in the selected daily case list.

    Returns:
        WarningBox
            A custom widget message box asking for user input.
    """
    case_numbers = '\n'.join(matched_cases_list)
    case_count = len(matched_cases_list)
    message = (
        f'There are {case_count} cases with the last name {last_name}.\n\nThe matching '
        + f'cases are:\n{case_numbers}\n\nDo you want to combine them into a single entry?'
    )
    return WarningBox(message, 'Companion Cases').exec()


def set_case_loader(daily_case_list: object) -> CmsCaseInformation:
    """Loads either a single case or multiple cases depending on user input.

    Args:
        daily_case_list: DailyCaseListCombobox
            The selected daily case list.

    Returns:
        CmsCaseInformation
            An instance of a CmsCaseInformation object with case data for a single case or mulitiple
            cases.
    """
    last_name, case_number = daily_case_list.currentText().split(' - ')
    case_match_count, matched_cases_list = check_for_last_name_match(daily_case_list, last_name)
    if case_match_count > 1:
        response = ask_if_cases_combined(last_name, matched_cases_list)
        if response == YES_BUTTON_RESPONSE:
            return load_multiple_cases(matched_cases_list)
    return load_single_case(case_number)


def load_case_information(daily_case_list: object) -> CmsCaseInformation:
    """Loads the CmsCaseInformation object model for loading to the template.

    Args:
        daily_case_list: DailyCaseListCombobox
            The selected daily case list.

    Returns:
        CmsCaseInformation
            An instance of a CmsCaseInformation object with or without data.
    """
    if daily_case_list.currentText() == '':
        return load_no_case()
    return set_case_loader(daily_case_list)


def load_no_case() -> CmsCaseInformation:
    """Loads the CmsCaseInformation model with no data.

    Avoids unnecessary call to the database when there is no data to load.

    Returns:
        CmsCaseInformation
            An instance of a CmsCaseInformation object without data.
    """
    return CmsCaseInformation()


def load_single_case(case_number: str) -> CmsCaseInformation:
    """Loads a single case into the CmsCaseInformation model.

    Args:
        case_number: str
            A string of the case number to be loaded.

    Returns:
        CmsCaseInformation
            An instance of a CmsCaseInformation object with data from a single case.
    """
    return sql_server.CriminalCaseSQLServer(case_number).load_case()


def load_multiple_cases(matched_case_numbers: list) -> CmsCaseInformation:
    """Loads multiple cases into the CmsCaseInformation model.

    Args:
        matched_case_numbers: list
            A list containing strings of all the case numbers to be loaded.

    Returns:
        CmsCaseInformation
            An instance of a CmsCaseInformation object with data from a single case.
    """
    return sql_server.MultipleCriminalCaseSQLServer(matched_case_numbers).load_case()
