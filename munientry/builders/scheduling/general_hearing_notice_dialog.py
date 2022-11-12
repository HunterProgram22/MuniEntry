"""Module containing classes for building the General Hearing Notice Dialog."""
from loguru import logger
from PyQt6.QtCore import QDate

from munientry.builders.scheduling import base_scheduling_builders as sched
from munientry.checkers.base_checks import BaseChecker
from munientry.helper_functions import set_assigned_judge, set_courtroom
from munientry.loaders.cms_case_loaders import SchedulingCmsLoader
from munientry.models.scheduling_information import SchedulingCaseInformation
from munientry.updaters.scheduling_updaters import (
    SchedulingDialogCaseInformationUpdater,
)
from munientry.views.general_notice_of_hearing_dialog_ui import (
    Ui_GeneralNoticeOfHearingDialog,
)

TODAY = QDate.currentDate()


class GeneralNoticeOfHearingDialogViewModifier(sched.SchedulingViewModifier):
    """View class that creates and modifies the view for the General Notice of Hearing Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_view_dates()

    def set_view_dates(self):
        self.dialog.plea_trial_date.setDate(TODAY)
        self.dialog.hearing_dateEdit.setDate(TODAY)


class GeneralNoticeOfHearingDialogSignalConnector(sched.SchedulingSignalConnector):
    """Class that connects signals to slots for General Notice of Hearing Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()


class GeneralNoticeOfHearingDialogSlotFunctions(sched.SchedulingSlotFunctions):
    """Class that adds to base slot functions for use by General Notice of Hearing Dialog.

    Currently no additional functions are added so only accesses BaseDialogSlotFunctions.
    """


class GeneralNoticeOfHearingCaseInformationUpdater(SchedulingDialogCaseInformationUpdater):
    """Class that updates case information for General Notice of Hearing Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.model.assigned_judge = self.dialog.assigned_judge
        self.model.courtroom = self.dialog.courtroom
        self.model.judicial_officer = self.dialog.judicial_officer

    def set_scheduling_dates(self):
        self.model.hearing_date = self.dialog.hearing_dateEdit.date().toString('MMMM dd, yyyy')
        self.model.hearing_time = self.dialog.hearing_time_box.currentText()
        self.model.hearing_type = self.dialog.hearing_type_box.currentText()
        self.model.hearing_location = self.dialog.hearing_location_box.currentText()


class GeneralNoticeOfHearingInfoChecker(BaseChecker):
    """Class with checks for the General Notice Hearing Info Checker."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.dialog_check_list = []
        self.check_status = self.perform_check_list()


class GeneralNoticeOfHearingDialog(sched.SchedulingDialogBuilder, Ui_GeneralNoticeOfHearingDialog):
    """Builder class for the General Notice of Hearing.

    The judicial_officer for this entry is the selected Assignment Commissioner.

    The assigned_judge and courtroom is set by the button pressed choosing the dialog and entry.
    """

    build_dict = {
        'dialog_name': 'General Notice Of Hearing Entry',
        'view': GeneralNoticeOfHearingDialogViewModifier,
        'slots': GeneralNoticeOfHearingDialogSlotFunctions,
        'signals': GeneralNoticeOfHearingDialogSignalConnector,
        'case_information_model': SchedulingCaseInformation,
        'loader': SchedulingCmsLoader,
        'updater': GeneralNoticeOfHearingCaseInformationUpdater,
        'info_checker': GeneralNoticeOfHearingInfoChecker,
    }

    def additional_setup(self):
        self.assigned_judge = set_assigned_judge(self.sender())
        self.courtroom = set_courtroom(self.sender())
        self.setWindowTitle(f'{self.dialog_name} Case Information - {self.assigned_judge}')
        self.hearing_location_box.setCurrentText(self.courtroom)


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
