"""Module for packaging data from SQL Server database for use in application."""
from __future__ import annotations

from functools import wraps

from loguru import logger
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

from munientry.appsettings.settings import DAILY_CASE_LIST_STORED_PROCS
from munientry.data.connections import close_db_connection, open_db_connection
from munientry.data.data_cleaners import clean_last_name, clean_offense_name, clean_statute_name
from munientry.models.cms_models import CriminalCmsCaseInformation
from munientry.models.privileges_models import DrivingPrivilegesInformation
from munientry.sqlserver.sql_server_queries import (
    daily_case_list_query,
    driving_case_search_query,
    general_case_search_query,
    get_case_docket_query,
)
from munientry.widgets.message_boxes import InfoBox

CRIM_DB_CONN = 'con_authority_court'
CASE_NUMBER = 'CaseNumber'


def log_crim_case_query(case_number: str) -> None:
    """Logs when a case number query to the Criminal Traffic database is made."""
    logger.info(f'Querying Authority Court for: {case_number}')


def database_connection(db_connection_string):
    """Decorator for opening a db connection, calling the function, then closing db connection."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            db_connection_obj = open_db_connection(db_connection_string)
            query_results = func(*args, db_connection=db_connection_obj, **kwargs)
            close_db_connection(db_connection_obj)
            return query_results
        return wrapper
    return decorator


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
def execute_query(query_string: str, db_connection: QSqlDatabase = None) -> list:
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
def get_fta_arraignment_cases(query_string: str, db_connection: QSqlDatabase = None) -> list[str]:
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
        self.database_connection_name = CRIM_DB_CONN
        self.database = open_db_connection(self.database_connection_name)

    def get_docket(self) -> list:
        query_string = get_case_docket_query(self.case_number)
        log_crim_case_query(self.case_number)
        query = QSqlQuery(self.database)
        query.prepare(query_string)
        query.exec()
        data_list = []
        while query.next():
            docket_item = (query.value('Date'), query.value('Remark'))
            data_list.append(docket_item)
        close_db_connection(self.database)
        return data_list


class CrimCaseData(object):
    """Packages case data from the SQL Server Authority Court database.

    The class accepts the case number to identify the case, then retrieves
    the case information from the SQL Server (AuthorityCourtDBO) database and packages it for
    loading into the application.

    :case_number: The entered case number from the on the case search tab of the main window of
        the application.
    """

    def __init__(self, case_number: str) -> None:
        self.case_number = case_number
        self.case = CriminalCmsCaseInformation()
        # self.database_connection_name = CRIM_DB_CONN
        # self.database = open_db_connection(self.database_connection_name)
        self.query_case_data()
        # self.load_query_data_into_case()
        # self.query.finish()
        # close_db_connection(self.database)

    @database_connection(CRIM_DB_CONN)
    def query_case_data(self, db_connection: QSqlDatabase = None) -> None:
        """Query database based on cms_case number to return the data to load for the dialog."""
        query_string = general_case_search_query(self.case_number)
        query = QSqlQuery(db_connection)
        query.prepare(query_string)
        log_crim_case_query(self.case_number)
        query.bindValue(self.case_number, self.case_number)
        query.exec()

    # def load_query_data_into_case(self) -> None:
        while query.next():
            if self.case.case_number is None:
                self.load_case_information(query)
            self.load_charge_information(query)
        # self.query.finish()

    def load_case_information(self, query_data) -> None:
        self.case.case_number = query_data.value(CASE_NUMBER)
        self.case.defendant.last_name = query_data.value('DefLastName').title()
        self.case.defendant.first_name = query_data.value('DefFirstName').title()
        self.case.fra_in_file = query_data.value('FraInFile')
        self.case.defense_counsel = query_data.value('DefenseCounsel').title()
        self.case.defense_counsel_type = query_data.value('PubDef')

    def load_charge_information(self, query_data) -> None:
        offense = clean_offense_name(query_data.value('Charge'))
        statute = clean_statute_name(query_data.value('Statute'))
        degree = query_data.value('DegreeCode')
        moving_bool = query_data.value('MovingBool')
        charge = (offense, statute, degree, moving_bool)
        self.case.charges_list.append(charge)

    def load_case(self) -> CriminalCmsCaseInformation:
        return self.case


class MultipleCrimCaseData(CrimCaseData):
    """Class for holding case data from multiple criminal/traffic cases."""

    def __init__(self, matched_case_numbers_list: list) -> None:
        self.all_case_numbers = matched_case_numbers_list
        self.database_connection_name = CRIM_DB_CONN
        self.database = open_db_connection(self.database_connection_name)
        self.case = CriminalCmsCaseInformation()
        self.query_case_data()
        self.query.finish()
        close_db_connection(self.database)

    def query_case_data(self) -> None:
        """Query database based on cms_case number to return the data to load for the dialog."""
        for case_number in self.all_case_numbers:
            self.case_number = case_number
            query_string = general_case_search_query(self.case_number)
            self.query = QSqlQuery(self.database)
            self.query.prepare(query_string)
            log_crim_case_query(self.case_number)
            self.query.bindValue(self.case_number, self.case_number)
            self.query.exec()
            self.load_query_data_into_case()

    def load_case_information(self) -> None:
        super().load_case_information()
        self.case.case_number = ', '.join(self.all_case_numbers)


class DrivingInfoSQLServer(object):
    """Packages driving privileges case data from the SQL Server Authority Court database.

    The class accepts the case number to identify the case, then retrieves
    the case information from the SQL Server (AuthorityCourtDBO) database and packages it for
    loading into the application.

    :case_number: The entered case number from the on the case search tab of the main window of
        the application.
    """

    def __init__(self, case_number: str) -> None:
        self.case_number = case_number
        self.database_connection_name = CRIM_DB_CONN
        self.database = open_db_connection(self.database_connection_name)
        self.case = DrivingPrivilegesInformation()
        self.query_case_data()
        self.check_query_for_conflicts()
        self.load_query_data_into_case()
        self.query.finish()
        close_db_connection(self.database)

    def query_case_data(self) -> None:
        """Query database based on cms_case number to return the data to load for the dialog."""
        query_string = driving_case_search_query(self.case_number)
        self.query = QSqlQuery(self.database)
        self.query.prepare(query_string)
        log_crim_case_query(self.case_number)
        self.query.bindValue(self.case_number, self.case_number)
        self.query.exec()

    def check_query_for_conflicts(self):
        count = 0
        while self.query.next():
            count += 1
        logger.info(f'Conflict check found {count} addresses for Defendant.')
        if count <= 1:
            return
        message = (
            'There are multiple addresses and/or driver license numbers associated with'
            + ' this case, please check fields closely and correct address fields if'
            + ' needed.'
        )
        InfoBox(message, 'Multiple Addreses for Defendant').exec()

    def load_query_data_into_case(self) -> None:
        self.query.first()
        self.load_case_information()

    def load_case_information(self) -> None:
        if self.query.value(CASE_NUMBER) is None:
            logger.info('NoneType returned from case search - loading empty case.')
            return
        self.case.case_number = self.query.value(CASE_NUMBER)
        self.case.defendant.first_name = self.query.value('DefFirstName').title()
        self.case.defendant.last_name = self.query.value('DefLastName').title()
        self.case.defendant.birth_date = self.query.value('DefBirthDate')
        if self.query.value('DefAddress') == '':
            self.case.defendant.address = self.query.value('CaseAddress').title()
            self.case.defendant.city = self.query.value('CaseCity').title()
            self.case.defendant.state = str(self.query.value('CaseState'))
            self.case.defendant.zipcode = self.query.value('CaseZipcode')
            self.case.defendant.license_number = self.query.value('DefLicenseNumber')
        else:
            self.case.defendant.address = self.query.value('DefAddress').title()
            self.case.defendant.city = self.query.value('DefCity').title()
            self.case.defendant.state = self.query.value('DefState')
            self.case.defendant.zipcode = self.query.value('DefZipcode')
            self.case.defendant.license_number = self.query.value('DefLicenseNumber')

    def load_case(self) -> DrivingPrivilegesInformation:
        return self.case
