"""Actions that are triggered by a menu function."""
import os
from collections import namedtuple

from loguru import logger
from PyQt6.QtSql import QSqlQuery
from PyQt6.QtWidgets import QInputDialog, QTableWidgetItem

from munientry.data.connections import close_db_connection, open_db_connection
from munientry.data.excel_getters import clean_offense_name
from munientry.data.sql_lite_queries import courtroom_event_report_query
from munientry.data.sql_server_queries import event_type_report_query
from munientry.paths import (
    BATCH_SAVE_PATH,
    CRIMTRAFFIC_SAVE_PATH,
    DRIVE_SAVE_PATH,
    JURY_PAY_SAVE_PATH,
    SCHEDULING_SAVE_PATH,
)
from munientry.widgets import table_widgets

# Arraignment - 27, Arraignment - 28, Continuance Arraignment - 77, Reset Case Arraignment - 361
ARRAIGNMENT_EVENT_IDS = "('27', '28', '77', '361')"
FINAL_PRETRIAL_EVENT_IDS = "('157', '160', '161')"

EVENT_IDS = {
    'Arraignments': ARRAIGNMENT_EVENT_IDS,
    'Final Pretrials': FINAL_PRETRIAL_EVENT_IDS,
}

FOLDER_PATH = {
    'batch_entries': BATCH_SAVE_PATH,
    'crimtraffic_entries': CRIMTRAFFIC_SAVE_PATH,
    'driving_privileges': DRIVE_SAVE_PATH,
    'jury_pay_entries': JURY_PAY_SAVE_PATH,
    'scheduling_entries': SCHEDULING_SAVE_PATH,
}

EVENT_REPORT_HEADERS = ('Case Number', 'Defendant Name', 'Primary Charge')


COURTROOM_NAME = {
    1: 'A',
    2: 'B',
    3: 'C',
}


def open_entries_folder(folder, _singal=None):
    """Menu function that opens the chosen folder where the chosen entries are saved."""
    folder_path = FOLDER_PATH.get(folder)
    os.startfile(f'{folder_path}')
    logger.info(f'The {folder} folder was opened.')


def run_event_type_report(mainwindow, event) -> None:
    report_date = get_report_date(mainwindow, event)
    event_ids = EVENT_IDS.get(event)
    query_string = event_type_report_query(report_date, event_ids)
    logger.info(query_string)
    show_report_table(mainwindow, event, report_date, query_string)


def get_report_date(mainwindow, report: str) -> str:
    event_date = QInputDialog.getText(
        mainwindow, f'{report} Date', f'Enter {report} Date in format YYYY-MM-DD:',
    )
    return event_date[0]


def show_report_table(mainwindow, report_name: str, report_date: str, query_string: str) -> None:
    db = open_db_connection('con_authority_court')
    data_list = get_report_data(db, query_string)
    mainwindow.report_window = create_event_report_window(data_list, report_name, report_date)
    mainwindow.report_window.table.setSortingEnabled(True)
    mainwindow.report_window.show()
    close_db_connection(db)


def get_report_data(db, query_string: str) -> list:
    query = QSqlQuery(db)
    query.prepare(query_string)
    query.exec()
    data_list = []
    while query.next():
        data_list.append(
            (
                query.value('CaseNumber'),
                query.value('DefFullName').title(),
                clean_offense_name(query.value('Charge')),
            ),
        )
    return data_list


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


def run_courtroom_report(mainwindow, courtroom: int) -> None:
    courtroom_name = COURTROOM_NAME.get(courtroom)
    report_date = get_report_date(mainwindow, f'Courtroom {courtroom_name} Event')
    query_string = courtroom_event_report_query(report_date, courtroom)
    logger.info(query_string)
    show_courtroom_events(mainwindow, f'Courtroom {courtroom_name} Events', report_date, query_string)


def show_courtroom_events(mainwindow, report_name: str, report_date: str, query_string: str) -> None:
    db = open_db_connection('con_munientry_db')
    data_list = get_courtroom_report_data(db, query_string)
    mainwindow.report_window = create_courtroom_report_window(data_list, report_name, report_date)
    mainwindow.report_window.table.setSortingEnabled(True)
    mainwindow.report_window.show()
    close_db_connection(db)


def get_courtroom_report_data(db, query_string: str) -> list:
    query = QSqlQuery(db)
    query.prepare(query_string)
    query.exec()
    data_list = []
    while query.next():
        data_list.append(
            (
                query.value('case_number'),
                query.value('event_type_name'),
                query.value('case_event_time'),
            ),
        )
    return data_list


COURTROOM_REPORT_HEADERS = ('Case Number', 'Event', 'Time')


def create_courtroom_report_window(
        data_list: list, report_name: str, report_date: str,
) -> table_widgets.ReportWindow:
    """Creates a window to load the event table and print buttons onto."""
    window = table_widgets.ReportWindow(
        len(data_list), 3, f'{report_name} Report for {report_date}',
    )
    window.table.setHorizontalHeaderLabels(list(COURTROOM_REPORT_HEADERS))
    Case = namedtuple('Case', 'case_number event time')
    for row, case in enumerate(data_list):
        case = Case(case[0], case[1], case[2])
        window.table.setItem(row, 0, QTableWidgetItem(case.case_number))
        window.table.setItem(row, 1, QTableWidgetItem(case.event))
        window.table.setItem(row, 2, QTableWidgetItem(case.time))
    return window
