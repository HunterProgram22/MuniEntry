"""Slot Functions for the MainWindow."""
from typing import Type

from loguru import logger
from PyQt5.QtSql import QSqlDatabase

from munientry.data.databases import (
    close_db_connection,
    create_daily_case_list_sql_tables,
    load_daily_case_list_data,
    open_db_connection,
    query_daily_case_list_data,
)


class MainWindowSlotFunctions(object):
    """Class that contains common functions for the main window."""

    def __init__(self, main_window: object) -> None:
        self.main_window = main_window

    def load_case_lists(self, db_connection: QSqlDatabase = None) -> None:
        """Loads the cms_case numbers of all the cases that are in the daily_case_list databases.

        This does not load the cms_case data for each cms_case.

        The case count is one less than length of list because a blank line is inserted at the
        top of the case list. The case count becomes actual number of cases loaded.
        """
        if db_connection is None:
            db_connection = open_db_connection('con_daily_case_lists')
        for table_name, case_list in self.main_window.database_table_dict.items():
            old_case_count = 0 if len(case_list) == 0 else len(case_list)- 1
            case_list.clear()
            case_list.addItems(query_daily_case_list_data(table_name, db_connection))
            case_count = len(case_list) - 1
            logger.info(f'Table: {table_name} - Preload Cases: {old_case_count}; Postload Cases {case_count}')
        close_db_connection(db_connection)

    def reload_case_lists(self) -> None:
        """This method is connected to the reload cases button only.

        The databases are only recreated on reload since the initial load of the
        application already loads the databases.
        """
        logger.info('Reload cases button pressed.')
        conn = open_db_connection('con_daily_case_lists')
        create_daily_case_list_sql_tables(conn)
        load_daily_case_list_data(conn)
        self.main_window.functions.load_case_lists(conn)
        conn.close()

    def show_hide_daily_case_lists(self) -> None:
        selected_case_list = self.main_window.radio_buttons_case_lists_dict.get(
            self.main_window.sender(),
        )
        for case_list in self.main_window.radio_buttons_case_lists_dict.values():
            if case_list == selected_case_list:
                case_list.setEnabled(True)
                case_list.setHidden(False)
                case_list.setFocus()
            else:
                case_list.setCurrentText('')
                case_list.setHidden(True)
                case_list.setEnabled(False)