"""Slot Functions for the MainWindow."""
from loguru import logger
from PyQt5.QtWidgets import QTableWidgetItem

from munientry.controllers.helper_functions import set_random_judge
from munientry.data import sql_lite_functions as sql_lite
from munientry.data import sql_server_getters as sql_server
from munientry.data.connections import close_db_connection, open_db_connection
from munientry.mainwindow.dialog_loader import DialogLoader, DialogPreloadChecker
from munientry.widgets.table_widgets import ReportWindow


class MainWindowSlotFunctionsMixin(object):
    """Class that contains common functions for the main window."""

    def load_case_lists(self, db_connection=None) -> None:
        """Loads the cms_case numbers of all the cases that are in the daily_case_list databases.

        This does not load the cms_case data for each cms_case.

        The case count is one less than length of list because a blank line is inserted at the
        top of the case list. The case count becomes actual number of cases loaded.
        """
        if db_connection is None:
            db_connection = open_db_connection('con_daily_case_lists')
        for case_list in self.daily_case_lists:
            old_case_count = len(case_list) - 1 if len(case_list) > 1 else 0
            case_list.clear()
            case_list.addItems(sql_lite.query_daily_case_list_data(case_list.name, db_connection))
            case_count = len(case_list) - 1
            logger.info(
                f'Table: {case_list.name} - Preload Cases: {old_case_count};'
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
        sql_lite.load_daily_case_list_data(conn)
        self.load_case_lists(conn)
        conn.close()

    def show_hide_daily_case_lists(self) -> None:
        for case_list in self.daily_case_lists:
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

    def start_crim_traffic_entry(self) -> None:
        """Starts a criminal/traffic dialog based on the dialog button that is pressed."""
        if DialogPreloadChecker(self).crimtraffic_checks():
            return DialogLoader(self).load_crimtraffic_entry()

    def start_scheduling_entry(self) -> None:
        """Starts a scheduling dialog based on the dialog button that is pressed."""
        if DialogPreloadChecker(self).scheduling_checks():
            return DialogLoader(self).load_scheduling_entry()

    def start_admin_entry(self) -> None:
        """Starts a admin dialog based on the dialog button that is pressed."""
        if DialogPreloadChecker(self).admin_checks():
            return DialogLoader(self).load_admin_entry()

    def set_person_stack_widget(self) -> None:
        logger.action('Entry Tab Changed')
        judicial_officers = self.judicial_officers_Stack
        assignment_commissioners = self.assignment_commissioners_Stack
        admin_staff = self.admin_staff_Stack
        if self.tabWidget.currentWidget().objectName() == 'crim_traffic_Tab':
            self.stackedWidget.setCurrentWidget(judicial_officers)
        if self.tabWidget.currentWidget().objectName() == 'scheduling_Tab':
            self.stackedWidget.setCurrentWidget(assignment_commissioners)
        if self.tabWidget.currentWidget().objectName() == 'admin_Tab':
            self.stackedWidget.setCurrentWidget(admin_staff)
        current_stacked_widget = self.stackedWidget.currentWidget().objectName()
        current_tab_widget = self.tabWidget.currentWidget().objectName()
        logger.info(f'Current stackedWidget is {current_stacked_widget}')
        logger.info(f'Current tabWidget is {current_tab_widget}')

    def query_case_info(self):
        """Queries the SQL Server database (AuthorityCourtDBO) and retreives case info."""
        case_number = self.case_search_box.text()
        case_number = update_case_number(case_number)
        self.case_search_box.setText(case_number)
        cms_case_data = sql_server.CriminalCaseSQLServer(case_number).load_case()
        self.set_case_info_from_search(cms_case_data)

    def set_case_info_from_search(self, cms_case_data) -> None:
        """Sets the case search fields on the UI with data from the case that is retrieved."""
        self.case_number_label_field.setText(cms_case_data.case_number)
        def_first_name = cms_case_data.defendant.first_name
        def_last_name = cms_case_data.defendant.last_name
        self.case_name_label_field.setText(f'State of Ohio v. {def_first_name} {def_last_name}')
        charge_list_text = ', '.join(str(charge[0]) for charge in cms_case_data.charges_list)
        self.case_charges_label_field.setText(charge_list_text)

    def show_case_docket_case_list(self):
        """TODO: ValueError catch put in to handle empty daily case list - fix daily case lists."""
        try:
            last_name, case_number = self.daily_case_list.currentText().split(' - ')
        except ValueError as err:
            logger.warning(err)
            return None
        self.show_case_docket(case_number)

    def show_case_docket(self, case_number=None):
        if case_number is None:
            case_number = self.case_search_box.text()
            case_number = update_case_number(case_number)
            self.case_search_box.setText(case_number)
        data_list = sql_server.CaseDocketSQLServer(case_number).get_docket()
        rows = len(data_list)
        self.window = ReportWindow(rows, 2, f'Docket Report for {case_number}')
        header_labels = ['Date', 'Docket Description']
        self.window.table.setHorizontalHeaderLabels(header_labels)
        for row, docket_item in enumerate(data_list):
            docket_item_stripped = ' '.join(docket_item[1].splitlines())
            docket_item_stripped = docket_item_stripped.title()
            docket_date = QTableWidgetItem(docket_item[0])
            docket_descr = QTableWidgetItem()
            docket_descr.setText(docket_item_stripped)
            docket_descr.setToolTip(docket_item[1])
            self.window.table.setItem(row, 0, docket_date)
            self.window.table.setItem(row, 1, docket_descr)
        self.window.show()


def update_case_number(case_number: str) -> str:
    """Updates the case number in case search to add 0's if full case number not provided."""
    zero_insert_dict = {
        9: '0',
        8: '00',
        7: '000',
        6: '0000',
    }
    case_number_length = len(case_number)
    if case_number_length == 10:
        return case_number
    elif zero_insert_dict.get(case_number_length) is not None:
        return case_number[:5] + zero_insert_dict.get(case_number_length) + case_number[5:]
    return case_number
