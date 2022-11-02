"""Module for creating a batch of Failure to Appear entries."""
from datetime import datetime

from docxtpl import DocxTemplate
from loguru import logger

from munientry.data.excel_functions import (
    create_headers_dict,
    get_excel_file_headers,
    load_active_worksheet,
)
from munientry.models.excel_models import BatchCaseInformation
from munientry.settings import TYPE_CHECKING
from munientry.paths import BATCH_SAVE_PATH, DB_PATH, TEMPLATE_PATH

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


def get_case_list_from_excel(excel_file: str) -> list[BatchCaseInformation]:
    """Loads active worksheet, generates header dict, and list with case data objects."""
    worksheet = load_active_worksheet(excel_file)
    header_list = get_excel_file_headers(worksheet)
    headers_dict = create_headers_dict(header_list)
    return create_batch_case_list(worksheet, headers_dict)


def create_batch_case_list(worksheet: 'Workbook.active', header_dict: dict) -> list[
    BatchCaseInformation
]:
    """Reads through an excel file and gets case data."""
    batch_case_data: list = []
    for row in range(2, worksheet.max_row + 1):
        case_number = get_cell_value(worksheet, row, header_dict[COL_CASE_NUMBER])
        case_type_code = get_cell_value(worksheet, row, header_dict[COL_CASE_TYPE])
        warrant_rule = set_warrant_rule(case_type_code)
        case_event_date = get_cell_value(worksheet, row, header_dict[COL_EVENT_DATE])
        def_first_name = get_cell_value(worksheet, row, header_dict[COL_DEF_FIRST_NAME]).title()
        def_last_name = get_cell_value(worksheet, row, header_dict[COL_DEF_LAST_NAME]).title()
        batch_case_data.append(BatchCaseInformation(
            case_number,
            warrant_rule,
            case_event_date,
            def_first_name,
            def_last_name,
        ))
    return batch_case_data


def get_cell_value(worksheet: 'Workbook.active', row: int, col: int) -> str:
    """Returns the cell value for a cell in the active excel worksheet."""
    cell_value = worksheet.cell(row=row, column=col).value
    if cell_value is None:
        return 'No Data'
    if isinstance(cell_value, datetime):
        return cell_value.strftime('%B %d, %Y')
    return cell_value


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


if __name__ == '__main__':
    run_batch_fta_arraignments()
    logger.info(f'{__name__} run directly.')
else:
    logger.info(f'{__name__} imported.')
