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

    if case_data.get('trial_date') is not None:
        event = Event(
            case_data.get('case_number'),
            'Jury Trial',
            case_data.get('hearing_location'),
            case_data.get('trial_date'),
            case_data.get('trial_time'),
        )

    query.prepare(insert_scheduling_data_query(event))

    query_result = query.exec()
    logger.debug(f'Query result: {query_result}')
    logger.debug(query.lastQuery())

    close_db_connection(conn)


def format_date_string(date_string: str) -> str:
    date_object = datetime.strptime(date_string, '%B %d, %Y')
    new_date_format = date_object.strftime('%Y-%m-%d')
    new_date_object = datetime.strptime(new_date_format, '%Y-%m-%d').date()
    return str(new_date_object)


class Event(object):

    def __init__(self, case_number, event_name, event_location, event_date, event_time='8:00 AM'):
        self.case_number = case_number
        self.event_name = event_name
        self.location_name = event_location
        self.event_date = format_date_string(event_date)
        self.event_time = self.set_event_time(event_time)

    def set_event_time(self, event_time):
        if event_time is None:
            return '8:00 AM'
