"""Module for creating a batch of Failure to Appear entries."""
from dataclasses import asdict, dataclass

from docxtpl import DocxTemplate
from loguru import logger
from openpyxl import load_workbook

from munientry.settings import DB_PATH, SAVE_PATH, TEMPLATE_PATH


def create_entry(case_data):
    """General create entry function that populates a template with data."""
    doc = DocxTemplate(fr'{TEMPLATE_PATH}\Batch_Failure_To_Appear_Arraignment_Template.docx')
    doc.render(case_data.get_case_information())
    docname = set_document_name(case_data.CaseNumber)
    doc.save(fr'{SAVE_PATH}\batch\{docname}')


def set_document_name(case_number: str) -> str:
    """Sets document name that includes case number."""
    return f'{case_number}_FTA_Arraignment.docx'


def return_data_from_excel(excel_file):
    """Reads through an excel file and gets case data."""
    batch_case_data = []
    workbook = load_workbook(excel_file, data_only=True)
    worksheet = workbook.active
    row_count = worksheet.max_row + 1
    for row in range(2, row_count):
        CaseNumber = worksheet.cell(row=row, column=1)
        case_event_date = get_case_event_date(worksheet, row=row, column=3)
        DefFirstName = worksheet.cell(row=row, column=5)
        clean_first_name = DefFirstName.value
        clean_first_name = clean_first_name.title()
        DefLastName = worksheet.cell(row=row, column=4)
        clean_last_name = DefLastName.value
        clean_last_name = clean_last_name.title()
        case_information = BatchCaseInformation(
            CaseNumber.value,
            case_event_date,
            clean_first_name,
            clean_last_name,
        )
        batch_case_data.append(case_information)
    return batch_case_data


def get_case_event_date(worksheet: object, row: int, column: int) -> str:
    event_date = worksheet.cell(row=row, column=3).value
    return event_date.strftime('%B %d, %Y')

@dataclass
class BatchCaseInformation:
    CaseNumber: str  = None
    CaseEventDate: str = None
    DefFirstName: str = None
    DefLastName: str = None

    def get_case_information(self):
        return asdict(self)


def run_batch_fta_arraignments() -> int:
    data_for_entries = return_data_from_excel(f'{DB_PATH}\\Batch_FTA_Arraignments.xlsx')
    entry_count = 0
    for index, person in enumerate(data_for_entries):
        logger.info(f'Creating Batch FTA entry for: {data_for_entries[index].CaseNumber}')
        create_entry(data_for_entries[index])
        entry_count +=1
    return entry_count


if __name__ == '__main__':
    run_batch_fta_arraignments()
    logger.info(f'{__name__} run directly.')
else:
    logger.info(f'{__name__} imported.')
