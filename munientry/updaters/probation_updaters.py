"""Module that contains Probation Updater classes."""
from loguru import logger

from munientry.updaters.base_updaters import BaseModelUpdater


class ProbationDialogCaseInformationUpdater(BaseModelUpdater):
    """Base class for Probation Updater."""

    def __init__(self, dialog: 'QDialog') -> None:
        super().__init__(dialog)
        self.set_party_information()
        self.update_terms_of_community_control()

    def update_terms_of_community_control(self):
        try:
            self.dialog.transfer_view_data_to_model(self.model)
        except AttributeError as err:
            logger.warning(err)
