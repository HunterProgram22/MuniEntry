from loguru import logger

from package.controllers.view_modifiers import BaseDialogViewModifier
from package.controllers.base_dialogs import BaseDialog
from package.views.scheduling_entry_dialog_ui import Ui_SchedulingEntryDialog

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

class SchedulingEntryDialog(BaseDialog, Ui_SchedulingEntryDialog):
    def __init__(
        self, judicial_officer=None, dialog_name=None, cms_case=None, case_table=None, parent=None
    ):
        self.case_table = case_table
        self.dialog_name = dialog_name
        super().__init__(parent)
        self.judicial_officer = judicial_officer
        self.cms_case = cms_case
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.entry_case_information = SchedulingCaseInformation()
        self.load_cms_data_to_view()
        self.functions.set_speedy_trial_date_label()
        self.functions.update_all_scheduled_dates()

    def load_cms_data_to_view(self):
        return CmsNoChargeLoader(self)

    def modify_view(self):
        return SchedulingEntryDialogViewModifier(self)

    def create_dialog_slot_functions(self) -> None:
        self.functions = SchedulingEntryDialogSlotFunctions(self)

    def connect_signals_to_slots(self) -> None:
        return SchedulingEntryDialogSignalConnector(self)

    def update_entry_case_information(self):
        return SchedulingEntryDialogCaseInformationUpdater(self)


class SchedulingEntryDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog = dialog
        self.dialog.setWindowTitle(f"{self.dialog.dialog_name} Case Information")
        self.set_view_dates()

    def set_view_dates(self):
        self.dialog.arrest_summons_date_box.setDate(TODAY)
        self.dialog.trial_dateEdit.setDate(TODAY)
        self.dialog.plea_trial_date.setDate(TODAY)


class SchedulingEntryDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog = dialog
        self.functions = dialog.functions
        self.dialog.clear_fields_case_Button.released.connect(self.functions.clear_case_information_fields)
        self.dialog.create_entry_Button.released.connect(self.functions.create_entry)
        self.dialog.close_dialog_Button.released.connect(self.dialog.functions.close_window)
        self.dialog.arrest_summons_date_box.dateChanged.connect(self.functions.set_speedy_trial_date_label)
        self.dialog.arrest_summons_date_box.dateChanged.connect(self.functions.update_all_scheduled_dates)
        self.dialog.highest_charge_box.currentIndexChanged.connect(self.functions.set_speedy_trial_date_label)
        self.dialog.days_in_jail_lineEdit.textChanged.connect(self.functions.set_speedy_trial_date_label)
        self.dialog.continuance_days_lineEdit.textChanged.connect(self.functions.set_speedy_trial_date_label)
        self.dialog.trial_dateEdit.dateChanged.connect(self.functions.update_final_pretrial_and_pretrial_only)
        self.dialog.highest_charge_box.currentIndexChanged.connect(self.functions.update_all_scheduled_dates)
        self.dialog.days_in_jail_lineEdit.textChanged.connect(self.functions.update_all_scheduled_dates)
        self.dialog.continuance_days_lineEdit.textChanged.connect(self.functions.update_all_scheduled_dates)
        self.dialog.four_week_pretrial_radioButton.clicked.connect(self.functions.update_final_pretrial_and_pretrial_only)
        self.dialog.three_week_pretrial_radioButton.clicked.connect(self.functions.update_final_pretrial_and_pretrial_only)
        self.dialog.two_week_pretrial_radioButton.clicked.connect(self.functions.update_final_pretrial_and_pretrial_only)
        self.dialog.no_pretrial_radioButton.clicked.connect(self.functions.update_final_pretrial_and_pretrial_only)
        self.dialog.four_week_pretrial_radioButton.clicked.connect(self.functions.set_pretrial_scheduled)
        self.dialog.three_week_pretrial_radioButton.clicked.connect(self.functions.set_pretrial_scheduled)
        self.dialog.two_week_pretrial_radioButton.clicked.connect(self.functions.set_pretrial_scheduled)
        self.dialog.no_pretrial_radioButton.clicked.connect(self.functions.set_pretrial_scheduled)


class SchedulingEntryDialogSlotFunctions(BaseDialogSlotFunctions):
    def __init__(self, dialog):
        self.dialog = dialog

    def set_pretrial_scheduled(self):
        if self.dialog.no_pretrial_radioButton.isChecked():
            self.dialog.entry_case_information.pretrial_scheduled = False
            self.dialog.pretrial_dateEdit.setHidden(True)
            self.dialog.pretrial_date_label.setHidden(True)
        else:
            self.dialog.entry_case_information.pretrial_scheduled = True
            self.dialog.pretrial_dateEdit.setHidden(False)
            self.dialog.pretrial_date_label.setHidden(False)

    def update_all_scheduled_dates(self):
        if self.dialog.dialog_name == "Rohrer Scheduling Entry":
            trial_date = self.set_event_date("Tuesday", "Trial")
            self.dialog.trial_dateEdit.setDate(trial_date)
            self.update_final_pretrial_and_pretrial_only()
        elif self.dialog.dialog_name == "Hemmeter Scheduling Entry":
            trial_date = self.set_event_date("Thursday", "Trial")
            self.dialog.trial_dateEdit.setDate(trial_date)
            self.update_final_pretrial_and_pretrial_only()

    def update_final_pretrial_and_pretrial_only(self):
        if self.dialog.dialog_name == "Rohrer Scheduling Entry":
            final_pretrial_date = self.set_event_date("Thursday", "Final Pretrial")
            pretrial_date = self.set_event_date("Monday", "Pretrial")
        elif self.dialog.dialog_name == "Hemmeter Scheduling Entry":
            final_pretrial_date = self.set_event_date("Tuesday", "Final Pretrial")
            pretrial_date =  self.set_event_date("Wednesday", "Pretrial")
        self.dialog.final_pretrial_dateEdit.setDate(final_pretrial_date)
        self.dialog.pretrial_dateEdit.setDate(pretrial_date)

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

    def get_pretrial_time(self) -> int:
        for button in [self.dialog.four_week_pretrial_radioButton, self.dialog.three_week_pretrial_radioButton,
                       self.dialog.two_week_pretrial_radioButton, self.dialog.no_pretrial_radioButton, ]:
            if button.isChecked():
                return PRETRIAL_TIME_DICT.get(button.text())

    def get_speedy_trial_date(self) -> QDate:
        speedy_trial_days = self.get_speedy_trial_days()
        days_in_jail = self.get_days_in_jail()
        continuance_days = self.get_continuance_days()
        speedy_trial_days = (speedy_trial_days + continuance_days) - days_in_jail
        speedy_trial_date = self.dialog.arrest_summons_date_box.date().addDays(speedy_trial_days)
        return speedy_trial_date

    def set_speedy_trial_date_label(self):
        speedy_trial_date = self.get_speedy_trial_date()
        speedy_trial_date = speedy_trial_date.toString("MMMM dd, yyyy")
        self.dialog.speedy_trial_date_label.setText(speedy_trial_date)

    def get_speedy_trial_days(self) -> int:
        key = self.dialog.highest_charge_box.currentText()
        speedy_trial_days = SPEEDY_TRIAL_TIME_DICT.get(key)
        return speedy_trial_days

    def get_days_in_jail(self) -> int:
        """Multiply days in jail times 3 for speedy trial calculations."""
        if self.dialog.days_in_jail_lineEdit.text() == "":
            days_in_jail = 0
        else:
            days_in_jail = int(self.dialog.days_in_jail_lineEdit.text())
        return 3 * days_in_jail

    def get_continuance_days(self) -> int:
        if self.dialog.continuance_days_lineEdit.text() == "":
            continuance_days = 0
        else:
            continuance_days = int(self.dialog.continuance_days_lineEdit.text())
        return continuance_days


class SchedulingEntryDialogCaseInformationUpdater(CaseInformationUpdater):
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
        self.model.pretrial_date = self.view.pretrial_dateEdit.date().toString("MMMM dd, yyyy")
        self.model.final_pretrial_time = self.view.final_pretrial_time_box.currentText()


if __name__ == "__main__":
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
