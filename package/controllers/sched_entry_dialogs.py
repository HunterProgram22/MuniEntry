from datetime import date, timedelta
from package.controllers.view_modifiers import BaseDialogViewModifier
from package.controllers.base_dialogs import BaseDialog
from package.views.scheduling_entry_dialog_ui import Ui_SchedulingEntryDialog

from PyQt5.QtCore import QDate

from package.controllers.helper_functions import set_future_date
TODAY = QDate.currentDate()

class SchedulingEntryDialog(BaseDialog, Ui_SchedulingEntryDialog):
    def __init__(self, parent: object = None):
        super().__init__(parent)
        self.dialog_name = "Scheduling Entry"
        self.update_speedy_trial_date()

    def modify_view(self):
        return SchedulingEntryDialogViewModifier(self)

    def create_dialog_slot_functions(self) -> None:
        pass

    def connect_signals_to_slots(self) -> None:
        self.arrest_summons_date_box.dateChanged.connect(self.update_speedy_trial_date)
        self.highest_charge_box.currentIndexChanged.connect(self.update_speedy_trial_date)
        self.days_in_jail_lineEdit.textChanged.connect(self.update_speedy_trial_date)
        self.continuance_days_lineEdit.textChanged.connect(self.update_speedy_trial_date)
        self.trial_dateEdit.dateChanged.connect(self.update_scheduled_dates)

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

class SchedulingEntryDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog = dialog
        self.dialog.plea_trial_date.setDate(TODAY)
        self.dialog.trial_dateEdit.setDate(TODAY)
        self.dialog.arrest_summons_date_box.setDate(TODAY)

