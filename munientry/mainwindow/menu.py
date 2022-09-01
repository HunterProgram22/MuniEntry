"""Module containing all functions for the mainwindow menu."""
import os
from collections import namedtuple

from loguru import logger
from PyQt5.QtGui import QKeySequence
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QInputDialog, QShortcut, QTableWidgetItem

from munientry.data.connections import close_db_connection, open_db_connection
from munientry.data.excel_getters import clean_offense_name
from munientry.data.sql_server_queries import event_type_report_query
from munientry.mainwindow.batch_entries import run_batch_fta_arraignments
from munientry.settings import LOG_PATH, SAVE_PATH, USER_LOG_NAME
from munientry.widgets import message_boxes, table_widgets

EVENT_REPORT_HEADERS = ('Case Number', 'Defendant Name', 'Primary Charge')

# Arraignment - 27, Arraignment - 28, Continuance Arraignment - 77, Reset Case Arraignment - 361
ARRAIGNMENT_EVENT_IDS = "('27', '28', '77', '361')"

FINAL_PRETRIAL_EVENT_IDS = "('157', '160', '161')"


def open_current_log(signal=None) -> None:
    """Menu function that opens the user logs directly or with keyboard shortcut."""
    os.startfile(f'{LOG_PATH}{USER_LOG_NAME}')
    logger.info(f'Current system log opened.')


def open_batch_entries_folder(_signal=None) -> None:
    """Menu function that opens the folder where batch entries are saved."""
    os.startfile(f'{SAVE_PATH}batch\\')
    logger.info('Batch entries folder opened.')


def run_batch_fta_process(_signal=None) -> None:
    """Creates batch entries for failure to appear and opens folder where entries are saved."""
    entries_created = run_batch_fta_arraignments()
    message = f'The batch process created {entries_created} entries.'
    message_boxes.InfoBox(message, 'Entries Created').exec()
    os.startfile(f'{SAVE_PATH}batch\\')
    logger.info(f'{message}')


def create_event_report_window(
    data_list: list, report_name: str, report_date: str,
) -> table_widgets.ReportWindow:
    """Creates a window to load the event table and print buttons onto."""
    window = table_widgets.ReportWindow(
        len(data_list), 3, f'{report_name} Report for {report_date}',
    )
    window.table.setHorizontalHeaderLabels(list(EVENT_REPORT_HEADERS))
    Case = namedtuple('Case', 'case_number defendant_name primary_charge')
    for row, case in enumerate(data_list):
        case = Case(case[0], case[1], case[2])
        window.table.setItem(row, 0, QTableWidgetItem(case.case_number))
        window.table.setItem(row, 1, QTableWidgetItem(case.defendant_name))
        window.table.setItem(row, 2, QTableWidgetItem(case.primary_charge))
    return window


class MainWindowMenu(object):
    """Class for setting up the menu for the Main Window."""

    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        self.connect_menu_functions()

    def connect_menu_functions(self) -> None:
        self.log_shortcut = QShortcut(QKeySequence('Ctrl+L'), self.mainwindow)
        self.log_shortcut.activated.connect(open_current_log)
        self.mainwindow.actionOpen_Current_Log.triggered.connect(open_current_log)
        self.mainwindow.actionOpen_batch_FTA_Entries_Folder.triggered.connect(
            open_batch_entries_folder,
        )
        self.mainwindow.actionRun_batch_FTA_Entries.triggered.connect(run_batch_fta_process)
        self.mainwindow.actionArraignments.triggered.connect(self.run_arraignments_report)
        self.mainwindow.actionFinal_Pretrials.triggered.connect(self.run_final_pretrials_report)

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

    def get_report_date(self, report: str) -> str:
        event_date = QInputDialog.getText(
            self.mainwindow, f'{report} Date', f'Enter {report} Date in format YYYY-MM-DD:',
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

    def show_report_table(self, report_name: str, report_date: str, query_string: str) -> None:
        db = open_db_connection('con_authority_court')
        data_list = self.get_report_data(db, query_string)
        self.report_window = create_event_report_window(data_list, report_name, report_date)
        self.report_window.table.setSortingEnabled(True)
        self.report_window.show()
        close_db_connection(db)
