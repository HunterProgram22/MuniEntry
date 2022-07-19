"""Module for creating and operating the Trial To Court Hearing Notice Dialog."""
from loguru import logger

from munientry.builders.base_dialogs import SchedulingBaseDialog
from munientry.controllers.helper_functions import set_assigned_judge, set_courtroom
from munientry.controllers.signal_connectors import BaseDialogSignalConnector
from munientry.controllers.slot_functions import BaseDialogSlotFunctions
from munientry.controllers.view_modifiers import BaseDialogViewModifier
from munientry.data.cms_case_loaders import CmsNoChargeLoader
from munientry.models.scheduling_information import SchedulingCaseInformation
from munientry.models.template_types import TEMPLATE_DICT
from munientry.settings import DAY_DICT, EVENT_DICT, TODAY, TYPE_CHECKING
from munientry.updaters.general_updaters import CaseInformationUpdater
from munientry.views.trial_to_court_hearing_dialog_ui import (
    Ui_TrialToCourtHearingDialog,
)


class TrialToCourtHearingDialog(SchedulingBaseDialog, Ui_TrialToCourtHearingDialog):
    """Builder class for the Trial to Court Notice of Hearing.

    The judicial_officer for this entry is the selected Assignment Commissioner.

    The assigned_judge and courtroom is set by the button pressed choosing the dialog and entry.
    """
    def __init__(
            self, judicial_officer=None, cms_case=None, case_table=None, parent=None
    ):
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.dialog_name = 'Trial To Court Notice Of Hearing Entry'
        logger.info(f'Loaded Dialog: {self.dialog_name}')
        self.assigned_judge = set_assigned_judge(self.sender())
        self.courtroom = set_courtroom(self.sender())
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.setWindowTitle(f'{self.dialog_name} Case Information - {self.assigned_judge}')
        self.hearing_location_box.setCurrentText(self.courtroom)

    def modify_view(self):
        return TrialToCourtDialogViewModifier(self)

    def connect_signals_to_slots(self) -> None:
        self.functions = TrialToCourtDialogSlotFunctions(self)
        TrialToCourtDialogSignalConnector(self)

    def load_entry_case_information_model(self):
        self.entry_case_information = SchedulingCaseInformation()
        self.entry_case_information.judicial_officer = self.judicial_officer

    def load_cms_data_to_view(self):
        return CmsNoChargeLoader(self)

    def update_entry_case_information(self):
        return TrialToCourtDialogCaseInformationUpdater(self)


class TrialToCourtDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog = dialog
        self.functions = dialog.functions
        self.dialog.clear_fields_case_Button.released.connect(self.functions.clear_case_information_fields)
        self.dialog.create_entry_Button.released.connect(self.functions.create_entry)
        self.dialog.close_dialog_Button.released.connect(self.dialog.functions.close_window)


class TrialToCourtDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog = dialog
        self.set_view_dates()

    def set_view_dates(self):
        self.dialog.trial_dateEdit.setDate(TODAY)
        self.dialog.plea_trial_date.setDate(TODAY)


class TrialToCourtDialogSlotFunctions(BaseDialogSlotFunctions):
    def __init__(self, dialog):
        self.dialog = dialog


class TrialToCourtDialogCaseInformationUpdater(CaseInformationUpdater):
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
        self.model.assigned_judge = self.view.assigned_judge
        self.model.courtroom = self.view.courtroom
        self.model.judicial_officer = self.view.judicial_officer
        self.set_scheduling_dates()

    def set_case_number_and_date(self):
        self.model.case_number = self.view.case_number_lineEdit.text()
        self.model.plea_trial_date = self.view.plea_trial_date.date().toString("MMMM dd, yyyy")

    def set_party_information(self):
        self.model.defendant.first_name = self.view.defendant_first_name_lineEdit.text()
        self.model.defendant.last_name = self.view.defendant_last_name_lineEdit.text()

    def set_defense_counsel_information(self):
        self.model.defense_counsel = self.view.defense_counsel_name_box.currentText()

    def set_scheduling_dates(self):
        self.model.trial_date = self.view.trial_dateEdit.date().toString("MMMM dd, yyyy")
        self.model.trial_time = self.view.trial_time_box.currentText()
        self.model.hearing_location = self.view.hearing_location_box.currentText()


if __name__ == "__main__":
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
