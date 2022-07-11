"""Module containing all sql queries used throughout the application."""
from loguru import logger


def create_daily_case_list_tables_sql_query(table: str) -> str:
    """If changes are made to this create_table string then the old table must
    be deleted. No comma after last item."""
    return f"""
      CREATE TABLE {table} (
          id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
          case_number VARCHAR(20) NOT NULL,
          defendant_last_name VARCHAR(50) NOT NULL,
          defendant_first_name VARCHAR(50) NOT NULL,
          offense VARCHAR(80) NOT NULL,
          statute VARCHAR(50) NOT NULL,
          degree VARCHAR(10) NOT NULL,
          fra_in_file VARCHAR(5) NOT NULL,
          moving_bool VARCHAR(15) NOT NULL,
          def_atty_last_name VARCHAR (50) NOT NULL,
          def_atty_first_name VARCHAR (50) NOT NULL,
          def_atty_type VARCHAR(5)
      )
      """


def create_charges_table_sql_query() -> str:
    return f"""
            CREATE TABLE charges (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            offense VARCHAR(60) UNIQUE NOT NULL,
            statute VARCHAR(50) NOT NULL,
            degree VARCHAR(50) NOT NULL,
            type VARCHAR(50) NOT NULL
        )
    """


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


def insert_charges_sql_query(table: str, charge: object) -> str:
    # Do not add comma after last value inserted
    return f"""
            INSERT INTO {table} (
            offense,
            statute,
            degree,
            type
        )
        VALUES (
            '{charge.offense}',
            '{charge.statute}',
            '{charge.degree}',
            '{charge.offense_type}'
        )
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