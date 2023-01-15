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

from loguru import logger
from PyQt6.QtSql import QSqlQuery
from PyQt6.QtWidgets import QInputDialog, QTableWidgetItem
from PyQt6.QtCore import Qt

from munientry.data.connections import close_db_connection, open_db_connection
from munientry.data.data_cleaners import clean_offense_name
from munientry.sqllite.sql_lite_queries import courtroom_event_report_query
from munientry.sqlserver.sql_server_queries import event_type_report_query
from munientry.appsettings.paths import (
    BATCH_SAVE_PATH,
    CRIMTRAFFIC_SAVE_PATH,
    DRIVE_SAVE_PATH,
    JURY_PAY_SAVE_PATH,
    SCHEDULING_SAVE_PATH,
)
from munientry.appsettings.settings import TYPE_CHECKING
from munientry.widgets.table_widgets import TableReportWindow

if TYPE_CHECKING:
    from PyQt6.QtWidgets import QMainWindow

# Authority Court Database Event Codes

# Arraignment - 27, Arraignment - 28, Continuance Arraignment - 77, Reset Case Arraignment - 361
ARRAIGNMENT_EVENT_IDS = "('27', '28', '77', '361')"

# Final Pretrial A - 160, Final Pretrial B - 161, 335 is Pretrial/ALS for A, 336 is a Pretrial/ALS for B
FINAL_PRETRIAL_EVENT_IDS = "('160', '161', '335', '336')"

# Trial to Court A (TCN) - 412, Trial to Court B (TCNB) - 413, Trial to Court C (TCNC) 414
TRIAL_TO_COURT_EVENT_IDS = "('412', '413', '414')"


COURTROOM_REPORT_HEADERS = ('Event', 'Time', 'Case Number', 'Defendant Name')
EVENT_REPORT_HEADERS = ('Time', 'Case Number', 'Defendant Name', 'Primary Charge', 'Comments')

COURTROOM_NAME = types.MappingProxyType({
    1: 'A',
    2: 'B',
    3: 'C',
})

EVENT_IDS = types.MappingProxyType({
    'Arraignments': ARRAIGNMENT_EVENT_IDS,
    'Final Pretrials': FINAL_PRETRIAL_EVENT_IDS,
    'Trials To Court': TRIAL_TO_COURT_EVENT_IDS,
})

FOLDER_PATH = types.MappingProxyType({
    'batch_entries': BATCH_SAVE_PATH,
    'crimtraffic_entries': CRIMTRAFFIC_SAVE_PATH,
    'driving_privileges': DRIVE_SAVE_PATH,
    'jury_pay_entries': JURY_PAY_SAVE_PATH,
    'scheduling_entries': SCHEDULING_SAVE_PATH,
})


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
                query.value('event_type_name'),
                query.value('case_event_time'),
                query.value('case_number'),
                query.value('def_full_name'),
            ),
        )
    close_db_connection(db_conn)
    return data_list


def get_event_report_data(query_string: str) -> list[tuple[str, str, str, str]]:
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
        comment_field = get_comment_field(query)
        data_list.append(
            (
                query.value('Time'),
                query.value('CaseNumber'),
                query.value('DefFullName').title(),
                clean_offense_name(query.value('Charge')),
                comment_field,
            ),
        )
    close_db_connection(db_conn)
    return data_list


def get_comment_field(query) -> str:
    event = query.value('EventID')
    judge = query.value('JudgeID')  # Judge Rohrer = 31, Judge Hemmeter = 42
    match (event, judge):
        case (160, 42):  # Final pretrial for Judge H listed in Courtroom A
            return 'Possible Data Issue - Judge Hemmeter assigned, FPT in CMI is set for Courtroom A'
        case (161, 42):  # Final pretrial for Judge H listed in Courtroom B
            return 'Courtroom B'
        case (334, 42) | (335, 42) | (336, 42) | (337, 42):  # Pretrial/ALS code likely should be Final pretrial code
            return 'Possible Data Issue - Event in CMI is Pretrial/ALS - Should likely be FPTN2B'
        case (160, 31):  # Final pretrial for Judge R listed in Courtroom A
            return 'Courtroom A'
        case (161, 31):  # Final pretrial for Judge R listed in Courtroom B
            return 'Possible Data Issue - Judge Rohrer assigned, FPT in CMI is set for Courtroom B'
        case (334, 31) | (335, 31) | (336, 31) | (337 | 31):  # Pretrial/ALS code likely should be Final pretrial code
            return 'Possible Data Issue - Event in CMI is Pretrial/ALS - Should likely be FPTN2'
        case (414, 31) | (414, 42):  # Trial to Court in C with Judge Assigned
            return 'Courtroom C'
        case (414, 0) | (414, 0):  # Trial to Court in C with No Judge Assigned
            return 'Trial to Court in C but No Judge Assigned'
        case (412, 31):  # Trial to Court in A with Judge Rohrer Assigned
            return 'Courtroom A - Trial to Court with Judge Rohrer'
        case (413, 42):  # Trial to Court in B with Judge Hemmeter Assigned
            return 'Courtroom B - Trial to Court with Judge Hemmeter'
        case (160, 0) | (161, 0):
            return 'No Judge Assigned to Case'
        case (27, 0) | (28, 0):
            return 'Arraignment'
        case (77, 0):
            return 'Arraignment - Previously Continued'
        case (361, 0):
            return 'Arraignment - Reset due to FTA or Other Reason'
        case _:
            return 'Unclassified Possible Data Error in Case'


def create_courtroom_report_window(data_list: list, report_name: str, report_date: str) -> TableReportWindow:
    """Creates a window to load the event table and contains print buttons."""
    window = TableReportWindow(f'{report_name} Report for {report_date}',)
    window.table  = window.add_table(len(data_list), 4, f'{report_name} Report for {report_date}', window)
    window.table.setHorizontalHeaderLabels(list(COURTROOM_REPORT_HEADERS))

    Case = namedtuple('Case', 'event time case_number def_name')
    for row, case in enumerate(data_list):
        case = Case(case[0], case[1], case[2], case[3])
        window.table.setItem(row, 0, QTableWidgetItem(case.event))
        window.table.setItem(row, 1, QTableWidgetItem(case.time))
        window.table.setItem(row, 2, QTableWidgetItem(case.case_number))
        window.table.setItem(row, 3, QTableWidgetItem(case.def_name))
    return window


def create_event_report_window(data_list: list, report_name: str, report_date: str) -> TableReportWindow:
    """Creates a window to load the event table and contains print buttons."""
    window = TableReportWindow(f'{report_name} Report for {report_date}')
    window.table = window.add_table(len(data_list), 5, f'{report_name} Report for {report_date}', window)
    window.table.setHorizontalHeaderLabels(list(EVENT_REPORT_HEADERS))

    Case = namedtuple('Case', 'time case_number defendant_name primary_charge comment_field')
    for row, case in enumerate(data_list):
        case = Case(case[0], case[1], case[2], case[3], case[4])
        window.table.setItem(row, 0, QTableWidgetItem(case.time))
        window.table.setItem(row, 1, QTableWidgetItem(case.case_number))
        window.table.setItem(row, 2, QTableWidgetItem(case.defendant_name))
        window.table.setItem(row, 3, QTableWidgetItem(case.primary_charge))
        window.table.setItem(row, 4, QTableWidgetItem(case.comment_field))
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
    mainwindow.report_window.table.sortByColumn(0, Qt.SortOrder.AscendingOrder)
    mainwindow.report_window.show()
