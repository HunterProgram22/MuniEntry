"""Module containing all functions that query the internal SQL Lite database."""
from loguru import logger
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

from munientry.data.excel_getters import return_cases_data_from_excel
from munientry.data.sql_lite_queries import (
    delete_table_sql_query,
    insert_daily_case_list_tables_sql_query,
    select_distinct_attorney_name_sql_query,
    select_distinct_def_last_case_number_query,
    select_distinct_offense_statute_sql_query,
    select_type_for_statute_in_charges,
    select_off_stat_deg_from_charges_query,
)
from munientry.settings import EXCEL_DAILY_CASE_LISTS
from munientry.paths import CASE_LISTS_PATH

OFFENSE = 'offense'
STATUTE = 'statute'
DEGREE = 'degree'


def load_daily_case_list_data(database: QSqlDatabase) -> None:
    """Loads case data from SSRS reports in Excel into the application.

    :database: The SQL Lite database object for MuniEntryDB.sqlite.

    The function loops through the six SSRS Excel reports for the daily case lists and loads the
    case data in those files into the application SQL Lite internal database.
    """
    for ssrs_report in EXCEL_DAILY_CASE_LISTS:
        excel_report, table_name = ssrs_report
        delete_existing_sql_table_data(database, table_name)
        insert_daily_case_list_sql_data(database, excel_report, table_name)


def insert_daily_case_list_sql_data(
    database: QSqlDatabase, excel_report: str, table_name: str,
) -> None:
    """Inserts data from each row of SSRS report as a case into SQL Lite database.

    :database: The SQL Lite database object for MuniEntryDB.sqlite.

    :excel_report: The name of the SSRS report (excel file). The path is added in the function.

    :table_name: The name of the SQL Lite table the data is being inserted into in the SQL Lite
        database.
    """
    cases_list = return_cases_data_from_excel(f'{CASE_LISTS_PATH}{excel_report}')
    query = QSqlQuery(database)
    query.prepare(insert_daily_case_list_tables_sql_query(table_name))
    for case in cases_list:
        query.addBindValue(case.case_number)
        query.addBindValue(case.defendant_last_name)
        query.addBindValue(case.defendant_first_name)
        query.addBindValue(case.offense)
        query.addBindValue(case.statute)
        query.addBindValue(case.degree)
        query.addBindValue(case.fra_in_file)
        query.addBindValue(case.moving_bool)
        query.addBindValue(case.def_atty_last_name)
        query.addBindValue(case.def_atty_first_name)
        query.addBindValue(case.def_atty_type)
        query.exec()


def delete_existing_sql_table_data(database: QSqlDatabase, table_name: str) -> None:
    """Function for deleting the data from a table, but not deleting the table itself.

    :database: The SQL Lite database object for MuniEntryDB.sqlite.

    :table_name: The name of the SSRS report that corresponds to the table in the SQL Lite
        database.
    """
    query = QSqlQuery(database)
    query.prepare(delete_table_sql_query(table_name))
    query.exec()


def query_offense_statute_data(database: QSqlDatabase, query_value: str) -> list:
    """Function for getting the offense or statute from the charges table.

    :database: The SQL Lite database object for MuniEntryDB.sqlite.

    :query_value: A string provided by the application based on the field being queried that
        will be either 'offense' or 'statute.'
    """
    query_string = select_distinct_offense_statute_sql_query()
    query = QSqlQuery(database)
    query.prepare(query_string)
    query.exec()
    item_list = []
    while query.next():
        if query_value == 'offense':
            item_list.append(query.value(0))
        elif query_value == 'statute':
            item_list.append(query.value(1))
    item_list.sort()
    return item_list


def query_attorney_list(database: QSqlDatabase) -> list:
    """Queries the attorneys table in the SQL Lite internal database (MuniEntryDB.sqlite).

    :database: The SQL Lite database object for MuniEntryDB.sqlite.

    Returns a list of all attorneys in the attorneys table.
    """
    query_string = select_distinct_attorney_name_sql_query()
    query = QSqlQuery(database)
    query.prepare(query_string)
    query.exec()
    item_list = []
    while query.next():
        attorney_full_name = query.value('attorney_full_name')
        item_list.append(attorney_full_name)
    item_list.sort()
    return item_list


def query_daily_case_list_data(table: str, database: QSqlDatabase) -> list:
    """Queries one of the case tables and returns a list of cases.

    :table: The specific table of cases to be queried.

    :database: The SQL Lite database object for MuniEntryDB.sqlite.

    Returns a list of distinct cases by party last name and case number.
    """
    query_string = select_distinct_def_last_case_number_query(table)
    query = QSqlQuery(database)
    query.prepare(query_string)
    query.exec()
    case_list = []
    while query.next():
        case_list_name = query.value('case_list_name')
        case_list.append(case_list_name)
    case_list.sort()
    case_list.insert(0, '')
    return case_list


def query_offense_type(statute: str, database: QSqlDatabase) -> str:
    """Queries the offense to get the offense type (Moving, Non-moving, or Criminal).

    Used by the AddChargeDialog.

    TODO: add to AmendChargeDialogSlotFunctions because amended charge could have new type.

    :database: The SQL Lite database object for MuniEntryDB.sqlite.

    Returns a string of Moving, Non-moving or Criminal.

    If no match is found this returns 'Moving' which is the highest court cost, so if
    the defendant is told the amount it should not be less than what it is owed.
    """
    query = QSqlQuery(database)
    query.prepare(select_type_for_statute_in_charges(statute))
    query.exec()
    if query.next() is None:
        return 'Moving'
    return query.value('type')


def query_charges_database(database: QSqlDatabase, key: str, field: str) -> tuple:
    query_string = select_off_stat_deg_from_charges_query(key, field)
    query = QSqlQuery(database)
    query.prepare(query_string)
    query.exec()
    query.next()
    offense = query.value(OFFENSE)
    statute = query.value(STATUTE)
    degree = query.value(DEGREE)
    query.finish()
    return offense, statute, degree


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
