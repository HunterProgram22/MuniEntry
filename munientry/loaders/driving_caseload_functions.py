"""Functions for loading driving privileges case information prior to loading.

**munientry.loaders.driving_caseload_functions**

Functions:
    load_no_case_driving() -> DrivingPrivilegesInformation
    load_single_driving_info_case(case_number) -> DrivingPrivilegesInformation
"""
from loguru import logger

from munientry.data import sql_server_getters as sql_server
from munientry.models.privileges_models import DrivingPrivilegesInformation


def load_no_case_driving() -> DrivingPrivilegesInformation:
    """Loads the DrivingPrivilegesInformation model with no data.

    Avoids unnecessary call to the database when there is no data to load.

    Returns:
        DrivingPrivilegesInformation
            The DrivingPrivilegesInformation model with no data loaded.
    """
    return DrivingPrivilegesInformation()


def load_single_driving_info_case(case_number: str) -> DrivingPrivilegesInformation:
    """Loads a single case with Driving Info query into the CmsCaseInformation model.

    Args:
        case_number: str
            The case number to load in the format: [2 digits][3 chars][5 digits].

            Examples: 22TRD12345, 21CRB00001, 20TRD01010

    Returns:
        DrivingPrivilegesInformation
            A DrivingPrivilegesInformation object with case data from the database.
    """
    return sql_server.DrivingInfoSQLServer(case_number).load_case()


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
