"""Module that contains Scheduling Updater classes."""
from munientry.updaters.base_updaters import BaseModelUpdater


class SchedulingDialogCaseInformationUpdater(BaseModelUpdater):
    """Base class for Scheduling Updater."""

    def __init__(self, dialog: 'QDialog') -> None:
        super().__init__(dialog)
        self.set_party_information()
        self.set_defense_counsel_information()
        self.set_scheduling_dates()

    def set_defense_counsel_information(self) -> None:
        self.model.defense_counsel = self.dialog.defense_counsel_name_box.currentText()
