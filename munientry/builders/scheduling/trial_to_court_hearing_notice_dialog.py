"""Module for creating and operating the Trial To Court Hearing Notice Dialog.

**munientry.builders.scheduling.trial_to_court_hearing_notice_dialog**
"""
from typing import TYPE_CHECKING

from loguru import logger
from PyQt6.QtCore import QDate

from munientry.settings.business_constants import DAY_DICT, SPEEDY_TRIAL_TIME_DICT
from munientry.builders.scheduling import base_scheduling_builders as sched
from munientry.checkers.base_checks import SchedulingChecker
from munientry.helper_functions import set_assigned_judge, set_courtroom
from munientry.loaders.cms_case_loaders import SchedulingCrimCmsLoader
from munientry.models.scheduling_information import SchedulingCaseInformation
from munientry.updaters.scheduling_updaters import (
    SchedulingModelUpdater,
)
from munientry.views.trial_to_court_hearing_dialog_ui import (
    Ui_TrialToCourtHearingDialog,
)

if TYPE_CHECKING:
    from PyQt6.QtCore import QDate

TRIAL = 'Trial'
ENTRY_DATE_FORMAT = 'MMMM dd, yyyy'


class TrialToCourtDialogViewModifier(sched.SchedulingViewModifier):
    """Class for building and modifying the Trial to Court Hearing Notice Dialog."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.set_view_dates()

    def set_view_dates(self) -> None:
        today = QDate.currentDate()
        self.dialog.trial_date.setDate(today)
        self.dialog.entry_date.setDate(today)


class TrialToCourtDialogSlotFunctions(sched.SchedulingSlotFunctions):
    """Class for Trial To Court Hearing Notice Functions - only inherits at present."""

    def set_event_date(self, day_to_set: str) -> 'QDate':
        today = QDate.currentDate()
        days_until_speedy_trial_date = today.daysTo(self.get_speedy_trial_date())
        event_date = today.addDays(days_until_speedy_trial_date)
        while event_date.dayOfWeek() != DAY_DICT.get(day_to_set):
            event_date = event_date.addDays(-1)
        return event_date

    def update_all_scheduled_dates(self):
        trial_date = self.set_event_date('Monday')
        self.dialog.trial_date.setDate(trial_date)

    def get_speedy_trial_date(self) -> 'QDate':
        speedy_trial_days = self.get_speedy_trial_days()
        days_in_jail = self.get_days_in_jail()
        continuance_days = self.get_continuance_days()
        speedy_trial_days = (speedy_trial_days + continuance_days) - days_in_jail
        return self.dialog.arrest_summons_date_box.date().addDays(speedy_trial_days)

    def set_speedy_trial_date_label(self):
        speedy_trial_date = self.get_speedy_trial_date()
        speedy_trial_date = speedy_trial_date.toString(ENTRY_DATE_FORMAT)
        self.dialog.speedy_trial_date_label.setText(speedy_trial_date)

    def get_speedy_trial_days(self) -> int:
        key = self.dialog.highest_charge_box.currentText()
        return SPEEDY_TRIAL_TIME_DICT.get(key)

    def get_days_in_jail(self) -> int:
        """Multiply days in jail times 3 for speedy trial calculations."""
        if self.dialog.days_in_jail_line.text() == '':
            days_in_jail = 0
        else:
            days_in_jail = int(self.dialog.days_in_jail_line.text())
        return 3 * days_in_jail

    def get_continuance_days(self) -> int:
        if self.dialog.continuance_days_line.text() == '':
            continuance_days = 0
        else:
            continuance_days = int(self.dialog.continuance_days_line.text())
        return continuance_days


class TrialToCourtDialogSignalConnector(sched.SchedulingSignalConnector):
    """Class for connecting signals for Trial to Court Hearing Notice Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()
        self.connect_dialog_specific_signals()

    def connect_dialog_specific_signals(self):
        func = self.dialog.functions
        self.dialog.arrest_summons_date_box.dateChanged.connect(func.set_speedy_trial_date_label)
        self.dialog.arrest_summons_date_box.dateChanged.connect(func.update_all_scheduled_dates)
        self.dialog.highest_charge_box.currentIndexChanged.connect(func.set_speedy_trial_date_label)
        self.dialog.days_in_jail_line.textChanged.connect(func.set_speedy_trial_date_label)
        self.dialog.continuance_days_line.textChanged.connect(func.set_speedy_trial_date_label)
        self.dialog.highest_charge_box.currentIndexChanged.connect(func.update_all_scheduled_dates)
        self.dialog.days_in_jail_line.textChanged.connect(func.update_all_scheduled_dates)
        self.dialog.continuance_days_line.textChanged.connect(func.update_all_scheduled_dates)


class TrialToCourtDialogCaseInformationUpdater(SchedulingModelUpdater):
    """Class for updating Trial To Court Hearing Notice Dialog information."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.model.assigned_judge = self.dialog.assigned_judge
        self.model.courtroom = self.dialog.courtroom
        self.model.judicial_officer = self.dialog.judicial_officer

    def set_scheduling_dates(self) -> None:
        self.model.trial_to_court_date = self.dialog.trial_date.date().toString('MMMM dd, yyyy')
        self.model.trial_to_court_time = self.dialog.trial_time_box.currentText()
        self.model.hearing_location = self.dialog.hearing_location_box.currentText()


class TrialToCourtDialogInfoChecker(SchedulingChecker):
    """Class with checks for the Trial To Court Info Checker."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.dialog_check_list = [
            'check_if_trial_date_is_today',
        ]
        self.check_status = self.perform_check_list()


class TrialToCourtHearingDialog(sched.SchedulingDialogBuilder, Ui_TrialToCourtHearingDialog):
    """Builder class for the Trial to Court Notice of Hearing.

    The judicial_officer for this entry is the selected Assignment Commissioner.

    The assigned_judge and courtroom is set by the button pressed choosing the dialog and entry.
    """

    _case_information_model = SchedulingCaseInformation
    _case_loader = SchedulingCrimCmsLoader
    _info_checker = TrialToCourtDialogInfoChecker
    _model_updater = TrialToCourtDialogCaseInformationUpdater
    _signal_connector = TrialToCourtDialogSignalConnector
    _slots = TrialToCourtDialogSlotFunctions
    _view_modifier = TrialToCourtDialogViewModifier
    dialog_name = 'Trial To Court Notice Hearing Entry'

    def additional_setup(self):
        self.assigned_judge = set_assigned_judge(self.sender())
        self.courtroom = set_courtroom(self.sender())
        self.setWindowTitle(f'{self.dialog_name} Case Information - {self.assigned_judge}')
        self.hearing_location_box.setCurrentText(self.courtroom)
