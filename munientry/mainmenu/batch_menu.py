"""Module for creating a batch of Failure to Appear entries."""
from datetime import datetime, timedelta

from docxtpl import DocxTemplate  # type: ignore # Ignores mypy error for no type hints
from loguru import logger
from PyQt6.QtWidgets import QInputDialog, QMainWindow

from munientry.settings.paths import BATCH_SAVE_PATH, TEMPLATE_PATH
from munientry.helper_functions import update_crim_case_number
from munientry.mainmenu.open_menu import open_entries_folder
from munientry.sqlserver.crim_getters import (
    CrimCaseData,
    get_fta_arraignment_cases,
)
from munientry.sqlserver.crim_sql_server_queries import batch_fta_query
from munientry.widgets import message_boxes

INPUT_DATE_FORMAT = '%Y-%m-%d'  # noqa: WPS323 - Flake8 check ignores % in string
STRING_DATE_FORMAT = '%B %d, %Y'  # noqa: WPS323 - Flake8 check ignores % in string


# Batch FTA Functions #
def run_batch_fta_process(mainwindow: QMainWindow, _signal=None) -> None:
    """Creates batch entries for failure to appear and opens folder where entries are saved."""
    event_date, ok_response = prompt_user_for_batch_date(mainwindow)
    if not ok_response:
        return
    next_day = add_one_day_to_date_string(event_date)
    query_string = batch_fta_query(event_date, next_day)
    case_list = get_fta_arraignment_cases(query_string)
    entries_created = create_fta_entries(case_list, event_date)
    show_entries_created_message(entries_created)
    open_entries_folder('batch_entries')
    log_entries_created(entries_created)


def prompt_user_for_batch_date(mainwindow: QMainWindow) -> tuple[str, bool]:
    """Prompts the user for a date and returns the date and a response indicating."""
    return QInputDialog.getText(
        mainwindow,
        'Batch FTA Entries',
        'Enter the Arraignment Date in format YYYY-MM-DD:',
    )


def add_one_day_to_date_string(date_string: str, date_format=INPUT_DATE_FORMAT) -> str:
    """Returns a string date one day later than the date string submitted."""
    date = datetime.strptime(date_string, date_format)
    date = date + timedelta(days=1)
    return date.strftime(date_format)


def create_fta_entries(batch_case_list: list, event_date: str) -> int:
    """Process that creates the entries and returns a count of total entries created."""
    entry_count = 0
    for case_number in batch_case_list:
        logger.info(f'Creating Batch FTA entry for: {case_number}')
        case_data = CrimCaseData(case_number)
        create_entry(case_data, event_date)
        entry_count += 1
    return entry_count


# Single FTA Functions #
def create_single_fta_entry(mainwindow: QMainWindow) -> None:
    """Process for creating an FTA entry for a single case number."""
    case_number, ok_response = QInputDialog.getText(
        mainwindow,
        'Create Single FTA Entry',
        'Enter the Case Number:',
    )
    case_number = update_crim_case_number(case_number)
    if not ok_response:
        return
    event_date, ok_response = prompt_user_for_batch_date(mainwindow)
    if not ok_response:
        return
    case_data = CrimCaseData(case_number)
    create_entry(case_data, event_date)
    show_entries_created_message(1)
    open_entries_folder('batch_entries')
    log_entries_created(1)


def create_entry(case_data: CrimCaseData, event_date: str) -> None:
    """General create entry function that populates a template with data."""
    doc = DocxTemplate(fr'{TEMPLATE_PATH}\Batch_Failure_To_Appear_Arraignment_Template.docx')
    date_obj = datetime.strptime(event_date, INPUT_DATE_FORMAT)
    formatted_event_date = date_obj.strftime(STRING_DATE_FORMAT)
    data_dict = {
        'case_number': case_data.case.case_number,
        'def_first_name': case_data.case.defendant.first_name,
        'def_last_name': case_data.case.defendant.last_name,
        'case_event_date': formatted_event_date,
        'warrant_rule': set_warrant_rule(case_data.case.case_number[2:5]),
    }
    doc.render(data_dict)
    docname = set_document_name(case_data.case_number)
    doc.save(f'{BATCH_SAVE_PATH}{docname}')


# Common FTA Functions #
def set_document_name(case_number: str) -> str:
    """Sets document name that includes case number."""
    return f'{case_number}_FTA_Arraignment.docx'


def set_warrant_rule(case_type_code: str) -> str:
    """Returns a string with the specific warrant rule based on the case type."""
    if case_type_code == 'CRB':
        return 'Criminal Rule 4'
    return 'Traffic Rule 7'


def show_entries_created_message(entries_created: int) -> None:
    """Displays a message with the number of entries created."""
    message = f'The batch process created {entries_created} entries.'
    message_boxes.InfoBox(message, 'Entries Created').exec()


def log_entries_created(entries_created: int) -> None:
    """Logs information about the number of entries created."""
    message = f'{entries_created} entries were created.'
    logger.info(message)
