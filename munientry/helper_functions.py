"""Helper functions that are used throughout the application."""
from __future__ import annotations
import random
from datetime import date, datetime, timedelta
from types import MappingProxyType
from typing import Any

from loguru import logger


def set_future_date(days_to_add: int, weekday_due_date: str) -> int:
    """Adds days to a date and sets a future weekday date.

    Accepts the number of days to add and a day of the week that will be added on to the
    number of days for the future court date that is to be set.
    """
    today = date.today()
    future_date = today + timedelta(days_to_add)
    future_date = next_court_day(future_date, weekday_due_date)
    return (future_date - today).days


def next_court_day(future_date: date, weekday_due_date: str) -> date:
    """Returns a date object that is the total number of days plus the days required to be added."""
    weekday_convert_dict = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4,
    }
    weekday = weekday_convert_dict.get(weekday_due_date, 0)
    days_ahead = weekday - future_date.weekday()
    if days_ahead <= 0:  # Target day already happened this week
        days_ahead += 7
    return future_date + timedelta(days_ahead)


def set_random_judge() -> tuple[str, str]:
    """Returns a random judge and the time the judge was assigned."""
    judge_list = ['Future Judge - Judge R - A Track', 'Judge Rohrer - B Track']
    assigned_judge = random.choice(judge_list)
    now = datetime.now()
    time_now = now.strftime('%B %d, %Y at %H:%M:%S %p')
    return (assigned_judge, time_now)


def set_assigned_judge(sender: 'QPushButton') -> str:
    """Returns the judge name as a string based on the button that is pressed."""
    TUESDAY_TRIAL_JUDGE = 'Judge Kyle E. Rohrer - Courtroom B Track'
    THURSDAY_TRIAL_JUDGE = 'Judge Kyle E. Rohrer - Courtroom A Track'
    assigned_judge_dict = {
        'rohrer_final_jury_hearingButton': TUESDAY_TRIAL_JUDGE,
        'rohrer_general_hearingButton': TUESDAY_TRIAL_JUDGE,
        'rohrer_trial_court_hearingButton': TUESDAY_TRIAL_JUDGE,
        'hemmeter_final_jury_hearingButton': THURSDAY_TRIAL_JUDGE,
        'hemmeter_general_hearingButton': THURSDAY_TRIAL_JUDGE,
        'hemmeter_trial_court_hearingButton': THURSDAY_TRIAL_JUDGE,
    }
    return assigned_judge_dict.get(sender.objectName(), '')


def set_courtroom(sender: 'QPushButton') -> str:
    """Returns a string with the courtroom letter based on the button that is pressed.

    Returns a blank if function called from a button that does not set a
    courtroom. This allows the user to manually enter courtroom in the Word doc.
    """
    courtroom_dict = {
        'rohrer_final_jury_hearingButton': 'Courtroom B',
        'rohrer_general_hearingButton': 'Courtroom B',
        'rohrer_trial_court_hearingButton': 'Courtroom C',
        'hemmeter_final_jury_hearingButton': 'Courtroom A',
        'hemmeter_general_hearingButton': 'Courtroom A',
        'hemmeter_trial_court_hearingButton': 'Courtroom C',
    }
    return courtroom_dict.get(sender.objectName(), '')


def format_date_string(date_string: str) -> str:
    """Formats a string that is a date into standard ISO extended format YYYY-MM-DD.

    Args:
        date_string (str): A string date in the format Month Day, Year (i.e. January, 09, 1980).

    Returns:
        string: A string in the format Year-Month-Day (i.e. 1980-09-01).
    """

    date_object = datetime.strptime(date_string, '%B %d, %Y')
    new_date_format = date_object.strftime('%Y-%m-%d')
    new_date_object = datetime.strptime(new_date_format, '%Y-%m-%d').date()
    return str(new_date_object)


def update_crim_case_number(case_number: str) -> str:
    """Updates the case number in case search to add 0's if full case number not provided."""
    if len(case_number) == 10:
        return case_number.upper()
    crim_letter_list = ['B', 'b']
    if any(letter in case_number for letter in crim_letter_list):
        try:
            case_year, case_five_number = case_number.split('b')
        except ValueError:
            case_year, case_five_number = case_number.split('B')
        case_year = case_year[:2]
        case_code = 'CRB'
        return reset_case_number(case_year, case_code, case_five_number)
    ovi_letter_list = ['C', 'c']
    if any(letter in case_number for letter in ovi_letter_list):
        try:
            case_year, case_five_number = case_number.split('c')
        except ValueError:
            case_year, case_five_number = case_number.split('C')
        case_year = case_year[:2]
        case_code = 'TRC'
        return reset_case_number(case_year, case_code, case_five_number)
    traffic_letter_list = ['D', 'd']
    if any(letter in case_number for letter in traffic_letter_list):
        try:
            case_year, case_five_number = case_number.split('d')
        except ValueError:
            case_year, case_five_number = case_number.split('D')
        case_year = case_year[:2]
        case_code = 'TRD'
        return reset_case_number(case_year, case_code, case_five_number)


def update_civil_case_number(case_number: str) -> str:
    """Updates the case number in case search to add 0's if full case number not provided."""
    if len(case_number) == 10:
        return case_number.upper()
    personal_injury_list = ['E', 'e']
    if any(letter in case_number for letter in personal_injury_list):
        try:
            case_year, case_five_number = case_number.split('e')
        except ValueError:
            case_year, case_five_number = case_number.split('E')
        case_year = case_year[:2]
        case_code = 'CVE'
        return reset_case_number(case_year, case_code, case_five_number)
    contracts_list = ['F', 'f']
    if any(letter in case_number for letter in contracts_list):
        try:
            case_year, case_five_number = case_number.split('f')
        except ValueError:
            case_year, case_five_number = case_number.split('F')
        case_year = case_year[:2]
        case_code = 'CVF'
        return reset_case_number(case_year, case_code, case_five_number)
    evictions_list = ['G', 'g']
    if any(letter in case_number for letter in evictions_list):
        try:
            case_year, case_five_number = case_number.split('g')
        except ValueError:
            case_year, case_five_number = case_number.split('G')
        case_year = case_year[:2]
        case_code = 'CVG'
        return reset_case_number(case_year, case_code, case_five_number)
    other_civil_list = ['H', 'h']
    if any(letter in case_number for letter in other_civil_list):
        try:
            case_year, case_five_number = case_number.split('h')
        except ValueError:
            case_year, case_five_number = case_number.split('H')
        case_year = case_year[:2]
        case_code = 'CVH'
        return reset_case_number(case_year, case_code, case_five_number)
    small_claims_list = ['I', 'i']
    if any(letter in case_number for letter in small_claims_list):
        try:
            case_year, case_five_number = case_number.split('i')
        except ValueError:
            case_year, case_five_number = case_number.split('I')
        case_year = case_year[:2]
        case_code = 'CVI'
        return reset_case_number(case_year, case_code, case_five_number)


def reset_case_number(case_year: str, case_code: str, case_five_number: str) -> str:
    """Adds 0's to the last 5 digits of a case number to make it 5 digits.

    22TRC1 -> 22TRC00001
    22CRB12 -> 22CRB00012
    22TRD205 -> 22TRD00205
    20CVG0210 -> 20CVG00210
    """
    match len(case_five_number):
        case 5:
            return f'{case_year}{case_code}{case_five_number}'
        case 4:
            return f'{case_year}{case_code}0{case_five_number}'
        case 3:
            return f'{case_year}{case_code}00{case_five_number}'
        case 2:
            return f'{case_year}{case_code}000{case_five_number}'
        case 1:
            return f'{case_year}{case_code}0000{case_five_number}'


WIDGET_TYPE_ACCESS_DICT = MappingProxyType({
    'NoScrollComboBox': 'currentText',
    'ConditionCheckbox': 'isChecked',
    'QCheckBox': 'isChecked',
    'QRadioButton': 'isChecked',
    'QLineEdit': 'text',
    'QTextEdit': 'toPlainText',
    'NoScrollDateEdit': 'get_date_as_string',
    'NoScrollTimeEdit': 'get_time_as_string',
})


def get_view_field_data(view: Any, widget_type: str) -> Any:
    """Returns the getter access method for a widget."""
    return getattr(view, WIDGET_TYPE_ACCESS_DICT.get(widget_type, 'None'))()


WIDGET_TYPE_SET_DICT = MappingProxyType({
    'NoScrollComboBox': 'setCurrentText',
    'QCheckBox': 'setChecked',
    'ConditionCheckbox': 'setChecked',
    'QRadioButton': 'setChecked',
    'QLineEdit': 'setText',
    'QTextEdit': 'setPlainText',
    'NoScrollDateEdit': 'set_date_from_string',
    'NoScrollTimeEdit': 'set_time_from_string',
})


def set_view_field_data(view: Any, widget_type: str, model_data: Any) -> None:
    """Returns the setter method for a widget."""
    getattr(view, WIDGET_TYPE_SET_DICT.get(widget_type))(model_data)
