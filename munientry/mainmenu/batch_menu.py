"""Module for creating a batch of Failure to Appear entries."""
import datetime
from os import startfile
from typing import List, Tuple

from PyQt6.QtSql import QSqlQuery
from PyQt6.QtWidgets import QInputDialog
from docxtpl import DocxTemplate
from loguru import logger

from munientry.data.connections import close_db_connection, open_db_connection
from munientry.appsettings.paths import BATCH_SAVE_PATH, DB_PATH, TEMPLATE_PATH
from munientry.sqlserver.sql_server_queries import batch_fta_query, general_case_search_query
from munientry.sqlserver.sql_server_getters import CriminalCaseSqlServer
from munientry.widgets import message_boxes


def create_entry(case_data, event_date):
    """General create entry function that populates a template with data."""
    doc = DocxTemplate(fr'{TEMPLATE_PATH}\Batch_Failure_To_Appear_Arraignment_Template.docx')
    data_dict = {
        'case_number':case_data.case.case_number,
        'def_first_name': case_data.case.defendant.first_name,
        'def_last_name': case_data.case.defendant.last_name,
        'case_event_date': event_date,
        'warrant_rule': set_warrant_rule(case_data.case.case_number[2:5])
    }
    doc.render(data_dict)
    docname = set_document_name(case_data.case_number)
    doc.save(f'{BATCH_SAVE_PATH}{docname}')


def set_document_name(case_number: str) -> str:
    """Sets document name that includes case number."""
    return f'{case_number}_FTA_Arraignment.docx'


def prompt_user_for_batch_date(mainwindow: 'QMainWindow') -> Tuple[str, bool]:
    """Prompts the user for a date and returns the date and a response indicating."""
    return QInputDialog.getText(
        mainwindow,
        'Batch FTA Entries',
        'Enter the Arraignment Date in format YYYY-MM-DD:',
        )


def set_warrant_rule(case_type_code: str) -> str:
    """Returns a string with the specific warrant rule based on the case type."""
    if case_type_code == 'CRB':
        return 'Criminal Rule 4'
    return 'Traffic Rule 7'


def get_fta_arraignment_cases(query_string) -> List[str]:
    db_conn = open_db_connection('con_authority_court')
    query = QSqlQuery(db_conn)
    query.prepare(query_string)
    query.exec()
    data_list = []
    while query.next():
        data_list.append(query.value('CaseNumber'))
    close_db_connection(db_conn)
    return data_list


def add_one_day_to_date_string(date_string, date_format='%Y-%m-%d'):
    date = datetime.datetime.strptime(date_string, date_format)
    date = date + datetime.timedelta(days=1)
    return date.strftime(date_format)


def create_fta_entries(batch_case_list, event_date) -> int:
    entry_count = 0
    for case_number in batch_case_list:
        logger.info(f'Creating Batch FTA entry for: {case_number}')
        case_data = CriminalCaseSqlServer(case_number)
        create_entry(case_data, event_date)
        entry_count += 1
    return entry_count


def run_batch_fta_process(mainwindow, _signal=None) -> None:
    """Creates batch entries for failure to appear and opens folder where entries are saved."""
    event_date, ok_response = prompt_user_for_batch_date(mainwindow)
    if not ok_response:
        return
    next_day = add_one_day_to_date_string(event_date)
    query_string = batch_fta_query(event_date, next_day)
    case_list = get_fta_arraignment_cases(query_string)
    entries_created = create_fta_entries(case_list, event_date)
    show_entries_created_message(entries_created)
    open_entry_folder()
    log_entries_created(entries_created)


def open_entry_folder() -> None:
    """Opens the folder where the entries are saved."""
    startfile(f'{BATCH_SAVE_PATH}')


def show_entries_created_message(entries_created: int) -> None:
    """Displays a message with the number of entries created."""
    message = f'The batch process created {entries_created} entries.'
    message_boxes.InfoBox(message, 'Entries Created').exec()


def log_entries_created(entries_created: int) -> None:
    """Logs information about the number of entries created."""
    message = f'{entries_created} entries were created.'
    logger.info(message)


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
