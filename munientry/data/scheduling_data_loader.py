"""Module for extracting scheduling data and loading into the MuniEntry Database.

**munientry.data.scheduling_data_loader**

Functions:

    execute_insert_query(query, event) -> None

    save_scheduling_data(case_data, dialog_name) -> None
"""
import types
from typing import Any, Dict

from loguru import logger
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

from munientry.data.connections import database_connection, MUNIENTRY_DB_CONN
from munientry.models import scheduling_events as se
from munientry.sqllite.sql_lite_queries import insert_scheduling_data_query

EVENT_CLASS_DICT = types.MappingProxyType({
    'hearing': se.GeneralHearingEvent,
    'pretrial': se.TelephonePretrialEvent,
    'final_pretrial': se.FinalPretrialEvent,
    'jury_trial': se.JuryTrialEvent,
    'trial_to_court': se.TrialToCourtEvent,
})

EVENT_DATE_FIELDS = (
    'hearing',
    'jury_trial',
    'trial_to_court',
    'final_pretrial',
    'pretrial',
)


def execute_insert_query(query: QSqlQuery, event: se.Event) -> None:
    """Prepares the SQL query and executes it, then logs whether it succeeds.

    Args:
        query (QSqlQuery): The connection to the database as a QSqlDatabase object.

        event (Event): An Event object.
    """
    query.prepare(insert_scheduling_data_query(event))
    query_result = query.exec()
    logger.info(f'Event insert result: {query_result}.')
    logger.info(
        f'{event.case_number}: {event.event_name} - {event.event_date} -'
        + f' {event.event_time} - {event.event_location}: {event.def_last_name},'
        + f' {event.def_first_name}.',
    )


@database_connection(MUNIENTRY_DB_CONN)
def save_scheduling_data(case_data: Dict[str, Any], db_connection: str) -> None:
    """Extracts data from case data and inserts into the MuniEntryDB.

    The event_class call to EVENT_CLASS_DICT sets a base Event object as the default value if the
    key is not in the dict. This should never be used, but was added to pass mypy typechecking. It
    has not been tested whether a base Event would actually insert data into the database.

    Args:
        case_data (object): A dataclass object model as a dict that contains case information.
    """
    logger.info(f'Scheduling data: {case_data}')
    query = QSqlQuery(db_connection)
    for case_event in EVENT_DATE_FIELDS:
        case_event_dict = case_data.get(case_event)
        event_date = case_event_dict.get('date')
        if event_date is None:
            continue
        event_class = EVENT_CLASS_DICT.get(case_event, se.Event)

        case_data_dict = {
            'case_number': case_data['case_number'],
            'defendant': case_data['defendant'],
            'event': case_event_dict,
        }
        event = event_class(case_data_dict)
        execute_insert_query(query, event)
