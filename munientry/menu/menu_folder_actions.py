"""Actions that are triggered by a menu function.

**munientry.menu.menu_folder_actions**

Functions:
    open_entries_folder(folder, _signal) -> None

    run_courtroom_report(mainwindow, courtroom) -> None

    run_event_type_report(mainwindow, event) -> None

    get_report_date(mainwindow, event) -> tuple[str, bool]

    get_courtroom_report_data(query_string) -> list[tuple[str, str, str]]

    get_event_report_data(query_string) -> list[tuple[str, str, str]]

    create_courtroom_report_window(data_list, report_name, report_date) -> ReportWindow

    create_event_report_window(data_list, report_name, report_date) -> ReportWindow

    show_courtroom_report(mainwindow, event, report_date, data_list) -> None

    show_event_report(mainwindow, event, report_date, data_list) -> None
"""
import types
from collections import namedtuple
from os import startfile

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
from munientry.settings import TYPE_CHECKING
from munientry.widgets import table_widgets

if TYPE_CHECKING:
    from PyQt6.QtWidgets import QMainWindow

# Arraignment - 27, Arraignment - 28, Continuance Arraignment - 77, Reset Case Arraignment - 361
ARRAIGNMENT_EVENT_IDS = "('27', '28', '77', '361')"
FINAL_PRETRIAL_EVENT_IDS = "('157', '160', '161')"

COURTROOM_REPORT_HEADERS = ('Case Number', 'Event', 'Time')
EVENT_REPORT_HEADERS = ('Case Number', 'Defendant Name', 'Primary Charge')

COURTROOM_NAME = types.MappingProxyType({
    1: 'A',
    2: 'B',
    3: 'C',
})

EVENT_IDS = types.MappingProxyType({
    'Arraignments': ARRAIGNMENT_EVENT_IDS,
    'Final Pretrials': FINAL_PRETRIAL_EVENT_IDS,
})

FOLDER_PATH = types.MappingProxyType({
    'batch_entries': BATCH_SAVE_PATH,
    'crimtraffic_entries': CRIMTRAFFIC_SAVE_PATH,
    'driving_privileges': DRIVE_SAVE_PATH,
    'jury_pay_entries': JURY_PAY_SAVE_PATH,
    'scheduling_entries': SCHEDULING_SAVE_PATH,
})


def open_entries_folder(folder: str, _singal=None) -> None:
    """Menu function that opens the folder where specific types of entries are saved.

    Args:
        folder (str): A string that identifies the type entry folder to open.
    """
    folder_path = FOLDER_PATH.get(folder)
    startfile(f'{folder_path}')
    logger.info(f'The {folder} folder was opened.')


def run_courtroom_report(mainwindow: 'QMainWindow', courtroom: int) -> None:
    """Menu function that generates a report of Courtroom events for a given date.

    Args:
        mainwindow (QMainWindow): The main window of the application.

        courtroom (int): An integer that maps to the courtroom (1=A, 2=B, 3=C).
    """
    courtroom_name = COURTROOM_NAME.get(courtroom)
    report_date, ok_response = get_report_date(mainwindow, f'Courtroom {courtroom_name} Event')
    event = f'Courtroom {courtroom_name} Events'
    if ok_response:
        query_string = courtroom_event_report_query(report_date, courtroom)
        logger.info(query_string)
        data_list = get_courtroom_report_data(query_string)
        show_courtroom_report(mainwindow, event, report_date, data_list)


def run_event_type_report(mainwindow: 'QMainWindow', event: str) -> None:
    """Menu function that generates a report of specific types of events.

    Args:
        mainwindow (QMainWindow): The main window of the application.

        event (str): A string that identifies the event type for the generated report.
    """
    report_date, ok_response = get_report_date(mainwindow, event)
    if ok_response:
        event_ids = EVENT_IDS.get(event)
        query_string = event_type_report_query(report_date, event_ids)
        logger.info(query_string)
        data_list = get_event_report_data(query_string)
        show_event_report(mainwindow, event, report_date, data_list)


def get_report_date(mainwindow: 'QMainWindow', event: str) -> tuple[str, bool]:
    """Opens an input dialog to query user for date of report.

    Args:
        mainwindow (QMainWindow): The main window of the application.

        event (str): A string that identifies the event type for the generated report.

    Returns:
        tuple: A string with the user entered report data and a bool of True if the user
        selected 'Ok.'
    """
    return QInputDialog.getText(
        mainwindow, f'{event} Date', f'Enter {event} Date in format YYYY-MM-DD:',
    )


def get_courtroom_report_data(query_string: str) -> list[tuple[str, str, str]]:
    """Queries the MuniEntryDB and loads courtroom events for a specific date.

    Args:
        query_string (str): A SQLite query string.

    Returns:
        list: A list of tuples containing the data queried from the MuniEntryDB.
    """
    db_conn = open_db_connection('con_munientry_db')
    query = QSqlQuery(db_conn)
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
    close_db_connection(db_conn)
    return data_list


def get_event_report_data(query_string: str) -> list[tuple[str, str, str]]:
    """Queries the AuthorityCourtDB and loads case events for a specific date.

    Args:
        query_string (str): A SQLServer query string.

    Returns:
        list: A list of tuples containing the data queried from the AuthorityCourtDB.
    """
    db_conn = open_db_connection('con_authority_court')
    query = QSqlQuery(db_conn)
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
    close_db_connection(db_conn)
    return data_list


def create_courtroom_report_window(
    data_list: list, report_name: str, report_date: str,
) -> table_widgets.ReportWindow:
    """Creates a window to load the event table and contains print buttons."""
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


def create_event_report_window(
    data_list: list, report_name: str, report_date: str,
) -> table_widgets.ReportWindow:
    """Creates a window to load the event table and contains print buttons."""
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


def show_courtroom_report(
    mainwindow: 'QMainWindow', event: str, report_date: str, data_list: list,
) -> None:
    """Shows a sortable table loaded with the data for the generated report.

    Args:
        mainwindow (QMainWindow): The main window of the application.

        event (str): A string that identifies the event type for the generated report.

        report_date (str): A string of the date for the report.

        data_list (list): A list of all data queried from the database.
    """
    mainwindow.report_window = create_courtroom_report_window(data_list, event, report_date)
    mainwindow.report_window.table.setSortingEnabled(True)
    mainwindow.report_window.show()


def show_event_report(
    mainwindow: 'QMainWindow', event: str, report_date: str, data_list: list,
) -> None:
    """Shows a sortable table loaded with the data for the generated report.

    Args:
        mainwindow (QMainWindow): The main window of the application.

        event (str): A string that identifies the event type for the generated report.

        report_date (str): A string of the date for the report.

        data_list (list): A list of all data queried from the database.
    """
    mainwindow.report_window = create_event_report_window(data_list, event, report_date)
    mainwindow.report_window.table.setSortingEnabled(True)
    mainwindow.report_window.show()