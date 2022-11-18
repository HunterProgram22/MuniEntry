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

    event = Event()

    query.prepare(insert_scheduling_data_query(event))

    query_result = query.exec()

    logger.debug(f'Query result: {query_result}')

    logger.debug(query.lastQuery())
    logger.debug(query.lastError().databaseText())

    close_db_connection(conn)


def format_date_string(date_string: str) -> str:
    date_object = datetime.strptime(date_string, '%B %d, %Y')
    new_date_format = date_object.strftime('%Y-%m-%d')
    new_date_object = datetime.strptime(new_date_format, '%Y-%m-%d').date()
    return str(new_date_object)


class Event(object):

    def __init__(self):
        self.case_number = '22TRD11223'
        self.event_date = '2022-01-15'
        self.event_time = '3:30 PM'
        self.event_name = 'Jury Trial'
        self.location_name = 'Courtroom C'
