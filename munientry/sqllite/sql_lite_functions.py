"""Module containing all functions that query the internal SQL Lite database."""
from loguru import logger
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

from munientry.sqllite.sql_lite_queries import (
    select_distinct_attorney_name_sql_query,
    select_distinct_def_last_case_number_query,
    select_distinct_offense_statute_sql_query,
    select_type_for_statute_in_charges,
    select_off_stat_deg_from_charges_query,
)
from munientry.appsettings.paths import CASE_LISTS_PATH

OFFENSE = 'offense'
STATUTE = 'statute'
DEGREE = 'degree'


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
