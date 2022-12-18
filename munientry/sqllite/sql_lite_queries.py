"""Module containing all SQL Lite queries used throughout the application."""
from loguru import logger


def select_distinct_offense_statute_sql_query() -> str:
    return 'SELECT DISTINCT offense, statute FROM charges'


def select_distinct_attorney_name_sql_query() -> str:
    return """
        SELECT DISTINCT
            id,
            attorney_first_name || ' ' || attorney_last_name AS attorney_full_name
        FROM attorneys
        """


def select_distinct_def_last_case_number_query(table: str) -> str:
    return f"""
        SELECT DISTINCT
            defendant_last_name || ' - ' || case_number AS case_list_name
        FROM {table}
        """


def select_type_for_statute_in_charges(statute: str) -> str:
    return f"""
        SELECT type
        FROM charges
        WHERE statute = '{statute}'
        """


def select_off_stat_deg_from_charges_query(key: str, field: str) -> str:
    return f"""
    SELECT
        offense,
        statute,
        degree
    FROM charges
    WHERE {field} LIKE '%{key}%'
    """


def insert_scheduling_data_query(event: object) -> str:
    return f"""
    INSERT INTO case_events (
        case_number,
        event_type_id,
        event_location_id,
        case_event_date,
        case_event_time,
        def_last_name,
        def_first_name
    )
    SELECT
       '{event.case_number}',
       et.event_type_id,
       el.location_id,
       '{event.event_date}',
       '{event.event_time}',
       '{event.def_last_name}',
       '{event.def_first_name}'
    FROM
        event_types as et,
        event_locations as el
    WHERE
        et.event_type_name = '{event.event_name}'
        AND el.location_name = '{event.event_location}';
    """


def courtroom_event_report_query(report_date: str, courtroom: int) -> str:
    return f"""
    SELECT
        case_number,
        et.event_type_name,
        case_event_time,
        ce.def_last_name || ', ' || ce.def_first_name AS def_full_name
    FROM
        case_events AS ce
    LEFT OUTER JOIN event_types AS et
        ON ce.event_type_id = et.event_type_id
    WHERE
        case_event_date = '{report_date}' AND event_location_id = {courtroom}
    """


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
