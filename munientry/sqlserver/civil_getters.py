"""Module for packaging data from SQL Server database for use in application."""
from loguru import logger
from PyQt6.QtSql import QSqlQuery

from munientry.models.cms_models import CivilCmsCaseInformation
from munientry.data.connections import CIVIL_DB_CONN, database_connection
from munientry.sqlserver.civil_sql_server_queries import general_civil_case_query


class CivilCaseData(object):
    """..."""

    @database_connection(CIVIL_DB_CONN)
    def __init__(self, case_number: str, db_connection: str) -> None:
        self.case_number = case_number
        self.case = CivilCmsCaseInformation()
        self.query_case_data(db_connection)
        self.load_query_data_into_case()
        self.query.finish()

    def query_case_data(self, db_connection: str) -> None:
        """Query database based on cms_case number to return the data to load for the dialog."""
        query_string = general_civil_case_query(self.case_number)
        self.query = QSqlQuery(db_connection)
        self.query.prepare(query_string)
        logger.info(f'Querying Authority Civil for: {self.case_number}')
        self.query.bindValue(self.case_number, self.case_number)
        self.query.exec()

    def load_query_data_into_case(self) -> None:
        while self.query.next():
            self.load_case_information()

    def load_case_information(self) -> None:
        if self.case.case_number is None:
            self.case.case_number = self.query.value('CaseNumber')
        if self.case.case_type is None:
            self.case.case_type = self.get_case_type()
        if self.case.primary_plaintiff.party_name is None:
            self.case.primary_plaintiff.party_name = self.get_plaintiff(self.query)
        if self.case.primary_defendant.party_name is None:
            self.case.primary_defendant.party_name = self.get_defendant(self.query)

    def get_case_type(self) -> str:
        case_type_code = self.case.case_number[4]
        civil_code_dict = {
            'E': 'Personal Injury and Property Damage',
            'F': 'Contracts',
            'G': 'FED (Evictions)',
            'H': 'Other Civil',
            'I': 'Small Claims',
        }
        return civil_code_dict.get(case_type_code)

    def get_plaintiff(self, query):
        if self.query.value('PartyType') == 'Plaintiff':
            return self.query.value('PartyName')

    def get_defendant(self, query):
        if self.query.value('PartyType') == 'Defendant':
            return self.query.value('PartyName')

    def load_case(self) -> CivilCmsCaseInformation:
        return self.case
