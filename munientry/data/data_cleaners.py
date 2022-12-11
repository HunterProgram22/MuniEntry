"""Module for getting case data from Excel files."""
from types import MappingProxyType

from loguru import logger

# from munientry.data.excel_functions import (
#     create_headers_dict,
#     get_excel_file_headers,
#     load_active_worksheet,
# )
# from munientry.models.excel_models import CaseExcelData
# from munientry.appsettings.settings import TYPE_CHECKING
#
# if TYPE_CHECKING:
#     from openpyxl import Workbook


# Column Headers
COL_CASE = 'CaseNumber'
COL_DEF_LAST_NAME = 'DefLastName'
COL_DEF_FIRST_NAME = 'DefFirstName'
COL_CHARGE = 'ChargeDescription'
COL_STATUTE = 'SectionCode'
COL_DEGREE = 'DegreeCode'
COL_INSURANCE = 'InsuranceStatus'
COL_MOVING_OFFENSE = 'IsMoving'
COL_DEF_ATTY_LAST_NAME = 'AttorneyLastName'
COL_DEF_ATTY_FIRST_NAME = 'AttorneyFirstName'
COL_DEF_ATTY_TYPE = 'PubDef'

NO_DATA = 'No Data'
OFFENSE_CLEAN_DICT = MappingProxyType({
    'UCM': '',
    'M1': '',
    'M2': '',
    'M3': '',
    'M4': '',
    'MM': '',
    'PETTY': '',
    '(UCM)': '',
    'DUS': 'DUS',
    'OVI': 'OVI',
    'BMV': 'BMV',
    'OBMV': 'BMV',
    'FRA': 'FRA',
    'OL': 'OL',
    'OMVI': 'OVI',
    'FRA/JUDGMENT': 'FRA / Judgment',
    'OR': '/',
    'W/O': 'Without',
    'A': 'a',
    'TO': 'to',
    'SUSP': 'Suspension',
    '-': '',
    'OF': 'of',
    'IN': 'in',
    'AND': 'and',
})


def clean_statute_name(statute: str) -> str:
    """Removes trailing asteriks that are often part of data from AuthorityCourt."""
    return statute.rstrip('*')


def clean_offense_name(offense: str) -> str:
    """Sets offense name to title case (except for abbreviations) and removes degree of charge."""
    offense_word_list = offense.split()
    clean_offense_word_list = []
    for word in offense_word_list:
        if OFFENSE_CLEAN_DICT.get(word) is not None:
            clean_offense_word_list.append(OFFENSE_CLEAN_DICT.get(word))
            continue
        clean_offense_word_list.append(word.capitalize())
    clean_offense = ' '.join([str(clean_word) for clean_word in clean_offense_word_list])
    return clean_offense.rstrip(' ')


def clean_last_name(last_name:str) -> str:
    """Removes spaces between hyphenated last names which caused a bug."""
    return last_name.replace(' - ', '-')


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
