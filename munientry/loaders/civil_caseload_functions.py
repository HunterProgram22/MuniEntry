"""Functions used for working with a civil case search prior to loading."""
from munientry.models.cms_models import CivilCmsCaseInformation
from munientry.sqlserver.civil_getters import CivilCaseData


def load_single_civil_case(case_number: str) -> CivilCmsCaseInformation:
    """Loads a single case into the CivCmsCaseInformation model.

    Args:
        case_number (str): A string of the case number to be loaded.

    Returns:
        CivCmsCaseInformation: An instance of a CivCmsCaseInformation object with data from a single case.
    """
    return CivilCaseData(case_number).load_case()


def get_civil_cms_case_data(mainwindow):
    """Returns a CivilCmsCaseInformation object with case data."""
    case_number = mainwindow.civil_case_search_box.text()
    return load_single_civil_case(case_number)
