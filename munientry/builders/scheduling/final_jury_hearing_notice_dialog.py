"""Module containing classes for hearing notices."""
from loguru import logger
from PyQt6.QtCore import QDate

from munientry.settings.business_constants import DAY_DICT, EVENT_DICT
from munientry.builders.scheduling import base_scheduling_builders as sched
from munientry.checkers.base_checks import BaseChecker
from munientry.helper_functions import set_assigned_judge, set_courtroom
from munientry.loaders.cms_case_loaders import SchedulingCrimCmsLoader
from munientry.models.scheduling_information import SchedulingCaseInformation
from munientry.updaters.scheduling_updaters import (
    SchedulingModelUpdater,
)
from munientry.views.final_jury_notice_of_hearing_dialog_ui import (
    Ui_FinalJuryNoticeOfHearingDialog,
)


class FinalJuryNoticeHearingViewModifier(sched.SchedulingViewModifier):
    """Class that sets and modifies the view for the Final Jury Notice of Hearing."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.set_view_dates()
        self.set_calculator_dates()
        self.dialog.final_pretrial_time_box.setCurrentText('1:00 PM')

    def set_view_dates(self) -> None:
        today = QDate.currentDate()
        self.dialog.entry_date.setDate(today)
        self.dialog.trial_dateEdit.setDate(today)
        self.dialog.final_pretrial_dateEdit.setDate(today)

    def set_calculator_dates(self) -> None:
        today = QDate.currentDate()
        self.dialog.old_speedy_trial_dateEdit.setDate(today)
        self.dialog.new_hearing_dateEdit.setDate(today)
        self.dialog.old_hearing_dateEdit.setDate(today)


class FinalJuryNoticeHearingSignalConnector(sched.SchedulingSignalConnector):
    """Class that connects all signals for the Final Jury Notice of Hearing."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()
        self.connect_other_dialog_signals()
        self.connect_continuance_calc_signals()

    def connect_other_dialog_signals(self) -> None:
        self.dialog.jury_trial_only_no_radioButton.toggled.connect(
            self.dialog.functions.show_hide_final_pretrial,
        )
        self.dialog.jury_trial_only_yes_radioButton.toggled.connect(
            self.dialog.functions.show_hide_final_pretrial,
        )
        self.dialog.final_pretrial_dateEdit.dateChanged.connect(
            self.dialog.functions.update_trial_date,
        )

    def connect_continuance_calc_signals(self) -> None:
        self.dialog.old_speedy_trial_dateEdit.dateChanged.connect(
            self.dialog.functions.update_speedy_trial_date,
        )
        self.dialog.old_hearing_dateEdit.dateChanged.connect(
            self.dialog.functions.update_speedy_trial_date,
        )
        self.dialog.new_hearing_dateEdit.dateChanged.connect(
            self.dialog.functions.update_speedy_trial_date,
        )


class FinalJuryNoticeHearingSlotFunctions(sched.SchedulingSlotFunctions):
    """Class for that contains all signals for the Final Jury Notice of Hearing."""

    def update_speedy_trial_date(self) -> None:
        days_to_add = self.dialog.old_hearing_dateEdit.date().daysTo(
            self.dialog.new_hearing_dateEdit.date(),
        )
        new_speedy_trial_date = self.dialog.old_speedy_trial_dateEdit.date().addDays(days_to_add)
        new_speedy_trial_date = new_speedy_trial_date.toString('MMMM dd, yyyy')
        self.dialog.speedy_trial_date_label.setText(new_speedy_trial_date)

    def update_trial_date(self) -> None:
        if self.dialog.assigned_judge == 'Judge Kyle E. Rohrer':
            trial_date = self.set_trial_date('Tuesday', 'Trial')
        if self.dialog.assigned_judge == 'Judge Marianne T. Hemmeter':
            trial_date = self.set_trial_date('Thursday', 'Trial')
        try:
            self.dialog.trial_dateEdit.setDate(trial_date)
        except UnboundLocalError as error:
            logger.warning(error)

    def set_trial_date(self, day_to_set: str, event_to_set: str):
        """Returns a QDate object."""
        days_to_event = EVENT_DICT.get(event_to_set)
        event_date = self.dialog.final_pretrial_dateEdit.date().addDays(days_to_event)
        while event_date.dayOfWeek() != DAY_DICT.get(day_to_set):
            event_date = event_date.addDays(1)
        return event_date

    def show_hide_final_pretrial(self) -> None:
        if self.dialog.jury_trial_only_no_radioButton.isChecked():
            self.dialog.final_pretrial_dateEdit.setHidden(False)
            self.dialog.final_pretrial_date_label.setHidden(False)
            self.dialog.final_pretrial_time_label.setHidden(False)
            self.dialog.final_pretrial_time_box.setHidden(False)
        else:
            self.dialog.final_pretrial_dateEdit.setHidden(True)
            self.dialog.final_pretrial_date_label.setHidden(True)
            self.dialog.final_pretrial_time_label.setHidden(True)
            self.dialog.final_pretrial_time_box.setHidden(True)


class FinalJuryNoticeHearingCaseInformationUpdater(SchedulingModelUpdater):
    """Class for that sets the Case Information model for the Final Jury Notice of Hearing."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.model.assigned_judge = self.dialog.assigned_judge
        self.model.courtroom = self.dialog.courtroom
        self.model.judicial_officer = self.dialog.judicial_officer

    def set_scheduling_dates(self) -> None:
        self.model.hearing_location = self.dialog.hearing_location_box.currentText()
        self.model.jury_trial_date = self.dialog.trial_dateEdit.date().toString('MMMM dd, yyyy')
        if self.dialog.jury_trial_only_no_radioButton.isChecked():
            self.model.jury_trial_only = 'No'
            self.model.final_pretrial_date = self.dialog.final_pretrial_dateEdit.date().toString(
                'MMMM dd, yyyy',
            )
            self.model.final_pretrial_time = self.dialog.final_pretrial_time_box.currentText()
        elif self.dialog.jury_trial_only_yes_radioButton.isChecked():
            self.model.jury_trial_only = 'Yes'
            self.model.final_pretrial_date = None
            self.model.final_pretrial_time = None


class FinalJuryNoticeHearingInfoChecker(BaseChecker):
    """Class with checks for the Final Jury Notice Dialog."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.dialog_check_list = [
            'check_if_final_pretrial_date_is_today',
            'check_if_trial_date_is_today',
        ]
        self.check_status = self.perform_check_list()


class FinalJuryNoticeHearingDialog(
    sched.SchedulingDialogBuilder, Ui_FinalJuryNoticeOfHearingDialog,
):
    """Builder class for the Final and Jury Trial Notice of Hearing.

    The judicial_officer for this entry is the selected Assignment Commissioner.

    The assigned_judge and courtroom is set by the button pressed choosing the dialog and entry.
    """

    _case_information_model = SchedulingCaseInformation
    _case_loader = SchedulingCrimCmsLoader
    _info_checker = FinalJuryNoticeHearingInfoChecker
    _model_updater = FinalJuryNoticeHearingCaseInformationUpdater
    _signal_connector = FinalJuryNoticeHearingSignalConnector
    _slots = FinalJuryNoticeHearingSlotFunctions
    _view_modifier = FinalJuryNoticeHearingViewModifier
    dialog_name = 'Final And Jury Notice Hearing Entry'

    def additional_setup(self):
        self.assigned_judge = set_assigned_judge(self.sender())
        self.setWindowTitle(f'{self.dialog_name} Case Information - {self.assigned_judge}')
        self.courtroom = set_courtroom(self.sender())
        self.hearing_location_box.setCurrentText(self.courtroom)
        self.set_instructions_label()
        self.functions.update_trial_date()

    def set_instructions_label(self) -> None:
        if self.assigned_judge == 'Judge Marianne T. Hemmeter':
            self.instructions_label.setText(
                'INSTRUCTIONS: Set the final pretrial date and the jury trial date will'
                + ' automatically update to the next Thursday.',
            )
        if self.assigned_judge == 'Judge Kyle E. Rohrer':
            self.instructions_label.setText(
                'INSTRUCTIONS: Set the final pretrial date and the jury trial date will'
                + ' automatically update to the next Tuesday.',
            )


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
