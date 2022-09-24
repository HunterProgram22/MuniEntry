"""The module that contains the main classes for creating an entry dialog."""
from loguru import logger

from munientry.builders.base_dialogs import CriminalBaseDialog
from munientry.checkers.base_checks import (
    FreeformDialogInfoChecker,
)
from munientry.controllers.signal_connectors import (
    FreeformDialogSignalConnector,
)
from munientry.controllers.slot_functions import (
    FreeformDialogSlotFunctions,
)
from munientry.controllers.view_modifiers import (
    FreeformDialogViewModifier,
)
from munientry.data.cms_case_loaders import CmsNoChargeLoader
from munientry.models.case_information.plea_entries import (
    FreeformEntryCaseInformation,
)
from munientry.models.template_types import TEMPLATE_DICT
from munientry.updaters.no_grid_case_updaters import (
    FreeformDialogUpdater,
)
from munientry.views.freeform_dialog_ui import Ui_FreeformEntryDialog


class FreeformDialog(CriminalBaseDialog, Ui_FreeformEntryDialog):
    """Dialog builder class for 'Freeform Entry'."""

    def __init__(
        self,
        judicial_officer: object,
        cms_case: str = None,
        case_table: str = None,
        parent: object = None,
    ):
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.dialog_name = 'Freeform Entry Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)

    def _modify_view(self) -> FreeformDialogViewModifier:
        return FreeformDialogViewModifier(self)

    def _connect_signals_to_slots(self) -> None:
        self.functions = FreeformDialogSlotFunctions(self)
        FreeformDialogSignalConnector(self)

    def load_entry_case_information_model(self) -> None:
        self.entry_case_information = FreeformEntryCaseInformation()
        self.entry_case_information.judicial_officer = self.judicial_officer

    def load_cms_data_to_view(self) -> CmsNoChargeLoader:
        return CmsNoChargeLoader(self)

    def update_entry_case_information(self) -> FreeformDialogUpdater:
        return FreeformDialogUpdater(self)

    def perform_info_checks(self) -> None:
        self.dialog_checks = FreeformDialogInfoChecker(self)


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
