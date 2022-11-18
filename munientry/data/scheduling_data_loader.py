"""Module for extracting scheduling data and loading into the MuniEntry Database."""
from datetime import datetime

from loguru import logger
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

from munientry.data.connections import open_db_connection, close_db_connection
from munientry.data.sql_lite_queries import insert_scheduling_data_query


def format_date_string(date_string: str) -> str:
    date_object = datetime.strptime(date_string, '%B %d, %Y')
    new_date_format = date_object.strftime('%Y-%m-%d')
    new_date_object = datetime.strptime(new_date_format, '%Y-%m-%d').date()
    return str(new_date_object)


def save_scheduling_data(case_data):
    logger.info(f' The case data is: {case_data}')
    conn = open_db_connection('con_munientry_db')
    query = QSqlQuery(conn)

    if case_data.get('trial_date') is not None:
        event = JuryTrialEvent(case_data)
        execute_insert_query(query, event)

    if case_data.get('pretrial_date') is not None:
        event = TelephonePretrialEvent(case_data)
        execute_insert_query(query, event)

    if case_data.get('final_pretrial_date') is not None:
        event = FinalPretrialEvent(case_data)
        execute_insert_query(query, event)

    close_db_connection(conn)


def execute_insert_query(query, event):
    query.prepare(insert_scheduling_data_query(event))
    query_result = query.exec()
    logger.debug(f'Query result: {query_result}')
    logger.debug(query.lastQuery())


class Event(object):

    def __init__(self, case_data_dict):
        self.case_number = case_data_dict.get('case_number')
        self.location_name = case_data_dict.get('hearing_location')

    def set_event_time(self, event_time):
        if event_time is None:
            return '8:00 AM'
        return event_time


class JuryTrialEvent(Event):

    def __init__(self, case_data_dict):
        super().__init__(case_data_dict)
        self.event_name = 'Jury Trial'
        self.event_date = format_date_string(case_data_dict.get('trial_date'))
        self.event_time = self.set_event_time(case_data_dict.get('trial_time'))


class TelephonePretrialEvent(Event):

    def __init__(self, case_data_dict):
        super().__init__(case_data_dict)
        self.event_name = 'Telephone Pretrial'
        self.event_date = format_date_string(case_data_dict.get('pretrial_date'))
        self.event_time = '3:00 PM'


class FinalPretrialEvent(Event):

    def __init__(self, case_data_dict):
        super().__init__(case_data_dict)
        self.event_name = 'Final Pretrial'
        self.event_date = format_date_string(case_data_dict.get('final_pretrial_date'))
        self.event_time = self.set_event_time(case_data_dict.get('final_pretrial_time'))
