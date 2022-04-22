from datetime import date, timedelta
from package.controllers.view_modifiers import BaseDialogViewModifier
from package.controllers.base_dialogs import BaseDialog
from package.views.scheduling_entry_dialog_ui import Ui_SchedulingEntryDialog

from package.models.template_types import TEMPLATE_DICT

from PyQt5.QtCore import QDate

from package.controllers.helper_functions import set_future_date
from package.models.scheduling_information import SchedulingCaseInformation
from package.controllers.signal_connectors import BaseDialogSignalConnector
from package.controllers.slot_functions import BaseDialogSlotFunctions
from package.controllers.case_updaters import CaseModelUpdater

TODAY = QDate.currentDate()

class SchedulingEntryDialog(BaseDialog, Ui_SchedulingEntryDialog):
    def __init__(self, parent: object = None):
        super().__init__(parent)
        self.dialog_name = "Scheduling Entry Dialog"
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.entry_case_information = SchedulingCaseInformation()
        self.update_speedy_trial_date()

    def modify_view(self):
        return SchedulingEntryDialogViewModifier(self)

    def create_dialog_slot_functions(self) -> None:
        self.functions = BaseDialogSlotFunctions(self)

    def connect_signals_to_slots(self) -> None:
        self.clear_fields_case_Button.released.connect(self.functions.clear_case_information_fields)
        self.create_entry_Button.released.connect(self.functions.create_entry)
        self.close_dialog_Button.released.connect(self.functions.close_dialog)
        self.arrest_summons_date_box.dateChanged.connect(self.update_speedy_trial_date)
        self.highest_charge_box.currentIndexChanged.connect(self.update_speedy_trial_date)
        self.days_in_jail_lineEdit.textChanged.connect(self.update_speedy_trial_date)
        self.continuance_days_lineEdit.textChanged.connect(self.update_speedy_trial_date)
        self.trial_dateEdit.dateChanged.connect(self.update_scheduled_dates)
        return SchedulingEntryDialogSignalConnector(self)

    def update_scheduled_dates(self):
        final_pretrial_date = self.trial_dateEdit.date().addDays(-2)
        self.final_pretrial_dateEdit.setDate(final_pretrial_date)
        pretrial_date = self.final_pretrial_dateEdit.date().addDays(-30)
        self.pretrial_dateEdit.setDate(pretrial_date)

    def update_speedy_trial_date(self):
        speedy_trial_days = self.get_speedy_trial_days()
        days_in_jail = self.get_days_in_jail()
        continuance_days = self.get_continuance_days()
        speedy_trial_days = speedy_trial_days - (days_in_jail + continuance_days)
        speedy_trial_date = self.arrest_summons_date_box.date().addDays(speedy_trial_days)
        speedy_trial_date = speedy_trial_date.toString("MMMM dd, yyyy")
        self.speedy_trial_date_label.setText(speedy_trial_date)

    def get_speedy_trial_days(self) -> int:
        speedy_trial_dict = {
            "M1": 90,
            "M2": 90,
            "M3": 45,
            "M4": 45,
            "MM": 30,
            "UCM": 30,
        }
        key = self.highest_charge_box.currentText()
        speedy_trial_days = speedy_trial_dict.get(key)
        return speedy_trial_days

    def get_days_in_jail(self) -> int:
        """Multiply days in jail times 3 for speedy trial calculations."""
        if self.days_in_jail_lineEdit.text() == "":
            days_in_jail = 0
        else:
            days_in_jail = int(self.days_in_jail_lineEdit.text())
        return 3*days_in_jail

    def get_continuance_days(self) -> int:
        if self.continuance_days_lineEdit.text() == "":
            continuance_days = 0
        else:
            continuance_days = int(self.continuance_days_lineEdit.text())
        return continuance_days

    def update_entry_case_information(self):
        return SchedulingEntryDialogCaseModelUpdater(self)


class SchedulingEntryDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog = dialog
        self.dialog.plea_trial_date.setDate(TODAY)
        self.dialog.trial_dateEdit.setDate(TODAY)
        self.dialog.arrest_summons_date_box.setDate(TODAY)


class SchedulingEntryDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)


class SchedulingEntryDialogCaseModelUpdater(CaseModelUpdater):
    def __init__(self, dialog):
        super().__init__(dialog)
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
        self.model.defense_counsel_type = self.view.defense_counsel_type_box.currentText()

    def set_scheduling_dates(self):
        self.model.trial_date = self.view.trial_dateEdit.date().toString("MMMM dd, yyyy")
        self.model.final_pretrial_date = self.view.final_pretrial_dateEdit.date().toString("MMMM dd, yyyy")
        self.model.pretrial_date = self.view.pretrial_dateEdit.date().toString("MMMM dd, yyyy")
        self.model.final_pretrial_time = self.view.final_pretrial_time_box.currentText()
