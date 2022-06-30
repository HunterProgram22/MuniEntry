"""The module that contains the main classes for creating an entry dialog."""
from loguru import logger

from package.controllers.cms_case_loaders import CmsNoChargeLoader
from package.controllers.signal_connectors import (
    FailureToAppearDialogSignalConnector,
    FreeformDialogSignalConnector,
)
from package.controllers.slot_functions import (
    FailureToAppearDialogSlotFunctions,
    FreeformDialogSlotFunctions,
)
from package.controllers.view_modifiers import (
    FailureToAppearDialogViewModifier,
    FreeformDialogViewModifier,
)
from package.dialog_builders.base_dialogs import CriminalBaseDialog
from package.information_checkers.base_checks import (
    FailureToAppearDialogInfoChecker,
    FreeformDialogInfoChecker,
)
from package.models.case_information.plea_entries import (
    FailureToAppearEntryCaseInformation,
    FreeformEntryCaseInformation,
)
from package.models.conditions_models import FailureToAppearConditions
from package.models.template_types import TEMPLATE_DICT
from package.updaters.no_grid_case_updaters import (
    FailureToAppearDialogUpdater,
    FreeformDialogUpdater,
)
from package.views.failure_to_appear_dialog_ui import Ui_FailureToAppearDialog
from package.views.freeform_dialog_ui import Ui_FreeformEntryDialog


class FailureToAppearDialog(CriminalBaseDialog, Ui_FailureToAppearDialog):
    """Dialog builder class for 'Failure To Appear / Issue Warrant' Entry."""

    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.dialog_name = 'Failure To Appear Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.entry_case_information.fta_conditions = FailureToAppearConditions()

    def modify_view(self):
        """Standard call to build the view, then updates appearance reason.

        Sets appearance reason to final pre-trial instead of change of plea if dialog opens a
        case from the final pretrials table.
        """
        FailureToAppearDialogViewModifier(self)
        if self.case_table == 'final_pretrials':
            self.appearance_reason_box.setCurrentText('final pre-trial')

    def create_dialog_slot_functions(self):
        self.functions = FailureToAppearDialogSlotFunctions(self)
        self.functions.hide_warrant_radius()
        self.functions.hide_bond_boxes()

    def connect_signals_to_slots(self):
        return FailureToAppearDialogSignalConnector(self)

    def load_entry_case_information_model(self):
        self.entry_case_information = FailureToAppearEntryCaseInformation()
        self.entry_case_information.judicial_officer = self.judicial_officer

    def load_cms_data_to_view(self):
        return CmsNoChargeLoader(self)

    def update_entry_case_information(self):
        return FailureToAppearDialogUpdater(self)

    def perform_info_checks(self):
        self.dialog_checks = FailureToAppearDialogInfoChecker(self)


class FreeformDialog(CriminalBaseDialog, Ui_FreeformEntryDialog):
    """Dialog builder class for 'Freeform Entry'."""

    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.dialog_name = 'Freeform Entry Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)

    def modify_view(self):
        return FreeformDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = FreeformDialogSlotFunctions(self)

    def connect_signals_to_slots(self):
        return FreeformDialogSignalConnector(self)

    def load_entry_case_information_model(self):
        self.entry_case_information = FreeformEntryCaseInformation()
        self.entry_case_information.judicial_officer = self.judicial_officer

    def load_cms_data_to_view(self):
        return CmsNoChargeLoader(self)

    def update_entry_case_information(self):
        return FreeformDialogUpdater(self)

    def perform_info_checks(self):
        self.dialog_checks = FreeformDialogInfoChecker(self)


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
