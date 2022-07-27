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
            SELECT *
            FROM {table}
            WHERE case_number = '{case_number}'
            """


def select_distinct_offense_statute_sql_query() -> str:
    return f"""SELECT DISTINCT offense, statute FROM charges"""


def select_distinct_attorney_name_sql_query() -> str:
    return f"""
    SELECT DISTINCT id, attorney_first_name, attorney_last_name FROM attorneys
    """


def select_distinct_def_last_def_first_case_number_sql_query(table: str) -> str:
    return f"""
    SELECT DISTINCT defendant_last_name, defendant_first_name, case_number FROM {table}
    """


def select_statute_from_charges_for_offense_type_sql_query() -> str:
    return f"""
    SELECT * FROM charges WHERE statute LIKE '%' || :key || '%'
    """


if __name__ == "__main__":
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
