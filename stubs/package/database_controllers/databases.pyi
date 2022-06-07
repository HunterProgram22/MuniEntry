import abc
from PyQt5.QtSql import QSqlDatabase
from abc import ABC, abstractmethod
from package.database_controllers.sql_queries import create_charges_table_sql_query as create_charges_table_sql_query, create_daily_case_list_tables_sql_query as create_daily_case_list_tables_sql_query, delete_table_sql_query as delete_table_sql_query, insert_charges_sql_query as insert_charges_sql_query, insert_daily_case_list_tables_sql_query as insert_daily_case_list_tables_sql_query, select_case_data_sql_query as select_case_data_sql_query, select_distinct_def_last_def_first_case_number_sql_query as select_distinct_def_last_def_first_case_number_sql_query, select_distinct_offense_statute_sql_query as select_distinct_offense_statute_sql_query, select_statute_from_charges_for_offense_type_sql_query as select_statute_from_charges_for_offense_type_sql_query
from package.models.cms_models import CmsCaseInformation as CmsCaseInformation
from typing import Any

class CaseSQLRetriever(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def query_case_data(self): ...
    @abstractmethod
    def load_data_into_case(self): ...
    @abstractmethod
    def load_case(self): ...

class CriminalCaseSQLRetriever(CaseSQLRetriever):
    case_number: Any
    case_table: Any
    abbreviation_list: Any
    delete_word_list: Any
    database: Any
    case: Any
    def __init__(self, case_number: str, case_table: str) -> None: ...
    query: Any
    def query_case_data(self) -> None: ...
    def load_data_into_case(self) -> None: ...
    def load_case_information(self) -> None: ...
    def load_charge_information(self) -> None: ...
    def clean_statute_name(self, statute: str) -> str: ...
    def clean_offense_name(self, offense: str) -> str: ...
    def load_case(self) -> CmsCaseInformation: ...

def open_db_connection(connection_name: str) -> QSqlDatabase: ...
def remove_db_connection(connection_name: str) -> None: ...
def create_db_connection(database_name: str, connection_name: str) -> QSqlDatabase: ...
def create_db(database_name: str, connection_name: str) -> QSqlDatabase: ...
def check_if_db_open(db_connection: QSqlDatabase, connection_name: str) -> bool: ...
def create_daily_case_list_sql_tables(con_daily_case_lists: QSqlDatabase) -> None: ...
def load_daily_case_list_data(con_daily_case_lists: QSqlDatabase) -> None: ...
def insert_daily_case_list_sql_data(con_daily_case_lists: QSqlDatabase, excel_report: str, table_name: str) -> None: ...
def delete_existing_sql_table(db_connection: QSqlDatabase, table_name: str) -> None: ...

class CaseExcelRetriever:
    case_number: str
    sub_case_number: str
    defendant_last_name: str
    defendant_first_name: str
    offense: str
    statute: str
    degree: str
    fra_in_file: str
    moving_bool: str
    def_atty_last_name: str
    def_atty_first_name: str
    def_atty_type: str
    def __init__(self) -> None: ...

def return_cases_data_from_excel(excel_file: str) -> list: ...
def get_cell_value(ws: object, row: int, col: int) -> str: ...
def query_offense_statute_data(query_value: str) -> list: ...
def query_daily_case_list_data(table: str) -> list: ...
def create_charges_sql_table(con_charges: str) -> None: ...
def insert_charges_sql_data(con_charges: QSqlDatabase, table_name: str) -> None: ...
def load_charges_data(con_charges: QSqlDatabase) -> None: ...

class Charge:
    offense: Any
    statute: Any
    degree: Any
    offense_type: Any
    def __init__(self, offense: str, statute: str, degree: str, offense_type: str) -> None: ...

def return_charges_data_from_excel(excel_file: str) -> list: ...
def sql_query_offense_type(key: str) -> str: ...
def extract_data(case_data: dict) -> None: ...
def main() -> None: ...
