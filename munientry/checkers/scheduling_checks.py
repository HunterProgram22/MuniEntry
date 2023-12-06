"""Module for checking scheduling-related dialogs."""
from datetime import date, datetime

from PyQt6.QtCore import QDate
from loguru import logger

from munientry.checkers.base_checks import BaseChecks, required_check, warning_check
from munientry.settings.pyqt_constants import NO_BUTTON_RESPONSE, YES_BUTTON_RESPONSE
from munientry.checkers.check_messages import (
    FINAL_DAY_TITLE,
    FINAL_DAY_MSG,
    FINAL_FUTURE_MSG,
    FINAL_FUTURE_TITLE,
    TRIAL_FUTURE_MSG,
    TRIAL_FUTURE_TITLE,
    TRIAL_DAY_MSG,
    TRIAL_DAY_TITLE,
)

DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

JUDGE_DAYS = {
    'Hemmeter': {'final_pretrial': 'Tuesday', 'trial': 'Thursday'},
    'Rohrer': {'final_pretrial': 'Thursday', 'trial': 'Tuesday'}
}


class SchedulingChecks(BaseChecks):
    """A class for checks related to scheduling dialogs."""

    @required_check(TRIAL_FUTURE_TITLE, TRIAL_FUTURE_MSG)
    def check_trial_date(self) -> bool:
        """Check if the trial date is set in the future.

        Returns:
            bool: True if the trial date is in the future, False otherwise.
        """
        return self.dialog.trial_date.date() > self.today

    @required_check(FINAL_FUTURE_TITLE, FINAL_FUTURE_MSG)
    def check_final_pretrial_date(self) -> bool:
        """Check if the final pretrial date is set in the future.

        Returns:
            bool: True if the final pretrial date is in the future, False otherwise.
        """
        if getattr(self.dialog, 'jury_trial_only_no_radio_btn', None) is not None:
            if self.dialog.jury_trial_only_no_radio_btn.isChecked():
                return self.dialog.final_pretrial_date.date() > self.today
        return True

    @warning_check(FINAL_DAY_TITLE, FINAL_DAY_MSG)
    def check_day_of_final_pretrial(self, msg_response: int = None) -> bool:
        """Check if the day of the final pretrial based on Judge.

        Judge Hemmeter is Tuesday, Judge Rohrer is Thursday.

        Returns:
            bool: True if the final pretrial day matches Judge day, False otherwise.
        """
        if msg_response is not None:
            return self.handle_day_check(msg_response)
        fpt_date = self.dialog.final_pretrial_date.date().toPyDate()
        return self.check_day(fpt_date, 'final_pretrial')

    @warning_check(TRIAL_DAY_TITLE, TRIAL_DAY_MSG)
    def check_day_of_trial(self, msg_response: int = None) -> bool:
        """Check if the day of the final pretrial based on Judge.

        Judge Hemmeter is Thursday, Judge Rohrer is Tuesday.

        Returns:
            bool: True if the trial day matches Judge day, False otherwise.
        """
        if msg_response is not None:
            return self.handle_day_check(msg_response)
        trial_date = self.dialog.trial_date.date().toPyDate()
        return self.check_day(trial_date, 'trial')

    def check_day(self, date, event_type):
        day_of_week = DAYS[date.weekday()]
        judge = self.get_judge()
        expected_day = JUDGE_DAYS.get(judge, {}).get(event_type)
        if expected_day is None:
            # Handle the case where the judge or event type is not found
            logger.warning('No Event or Judge found.')
            return True
        return day_of_week == expected_day

    def get_judge(self):
        dialog_name_map = {
            'Rohrer Scheduling Entry': 'Rohrer',
            'Hemmeter Scheduling Entry': 'Hemmeter'
        }
        judge = dialog_name_map.get(self.dialog.dialog_name)
        if judge:
            return judge
        assigned_judge_map = {
            'Judge Marianne T. Hemmeter': 'Hemmeter',
            'Judge Kyle E. Rohrer': 'Rohrer'
        }
        return assigned_judge_map.get(self.dialog.assigned_judge, 'Unknown')

    def handle_day_check(self, msg_response: int) -> bool:
        return msg_response == YES_BUTTON_RESPONSE

