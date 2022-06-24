"""Module for loading non-CMS charge data from Excel files."""
from loguru import logger
from package.excel_loaders.loader_functions import load_active_worksheet
from package.models.excel_models import ChargeExcelData


def create_charges_data_list(excel_file: str) -> list[ChargeExcelData]:
    """Returns a list of CaseExcelData objects.

    The ChargeExcelData object is loaded with the data from each row (charge) and the attributes
    of each charge are mapped to the specific column that contains the charge attribute. The load
    portion of the function starts with row 2 because row 1 is headers.

    The columns are hardcoded - see case_excel_loader.py and headers_dict in loader_functions.py
    for future refactoring to set them as constants.
    """
    worksheet = load_active_worksheet(excel_file)
    charge_data_list: list = []
    row_count: int = worksheet.max_row + 1
    for row in range(2, row_count):
        charge = ChargeExcelData()
        charge.offense = worksheet.cell(row=row, column=1).value
        charge.statute = worksheet.cell(row=row, column=2).value
        charge.degree = worksheet.cell(row=row, column=3).value
        charge.offense_type = worksheet.cell(row=row, column=4).value
        charge_data_list.append(charge)
    return charge_data_list


if __name__ == "__main__":
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
