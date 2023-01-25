"""Slot Functions for the MainWindow."""
from loguru import logger
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtSql import QSqlQuery

from munientry.data.data_cleaners import clean_last_name
from munientry.sqllite import sql_lite_functions as sql_lite
from munientry.sqlserver import civil_getters as civil
from munientry.sqlserver import sql_server_getters as sql_server
from munientry.sqlserver import sql_server_queries as sql_query
from munientry.data.connections import close_db_connection, open_db_connection
from munientry.helper_functions import set_random_judge
from munientry.widgets.table_widgets import ReportWindow


class MainWindowSlotFunctionsMixin(object):
    """Class that contains common functions for the main window."""

    def load_case_lists(self) -> None:
        """Loads the cms_case numbers of all the cases that are in the daily_case_list databases.

        This does not load the cms_case data for each cms_case.

        The case count is one less than length of list because a blank line is inserted at the
        top of the case list. The case count becomes actual number of cases loaded.
        """
        db_connection = open_db_connection('con_authority_court')
        STORED_PROC_DICT = {
            self.arraignments_cases_box: '[reports].[DMCMuniEntryArraignment]',
            self.slated_cases_box: '[reports].[DMCMuniEntrySlated]',
            self.pleas_cases_box: '[reports].[DMCMuniEntryPleas]',
            self.pcvh_fcvh_cases_box: '[reports].[DMCMuniEntryPrelimCommContViolHearings]',
            self.final_pretrial_cases_box: '[reports].[DMCMuniEntryFinalPreTrials]',
            self.trials_to_court_cases_box: '[reports].[DMCMuniEntryBenchTrials]',
        }

        for case_list in self.daily_case_lists:
            stored_proc = STORED_PROC_DICT.get(case_list)
            query_string = sql_query.daily_case_list_query(stored_proc)
            self.query = QSqlQuery(db_connection)
            self.query.prepare(query_string)
            self.query.exec()
            daily_case_list = []
            while self.query.next():
                case_number = self.query.value('CaseNumber')
                last_name = self.query.value('LastName').title()
                last_name = clean_last_name(last_name)
                case = f'{last_name} - {case_number}'
                daily_case_list.append(case)

            daily_case_list.insert(0, '')
            old_case_count = len(case_list) - 1 if len(case_list) > 1 else 0
            daily_case_list = sorted(daily_case_list)
            case_list.clear()
            case_list.addItems(daily_case_list)
            case_count = len(case_list) - 1
            logger.info(
                f'Table: {case_list.name} - Preload Cases: {old_case_count};'
                + f' Postload Cases {case_count}',
            )
        close_db_connection(db_connection)

    def reload_case_lists(self) -> None:
        """This method is connected to the reload cases button and calls load_case_lists."""
        logger.info('Reload cases button pressed.')
        self.load_case_lists()

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

        logger.debug(self.tabWidget.currentWidget().objectName())
        if self.search_tabWidget.currentWidget().objectName() == 'case_search_tab':
            case_number = self.case_search_box.text()
            case_number = update_case_number(case_number)
            self.case_search_box.setText(case_number)
            cms_case_data = sql_server.CriminalCaseSqlServer(case_number).load_case()
            self.set_case_info_from_search(cms_case_data)

        elif self.search_tabWidget.currentWidget().objectName() == 'civil_case_search_tab':
            case_number = self.civil_case_search_box.text()
            cms_case_data = civil.CivilCaseSqlServer(case_number).load_case()
            self.set_civil_case_info_from_search(cms_case_data)

    def set_case_info_from_search(self, cms_case_data) -> None:
        """Sets the case search fields on the UI with data from the case that is retrieved."""
        self.case_number_label_field.setText(cms_case_data.case_number)
        def_first_name = cms_case_data.defendant.first_name
        def_last_name = cms_case_data.defendant.last_name
        self.case_name_label_field.setText(f'State of Ohio v. {def_first_name} {def_last_name}')
        charge_list_text = ', '.join(str(charge[0]) for charge in cms_case_data.charges_list)
        self.case_charges_label_field.setText(charge_list_text)

    def set_civil_case_info_from_search(self, cms_case_data):
        self.civil_case_number_label_field.setText(cms_case_data.case_number)
        logger.debug('civil called')

    def show_case_docket_case_list(self):
        """Value Error catch put in to handle if the empty slot of daily case list is selected."""
        try:
            last_name, case_number = self.daily_case_list.currentText().split(' - ')
        except ValueError as err:
            logger.warning(err)
            case_number = ''
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
    if len(case_number) == 10:
        return case_number.upper()
    crim_letter_list = ['B', 'b']
    if any(letter in case_number for letter in crim_letter_list):
        try:
            case_year, case_five_number = case_number.split('b')
        except ValueError:
            case_year, case_five_number = case_number.split('B')
        case_year = case_year[:2]
        case_code = 'CRB'
        return reset_case_number(case_year, case_code, case_five_number)
    ovi_letter_list = ['C', 'c']
    if any(letter in case_number for letter in ovi_letter_list):
        try:
            case_year, case_five_number = case_number.split('c')
        except ValueError:
            case_year, case_five_number = case_number.split('C')
        case_year = case_year[:2]
        case_code = 'TRC'
        return reset_case_number(case_year, case_code, case_five_number)
    traffic_letter_list = ['D', 'd']
    if any(letter in case_number for letter in traffic_letter_list):
        try:
            case_year, case_five_number = case_number.split('d')
        except ValueError:
            case_year, case_five_number = case_number.split('D')
        case_year = case_year[:2]
        case_code = 'TRD'
        return reset_case_number(case_year, case_code, case_five_number)


def reset_case_number(case_year: str, case_code: str, case_five_number: str) -> str:
    """Adds 0's to the last 5 digits of a case number to make it 5 digits.

    22TRC1 -> 22TRC00001
    22CRB12 -> 22CRB00012
    22TRD205 -> 22TRD00205
    """
    match len(case_five_number):
        case 5:
            return f'{case_year}{case_code}{case_five_number}'
        case 4:
            return f'{case_year}{case_code}0{case_five_number}'
        case 3:
            return f'{case_year}{case_code}00{case_five_number}'
        case 2:
            return f'{case_year}{case_code}000{case_five_number}'
        case 1:
            return f'{case_year}{case_code}0000{case_five_number}'
