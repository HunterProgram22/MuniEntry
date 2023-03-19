"""Module that contains Probation Updater classes."""
from munientry.updaters.base_updaters import BaseDialogUpdater


class ProbationModelUpdater(BaseDialogUpdater):
    """Base class for Probation Updater."""

    def __init__(self, dialog: 'QDialog') -> None:
        super().__init__(dialog)
        self.update_model_with_case_information_frame_data()
        self.update_conditional_data()

    def update_model_with_case_information_frame_data(self):
        self.set_case_number_and_date()
        self.set_party_information()

    def update_conditional_data(self):
        self.dialog.transfer_view_data_to_model(self.model)

    def set_case_number_and_date(self):
        self.model.case_number = self.dialog.case_number_lineEdit.text()
        self.model.entry_date = self.dialog.entry_date.date().toString('MMMM dd, yyyy')

    def set_party_information(self):
        self.model.defendant.first_name = self.dialog.defendant_first_name_lineEdit.text()
        self.model.defendant.last_name = self.dialog.defendant_last_name_lineEdit.text()
