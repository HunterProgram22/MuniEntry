"""Module for extracting scheduling data and loading into the MuniEntry Database."""
from datetime import datetime

from loguru import logger
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

from munientry.data.connections import open_db_connection, close_db_connection
from munientry.data.sql_lite_queries import insert_scheduling_data_query


def save_scheduling_data(case_data):
    logger.info(f' The case data is: {case_data}')
    conn = open_db_connection('con_munientry_db')
    query = QSqlQuery(conn)
    query.prepare(insert_scheduling_data_query('sched_final_pretrial'))
    query.addBindValue(case_data.get('case_number'))
    date_string = case_data.get('final_pretrial_date')
    date_string = format_date_string(date_string)
    query.addBindValue(date_string)
    query.addBindValue(case_data.get('final_pretrial_time'))
    query.exec()
    close_db_connection(conn)


def format_date_string(date_string: str) -> str:
    date_object = datetime.strptime(date_string, '%B %d, %Y')
    new_date_format = date_object.strftime('%Y-%m-%d')
    new_date_object = datetime.strptime(new_date_format, '%Y-%m-%d').date()
    return str(new_date_object)