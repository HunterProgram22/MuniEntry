"""Checks for Scheduling Dialogs."""
from munientry.checkers.base_checks import BaseChecks, RequiredCheck
from munientry.checkers.check_messages import (
    FINAL_TODAY_MSG,
    FINAL_TODAY_TITLE,
    TRIAL_TODAY_MSG,
    TRIAL_TODAY_TITLE,
)


class SchedulingChecks(BaseChecks):
    """Checks used specifically for Scheduling Dialogs."""

    @RequiredCheck(TRIAL_TODAY_MSG, TRIAL_TODAY_TITLE)
    def check_if_trial_date_is_today(self) -> bool:
        """Scheduling date checker to make sure trial date is not set to today."""
        return self.dialog.trial_date.date() == self.today

    @RequiredCheck(FINAL_TODAY_MSG, FINAL_TODAY_TITLE)
    def check_if_final_pretrial_date_is_today(self) -> bool:
        """Scheduling date checker to make sure final pretrial date is not set to today."""
        if self.dialog.jury_trial_only_no_radio_btn.isChecked():
            return self.dialog.final_pretrial_date.date() == self.today
        return False
