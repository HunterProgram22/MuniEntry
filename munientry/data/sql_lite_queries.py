"""Module containing all SQL Lite queries used throughout the application."""
from loguru import logger


def insert_daily_case_list_tables_sql_query(table: str) -> str:
    # Do not add comma after last value inserted
    return f"""
        INSERT INTO {table} (
            case_number,
            defendant_last_name,
            defendant_first_name,
            offense,
            statute,
            degree,
            fra_in_file,
            moving_bool,
            def_atty_last_name,
            def_atty_first_name,
            def_atty_type
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """


def delete_table_sql_query(table: str) -> str:
    """This clears all data from the table."""
    return f"""
        DELETE FROM {table};
        """


def select_case_data_sql_query(table: str, case_number: str) -> str:
    return f"""
        SELECT
        case_number,
        defendant_last_name,
        defendant_first_name,
        offense,
        statute,
        degree,
        fra_in_file,
        moving_bool,
        def_atty_first_name || ' ' || def_atty_last_name AS defense_counsel,
        def_atty_type
        FROM {table}
        WHERE case_number = '{case_number}'
        """


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
        SELECT
        type
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
        case_event_time
    )
    SELECT
       '{event.case_number}',
       et.event_type_id,
       el.location_id,
       '{event.event_date}',
       '{event.event_time}'
    FROM
        event_types as et,
        event_locations as el
    WHERE 
        et.event_type_name = '{event.event_name}'
        AND el.location_name = '{event.event_location}';
    """


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
