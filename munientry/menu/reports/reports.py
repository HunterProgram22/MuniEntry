"""Module for report menu processes."""
from collections import namedtuple

from loguru import logger
from PyQt6.QtCore import Qt
from PyQt6.QtSql import QSqlQuery
from PyQt6.QtWidgets import QInputDialog, QMainWindow, QTableWidgetItem

from munientry.data.connections import close_db_connection, open_db_connection
from munientry.data.data_cleaners import clean_offense_name
from munientry.menu.reports.comments import get_comment_writer
from munientry.menu.reports.report_constants import EVENT_IDS
from munientry.sqlserver.sql_server_queries import event_type_report_query
from munientry.widgets.table_widgets import TableReportWindow

EVENT_REPORT_HEADERS = ('Time', 'Case Number', 'Defendant Name', 'Primary Charge', 'Attorney', 'Comments')


def run_event_type_report(mainwindow: 'QMainWindow', event: str) -> None:
    """Menu function that generates a report of specific types of events.

    Args:
        mainwindow (QMainWindow): The main window of the application.

        event (str): A string that identifies the event type for the generated report.
    """
    report_date, ok_response = user_input_get_report_date(mainwindow, event)
    if ok_response:
        event_ids = EVENT_IDS.get(event)
        query_string = event_type_report_query(report_date, event_ids)
        logger.info(query_string)
        data_list = get_event_report_data(query_string, event)
        show_event_report(mainwindow, event, report_date, data_list)


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
        mainwindow, f'{event} Date', f'Enter {event} Date in format YYYY-MM-DD:',
    )


def get_event_report_data(query_string: str, event: str) -> list[tuple[str]]:
    """Queries the AuthorityCourtDB and loads case events for a specific date.

    Args:
        query_string (str): A SQLServer query string.

        event (str): The name of the event for the report query.

    Returns:
        list: A list of tuples containing the data queried from the AuthorityCourtDB.
    """
    db_conn = open_db_connection('con_authority_court')
    query = QSqlQuery(db_conn)
    query.prepare(query_string)
    query.exec()
    data_list = []
    comment_writer = get_comment_writer(event)
    while query.next():
        comment_field = comment_writer.get_comment(query)
        data_list.append(
            (
                query.value('Time'),
                query.value('CaseNumber'),
                query.value('DefFullName').title(),
                clean_offense_name(query.value('Charge')),
                query.value('DefenseCounsel').title(),
                comment_field,
            ),
        )
    close_db_connection(db_conn)
    return data_list


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


def create_event_report_window(data_list: list, report_name: str, report_date: str) -> TableReportWindow:
    """Creates a window to load the event table and contains print buttons."""
    window = TableReportWindow(f'{report_name} Report for {report_date}')
    window.table = window.add_table(len(data_list), 6, f'{report_name} Report for {report_date}', window)
    window.table.setHorizontalHeaderLabels(list(EVENT_REPORT_HEADERS))
    populate_report_data(window, data_list)
    return window


def populate_report_data(window, data_list):
    """Loads the data from the query into the table."""
    Case = namedtuple('Case', 'time case_number defendant_name primary_charge attorney_name comment_field')
    for row, case in enumerate(data_list):
        case = Case(case[0], case[1], case[2], case[3], case[4], case[5])
        window.table.setItem(row, 0, QTableWidgetItem(case.time))
        window.table.setItem(row, 1, QTableWidgetItem(case.case_number))
        window.table.setItem(row, 2, QTableWidgetItem(case.defendant_name))
        window.table.setItem(row, 3, QTableWidgetItem(case.primary_charge))
        window.table.setItem(row, 4, QTableWidgetItem(case.attorney_name))
        window.table.setItem(row, 5, QTableWidgetItem(case.comment_field))
