"""Module containing classes for hearing notices."""
from loguru import logger
from PyQt5.QtCore import QDate

from munientry.builders.base_dialogs import BaseDialog
from munientry.controllers.signal_connectors import BaseDialogSignalConnector
from munientry.controllers.slot_functions import BaseDialogSlotFunctions
from munientry.controllers.view_modifiers import BaseDialogViewModifier
from munientry.data.cms_case_loaders import CmsNoChargeLoader
from munientry.models.scheduling_information import SchedulingCaseInformation
from munientry.models.template_types import TEMPLATE_DICT
from munientry.updaters.general_updaters import CaseInformationUpdater
from munientry.views.final_jury_notice_of_hearing_dialog_ui import (
    Ui_FinalJuryNoticeOfHearingDialog,
)

TODAY = QDate.currentDate()


class FinalJuryNoticeOfHearingDialog(BaseDialog, Ui_FinalJuryNoticeOfHearingDialog):
    def __init__(
            self, judicial_officer=None, cms_case=None, case_table=None, parent=None
    ):
        self.case_table = case_table
        logger.info(f'Loading case from {self.case_table}')
        if judicial_officer.last_name == 'Hemmeter':
            self.dialog_name = 'Notice Of Hearing Entry Hemmeter'
        elif judicial_officer.last_name == 'Rohrer':
            self.dialog_name = 'Notice Of Hearing Entry Rohrer'
        else:
            self.dialog_name = 'Notice Of Hearing Entry'
        super().__init__(parent)
        logger.info(f'Loaded Dialog: {self.dialog_name}')
        self.judicial_officer = judicial_officer
        self.cms_case = cms_case
        logger.info(f'Loaded Case {self.cms_case.case_number}')
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.entry_case_information = SchedulingCaseInformation()
        self.load_cms_data_to_view()

    def load_cms_data_to_view(self):
        return CmsNoChargeLoader(self)

    def modify_view(self):
        return FinalJuryNoticeOfHearingDialogViewModifier(self)

    def connect_signals_to_slots(self) -> None:
        self.functions = FinalJuryNoticeOfHearingDialogSlotFunctions(self)
        FinalJuryNoticeOfHearingDialogSignalConnector(self)

    def update_entry_case_information(self):
        return FinalJuryNoticeOfHearingDialogCaseInformationUpdater(self)


class FinalJuryNoticeOfHearingDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog = dialog
        self.set_view_dates()

    def set_view_dates(self):
        self.dialog.plea_trial_date.setDate(TODAY)
        self.dialog.trial_dateEdit.setDate(TODAY)
        self.dialog.final_pretrial_dateEdit.setDate(TODAY)


class FinalJuryNoticeOfHearingDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog = dialog
        self.functions = dialog.functions
        self.dialog.clear_fields_case_Button.released.connect(self.functions.clear_case_information_fields)
        self.dialog.create_entry_Button.released.connect(self.functions.create_entry)
        self.dialog.close_dialog_Button.released.connect(self.dialog.functions.close_window)
        self.dialog.jury_trial_only_no_radioButton.toggled.connect(self.functions.show_hide_final_pretrial)
        self.dialog.jury_trial_only_yes_radioButton.toggled.connect(self.functions.show_hide_final_pretrial)


class FinalJuryNoticeOfHearingDialogSlotFunctions(BaseDialogSlotFunctions):
    def __init__(self, dialog):
        self.dialog = dialog

    def show_hide_final_pretrial(self):
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


class FinalJuryNoticeOfHearingDialogCaseInformationUpdater(CaseInformationUpdater):
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
        self.model.final_pretrial_date = self.view.final_pretrial_dateEdit.date().toString(
            "MMMM dd, yyyy"
        )
        self.model.final_pretrial_time = self.view.final_pretrial_time_box.currentText()
        if self.view.jury_trial_only_no_radioButton.isChecked():
            self.model.jury_trial_only = 'No'
        elif self.view.jury_trial_only_yes_radioButton.isChecked():
            self.model.jury_trial_only = 'Yes'


if __name__ == "__main__":
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
