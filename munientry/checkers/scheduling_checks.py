"""Checks for Scheduling Dialogs."""
from munientry.checkers.base_checks import BaseChecks
from munientry.widgets.message_boxes import RequiredBox, FAIL, PASS


class SchedulingChecks(BaseChecks):
    """Checks used specifically for Scheduling Dialogs."""

    def check_if_trial_date_is_today(self) -> str:
        """Scheduling date checker to make sure trial date is not set to today."""
        if self.dialog.trial_date.date() == self.today:
            message = (
                'The Trial Date is Today, but must be a date in the future. Please enter'
                + ' a date in the Trial Date box after today.'
            )
            RequiredBox(message).exec()
            return FAIL
        return PASS

    def check_if_final_pretrial_date_is_today(self) -> str:
        """Scheduling date checker to make sure final pretrial date is not set to today."""
        if self.dialog.jury_trial_only_no_radio_btn.isChecked():
            if self.dialog.final_pretrial_date.date() == self.today:
                message = (
                    'The Final Pretrial Date is Today, but must be a date in the future. Please'
                    + ' enter a date in the Final Pretrial Date box after today.'
                )
                RequiredBox(message).exec()
                return FAIL
            return PASS
        return PASS
