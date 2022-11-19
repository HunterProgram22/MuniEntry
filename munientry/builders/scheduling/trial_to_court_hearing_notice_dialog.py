"""Module for creating and operating the Trial To Court Hearing Notice Dialog."""
from loguru import logger

from munientry.builders.scheduling import base_scheduling_builders as sched
from munientry.checkers.base_checks import BaseChecker
from munientry.helper_functions import set_assigned_judge, set_courtroom
from munientry.loaders.cms_case_loaders import SchedulingCmsLoader
from munientry.models.scheduling_information import SchedulingCaseInformation
from munientry.appsettings.pyqt_constants import TODAY
from munientry.updaters.scheduling_updaters import (
    SchedulingDialogCaseInformationUpdater,
)
from munientry.views.trial_to_court_hearing_dialog_ui import (
    Ui_TrialToCourtHearingDialog,
)


class TrialToCourtDialogViewModifier(sched.SchedulingViewModifier):
    """Class for building and modifying the Trial to Court Hearing Notice Dialog."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.set_view_dates()

    def set_view_dates(self) -> None:
        self.dialog.trial_dateEdit.setDate(TODAY)
        self.dialog.plea_trial_date.setDate(TODAY)


class TrialToCourtDialogSlotFunctions(sched.SchedulingSlotFunctions):
    """Class for Trial To Court Hearing Notice Functions - only inherits at present."""


class TrialToCourtDialogSignalConnector(sched.SchedulingSignalConnector):
    """Class for connecting signals for Trial to Court Hearing Notice Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()


class TrialToCourtDialogCaseInformationUpdater(SchedulingDialogCaseInformationUpdater):
    """Class for updating Trial To Court Hearing Notice Dialog information."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.model.assigned_judge = self.dialog.assigned_judge
        self.model.courtroom = self.dialog.courtroom
        self.model.judicial_officer = self.dialog.judicial_officer

    def set_scheduling_dates(self) -> None:
        self.model.trial_to_court_date = self.dialog.trial_dateEdit.date().toString('MMMM dd, yyyy')
        self.model.trial_to_court_time = self.dialog.trial_time_box.currentText()
        self.model.hearing_location = self.dialog.hearing_location_box.currentText()


class TrialToCourtDialogInfoChecker(BaseChecker):
    """Class with checks for the Trial To Court Info Checker."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.dialog_check_list = []
        self.check_status = self.perform_check_list()


class TrialToCourtHearingDialog(sched.SchedulingDialogBuilder, Ui_TrialToCourtHearingDialog):
    """Builder class for the Trial to Court Notice of Hearing.

    The judicial_officer for this entry is the selected Assignment Commissioner.

    The assigned_judge and courtroom is set by the button pressed choosing the dialog and entry.
    """

    build_dict = {
        'dialog_name': 'Trial To Court Notice Of Hearing Entry',
        'view': TrialToCourtDialogViewModifier,
        'slots': TrialToCourtDialogSlotFunctions,
        'signals': TrialToCourtDialogSignalConnector,
        'case_information_model': SchedulingCaseInformation,
        'loader': SchedulingCmsLoader,
        'updater': TrialToCourtDialogCaseInformationUpdater,
        'info_checker': TrialToCourtDialogInfoChecker,
    }

    def additional_setup(self):
        self.assigned_judge = set_assigned_judge(self.sender())
        self.courtroom = set_courtroom(self.sender())
        self.setWindowTitle(f'{self.dialog_name} Case Information - {self.assigned_judge}')
        self.hearing_location_box.setCurrentText(self.courtroom)


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
