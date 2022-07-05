"""The module that contains the main classes for creating an entry dialog."""
from loguru import logger

from munientry.builders.base_dialogs import CriminalBaseDialog
from munientry.controllers.cms_case_loaders import CmsNoChargeLoader
from munientry.controllers.signal_connectors import (
    FailureToAppearDialogSignalConnector,
    FreeformDialogSignalConnector,
)
from munientry.controllers.slot_functions import (
    FailureToAppearDialogSlotFunctions,
    FreeformDialogSlotFunctions,
)
from munientry.controllers.view_modifiers import (
    FailureToAppearDialogViewModifier,
    FreeformDialogViewModifier,
)
from munientry.checkers.base_checks import (
    FailureToAppearDialogInfoChecker,
    FreeformDialogInfoChecker,
)
from munientry.models.case_information.plea_entries import (
    FailureToAppearEntryCaseInformation,
    FreeformEntryCaseInformation,
)
from munientry.models.conditions_models import FailureToAppearConditions
from munientry.models.template_types import TEMPLATE_DICT
from munientry.updaters.no_grid_case_updaters import (
    FailureToAppearDialogUpdater,
    FreeformDialogUpdater,
)
from munientry.views.failure_to_appear_dialog_ui import Ui_FailureToAppearDialog
from munientry.views.freeform_dialog_ui import Ui_FreeformEntryDialog


class FailureToAppearDialog(CriminalBaseDialog, Ui_FailureToAppearDialog):
    """Dialog builder class for 'Failure To Appear / Issue Warrant' Entry."""

    def __init__(
        self,
        judicial_officer: object,
        cms_case: str = None,
        case_table: str = None,
        parent: object = None,
    ) -> None:
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.dialog_name = 'Failure To Appear Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.entry_case_information.fta_conditions = FailureToAppearConditions()

    def modify_view(self) -> None:
        """Standard call to build the view, then updates appearance reason.

        Sets appearance reason to final pre-trial instead of change of plea if dialog opens a
        case from the final pretrials table.
        """
        FailureToAppearDialogViewModifier(self)
        if self.case_table == 'final_pretrials':
            self.appearance_reason_box.setCurrentText('final pre-trial')

    def connect_signals_to_slots(self) -> None:
        self.functions = FailureToAppearDialogSlotFunctions(self)
        self.functions.hide_warrant_radius()
        self.functions.hide_bond_boxes()
        FailureToAppearDialogSignalConnector(self)

    def load_entry_case_information_model(self) -> None:
        self.entry_case_information = FailureToAppearEntryCaseInformation()
        self.entry_case_information.judicial_officer = self.judicial_officer

    def load_cms_data_to_view(self) -> CmsNoChargeLoader:
        return CmsNoChargeLoader(self)

    def update_entry_case_information(self) -> FailureToAppearDialogUpdater:
        return FailureToAppearDialogUpdater(self)

    def perform_info_checks(self) -> None:
        self.dialog_checks = FailureToAppearDialogInfoChecker(self)


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

    def modify_view(self) -> FreeformDialogViewModifier:
        return FreeformDialogViewModifier(self)

    def connect_signals_to_slots(self) -> None:
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
