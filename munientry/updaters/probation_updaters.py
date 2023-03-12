"""Module that contains Probation Updater classes."""
from loguru import logger

from munientry.updaters.base_updaters import BaseDialogUpdater


class ProbationDialogCaseInformationUpdater(BaseDialogUpdater):
    """Base class for Probation Updater."""

    def __init__(self, dialog: 'QDialog') -> None:
        super().__init__(dialog)
        self.update_model_with_case_information_frame_data()
        self.update_terms_of_community_control()

    def update_model_with_case_information_frame_data(self) -> None:
        self.set_case_number_and_date()
        self.set_party_information()

    def update_terms_of_community_control(self):
        self.dialog.transfer_view_data_to_model(self.model)

    def set_case_number_and_date(self) -> None:
        self.model.case_number = self.dialog.case_number_lineEdit.text()
        self.model.entry_date = self.dialog.entry_date.date().toString('MMMM dd, yyyy')

    def set_party_information(self) -> None:
        self.model.defendant.first_name = self.dialog.defendant_first_name_lineEdit.text()
        self.model.defendant.last_name = self.dialog.defendant_last_name_lineEdit.text()
