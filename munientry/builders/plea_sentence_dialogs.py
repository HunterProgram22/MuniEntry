"""Module containing classes to build Plea and Sentencing Dialogs."""
from loguru import logger

from munientry.builders.base_dialogs import CriminalBaseDialog
from munientry.checkers.no_jail_sentencing_checkers import (
    FineOnlyDialogInfoChecker,
)
from munientry.controllers.signal_connectors import (
    FineOnlyDialogSignalConnector,
)
from munientry.controllers.slot_functions import (
    FineOnlyDialogSlotFunctions,
)
from munientry.controllers.view_modifiers import (
    FineOnlyDialogViewModifier,
)
from munientry.data.cms_case_loaders import CmsFraLoader
from munientry.models.case_information.sentencing_entries import (
    FineOnlyEntryCaseInformation,
)
from munientry.models.template_types import TEMPLATE_DICT
from munientry.updaters.grid_case_updaters import (
    FineOnlyDialogUpdater,
)
from munientry.views.fine_only_plea_dialog_ui import Ui_FineOnlyPleaDialog


class FineOnlyPleaDialog(CriminalBaseDialog, Ui_FineOnlyPleaDialog):
    """Dialog builder class for 'Fine Only' dialog."""

    def __init__(
        self,
        judicial_officer: object,
        cms_case: str = None,
        case_table: str = None,
        parent: object = None,
    ) -> None:
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.additional_conditions_list = [
            ('license_suspension_checkBox', self.entry_case_information.license_suspension),
            ('community_service_checkBox', self.entry_case_information.community_service),
            ('other_conditions_checkBox', self.entry_case_information.other_conditions),
        ]
        self.dialog_name = 'Fine Only Plea Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)

    def _modify_view(self) -> None:
        FineOnlyDialogViewModifier(self)

    def _connect_signals_to_slots(self) -> None:
        self.functions = FineOnlyDialogSlotFunctions(self)
        self.functions.set_fines_credit_for_jail_field()
        FineOnlyDialogSignalConnector(self)

    def load_entry_case_information_model(self) -> None:
        self.entry_case_information = FineOnlyEntryCaseInformation()
        self.entry_case_information.judicial_officer = self.judicial_officer

    def load_cms_data_to_view(self) -> None:
        CmsFraLoader(self)

    def update_entry_case_information(self) -> None:
        FineOnlyDialogUpdater(self)

    def perform_info_checks(self) -> None:
        self.dialog_checks = FineOnlyDialogInfoChecker(self)


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
