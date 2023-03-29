"""Checks for Scheduling Dialogs."""
from munientry.checkers.base_checks import BaseChecks, RequiredCheck
from munientry.checkers.check_messages import (
    FINAL_FUTURE_MSG,
    FINAL_FUTURE_TITLE,
    TRIAL_FUTURE_MSG,
    TRIAL_FUTURE_TITLE,
)


class SchedulingChecks(BaseChecks):
    """Checks used specifically for Scheduling Dialogs."""

    @RequiredCheck(TRIAL_FUTURE_TITLE, TRIAL_FUTURE_MSG)
    def check_trial_date(self) -> bool:
        """Returns False (Fails check) if trial date is not set in the future."""
        return self.dialog.trial_date.date() > self.today

    @RequiredCheck(FINAL_FUTURE_TITLE, FINAL_FUTURE_MSG)
    def check_final_pretrial_date(self) -> bool:
        """Returns False (Fails check) if final pretrial date is not set in the future."""
        if hasattr(self.dialog, 'jury_trial_only_no_radio_btn'):
            if self.dialog.jury_trial_only_no_radio_btn.isChecked():
                return self.dialog.final_pretrial_date.date() > self.today
        return self.dialog.final_pretrial_date.date() > self.today
