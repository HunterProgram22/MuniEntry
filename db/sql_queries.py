def create_daily_case_list_tables_sql_query(table):
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
          def_atty_last_name VARCHAR (50),
          def_atty_first_name VARCHAR (50),
          def_atty_type VARCHAR(5)
      )
      """


def insert_daily_case_list_tables_sql_query(table, case):
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
            '{case[0]}',
            '{case[1]}',
            '{case[2]}',
            '{case[3]}',
            '{case[4]}',
            '{case[5]}',
            '{case[6]}',
            '{case[7]}',
            '{case[8]}',
            '{case[9]}',
            '{case[10]}'
        )
        """


def delete_daily_case_list_tables_sql_query(table):
    """This clears all data from the table."""
    return f"""
        DELETE FROM {table};
        """


def select_case_data_sql_query(table, case_number):
    return f"""
            SELECT *
            FROM {table}
            WHERE case_number = '{case_number}'
            """
