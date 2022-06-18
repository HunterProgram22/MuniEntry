from dataclasses import dataclass

NO_DATA = 'No Data'


@dataclass
class CaseExcelData(object):
    """Class for holding case data that is extracted from excel file."""

    case_number: str = NO_DATA
    sub_case_number: str = NO_DATA
    defendant_last_name: str = NO_DATA
    defendant_first_name: str = NO_DATA
    offense: str = NO_DATA
    statute: str = NO_DATA
    degree: str = NO_DATA
    fra_in_file: str = 'U'
    moving_bool: str = NO_DATA
    def_atty_last_name: str = ''
    def_atty_first_name: str = ''
    def_atty_type: str = NO_DATA


@dataclass
class ChargeExcelData(object):
    """Class for holding charge data that is extracted from excel file."""

    offense: str = NO_DATA
    statute: str = NO_DATA
    degree: str = NO_DATA
    offense_type: str = NO_DATA