"""Functions for loading driving privileges case information prior to loading.

**munientry.loaders.driving_caseload_functions**

Functions:
    load_no_case_driving() -> DrivingPrivilegesInformation

    load_single_driving_info_case(case_number) -> DrivingPrivilegesInformation
"""
from munientry.loaders.criminal_caseload_functions import get_crim_case_number
from munientry.sqlserver import crim_getters as sql_server
from munientry.models.privileges_models import DrivingPrivilegesInformation


def load_no_case_driving() -> DrivingPrivilegesInformation:
    """Loads the DrivingPrivilegesInformation model with no data.

    Avoids unnecessary call to the database when there is no data to load.

    Returns:
        DrivingPrivilegesInformation: The DrivingPrivilegesInformation model with no data loaded.
    """
    return DrivingPrivilegesInformation()


def load_single_driving_info_case(case_number: str) -> DrivingPrivilegesInformation:
    """Loads a single case with Driving Info query into the CriminalCmsCaseInformation model.

    Args:
        case_number (str): The case number to load in the format: [2 digits][3 chars][5 digits].

        Examples: 22TRD12345, 21CRB00001, 20TRD01010

    Returns:
        DrivingPrivilegesInformation: A DrivingPrivilegesInformation object with case data from
        the database.
    """
    return sql_server.DrivingInfoSQLServer(case_number).load_case()


def get_cms_driving_case_data(mainwindow):
    """Returns the DrivingPrivilegesInformation with case data."""
    case_number = get_crim_case_number(mainwindow)
    if case_number is None:
        return load_no_case_driving()
    return load_single_driving_info_case(case_number)
