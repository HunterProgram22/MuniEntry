"""Module containing classes for hearing notices."""
from loguru import logger

from package.controllers.view_modifiers import BaseDialogViewModifier
from package.controllers.base_dialogs import BaseDialog
from package.views.notice_of_hearing_dialog_ui import Ui_NoticeOfHearingDialog

from package.models.template_types import TEMPLATE_DICT

from PyQt5.QtCore import QDate

from package.models.scheduling_information import SchedulingCaseInformation
from package.controllers.signal_connectors import BaseDialogSignalConnector
from package.controllers.slot_functions import BaseDialogSlotFunctions
from package.updaters.general_updaters import CaseInformationUpdater
from package.controllers.cms_case_loaders import CmsNoChargeLoader

TODAY = QDate.currentDate()
SPEEDY_TRIAL_TIME_DICT = {
    "M1": 90,
    "M2": 90,
    "M3": 45,
    "M4": 45,
    "MM": 30,
    "UCM": 30,
}
DAY_DICT = {
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
}

EVENT_DICT = {
    "Final Pretrial": 2,
    "Pretrial": 28,
}
PRETRIAL_TIME_DICT = {
    "Pretrial 4 weeks before trial": 28,
    "Pretrial 3 weeks before trial": 21,
    "Pretrial 2 weeks before trial": 14,
    "No Pretrial": 0,
}


class NoticeOfHearingDialog(BaseDialog, Ui_NoticeOfHearingDialog):
    def __init__(
            self, judicial_officer=None, cms_case=None, case_table=None, parent=None
    ):
        self.case_table = case_table
        self.dialog_name = "Notice Of Hearing Entry"
        super().__init__(parent)
        self.judicial_officer = judicial_officer
        logger.debug(self.judicial_officer.last_name)
        self.cms_case = cms_case
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.entry_case_information = SchedulingCaseInformation()
        self.load_cms_data_to_view()
        self.functions.update_final_pretrial_date()

    def load_cms_data_to_view(self):
        return CmsNoChargeLoader(self)

    def modify_view(self):
        return NoticeOfHearingDialogViewModifier(self)

    def create_dialog_slot_functions(self) -> None:
        self.functions = NoticeOfHearingDialogSlotFunctions(self)

    def connect_signals_to_slots(self) -> None:
        return NoticeOfHearingDialogSignalConnector(self)

    def update_entry_case_information(self):
        return NoticeOfHearingDialogCaseInformationUpdater(self)


class NoticeOfHearingDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog = dialog
        self.dialog.setWindowTitle(f"{self.dialog.dialog_name} Case Information")
        self.set_view_dates()

    def set_view_dates(self):
        self.dialog.trial_dateEdit.setDate(TODAY)
        self.dialog.plea_trial_date.setDate(TODAY)


class NoticeOfHearingDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog = dialog
        self.functions = dialog.functions
        self.dialog.clear_fields_case_Button.released.connect(self.functions.clear_case_information_fields)
        self.dialog.create_entry_Button.released.connect(self.functions.create_entry)
        self.dialog.close_dialog_Button.released.connect(self.dialog.functions.close_window)
        self.dialog.trial_dateEdit.dateChanged.connect(self.functions.update_final_pretrial_date)


class NoticeOfHearingDialogSlotFunctions(BaseDialogSlotFunctions):
    def __init__(self, dialog):
        self.dialog = dialog

    def update_final_pretrial_date(self):
        if self.dialog.judicial_officer.last_name == "Rohrer":
            final_pretrial_date = self.set_event_date("Thursday", "Final Pretrial")
        elif self.dialog.judicial_officer.last_name == "Hemmeter":
            final_pretrial_date = self.set_event_date("Tuesday", "Final Pretrial")
        self.dialog.final_pretrial_dateEdit.setDate(final_pretrial_date)

    def set_event_date(self, day_to_set: str, event_to_set: str) -> QDate:
        if event_to_set == "Trial":
            days_until_speedy_trial_date = TODAY.daysTo(self.get_speedy_trial_date())
            event_date = TODAY.addDays(days_until_speedy_trial_date)
        elif event_to_set == "Pretrial":
            pretrial_time = self.get_pretrial_time()
            event_date = self.dialog.trial_dateEdit.date().addDays(-pretrial_time)
        else:
            days_to_event = EVENT_DICT.get(event_to_set)
            event_date = self.dialog.trial_dateEdit.date().addDays(-days_to_event)
        while event_date.dayOfWeek() != DAY_DICT.get(day_to_set):
            event_date = event_date.addDays(-1)
        return event_date


class NoticeOfHearingDialogCaseInformationUpdater(CaseInformationUpdater):
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


if __name__ == "__main__":
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
