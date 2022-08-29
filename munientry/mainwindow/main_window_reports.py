"""Report Functions for the MainWindow."""
from collections import namedtuple

from loguru import logger
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QInputDialog, QTableWidgetItem

from munientry.data.connections import close_db_connection, open_db_connection
from munientry.data.excel_getters import clean_offense_name
from munientry.data.sql_server_queries import event_type_report_query
from munientry.widgets.table_widgets import ReportTable, ReportWindow

EVENT_REPORT_HEADERS = ('Case Number', 'Defendant Name', 'Primary Charge')
ARRAIGNMENT_EVENT_IDS = "('27', '28')"
FINAL_PRETRIAL_EVENT_IDS = "('157', '160', '161')"


class MainWindowReportsMixin(object):
    """Class that contains common report functions for the main window."""

    def get_report_date(self, report: str) -> str:
        event_date = QInputDialog.getText(
            self, f'{report} Date', f'Enter {report} Date in format YYYY-MM-DD:',
        )
        return event_date[0]

    def get_report_data(self, db, query_string: str) -> list:
        self.query = QSqlQuery(db)
        self.query.prepare(query_string)
        self.query.exec()
        data_list = []
        while self.query.next():
            data_list.append(
                (
                    self.query.value('CaseNumber'),
                    self.query.value('DefFullName').title(),
                    clean_offense_name(self.query.value('Charge')),
                ),
            )
        return data_list

    def create_event_report_table(
        self, data_list: list, report_name: str, report_date: str,
    ) -> ReportWindow:
        window = ReportWindow(len(data_list), 3, f'{report_name} Report for {report_date}')
        window.table.setHorizontalHeaderLabels(list(EVENT_REPORT_HEADERS))
        Case = namedtuple('Case', 'case_number defendant_name primary_charge')
        for row, case in enumerate(data_list):
            case = Case(case[0], case[1], case[2])
            window.table.setItem(row, 0, QTableWidgetItem(case.case_number))
            window.table.setItem(row, 1, QTableWidgetItem(case.defendant_name))
            window.table.setItem(row, 2, QTableWidgetItem(case.primary_charge))
        return window

    def run_arraignments_report(self) -> None:
        report_date = self.get_report_date('Arraignments')
        query_string = event_type_report_query(report_date, ARRAIGNMENT_EVENT_IDS)
        logger.info(query_string)
        self.show_report_table('Arraignments', report_date, query_string)

    def run_final_pretrials_report(self) -> None:
        report_date = self.get_report_date('Final Pretrials')
        query_string = event_type_report_query(report_date, FINAL_PRETRIAL_EVENT_IDS)
        logger.info(query_string)
        self.show_report_table('Final Pretrials', report_date, query_string)

    def show_report_table(self, report_name: str, report_date: str, query_string: str) -> None:
        db = open_db_connection('con_authority_court')
        data_list = self.get_report_data(db, query_string)
        self.report_window = self.create_event_report_table(data_list, report_name, report_date)
        self.report_window.table.setSortingEnabled(True)
        self.report_window.show()
        close_db_connection(db)
