"""Module for extracting scheduling data and loading into the MuniEntry Database.

**munientry.data.scheduling_data_loader**

Classes:

    Event(object)

    FinalPretrialEvent(Event)

    GeneralHearingEvent(Event)

    JuryTrialEvent(Event)

    TelephonePretrialEvent(Event)

    TrialToCourtEvent(Event)

Functions:

    execute_insert_query(query, event) -> None

    save_scheduling_data(case_data, dialog_name) -> None
"""
from loguru import logger
from PyQt6.QtSql import QSqlQuery

from munientry.data.connections import close_db_connection, open_db_connection
from munientry.data.sql_lite_queries import insert_scheduling_data_query
from munientry.helper_functions import format_date_string


class Event(object):
    """Object for storing and packaging case event data to be inserted into the MuniEntryDB."""

    def __init__(self, case_data_dict):
        self.case_number = case_data_dict.get('case_number')
        self.event_location = case_data_dict.get('hearing_location')

    def set_event_time(self, event_time):
        if event_time is None:
            return '8:00 AM'
        return event_time


class GeneralHearingEvent(Event):
    """Event object for the General Notice of Hearing Entry.

    The General Notice of Hearing Entry schedules for multiple different types of hearings, but
    the dialog only schedules for a single date.
    """

    def __init__(self, case_data_dict):
        super().__init__(case_data_dict)
        self.event_name = case_data_dict.get('hearing_type')
        self.event_date = format_date_string(case_data_dict.get('hearing_date'))
        self.event_time = self.set_event_time(case_data_dict.get('hearing_time'))


class JuryTrialEvent(Event):
    """Event object for jury trial event."""

    def __init__(self, case_data_dict):
        super().__init__(case_data_dict)
        self.event_name = 'Jury Trial'
        self.event_date = format_date_string(case_data_dict.get('trial_date'))
        self.event_time = self.set_event_time(case_data_dict.get('trial_time'))


class TrialToCourtEvent(Event):
    """Event object for trial to court event."""

    def __init__(self, case_data_dict):
        super().__init__(case_data_dict)
        self.event_name = 'Trial to Court'
        self.event_date = format_date_string(case_data_dict.get('trial_date'))
        self.event_time = self.set_event_time(case_data_dict.get('trial_time'))


class TelephonePretrialEvent(Event):
    """Event object for telephone pretrial court event."""

    def __init__(self, case_data_dict):
        super().__init__(case_data_dict)
        self.event_name = 'Telephone Pretrial'
        self.event_date = format_date_string(case_data_dict.get('pretrial_date'))
        self.event_time = '3:00 PM'


class FinalPretrialEvent(Event):
    """Event object for final pretrial court event."""

    def __init__(self, case_data_dict):
        super().__init__(case_data_dict)
        self.event_name = 'Final Pretrial'
        self.event_date = format_date_string(case_data_dict.get('final_pretrial_date'))
        self.event_time = self.set_event_time(case_data_dict.get('final_pretrial_time'))


def execute_insert_query(query: object, event: Event) -> None:
    """Prepares the SQL query and executes it, then logs whether it succeeds.

    Args:
        query (object): The connection to the database as a QSqlDatabase object.

        event (Event): An Event object.
    """
    query.prepare(insert_scheduling_data_query(event))
    query_result = query.exec()
    logger.database(f'Event insert result: {query_result}.')
    logger.database(
        f'{event.case_number} - {event.event_name} - {event.event_date} -'
        + f' {event.event_time} - {event.event_location}.',
    )


def save_scheduling_data(case_data: object, dialog_name: str) -> None:
    """Extracts data from case data and inserts into the MuniEntryDB.

    Args:
        case_data (object): A dataclass object model that contains case information.

        dialog_name (str): The name of the dialog that the user entered the case information into.
    """
    logger.info(f' The case data is: {case_data}')
    conn = open_db_connection('con_munientry_db')
    query = QSqlQuery(conn)

    if dialog_name == 'General Notice Of Hearing Entry':
        if case_data.get('hearing_date') is not None:
            event = GeneralHearingEvent(case_data)
            execute_insert_query(query, event)

    else:
        if case_data.get('trial_date') is not None:
            if dialog_name == 'Trial To Court Notice Of Hearing Entry':
                event = TrialToCourtEvent(case_data)
                execute_insert_query(query, event)
            else:
                event = JuryTrialEvent(case_data)
                execute_insert_query(query, event)

        if case_data.get('pretrial_date') is not None:
            event = TelephonePretrialEvent(case_data)
            execute_insert_query(query, event)

        if case_data.get('final_pretrial_date') is not None:
            event = FinalPretrialEvent(case_data)
            execute_insert_query(query, event)

    close_db_connection(conn)
