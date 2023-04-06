"""Module containing classes for building the General Hearing Notice Dialog."""
from loguru import logger
from PyQt6.QtCore import QDate

from munientry.builders.scheduling import base_scheduling_builders as sched
from munientry.checkers.scheduling_checks import SchedulingChecks
from munientry.helper_functions import set_assigned_judge, set_courtroom
from munientry.loaders.cms_case_loaders import SchedulingCrimCmsLoader
from munientry.models.scheduling_information import SchedulingCaseInformation
from munientry.updaters.scheduling_updaters import  SchedulingModelUpdater
from munientry.views.general_notice_of_hearing_dialog_ui import Ui_GeneralNoticeOfHearingDialog


class GeneralNoticeOfHearingDialogViewModifier(sched.SchedulingViewModifier):
    """View class that creates and modifies the view for the General Notice of Hearing Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_view_dates()

    def set_view_dates(self):
        today = QDate.currentDate()
        self.dialog.entry_date.setDate(today)
        self.dialog.hearing_date.setDate(today)


class GeneralNoticeOfHearingDialogSignalConnector(sched.SchedulingSignalConnector):
    """Class that connects signals to slots for General Notice of Hearing Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()
        self.connect_dialog_specific_signals()

    def connect_dialog_specific_signals(self) -> None:
        func = self.dialog.functions
        self.dialog.old_speedy_trial_date.dateChanged.connect(func.update_speedy_trial_date)
        self.dialog.old_hearing_date.dateChanged.connect(func.update_speedy_trial_date)
        self.dialog.new_hearing_date.dateChanged.connect(func.update_speedy_trial_date)


class GeneralNoticeOfHearingDialogSlotFunctions(sched.SchedulingSlotFunctions):
    """Class that adds to base slot functions for use by General Notice of Hearing Dialog.

    Currently no additional functions are added so only accesses BaseDialogSlotFunctions.
    """

    def update_speedy_trial_date(self) -> None:
        days_to_add = self.dialog.old_hearing_date.date().daysTo(
            self.dialog.new_hearing_date.date(),
        )
        new_speedy_trial_date = self.dialog.old_speedy_trial_date.date().addDays(days_to_add)
        new_speedy_trial_date = new_speedy_trial_date.toString('MMMM dd, yyyy')
        self.dialog.speedy_trial_date_label.setText(new_speedy_trial_date)


class GeneralNoticeOfHearingCaseInformationUpdater(SchedulingModelUpdater):
    """Class that updates case information for General Notice of Hearing Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.model.assigned_judge = self.dialog.assigned_judge
        self.model.courtroom = self.dialog.courtroom
        self.model.judicial_officer = self.dialog.judicial_officer

    def set_scheduling_dates(self):
        self.model.hearing_date = self.dialog.hearing_date.date().toString('MMMM dd, yyyy')
        self.model.hearing_time = self.dialog.hearing_time_box.currentText()
        self.model.hearing_type = self.dialog.hearing_type_box.currentText()
        self.model.hearing_location = self.dialog.hearing_location_box.currentText()


class GeneralNoticeOfHearingCheckList(SchedulingChecks):
    """Class with checks for the General Notice Hearing."""
    check_list = []


class GeneralNoticeOfHearingDialog(sched.SchedulingDialogBuilder, Ui_GeneralNoticeOfHearingDialog):
    """Builder class for the General Notice of Hearing.

    The judicial_officer for this entry is the selected Assignment Commissioner.

    The assigned_judge and courtroom is set by the button pressed choosing the dialog and entry.
    """

    _case_information_model = SchedulingCaseInformation
    _case_loader = SchedulingCrimCmsLoader
    _info_checker = GeneralNoticeOfHearingCheckList
    _model_updater = GeneralNoticeOfHearingCaseInformationUpdater
    _signal_connector = GeneralNoticeOfHearingDialogSignalConnector
    _slots = GeneralNoticeOfHearingDialogSlotFunctions
    _view_modifier = GeneralNoticeOfHearingDialogViewModifier
    dialog_name = 'General Notice Of Hearing Entry'

    def additional_setup(self):
        self.assigned_judge = set_assigned_judge(self.sender())
        self.courtroom = set_courtroom(self.sender())
        self.setWindowTitle(f'{self.dialog_name} Case Information - {self.assigned_judge}')
        self.hearing_location_box.setCurrentText(self.courtroom)
