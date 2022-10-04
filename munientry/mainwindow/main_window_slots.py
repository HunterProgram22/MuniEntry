"""Slot Functions for the MainWindow."""
from loguru import logger
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import (
    QDialog,
    QTableWidgetItem,
)

from munientry.controllers.helper_functions import set_random_judge
from munientry.data.connections import close_db_connection, open_db_connection
from munientry.data.sql_lite_functions import (
    load_daily_case_list_data,
    query_daily_case_list_data,
)
from munientry.data.sql_server_getters import CriminalCaseSQLServer, DrivingInfoSQLServer
from munientry.data.sql_server_queries import get_case_docket_query
from munientry.settings import TYPE_CHECKING
from munientry.widgets.message_boxes import RequiredBox
from munientry.widgets.table_widgets import ReportWindow

if TYPE_CHECKING:
    from PyQt5.QtSql import QSqlDatabase

    from munientry.models.cms_models import CmsCaseInformation


class DialogLoader(object):
    """Loads the Dialog that is selected from the Main Window UI."""

    def __init__(self, mainwindow):
        self.mainwindow = mainwindow

    def load_crimtraffic_entry(self):
        button_dict = self.mainwindow.crim_traffic_dialog_buttons_dict
        return self.set_dialog(button_dict)

    def load_scheduling_entry(self):
        button_dict = self.mainwindow.scheduling_dialog_buttons_dict
        return self.set_dialog(button_dict)

    def load_admin_entry(self):
        button_dict = self.mainwindow.admin_dialog_buttons_dict
        return self.set_dialog(button_dict)

    def set_dialog(self, button_dict):
        if self.mainwindow.search_tabWidget.currentWidget().objectName() == 'case_search_tab':
            self.mainwindow.dialog = self.set_dialog_from_case_search(button_dict)
        else:
            self.mainwindow.dialog = self.set_dialog_from_daily_case_list(button_dict)
        try:
            dialog_name = self.mainwindow.dialog.objectName()
        except AttributeError as err:
            logger.warning(err)
            return None
        logger.dialog(f'{dialog_name} Opened')
        return self.mainwindow.dialog.exec()

    def set_dialog_from_daily_case_list(self, button_dict: dict) -> QDialog:
        """Sets the case to be loaded from the daily case list tab."""
        if not any(case_list.radio_button.isChecked() for case_list in self.mainwindow.daily_case_lists):
            return RequiredBox(
                'You must select a case list. If not loading a case in the case list '
                + 'leave the case list field blank.', 'Daily Case List Required',
            ).exec()
        cms_case_data = self.mainwindow.set_case_to_load(self.mainwindow.daily_case_list)
        logger.info(cms_case_data)
        return button_dict[self.mainwindow.sender()](
            self.mainwindow.judicial_officer,
            cms_case=cms_case_data,
            case_table=self.mainwindow.daily_case_list.name,
        )

    def set_dialog_from_case_search(self, button_dict: dict) -> QDialog:
        """Sets the case to be loaded from the case search tab."""
        logger.debug(self.mainwindow.sender().objectName())
        case_number = self.mainwindow.case_search_box.text()
        if self.mainwindow.sender().objectName() == 'limited_driving_privilegesButton':
            cms_case_data = DrivingInfoSQLServer(case_number).load_case()
        else:
            cms_case_data = CriminalCaseSQLServer(case_number).load_case()
        logger.info(cms_case_data)
        return button_dict[self.mainwindow.sender()](
            self.mainwindow.judicial_officer,
            cms_case=cms_case_data,
            case_table=None,
        )


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
        for case_list in self.daily_case_lists:
            old_case_count = len(case_list) - 1 if len(case_list) > 1 else 0
            case_list.clear()
            case_list.addItems(query_daily_case_list_data(case_list.name, db_connection))
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
        load_daily_case_list_data(conn)
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
        """Starts a criminal/traffic dialog based on the dialog button that is pressed.

        TODO: Refactor and fix signature on return.
        """
        if self.judicial_officer is None:
            return RequiredBox(
                'You must select a judicial officer.', 'Judicial Officer Required',
            ).exec()
        if self.judicial_officer.officer_type == 'Assignment Commissioner':
            return RequiredBox(
                'You must select a judicial officer.', 'Judicial Officer Required',
            ).exec()
        return DialogLoader(self).load_crimtraffic_entry()

    def start_scheduling_entry(self) -> None:
        """Starts a scheduling dialog based on the dialog button that is pressed."""
        if self.judicial_officer is None:
            return RequiredBox(
                'You must select an assignment commissioner.', 'Assignment Commissioner Required',
            ).exec()
        if self.judicial_officer.officer_type != 'Assignment Commissioner':
            return RequiredBox(
                'You must select an assignment commissioner.', 'Assignment Commissioner Required',
            ).exec()
        return DialogLoader(self).load_scheduling_entry()

    def start_admin_entry(self) -> None:
        """Starts a admin dialog based on the dialog button that is pressed."""
        if self.judicial_officer is None:
            return RequiredBox(
                'You must select an assignment commissioner.', 'Assignment Commissioner Required',
            ).exec()
        if self.judicial_officer.officer_type != 'Assignment Commissioner':
            return RequiredBox(
                'You must select an assignment commissioner.', 'Assignment Commissioner Required',
            ).exec()
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
        cms_case_data = CriminalCaseSQLServer(case_number).load_case()
        self.set_case_info_from_search(cms_case_data)

    def set_case_info_from_search(self, cms_case_data: 'CmsCaseInformation') -> None:
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
        db = open_db_connection('con_authority_court')
        query_string = get_case_docket_query(case_number)
        logger.info(query_string)
        self.query = QSqlQuery(db)
        self.query.prepare(query_string)
        self.query.exec()
        data_list = []
        while self.query.next():
            docket_item = (self.query.value('Date'), self.query.value('Remark'))
            data_list.append(docket_item)

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
        close_db_connection(db)

def update_case_number(case_number: str) -> str:
    zero_insert_dict = {
        9: '0',
        8: '00',
        7: '000',
        6: '0000',
    }
    case_number_length = len(case_number)
    if case_number_length== 10:
        return case_number
    elif zero_insert_dict.get(case_number_length) is not None:
        return case_number[:5] + zero_insert_dict.get(case_number_length)+ case_number[5:]
    return case_number
