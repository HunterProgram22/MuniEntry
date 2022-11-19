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
from typing import Any, Dict

from loguru import logger
from PyQt6.QtSql import QSqlQuery

from munientry.data.connections import close_db_connection, open_db_connection
from munientry.data.sql_lite_queries import insert_scheduling_data_query
from munientry.helper_functions import format_date_string


class Event(object):
    """Object for storing and packaging case event data to be inserted into the MuniEntryDB."""

    event_name_field: str
    event_date_field: str
    event_time_field: str

    def __init__(self, case_data_dict: dict):
        self.case_data_dict = case_data_dict
        self.case_number = self.case_data_dict.get('case_number')
        self.event_location = self.case_data_dict.get('hearing_location')
        self.event_name = self.load_event_name(self.event_name_field)
        self.event_date = format_date_string(self.case_data_dict.get(self.event_date_field))
        self.event_time = self.load_event_time(self.event_time_field, self.event_name_field)

    def load_event_name(self, event_name_field: str) -> str:
        if event_name_field == 'hearing_type':
            return self.case_data_dict.get('hearing_type', 'None')
        return event_name_field

    def load_event_time(self, event_time_field: str, event_name_field: str) -> str:
        if event_time_field is None:
            return '8:00 AM'
        if event_time_field == 'pretrial_time':
            return '3:00 PM'
        if event_time_field == 'trial_time' and event_name_field == 'Jury Trial':
            return '8:00 AM'
        return self.case_data_dict.get(event_time_field, 'None')


class GeneralHearingEvent(Event):
    """Event object for the General Notice of Hearing Entry.

    The General Notice of Hearing Entry schedules for multiple different types of hearings, but
    the dialog only schedules for a single date.
    """

    event_name_field = 'hearing_type'
    event_date_field = 'hearing_date'
    event_time_field = 'hearing_time'


class JuryTrialEvent(Event):
    """Event object for jury trial event."""

    event_name_field = 'Jury Trial'
    event_date_field = 'trial_date'
    event_time_field = 'trial_time'


class TrialToCourtEvent(Event):
    """Event object for trial to court event."""

    event_name_field = 'Trial to Court'
    event_date_field = 'trial_date'
    event_time_field = 'trial_time'


class TelephonePretrialEvent(Event):
    """Event object for telephone pretrial court event."""

    event_name_field = 'Telephone Pretrial'
    event_date_field = 'pretrial_date'
    event_time_field = 'pretrial_time'


class FinalPretrialEvent(Event):
    """Event object for final pretrial court event."""

    event_name_field = 'Final Pretrial'
    event_date_field = 'final_pretrial_date'
    event_time_field = 'final_pretrial_time'


def execute_insert_query(query: QSqlQuery, event: Event) -> None:
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


def save_scheduling_data(case_data: Dict[str, Any], dialog_name: str) -> None:
    """Extracts data from case data and inserts into the MuniEntryDB.

    Args:
        case_data (object): A dataclass object model that contains case information.

        dialog_name (str): The name of the dialog that the user entered the case information into.
    """
    logger.info(f' The case data is: {case_data}')
    conn = open_db_connection('con_munientry_db')
    event_class_dict = {
        'hearing_date': GeneralHearingEvent,
        'pretrial_date': TelephonePretrialEvent,
        'final_pretrial_date': FinalPretrialEvent,
        'jury_trial_date': JuryTrialEvent,
        'trial_to_court_date': TrialToCourtEvent,
    }
    query = QSqlQuery(conn)
    for date_field in ['hearing_date', 'trial_date', 'final_pretrial_date', 'pretrial_date']:
        if case_data.get(date_field) is None:
            continue
        event_class = event_class_dict.get(date_field)



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


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
