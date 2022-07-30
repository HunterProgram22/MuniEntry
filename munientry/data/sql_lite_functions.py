"""Module containing all functions that query the internal SQL Lite database."""
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from munientry.data.case_excel_loader import return_cases_data_from_excel
from munientry.data.connections import open_db_connection, close_db_connection
from munientry.data.sql_lite_queries import insert_daily_case_list_tables_sql_query, \
    delete_table_sql_query, select_distinct_offense_statute_sql_query, \
    select_distinct_attorney_name_sql_query, \
    select_distinct_def_last_def_first_case_number_sql_query, \
    select_statute_from_charges_for_offense_type_sql_query
from munientry.settings import EXCEL_DAILY_CASE_LISTS, DB_PATH


def load_daily_case_list_data(con_daily_case_lists: QSqlDatabase) -> None:
    for item in EXCEL_DAILY_CASE_LISTS:
        excel_report: str
        table_name: str
        excel_report, table_name = item
        delete_existing_sql_table_data(con_daily_case_lists, table_name)
        insert_daily_case_list_sql_data(con_daily_case_lists, excel_report, table_name)


def insert_daily_case_list_sql_data(
    con_daily_case_lists: QSqlDatabase, excel_report: str, table_name: str
) -> None:
    cases_from_table = return_cases_data_from_excel(f"{DB_PATH}{excel_report}")
    insert_data_query = QSqlQuery(con_daily_case_lists)
    insert_data_query.prepare(insert_daily_case_list_tables_sql_query(table_name))
    for case in cases_from_table:
        insert_data_query.addBindValue(case.case_number)
        insert_data_query.addBindValue(case.defendant_last_name)
        insert_data_query.addBindValue(case.defendant_first_name)
        insert_data_query.addBindValue(case.offense)
        insert_data_query.addBindValue(case.statute)
        insert_data_query.addBindValue(case.degree)
        insert_data_query.addBindValue(case.fra_in_file)
        insert_data_query.addBindValue(case.moving_bool)
        insert_data_query.addBindValue(case.def_atty_last_name)
        insert_data_query.addBindValue(case.def_atty_first_name)
        insert_data_query.addBindValue(case.def_atty_type)
        insert_data_query.exec()


def delete_existing_sql_table_data(db_connection: QSqlDatabase, table_name: str) -> None:
    delete_table = QSqlQuery(db_connection)
    delete_table.prepare(delete_table_sql_query(table_name))
    delete_table.exec()


def query_offense_statute_data(db_connection: QSqlDatabase, query_value: str) -> list:
    query_string = select_distinct_offense_statute_sql_query()
    query = QSqlQuery(db_connection)
    query.prepare(query_string)
    query.exec()
    item_list = []
    while query.next():
        if query_value == "offense":
            item_list.append(query.value(0))
        elif query_value == "statute":
            item_list.append(query.value(1))
    item_list.sort()
    return item_list


def query_attorney_list(db_connection: QSqlDatabase) -> list:
    query_string = select_distinct_attorney_name_sql_query()
    query = QSqlQuery(db_connection)
    query.prepare(query_string)
    query.exec()
    item_list = []
    while query.next():
        attorney_full_name = f'{query.value(1)} {query.value(2)}'
        item_list.append(attorney_full_name)
    item_list.sort()
    return item_list


def query_daily_case_list_data(table: str, db_connection: QSqlDatabase) -> list:
    query_string = select_distinct_def_last_def_first_case_number_sql_query(table)
    query = QSqlQuery(db_connection)
    query.prepare(query_string)
    query.exec()
    item_list = []
    while query.next():
        last_name = query.value(0).title()
        case_number = query.value(2)
        name = f"{last_name} - {case_number}"
        item_list.append(name)
    item_list.sort()
    item_list.insert(0, "")
    return item_list


def sql_query_offense_type(key: str, db_connection: QSqlDatabase) -> str:
    """This is called from the AddChargeDialogSlotFunctions to set the offense type to calculate
    court costs. If no match is found this returns "Moving" which is the highest court cost, so if
    the defendant is told the amount it should not be less than what it is owed.
    TODO: add for AmendChargeDialogSlotFunctions."""
    query = QSqlQuery(db_connection)
    query.prepare(select_statute_from_charges_for_offense_type_sql_query())
    query.bindValue(":key", key)
    query.exec()
    offense_type = "Moving"
    while query.next():
        statute = query.value(2)
        offense_type = query.value(4)
        if statute == key:
            query.finish()
            return offense_type
    return offense_type


def main():
    con_daily_case_lists = open_db_connection("con_daily_case_lists")
    load_daily_case_list_data(con_daily_case_lists)
    close_db_connection(con_daily_case_lists)