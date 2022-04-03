"""Module containing all sql queries used throughout the application."""

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


def insert_daily_case_list_tables_sql_query(table: str, case: object) -> str:
    # Do not add comma to last value inserted
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
        VALUES (
            '{case.case_number}',
            '{case.defendant_last_name}',
            '{case.defendant_first_name}',
            '{case.offense}',
            '{case.statute}',
            '{case.degree}',
            '{case.fra_in_file}',
            '{case.moving_bool}',
            '{case.def_atty_last_name}',
            '{case.def_atty_first_name}',
            '{case.def_atty_type}'
        )
        """


def delete_daily_case_list_tables_sql_query(table: str) -> str:
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