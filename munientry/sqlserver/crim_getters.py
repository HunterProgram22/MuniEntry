"""Module for packaging data from SQL Server database for use in application."""
from typing import Any

from loguru import logger
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

from munientry.data.connections import CRIM_DB_CONN, database_connection
from munientry.data.data_cleaners import (
    clean_defense_counsel_name,
    clean_last_name,
    clean_offense_name,
    clean_statute_name,
)
from munientry.models.cms_models import CriminalCmsCaseInformation
from munientry.models.privileges_models import DrivingPrivilegesInformation
from munientry.settings.app_settings import DAILY_CASE_LIST_STORED_PROCS
from munientry.sqlserver.crim_sql_server_queries import (
    daily_case_list_query,
    driving_case_search_query,
    general_case_search_query,
    get_case_docket_query,
)
from munientry.widgets.message_boxes import InfoBox

CASE_NUMBER = 'CaseNumber'


def log_crim_case_query(case_number: str) -> None:
    """Logs when a case number query to the Criminal Traffic database is made."""
    logger.info(f'Querying Authority Court for: {case_number}')


def get_daily_case_list(table_name: str) -> list[str]:
    """Uses stored procedures in AuthorityCourt DBO to get the cases for each daily case list."""
    stored_proc = DAILY_CASE_LIST_STORED_PROCS.get(table_name)
    cases = execute_query(daily_case_list_query(stored_proc))
    daily_case_list = []
    for case in cases:
        last_name = clean_last_name(case['LastName'].title())
        case_number = case[CASE_NUMBER]
        daily_case_list.append(f'{last_name} - {case_number}')
    daily_case_list.insert(0, '')
    return sorted(daily_case_list)


@database_connection(CRIM_DB_CONN)
def execute_query(query_string: str, db_connection: str = CRIM_DB_CONN) -> list:
    """Executes a sql query on the Authority Court DBO."""
    query = QSqlQuery(db_connection)
    query.prepare(query_string)
    query.exec()
    query_results = []
    while query.next():
        query_row = {}
        for index in range(query.record().count()):
            name = query.record().fieldName(index)
            query_row[name] = query.value(index)
        query_results.append(query_row)
    return query_results


@database_connection(CRIM_DB_CONN)
def get_fta_arraignment_cases(query_string: str, db_connection: QSqlDatabase) -> list[str]:
    """Queries AuthorityCourtDB to get all cases that need a FTA warrant."""
    query = QSqlQuery(db_connection)
    query.prepare(query_string)
    query.exec()
    data_list = []
    while query.next():
        data_list.append(query.value(CASE_NUMBER))
    return data_list


class CrimCaseDocket(object):
    """Packages case docket data from the SQL Server Authority Court database."""

    def __init__(self, case_number: str) -> None:
        self.case_number = case_number

    @database_connection(CRIM_DB_CONN)
    def get_docket(self, db_connection: str = CRIM_DB_CONN) -> list[tuple[Any, Any]]:
        query_string = get_case_docket_query(self.case_number)
        log_crim_case_query(self.case_number)
        query = QSqlQuery(db_connection)
        query.prepare(query_string)
        query.exec()
        data_list = []
        while query.next():
            docket_item = (query.value('Date'), query.value('Remark'))
            data_list.append(docket_item)
        return data_list


class CrimCaseData(object):
    """Packages case data from the SQL Server Authority Court database.

    The class accepts the case number to identify the case, then retrieves
    the case information from the SQL Server (AuthorityCourtDBO) database and packages it for
    loading into the application.
    """

    def __init__(self, case_number: str) -> None:
        self.case_number = case_number
        self.case = CriminalCmsCaseInformation()
        self.query_case_data()

    @database_connection(CRIM_DB_CONN)
    def query_case_data(self, db_connection: str = CRIM_DB_CONN) -> None:
        """Query database for single cms_case number to load for the dialog."""
        query_string = general_case_search_query(self.case_number)
        query = QSqlQuery(db_connection)
        query.prepare(query_string)
        log_crim_case_query(self.case_number)
        query.bindValue(self.case_number, self.case_number)
        query.exec()
        while query.next():
            self.load_case_information(query)
        query.finish()

    def load_case_information(self, query_data) -> None:
        if self.case.case_number is None:
            self.case.case_number = query_data.value(CASE_NUMBER)
            self.case.defendant.last_name = query_data.value('DefLastName').title()
            self.case.defendant.first_name = query_data.value('DefFirstName').title()
            self.case.fra_in_file = query_data.value('FraInFile')
            self.case.defense_counsel = clean_defense_counsel_name(
                query_data.value('DefenseCounsel'),
            )
            self.case.defense_counsel_type = query_data.value('PubDef')
            self.case.violation_date = query_data.value('ViolationDate')

        offense = clean_offense_name(query_data.value('Charge'))
        statute = clean_statute_name(query_data.value('Statute'))
        degree = query_data.value('DegreeCode')
        violation_date = query_data.value('ViolationDate')
        moving_bool = query_data.value('MovingBool')
        charge = (offense, statute, degree, moving_bool, violation_date)
        self.case.charges_list.append(charge)

    def load_case(self) -> CriminalCmsCaseInformation:
        return self.case


class MultipleCrimCaseData(CrimCaseData):
    """Class for holding case data from multiple criminal/traffic cases."""

    def __init__(self, matched_case_numbers_list: list) -> None:
        self.all_case_numbers = matched_case_numbers_list
        self.case = CriminalCmsCaseInformation()
        self.query_multiple_cases_data()

    def query_multiple_cases_data(self) -> None:
        """Query database for multiple cms_case numbers to load case data for the dialog."""
        for case_number in self.all_case_numbers:
            self.case_number = case_number
            self.query_case_data()
        self.case.case_number = ', '.join(self.all_case_numbers)


class DrivingInfoSQLServer(object):
    """Packages driving privileges case data from the SQL Server Authority Court database.

    The class accepts the case number to identify the case, then retrieves
    the case information from the SQL Server (AuthorityCourtDBO) database and packages it for
    loading into the application.
    """

    @database_connection(CRIM_DB_CONN)
    def __init__(self, case_number: str, db_connection: str) -> None:
        self.case_number = case_number
        self.case = DrivingPrivilegesInformation()
        self.query_case_data(db_connection)

    def query_case_data(self, db_connection: str) -> None:
        """Query database based on cms_case number to return the data to load for the dialog."""
        query_string = driving_case_search_query(self.case_number)
        query = QSqlQuery(db_connection)
        query.prepare(query_string)
        log_crim_case_query(self.case_number)
        query.bindValue(self.case_number, self.case_number)
        query.exec()
        self.check_query_for_conflicts(query)
        self.load_query_data_into_case(query)
        query.finish()

    def check_query_for_conflicts(self, query: QSqlQuery):
        count = 0
        while query.next():
            count += 1
        logger.info(f'Conflict check found {count} addresses for Defendant.')
        if count <= 1:
            return
        message = (
            'There are multiple addresses and/or driver license numbers associated with'
            + ' this case, please check fields closely and correct address fields if needed.'
        )
        InfoBox(message, 'Multiple Addreses for Defendant').exec()

    def load_query_data_into_case(self, query: QSqlQuery) -> None:
        query.first()
        self.load_case_information(query)

    def load_case_information(self, query) -> None:
        if query.value(CASE_NUMBER) is None:
            logger.info('NoneType returned from case search - loading empty case.')
            return
        self.case.case_number = query.value(CASE_NUMBER)
        self.case.defendant.first_name = query.value('DefFirstName').title()
        self.case.defendant.last_name = query.value('DefLastName').title()
        self.case.defendant.birth_date = query.value('DefBirthDate')
        if query.value('DefAddress') == '':
            self.case.defendant.address = query.value('CaseAddress').title()
            self.case.defendant.city = query.value('CaseCity').title()
            self.case.defendant.state = str(query.value('CaseState'))
            self.case.defendant.zipcode = query.value('CaseZipcode')
            self.case.defendant.license_number = query.value('DefLicenseNumber')
        else:
            self.case.defendant.address = query.value('DefAddress').title()
            self.case.defendant.city = query.value('DefCity').title()
            self.case.defendant.state = query.value('DefState')
            self.case.defendant.zipcode = query.value('DefZipcode')
            self.case.defendant.license_number = query.value('DefLicenseNumber')

    def load_case(self) -> DrivingPrivilegesInformation:
        return self.case
