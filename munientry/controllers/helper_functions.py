"""Helper functions that are used throughout the application."""
from __future__ import annotations

import random
from datetime import date, datetime, timedelta

from loguru import logger

from munientry.widgets.custom_widgets import RequiredBox


def check_judicial_officer(func):
    """Prohibits opening a dialog unless a judicial officer is selected."""
    def wrapper(self):
        if self.judicial_officer is None:
            RequiredBox('You must select a judicial officer.', 'Judicial Officer Required').exec()
        else:
            func(self)

    return wrapper


def check_assignment_commissioner(func):
    """Prohibits opening a dialog unless an assignment commissioner is selected."""
    def wrapper(self):
        if self.judicial_officer is None:
            RequiredBox('You must select an assignment commissioner.', 'Assignment Commissioner Required').exec()
        else:
            func(self)

    return wrapper


def check_case_list_selected(func):
    """Probhitis opening a dialog unless a daily case list is selected."""
    def wrapper(self):
        if any(key.isChecked() for key in self.daily_case_list_buttons_dict.keys()):
            func(self)
        else:
            RequiredBox(
                'You must select a case list. If not loading a case in the case list '
                + 'leave the case list field blank.', 'Daily Case List Required',
            ).exec()

    return wrapper


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
    judge_list = ['Judge Hemmeter', 'Judge Rohrer']
    assigned_judge = random.choice(judge_list)
    now = datetime.now()
    time_now = now.strftime('%B %d, %Y at %H:%M:%S %p')
    return (assigned_judge, time_now)


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')


def set_assigned_judge(sender: 'QPushButton') -> str:
    """Returns the judge name as a string based on the button that is pressed."""
    assigned_judge_dict = {
        'rohrer_final_jury_hearingButton': 'Judge Kyle E. Rohrer',
        'rohrer_general_hearingButton': 'Judge Kyle E. Rohrer',
        'rohrer_trial_court_hearingButton': 'Judge Kyle E. Rohrer',
        'hemmeter_final_jury_hearingButton': 'Judge Marianne T. Hemmeter',
        'hemmeter_general_hearingButton': 'Judge Marianne T. Hemmeter',
        'hemmeter_trial_court_hearingButton': 'Judge Marianne T. Hemmeter',
    }
    return assigned_judge_dict.get(sender.objectName(), '')


def set_courtroom(sender: 'QPushButton') -> str:
    """Returns a string with the courtroom letter based on the button that is pressed.

    Returns a blank if function called from a button that does not set a
    courtroom. This allows the user to manually enter courtroom in the Word doc.
    """
    courtroom_dict = {
        'rohrer_final_jury_hearingButton': 'Courtroom A',
        'rohrer_general_hearingButton': 'Courtroom A',
        'rohrer_trial_court_hearingButton': 'Courtroom C',
        'hemmeter_final_jury_hearingButton': 'Courtroom B',
        'hemmeter_general_hearingButton': 'Courtroom B',
        'hemmeter_trial_court_hearingButton': 'Courtroom C',
    }
    return courtroom_dict.get(sender.objectName(), '')