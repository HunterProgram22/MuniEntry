"""Module containing classes for building the General Hearing Notice Dialog."""
from loguru import logger
from PyQt5.QtCore import QDate

from munientry.builders.base_dialogs import BaseDialogSignalConnector
from munientry.builders.crimtraffic.base_crimtraffic_builders import (
    BaseDialogSlotFunctions,
    BaseDialogViewModifier,
)
from munientry.builders.scheduling.base_scheduling_builders import SchedulingBaseDialog
from munientry.checkers.base_checks import BaseChecker
from munientry.controllers.helper_functions import set_assigned_judge, set_courtroom
from munientry.data.cms_case_loaders import CmsNoChargeLoader
from munientry.models.scheduling_information import SchedulingCaseInformation
from munientry.updaters.general_updaters import CaseInformationUpdater
from munientry.views.general_notice_of_hearing_dialog_ui import (
    Ui_GeneralNoticeOfHearingDialog,
)

TODAY = QDate.currentDate()


class GeneralNoticeOfHearingDialogViewModifier(BaseDialogViewModifier):
    """View class that creates and modifies the view for the General Notice of Hearing Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog = dialog
        self.set_view_dates()

    def set_view_dates(self):
        self.dialog.plea_trial_date.setDate(TODAY)
        self.dialog.hearing_dateEdit.setDate(TODAY)


class GeneralNoticeOfHearingDialogSignalConnector(BaseDialogSignalConnector):
    """Class that connects signals to slots for General Notice of Hearing Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()


class GeneralNoticeOfHearingDialogSlotFunctions(BaseDialogSlotFunctions):
    """Class that adds to base slot functions for use by General Notice of Hearing Dialog.

    Currently no additional functions are added so only accesses BaseDialogSlotFunctions.
    """


class GeneralNoticeOfHearingCaseInformationUpdater(CaseInformationUpdater):
    """Class that updates case information for General Notice of Hearing Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.view = dialog
        self.update_model_with_case_information_frame_data()

    def update_model_with_case_information_frame_data(self):
        self.set_case_number_and_date()
        self.set_party_information()
        self.set_defense_counsel_information()
        self.set_scheduling_dates()
        self.model.assigned_judge = self.view.assigned_judge
        self.model.courtroom = self.view.courtroom
        self.model.judicial_officer = self.view.judicial_officer

    def set_case_number_and_date(self):
        self.model.case_number = self.view.case_number_lineEdit.text()
        self.model.plea_trial_date = self.view.plea_trial_date.date().toString('MMMM dd, yyyy')

    def set_party_information(self):
        self.model.defendant.first_name = self.view.defendant_first_name_lineEdit.text()
        self.model.defendant.last_name = self.view.defendant_last_name_lineEdit.text()

    def set_defense_counsel_information(self):
        self.model.defense_counsel = self.view.defense_counsel_name_box.currentText()

    def set_scheduling_dates(self):
        self.model.hearing_date = self.view.hearing_dateEdit.date().toString('MMMM dd, yyyy')
        self.model.hearing_time = self.view.hearing_time_box.currentText()
        self.model.hearing_type = self.view.hearing_type_box.currentText()
        self.model.hearing_location = self.view.hearing_location_box.currentText()


class GeneralNoticeOfHearingInfoChecker(BaseChecker):
    """Class with checks for the General Notice Hearing Info Checker."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.dialog_check_list = []
        self.check_status = self.perform_check_list()


class GeneralNoticeOfHearingDialog(SchedulingBaseDialog, Ui_GeneralNoticeOfHearingDialog):
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
        'loader': CmsNoChargeLoader,
        'updater': GeneralNoticeOfHearingCaseInformationUpdater,
        'info_checker': GeneralNoticeOfHearingInfoChecker,
    }

    def additional_setup(self):
        self.assigned_judge = set_assigned_judge(self.sender())
        self.courtroom = set_courtroom(self.sender())
        self.setWindowTitle(f'{self.dialog_name} Case Information - {self.assigned_judge}')
        self.hearing_location_box.setCurrentText(self.courtroom)


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
