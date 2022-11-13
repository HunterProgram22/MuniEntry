"""Contains functions for loading driving privileges case information prior to loading."""

from munientry.data import sql_server_getters as sql_server
from munientry.models.privileges_models import DrivingPrivilegesInformation


def load_no_case_driving():
    """Loads the DrivingPrivilegesInformation model with no data.

    Avoids unnecessary call to the database when there is no data to load.

    :return: A DrivingPrivilegesInformation object with no data.
    :rtype: DrivingPrivilegesInformation
    """
    return DrivingPrivilegesInformation()


def load_single_driving_info_case(case_number: str):
    """Loads a single case with Driving Info query into the CmsCaseInformation model.

    :param case_number: A string of the case number in the format: [2 digits][3 chars][5 digits].
        Example: 22TRD12345, 21CRB00001, 20TRD01010
    :type case_number: str
    :return: A DrivingPrivilegesInformation object with case data from the database.
    :rtype: DrivingPrivilegesInformation
    """
    return sql_server.DrivingInfoSQLServer(case_number).load_case()
