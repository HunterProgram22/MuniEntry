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

from munientry.data.connections import close_db_connection, open_db_connection
from munientry.models import scheduling_events as se
from munientry.sqllite.sql_lite_queries import insert_scheduling_data_query

EVENT_CLASS_DICT = types.MappingProxyType({
    'hearing_date': se.GeneralHearingEvent,
    'pretrial_date': se.TelephonePretrialEvent,
    'final_pretrial_date': se.FinalPretrialEvent,
    'jury_trial_date': se.JuryTrialEvent,
    'trial_to_court_date': se.TrialToCourtEvent,
})

EVENT_DATE_FIELDS = (
    'hearing_date',
    'jury_trial_date',
    'trial_to_court_date',
    'final_pretrial_date',
    'pretrial_date',
)


def execute_insert_query(query: QSqlQuery, event: se.Event) -> None:
    """Prepares the SQL query and executes it, then logs whether it succeeds.

    Args:
        query (QSqlQuery): The connection to the database as a QSqlDatabase object.

        event (Event): An Event object.
    """
    query.prepare(insert_scheduling_data_query(event))
    query_result = query.exec()
    logger.database(f'Event insert result: {query_result}.')
    logger.database(
        f'{event.case_number}: {event.event_name} - {event.event_date} -'
        + f' {event.event_time} - {event.event_location}: {event.def_last_name},'
        + f' {event.def_first_name}.',
    )


def save_scheduling_data(case_data: Dict[str, Any]) -> None:
    """Extracts data from case data and inserts into the MuniEntryDB.

    The event_class call to EVENT_CLASS_DICT sets a base Event object as the default value if the
    key is not in the dict. This should never be used, but was added to pass mypy typechecking. It
    has not been tested whether a base Event would actually insert data into the database.

    Args:
        case_data (object): A dataclass object model as a dict that contains case information.
    """
    logger.info(f'Scheduling data: {case_data}')
    conn = open_db_connection('con_munientry_db')
    query = QSqlQuery(conn)
    for date_field in EVENT_DATE_FIELDS:
        if case_data.get(date_field) is None:
            continue
        event_class = EVENT_CLASS_DICT.get(date_field, se.Event)
        event = event_class(case_data)
        execute_insert_query(query, event)
    close_db_connection(conn)


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
