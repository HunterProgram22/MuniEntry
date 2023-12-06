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
        """Check if the Final Pretrial is set for the correct day of the week.

        Judge Hemmeter is Tuesday, Judge Rohrer is Thursday.

        Returns:
            bool: True if final pretrial day matches Judge set day, False otherwise.
        """
        fpt_date = self.dialog.final_pretrial_date.date().toPyDate()
        fpt_date_index = fpt_date.weekday()
        day_of_week = DAYS[fpt_date_index]
        if msg_response is not None:
            return self.handle_day_check(msg_response)
        judge = self.get_judge()
        if judge == 'Rohrer':
            if day_of_week != 'Thursday':
                return False
        if judge == 'Hemmeter':
            if day_of_week != 'Tuesday':
                return False
        return True

    @warning_check(TRIAL_DAY_TITLE, TRIAL_DAY_MSG)
    def check_day_of_trial(self, msg_response: int = None) -> bool:
        """Check if the Trial is set for the correct day of the week.

        Judge Hemmeter is Thursday, Judge Rohrer is Tuesday.

        Returns:
            bool: True if trial day matches Judge set day, False otherwise.
        """
        trial_date = self.dialog.trial_date.date().toPyDate()
        trial_date_index = trial_date.weekday()
        day_of_week = DAYS[trial_date_index]
        if msg_response is not None:
            return self.handle_day_check(msg_response)
        judge = self.get_judge()
        if judge == 'Rohrer':
            if day_of_week != 'Tuesday':
                return False
        if judge == 'Hemmeter':
            if day_of_week != 'Thursday':
                return False
        return True

    def get_judge(self):
        if self.dialog.dialog_name == 'Rohrer Scheduling Entry':
            return 'Rohrer'
        elif self.dialog.dialog_name == 'Hemmeter Scheduling Entry':
            return 'Hemmeter'
        else:
            try:
                if self.dialog.assigned_judge == 'Judge Marianne T. Hemmeter':
                    return 'Hemmeter'
                if self.dialog.assigned_judge == 'Judge Kyle E. Rohrer':
                    return 'Rohrer'
            except AttributeError as err:
                logger.warning(err)


    def handle_day_check(self, msg_response: int) -> bool:
        if msg_response == NO_BUTTON_RESPONSE:
            return False
        elif msg_response == YES_BUTTON_RESPONSE:
            return True
