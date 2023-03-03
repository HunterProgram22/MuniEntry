"""Module for MuniEntry daily reports."""
from collections import namedtuple

from loguru import logger
from PyQt6.QtSql import QSqlQuery
from PyQt6.QtWidgets import QInputDialog, QMainWindow, QTableWidgetItem

from munientry.data.connections import close_db_connection, open_db_connection
from munientry.sqlserver.sql_server_queries import not_guilty_report_query
from munientry.widgets.table_widgets import TableReportWindow

def run_not_guilty_report(mainwindow: 'QMainWindow') -> None:
    """Menu function that generates a report of cases with a potentail not guilty for a given date.
    """
    report_date, ok_response = user_input_get_report_date(mainwindow, 'Not Guilty Report')
    event = f'Not Guilty Events'
    if ok_response:
        query_string = not_guilty_report_query(report_date, courtroom)
        logger.info(query_string)
        data_list = get_not_guilty_report_data(query_string)
        show_not_guilty_report(mainwindow, event, report_date, data_list)


def user_input_get_report_date(mainwindow: 'QMainWindow', event: str) -> tuple[str, bool]:
    """Opens an input dialog to query user for date of report."""
    return QInputDialog.getText(
        mainwindow,
        f'{event} Report',
        'This report will query all cases set for arraignment for the date entered and return cases'
        + ' that have a Journal Entry for that same date that is for a Not Guilty plea or a'
        + ' Continuance.\n\n'
        + f'Enter {event} Date in format YYYY-MM-DD:',
        )


def get_not_guilty_report_data(query_string: str) -> list[tuple[str]]:
    """Queries the AuthorityCourtDB and loads Journal Entry docket events for a specific date."""
    db_conn = open_db_connection('con_authority_court')
    query = QSqlQuery(db_conn)
    query.prepare(query_string)
    query.exec()
    data_list = []
    while query.next():
        data_list.append(
            (
                query.value('CaseNumber'),
                query.value('DefFullName'),
                query.value('Remark'),
            ),
        )
    close_db_connection(db_conn)
    return data_list


DAILY_REPORT_HEADERS = ('Case Number', 'Defendant Name', 'Docket Entry')


def create_daily_report_window(data_list: list, report_name: str, report_date: str) -> TableReportWindow:
    """Creates a window to load the event table and contains print buttons."""
    window = TableReportWindow(f'{report_name} Report for {report_date}',)
    window.table  = window.add_table(len(data_list), 4, f'{report_name} Report for {report_date}', window)
    window.table.setHorizontalHeaderLabels(list(DAILY_REPORT_HEADERS))

    Case = namedtuple('Case', 'case_number def_name remark')
    for row, case in enumerate(data_list):
        case = Case(case[0], case[1], case[2])
        window.table.setItem(row, 0, QTableWidgetItem(case.case_number))
        window.table.setItem(row, 1, QTableWidgetItem(case.def_name))
        window.table.setItem(row, 2, QTableWidgetItem(case.remark))
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
    mainwindow.report_window = create_daily_report_window(data_list, event, report_date)
    mainwindow.report_window.table.setSortingEnabled(True)
    mainwindow.report_window.show()
