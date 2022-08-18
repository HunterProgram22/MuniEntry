"""Module for packaging data from SQL Lite internal database for use in application."""

from loguru import logger
from PyQt5.QtSql import QSqlQuery

from munientry.data.connections import close_db_connection, open_db_connection
from munientry.data.sql_lite_queries import select_case_data_sql_query
from munientry.models.cms_models import CmsCaseInformation


class CriminalCaseSQLRetriever(object):
    """Packages case data from the SQL Lite internal database.

    The class accepts the case number and case table to identify the case, then retrieves
    the case information from the SQL Lite (MuniEntryDB) database and packages it for loading
    into the application.

    :case_number: The selected case number from the case selected in the daily case lists box
        on the main window of the application.

    :case_table: The string name of the daily case list box that the case is selected from. Used
        to select the table in the database from which to obtain the case.
    """

    def __init__(self, case_number: str, case_table: str) -> None:
        self.case_number = case_number
        self.case_table = case_table
        self.database_connection_name = 'con_munientry_db'
        self.database = open_db_connection(self.database_connection_name)
        self.case = CmsCaseInformation()
        self.query_case_data()
        self.load_query_data_into_case()
        self.query.finish()
        close_db_connection(self.database)

    def query_case_data(self) -> None:
        """Query database based on cms_case number to return the data to load for the dialog."""
        query_string = select_case_data_sql_query(self.case_table, self.case_number)
        self.query = QSqlQuery(self.database)
        self.query.prepare(query_string)
        logger.database(f'Querying {self.database_connection_name}')
        logger.database(f'Query: {query_string}')
        self.query.bindValue(self.case_number, self.case_number)
        self.query.exec()

    def load_query_data_into_case(self) -> None:
        while self.query.next():
            if self.case.case_number is None:
                self.load_case_information()
            self.load_charge_information()

    def load_case_information(self) -> None:
        self.case.case_number = self.query.value('case_number')
        self.case.defendant.last_name = self.query.value('defendant_last_name')
        self.case.defendant.first_name = self.query.value('defendant_first_name')
        self.case.fra_in_file = self.query.value('fra_in_file')
        self.case.defense_counsel = self.query.value('defense_counsel')
        self.case.defense_counsel_type = self.query.value('def_atty_type')

    def load_charge_information(self) -> None:
        offense = self.query.value('offense')
        statute = self.query.value('statute')
        degree = self.query.value('degree')
        moving_bool = self.query.value('moving_bool')
        charge = (offense, statute, degree, moving_bool)
        self.case.charges_list.append(charge)

    def load_case(self) -> CmsCaseInformation:
        return self.case


class MultipleCriminalCaseSQLRetriever(CriminalCaseSQLRetriever):

    def __init__(self, matched_case_numbers_list: list, case_table: str) -> None:
        logger.debug(matched_case_numbers_list)
        self.all_case_numbers = matched_case_numbers_list
        self.case_table = case_table
        self.database_connection_name = 'con_munientry_db'
        self.database = open_db_connection(self.database_connection_name)
        self.case = CmsCaseInformation()
        self.query_case_data()
        self.query.finish()
        close_db_connection(self.database)

    def query_case_data(self) -> None:
        """Query database based on cms_case number to return the data to load for the dialog."""
        for case_number in self.all_case_numbers:
            self.case_number = case_number
            query_string = select_case_data_sql_query(self.case_table, self.case_number)
            self.query = QSqlQuery(self.database)
            self.query.prepare(query_string)
            logger.database(f'Querying {self.database_connection_name}')
            logger.database(f'Query: {query_string}')
            self.query.bindValue(self.case_number, self.case_number)
            self.query.exec()
            self.load_query_data_into_case()

    def load_case_information(self) -> None:
        super().load_case_information()
        self.case.case_number = ', '.join(self.all_case_numbers)


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
