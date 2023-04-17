"""Module for extracting scheduling data and loading into the MuniEntry Database.

**munientry.data.scheduling_data_loader**

Functions:

    execute_insert_query(query, event) -> None

    save_scheduling_data(case_data, dialog_name) -> None
"""
import types
from typing import Any, Dict

from loguru import logger
from PyQt6.QtSql import QSqlQuery

from munientry.data.connections import MUNIENTRY_DB_CONN, database_connection
from munientry.models import scheduling_events as se
from munientry.sqllite.sql_lite_queries import insert_scheduling_data_query

EVENT_TYPE_DICT = types.MappingProxyType({
    'hearing': se.GeneralHearingEvent,
    'pretrial': se.TelephonePretrialEvent,
    'final_pretrial': se.FinalPretrialEvent,
    'jury_trial': se.JuryTrialEvent,
    'trial_to_court': se.TrialToCourtEvent,
})

CASE_EVENTS = (
    'hearing',
    'jury_trial',
    'trial_to_court',
    'final_pretrial',
    'pretrial',
)


class DatabaseQueryExecutor(object):
    """Executes database queries and logs the results."""

    def __init__(self, query: QSqlQuery) -> None:
        self.query = query

    def execute_insert(self, event: se.Event) -> None:
        self.query.prepare(insert_scheduling_data_query(event))
        query_result = self.query.exec()
        self._log_result(query_result, event)

    def _log_result(self, query_result: bool, event: se.Event) -> None:
        logger.info(f'Event insert result: {query_result}.')
        logger.info(
            f'{event.case_number}: {event.event_name} - {event.event_date} - {event.event_time} -'
            + f' {event.event_location}: {event.def_last_name}, {event.def_first_name}.',
        )


def execute_insert_query(query: QSqlQuery, event: se.Event) -> None:
    """Prepares the SQL query and executes it, then logs whether it succeeds.

    Args:
        query (QSqlQuery): The connection to the database as a QSqlDatabase object.
        event (Event): An Event object.
    """
    executor = DatabaseQueryExecutor(query)
    executor.execute_insert(event)


class CaseEvent(object):
    """Represents a case event extracted from the case data."""

    def __init__(self, case_data: Dict[str, Any], case_event: str) -> None:
        self.case_number = case_data['case_number']
        self.defendant = case_data['defendant']
        self.event_data = case_data.get(case_event)
        self.event_type = case_event

    def has_event_date(self) -> bool:
        return self.event_data is not None and self.event_data.get('date') is not None

    def to_event(self) -> se.Event:
        event_class = EVENT_TYPE_DICT.get(self.event_type, se.Event)
        return event_class(self.__dict__)


class SchedulingDataSaver(object):
    """Saves scheduling data to the MuniEntryDB."""

    def __init__(self, db_connection: str) -> None:
        self.query = QSqlQuery(db_connection)

    def save_case_event(self, case_event: CaseEvent) -> None:
        if case_event.has_event_date():
            event = case_event.to_event()
            execute_insert_query(self.query, event)


@database_connection(MUNIENTRY_DB_CONN)
def save_scheduling_data(case_data: Dict[str, Any], db_connection: str) -> None:
    """Extracts data from case data and inserts into the MuniEntryDB.

    Args:
        case_data (dict): A dataclass object model as a dict that contains case information.
        db_connection (str): The string name of the database connection.
    """
    logger.info(f'Scheduling data: {case_data}')

    data_saver = SchedulingDataSaver(db_connection)
    for case_event in CASE_EVENTS:
        event = CaseEvent(case_data, case_event)
        data_saver.save_case_event(event)
