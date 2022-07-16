"""Module for creating a batch of Failure to Appear entries."""
import datetime
import os
import sys
import pathlib
from dataclasses import dataclass, field, asdict
from loguru import logger

from openpyxl import load_workbook
from docxtpl import DocxTemplate

# from munientry.settings import DB_PATH, SAVE_PATH, TEMPLATE_PATH
# PATH = str(pathlib.Path().absolute())
PATH = 'C:\\Users\\justi\\appdata\\local\\programs\\python\\python310\\MuniEntry\\'
TEMPLATE_PATH = fr'{PATH}\resources\templates\\'
SAVE_PATH = fr'{PATH}\resources\saved\\'
DB_PATH = fr'{PATH}\db\\'


def create_entry(data):
    doc = DocxTemplate(f'{TEMPLATE_PATH}\\Batch_Failure_To_Appear_Arraignment_Template.docx')
    doc.render(data.get_case_information())
    docname = set_document_name(data)
    doc.save(f'{SAVE_PATH}\\batch\\{docname}')


def set_document_name(data):
    docname = f'{data.CaseNumber}.docx'
    return docname


def return_data_from_excel(excel_file):
    data = []
    workbook = load_workbook(excel_file, data_only=True)
    worksheet = workbook.active
    row_count = worksheet.max_row + 1
    for row in range(2, row_count):
        CaseNumber = worksheet.cell(row=row, column=1)
        CaseEventDate = worksheet.cell(row=row, column=3)
        clean_date = CaseEventDate.value
        clean_date = clean_date.strftime('%B %d, %Y')
        DefFirstName = worksheet.cell(row=row, column=5)
        clean_first_name = DefFirstName.value
        clean_first_name = clean_first_name.title()
        DefLastName = worksheet.cell(row=row, column=4)
        clean_last_name = DefLastName.value
        clean_last_name = clean_last_name.title()
        case_information = BatchCaseInformation(
            CaseNumber.value,
            clean_date,
            clean_first_name,
            clean_last_name,
        )
        data.append(case_information)
    return data


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
        logger.info(f'Creating entry for: {data_for_entries[index]}')
        create_entry(data_for_entries[index])
        entry_count +=1
    return entry_count


if __name__ == "__main__":
    run_batch_fta_arraignments()
    logger.info(f'{__name__} run directly.')
else:
    logger.info(f'{__name__} imported.')
