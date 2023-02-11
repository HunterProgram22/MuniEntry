"""Module for creating a batch of Failure to Appear entries."""
import datetime
from os import startfile

from PyQt6.QtWidgets import QInputDialog
from docxtpl import DocxTemplate
from loguru import logger

from munientry.data.excel_functions import (
    create_headers_dict,
    get_excel_file_headers,
    load_active_worksheet,
)
from munientry.models.excel_models import BatchCaseInformation
from munientry.appsettings.settings import TYPE_CHECKING
from munientry.appsettings.paths import BATCH_SAVE_PATH, DB_PATH, TEMPLATE_PATH
from munientry.sqlserver.sql_server_queries import batch_fta_query
from munientry.widgets import message_boxes

if TYPE_CHECKING:
    from openpyxl import Workbook

COL_CASE_NUMBER = 'CaseNumber'
COL_CASE_TYPE = 'CaseTypeCode'
COL_EVENT_DATE = 'CaseEventDate'
COL_DEF_LAST_NAME = 'DefLastName'
COL_DEF_FIRST_NAME = 'DefFirstName'


def create_entry(case_data):
    """General create entry function that populates a template with data."""
    doc = DocxTemplate(fr'{TEMPLATE_PATH}\Batch_Failure_To_Appear_Arraignment_Template.docx')
    doc.render(case_data.get_case_information())
    docname = set_document_name(case_data.case_number)
    doc.save(f'{BATCH_SAVE_PATH}{docname}')


def set_document_name(case_number: str) -> str:
    """Sets document name that includes case number."""
    return f'{case_number}_FTA_Arraignment.docx'


def user_input_get_batch_date(mainwindow: 'QMainWindow') -> tuple[str, bool]:
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
        f'Batch FTA Entries',
        f'This will query AuthorityCourt/CMI for all cases that were set for an arraignment on the'
        + ' date provided that were mandatory appearence cases.\nIt then generates an FTA warrant'
        + ' entry for each case.\nDefendants with multiple cases will have an FTA warrant entry'
        + ' generated for each case.\n\n'
        + f'Enter the Arraignment Date in format YYYY-MM-DD:',
        )


def set_warrant_rule(case_type_code: str) -> str:
    """Returns a string with the specific warrant rule based on the case type."""
    if case_type_code == 'CRB':
        return 'Criminal Rule 4'
    return 'Traffic Rule 7'


def run_batch_fta_arraignments() -> int:
    """The main function for the batch_fta_entries process."""
    batch_case_list = get_case_list_from_excel(fr'{DB_PATH}\Batch_FTA_Arraignments.xlsx')
    entry_count = 0
    for case in batch_case_list:
        logger.info(f'Creating Batch FTA entry for: {case.case_number}')
        create_entry(case)
        entry_count += 1
    return entry_count


def add_one_day_to_date_string(date_string, date_format='%Y-%m-%d'):
    date = datetime.datetime.strptime(date_string, date_format)
    date = date + datetime.timedelta(days=1)
    return date.strftime(date_format)


def run_batch_fta_process(mainwindow, _signal=None) -> None:
    """Creates batch entries for failure to appear and opens folder where entries are saved."""
    # entries_created = run_batch_fta_arraignments()
    event_date, ok_response = user_input_get_batch_date(mainwindow)
    if ok_response:
        next_day = add_one_day_to_date_string(event_date)
        logger.debug(next_day)
        case_numbers = batch_fta_query(event_date, next_day)
        logger.debug(case_numbers)
        # message = f'The batch process created {entries_created} entries.'
        # message_boxes.InfoBox(message, 'Entries Created').exec()
        # startfile(f'{BATCH_SAVE_PATH}')
        # logger.info(f'{message}')


if __name__ == '__main__':
    run_batch_fta_arraignments()
    logger.info(f'{__name__} run directly.')
