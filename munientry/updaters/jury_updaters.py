"""Module that contains Jury Payment Updater classes."""
from loguru import logger

from munientry.updaters.base_updaters import BaseDialogUpdater


class JuryPaymentCaseInformationUpdater(BaseDialogUpdater):
    """Base class for Jury Payment Updater."""

    def __init__(self, dialog: 'QDialog') -> None:
        super().__init__(dialog)
        self.update_model_with_case_information_frame_data()

    def update_model_with_case_information_frame_data(self) -> None:
        """The set_scheduling_dates method is called by subclassed dialogs."""
        self.set_case_number_and_date()
        self.set_party_information()

    def set_case_number_and_date(self) -> None:
        self.model.case_number = self.dialog.case_number_lineEdit.text()
        self.model.trial_date = self.dialog.trial_date.date().toString('MMMM dd, yyyy')
        self.model.entry_date = self.dialog.entry_date.date().toString('MMMM dd, yyyy')

    def set_party_information(self) -> None:
        self.model.defendant.first_name = self.dialog.defendant_first_name_lineEdit.text()
        self.model.defendant.last_name = self.dialog.defendant_last_name_lineEdit.text()
