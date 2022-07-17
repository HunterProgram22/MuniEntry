"""Slot Functions for the MainWindow."""
from loguru import logger
from PyQt5.QtWidgets import QComboBox

from munientry.controllers.helper_functions import (
    check_assignment_commissioner,
    check_case_list_selected,
    check_judicial_officer,
    set_random_judge,
)
from munientry.data.databases import (
    close_db_connection,
    create_daily_case_list_sql_tables,
    load_daily_case_list_data,
    open_db_connection,
    query_daily_case_list_data,
)
from munientry.settings import TYPE_CHECKING

if TYPE_CHECKING:
    from PyQt5.QtSql import QSqlDatabase


class MainWindowSlotFunctionsMixin(object):
    """Class that contains common functions for the main window."""

    def load_case_lists(self, db_connection: 'QSqlDatabase' = None) -> None:
        """Loads the cms_case numbers of all the cases that are in the daily_case_list databases.

        This does not load the cms_case data for each cms_case.

        The case count is one less than length of list because a blank line is inserted at the
        top of the case list. The case count becomes actual number of cases loaded.
        """
        if db_connection is None:
            db_connection = open_db_connection('con_daily_case_lists')
        for table_name, case_list in self.database_table_dict.items():
            old_case_count = len(case_list) - 1 if len(case_list) > 1 else 0
            case_list.clear()
            case_list.addItems(query_daily_case_list_data(table_name, db_connection))
            case_count = len(case_list) - 1
            logger.info(
                f'Table: {table_name} - Preload Cases: {old_case_count};'
                + f' Postload Cases {case_count}',
            )
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
        self.load_case_lists(conn)
        conn.close()

    def show_hide_daily_case_lists(self) -> None:
        selected_case_list = self.radio_buttons_case_lists_dict.get(
            self.sender(),
        )
        for case_list in self.radio_buttons_case_lists_dict.values():
            if case_list == selected_case_list:
                case_list.setEnabled(True)
                case_list.setHidden(False)
                case_list.setFocus()
            else:
                case_list.setCurrentText('')
                case_list.setHidden(True)
                case_list.setEnabled(False)

    def assign_judge(self) -> None:
        assigned_judge, time_now = set_random_judge()
        self.assign_judge_label.setText(assigned_judge)
        self.last_judge_assigned_label.setText(
            f'The last judge assigned was {assigned_judge}.\n'
            + f' The assignment was made at {time_now}.',
        )

    @check_judicial_officer
    @check_case_list_selected
    def start_dialog_from_entry_button(self) -> None:
        """The decorator checks prevent the dialog execution unless compliant.

        :check_judicial_officer: Requires that a judicial officer is selected.

        'check_case_list_selected: Requires that a daily case list is selected, if no case
        is needed then must select a case list with the field blank.
        """
        selected_case_table = self.database_table_dict.get(
            self.case_table, QComboBox,
        )
        cms_case_data = self.set_case_to_load(selected_case_table)
        self.dialog = self.crim_traffic_dialog_buttons_dict[self.sender()](
            self.judicial_officer,
            cms_case=cms_case_data,
            case_table=self.case_table,
        )
        dialog_name = self.dialog.objectName()
        logger.dialog(f'{dialog_name} Opened')
        self.dialog.exec()

    @check_assignment_commissioner
    @check_case_list_selected
    def start_scheduling_entry(self) -> None:
        selected_case_table = self.database_table_dict.get(
            self.case_table, QComboBox,
        )
        cms_case_data = self.set_case_to_load(selected_case_table)
        self.dialog = self.scheduling_dialog_buttons_dict[self.sender()](
            self.judicial_officer,
            cms_case=cms_case_data,
            case_table=self.case_table,
        )
        dialog_name = self.dialog.objectName()
        logger.dialog(f'{dialog_name} Opened')
        self.dialog.exec()

    def set_person_stack_widget(self) -> None:
        logger.action('Entry Tab Changed')
        judicial_officers = self.judicial_officers_Stack
        assignment_commissioners = self.assignment_commissioners_Stack
        if self.tabWidget.currentWidget().objectName() == 'crim_traffic_Tab':
            self.stackedWidget.setCurrentWidget(judicial_officers)
        if self.tabWidget.currentWidget().objectName() == 'scheduling_Tab':
            self.stackedWidget.setCurrentWidget(assignment_commissioners)
        current_stacked_widget = self.stackedWidget.currentWidget().objectName()
        current_tab_widget = self.tabWidget.currentWidget().objectName()
        logger.info(f'Current stackedWidget is {current_stacked_widget}')
        logger.info(f'Current tabWidget is {current_tab_widget}')
