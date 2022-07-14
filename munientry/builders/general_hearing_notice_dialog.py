"""Module containing classes for building the General Hearing Notice Dialog."""
from loguru import logger
from PyQt5.QtCore import QDate

from munientry.builders.base_dialogs import SchedulingBaseDialog
from munientry.controllers.signal_connectors import BaseDialogSignalConnector
from munientry.controllers.slot_functions import BaseDialogSlotFunctions
from munientry.controllers.view_modifiers import BaseDialogViewModifier
from munientry.data.cms_case_loaders import CmsNoChargeLoader
from munientry.models.scheduling_information import SchedulingCaseInformation
from munientry.models.template_types import TEMPLATE_DICT
from munientry.updaters.general_updaters import CaseInformationUpdater
from munientry.views.general_notice_of_hearing_dialog_ui import (
    Ui_GeneralNoticeOfHearingDialog,
)

TODAY = QDate.currentDate()


def set_assigned_judge(sender) -> str:
    if sender.objectName() == 'hemmeter_general_hearingButton':
        return 'Judge Marianne T. Hemmeter'
    if sender.objectName() == 'rohrer_general_hearingButton':
        return 'Judge Kyle E. Rohrer'


def set_courtroom(sender) -> str:
    if sender.objectName() == 'hemmeter_general_hearingButton':
        return 'Courtroom B'
    if sender.objectName() == 'rohrer_general_hearingButton':
        return 'Courtroom A'


class GeneralNoticeOfHearingDialog(SchedulingBaseDialog, Ui_GeneralNoticeOfHearingDialog):
    """Builder class for the General Notice of Hearing.

    The judicial_officer for this entry is the selected Assignment Commissioner.

    The assigned_judge and courtroom is set by the button pressed choosing the dialog and entry.
    """

    def __init__(
        self, judicial_officer=None, cms_case=None, case_table=None, parent=None
    ):
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.dialog_name = 'General Notice Of Hearing Entry'
        logger.info(f'Loaded Dialog: {self.dialog_name}')
        self.assigned_judge = set_assigned_judge(self.sender())
        self.courtroom = set_courtroom(self.sender())
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.setWindowTitle(f'{self.dialog_name} Case Information - {self.assigned_judge}')
        self.hearing_location_box.setCurrentText(self.courtroom)

    def load_cms_data_to_view(self):
        return CmsNoChargeLoader(self)

    def modify_view(self):
        return GeneralNoticeOfHearingDialogViewModifier(self)

    def connect_signals_to_slots(self) -> None:
        self.functions = GeneralNoticeOfHearingDialogSlotFunctions(self)
        GeneralNoticeOfHearingDialogSignalConnector(self)

    def update_entry_case_information(self):
        return GeneralNoticeOfHearingDialogCaseInformationUpdater(self)


class GeneralNoticeOfHearingDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog = dialog
        self.set_view_dates()

    def set_view_dates(self):
        self.dialog.plea_trial_date.setDate(TODAY)
        self.dialog.hearing_dateEdit.setDate(TODAY)


class GeneralNoticeOfHearingDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog = dialog
        self.functions = dialog.functions
        self.dialog.clear_fields_case_Button.released.connect(self.functions.clear_case_information_fields)
        self.dialog.create_entry_Button.released.connect(self.functions.create_entry)
        self.dialog.close_dialog_Button.released.connect(self.dialog.functions.close_window)


class GeneralNoticeOfHearingDialogSlotFunctions(BaseDialogSlotFunctions):
    def __init__(self, dialog):
        self.dialog = dialog


class GeneralNoticeOfHearingDialogCaseInformationUpdater(CaseInformationUpdater):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.view = dialog
        self.update_model_with_case_information_frame_data()

    def update_model_with_case_information_frame_data(self):
        """Calls the methods that update all model with all fields in the case information (top
        frame) in all main entry dialogs."""
        self.set_case_number_and_date()
        self.set_party_information()
        self.set_defense_counsel_information()
        self.set_scheduling_dates()
        self.model.assigned_judge = self.view.assigned_judge
        self.model.courtroom = self.view.courtroom
        self.model.judicial_officer = self.view.judicial_officer

    def set_case_number_and_date(self):
        self.model.case_number = self.view.case_number_lineEdit.text()
        self.model.plea_trial_date = self.view.plea_trial_date.date().toString("MMMM dd, yyyy")

    def set_party_information(self):
        self.model.defendant.first_name = self.view.defendant_first_name_lineEdit.text()
        self.model.defendant.last_name = self.view.defendant_last_name_lineEdit.text()

    def set_defense_counsel_information(self):
        self.model.defense_counsel = self.view.defense_counsel_name_box.currentText()

    def set_scheduling_dates(self):
        self.model.hearing_date = self.view.hearing_dateEdit.date().toString("MMMM dd, yyyy")
        self.model.hearing_time = self.view.hearing_time_box.currentText()
        self.model.hearing_type = self.view.hearing_type_box.currentText()
        self.model.hearing_location = self.view.hearing_location_box.currentText()


if __name__ == "__main__":
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
