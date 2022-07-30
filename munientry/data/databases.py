"""Module for packaging data from SQL Lite internal database for use in application."""

from loguru import logger
from PyQt5.QtSql import QSqlQuery

from munientry.data.connections import close_db_connection, open_db_connection
from munientry.data.sql_lite_queries import select_case_data_sql_query
from munientry.models.cms_models import CmsCaseInformation

CAPITAL_CHARGE_LIST = ('DUS', 'OVI', 'BMV', 'FRA', 'OL')
DELETE_CHARGE_WORD_LIST = ('UCM', 'M1', 'M2', 'M3', 'M4', 'MM', 'PETTY', '(UCM)')


def clean_statute_name(statute: str) -> str:
    """Removes trailing asteriks that are part often part of data from AuthorityCourt."""
    return statute.rstrip('*')


def clean_offense_name(offense: str) -> str:
    """Sets an offense name to title case, but leaves certain abbreviations and removes
    degree of charge if in offense name."""
    offense_word_list = offense.split()
    clean_offense_word_list = []
    for word in offense_word_list:
        if word == 'OMVI':
            clean_offense_word_list.append('OVI')
            continue
        elif word == 'FRA/JUDGMENT':
            clean_offense_word_list.append('FRA / Judgment')
            continue
        elif word in CAPITAL_CHARGE_LIST:
            clean_offense_word_list.append(word)
            continue
        elif word in DELETE_CHARGE_WORD_LIST:
            continue
        else:
            clean_offense_word_list.append(word.capitalize())
    return ' '.join([str(word) for word in clean_offense_word_list])


class CriminalCaseSQLRetriever(object):
    """Class for getting case data from the SQL Lite internal database.

    The class accepts the case number and case table to identify the case, then retrieves
    the case information from the SQL Lite (MuniEntryDB) database and packages it for loading
    into the application.

    The class also cleans the data when packaging it to address various formatting (i.e. all caps)
    issues.

    :case_number: The selected case number from the case selected in the daily case lists box
    on the main window of the application.

    :case_table: The string name of the daily case list box that the case is selected from. Used
    to select the table in the database from which to obtain the case.
    """

    def __init__(self, case_number: str, case_table: str) -> None:
        self.case_number = case_number
        self.case_table = case_table
        self.database = open_db_connection('con_munientry_db')
        self.case = CmsCaseInformation()
        self.query_case_data()
        self.load_data_into_case()
        self.query.finish()
        close_db_connection(self.database)

    def query_case_data(self) -> None:
        '''Query database based on cms_case number to return the data to load for the dialog.
        Current - Query.value(0) is id, then 1 is case_number, 2 is last_name, 3 is first_name.'''
        query_string = select_case_data_sql_query(self.case_table, self.case_number)
        self.query = QSqlQuery(self.database)
        self.query.prepare(query_string)
        logger.database(f'Querying {self.database.connectionName()}')
        logger.database(f'Query: {query_string}')
        self.query.bindValue(self.case_number, self.case_number)
        self.query.exec()

    def load_data_into_case(self) -> None:
        while self.query.next():
            if self.case.case_number is None:
                self.load_case_information()
            self.load_charge_information()

    def load_case_information(self) -> None:
        self.case.case_number = self.query.value(1)
        self.case.defendant.last_name = self.query.value(2).title()
        self.case.defendant.first_name = self.query.value(3).title()
        self.case.fra_in_file = self.query.value(7)
        self.case.defense_counsel = f'{self.query.value(10).title()} {self.query.value(9).title()}'
        self.case.defense_counsel_type = self.query.value(11)

    def load_charge_information(self) -> None:
        offense = clean_offense_name(self.query.value(4))
        statute = clean_statute_name(self.query.value(5))
        degree = self.query.value(6)
        moving_bool = self.query.value(8)
        charge = (offense, statute, degree, moving_bool)
        self.case.charges_list.append(charge)

    def load_case(self) -> CmsCaseInformation:
        return self.case


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
