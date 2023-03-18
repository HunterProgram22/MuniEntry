"""Module that contains Probation Updater classes."""
from munientry.updaters.base_updaters import BaseModelUpdater


class ProbationCaseInformationUpdater(BaseModelUpdater):
    """Base class for Probation Updater."""

    def __init__(self, dialog: 'QDialog') -> None:
        super().__init__(dialog)
        self.set_party_information()
        self.update_conditional_data()

    def update_conditional_data(self):
        self.dialog.transfer_view_data_to_model(self.model)
