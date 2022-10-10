"""Module that contains Scheduling Updater classes."""
from loguru import logger

from munientry.updaters.base_updaters import BaseDialogUpdater


class SchedulingDialogCaseInformationUpdater(BaseDialogUpdater):
    """Base class for Scheduling Updater."""

    def __init__(self, dialog: 'QDialog') -> None:
        super().__init__(dialog)
        self.update_model_with_case_information_frame_data()

    def update_model_with_case_information_frame_data(self) -> None:
        """The set_scheduling_dates method is called by subclassed dialogs."""
        self.set_case_number_and_date()
        self.set_party_information()
        self.set_defense_counsel_information()
        self.set_scheduling_dates()

    def set_case_number_and_date(self) -> None:
        self.model.case_number = self.dialog.case_number_lineEdit.text()
        self.model.plea_trial_date = self.dialog.plea_trial_date.date().toString('MMMM dd, yyyy')

    def set_party_information(self) -> None:
        self.model.defendant.first_name = self.dialog.defendant_first_name_lineEdit.text()
        self.model.defendant.last_name = self.dialog.defendant_last_name_lineEdit.text()

    def set_defense_counsel_information(self) -> None:
        self.model.defense_counsel = self.dialog.defense_counsel_name_box.currentText()
