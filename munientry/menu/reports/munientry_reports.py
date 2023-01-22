"""Module for MuniEntry report menu processes."""
from collections import namedtuple

from loguru import logger
from PyQt6.QtSql import QSqlQuery
from PyQt6.QtWidgets import QInputDialog, QMainWindow, QTableWidgetItem

from munientry.data.connections import close_db_connection, open_db_connection
from munientry.menu.reports.report_constants import COURTROOM_REPORT_HEADERS, COURTROOM_NAME
from munientry.sqllite.sql_lite_queries import courtroom_event_report_query
from munientry.widgets.table_widgets import TableReportWindow


def run_courtroom_report(mainwindow: 'QMainWindow', courtroom: int) -> None:
    """Menu function that generates a report of Courtroom events for a given date.

    Args:
        mainwindow (QMainWindow): The main window of the application.

        courtroom (int): An integer that maps to the courtroom (1=A, 2=B, 3=C).
    """
    courtroom_name = COURTROOM_NAME.get(courtroom)
    report_date, ok_response = user_input_get_report_date(mainwindow, f'Courtroom {courtroom_name} Event')
    event = f'Courtroom {courtroom_name} Events'
    if ok_response:
        query_string = courtroom_event_report_query(report_date, courtroom)
        logger.info(query_string)
        data_list = get_courtroom_report_data(query_string)
        show_courtroom_report(mainwindow, event, report_date, data_list)


def user_input_get_report_date(mainwindow: 'QMainWindow', event: str) -> tuple[str, bool]:
    """Opens an input dialog to query user for date of report.

    Args:
        mainwindow (QMainWindow): The main window of the application.

        event (str): A string that identifies the event type for the generated report.

    Returns:
        tuple: A string with the user entered report data and a bool of True if the user
        selected 'Ok.'
    """
    return QInputDialog.getText(
        mainwindow,
        f'{event} Report',
        f'This report will query the MuniEntry Database for all {event} set for the date provided.\n'
        + f'Enter {event} Date in format YYYY-MM-DD:',
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