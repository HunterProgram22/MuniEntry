"""Module for checking scheduling-related dialogs."""
from munientry.checkers.base_checks import BaseChecks, required_check
from munientry.checkers.check_messages import (
    FINAL_FUTURE_MSG,
    FINAL_FUTURE_TITLE,
    TRIAL_FUTURE_MSG,
    TRIAL_FUTURE_TITLE,
)


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
        return self.dialog.final_pretrial_date.date() > self.today
