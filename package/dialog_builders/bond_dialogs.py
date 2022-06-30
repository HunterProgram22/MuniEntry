"""Module for building main entry bond dialogs."""
from loguru import logger

from package.controllers.cms_case_loaders import CmsNoChargeLoader
from package.controllers.signal_connectors import (
    BondHearingDialogSignalConnector,
    NoPleaBondDialogSignalConnector,
    ProbationViolationBondDialogSignalConnector,
)
from package.controllers.slot_functions import (
    BondHearingDialogSlotFunctions,
    NoPleaBondDialogSlotFunctions,
    ProbationViolationBondDialogSlotFunctions,
)
from package.controllers.view_modifiers import (
    BondHearingDialogViewModifier,
    NoPleaBondDialogViewModifier,
    ProbationViolationBondDialogViewModifier,
)
from package.dialog_builders.base_dialogs import CriminalBaseDialog
from package.information_checkers.bond_checkers import (
    BondHearingDialogInfoChecker,
    NoPleaBondDialogInfoChecker,
    ProbationViolationBondDialogInfoChecker,
)
from package.models.case_information.plea_entries import (
    BondHearingEntryCaseInformation,
    CommunityControlViolationEntryCaseInformation,
    NoPleaBondEntryCaseInformation,
)
from package.models.conditions_models import (
    BondConditions,
    BondModificationConditions,
    CommunityControlViolationBondConditions,
)
from package.models.template_types import TEMPLATE_DICT
from package.updaters.no_grid_case_updaters import (
    BondHearingDialogUpdater,
    NoPleaBondDialogUpdater,
    ProbationViolationBondDialogUpdater,
)
from package.views.bond_hearing_dialog_ui import Ui_BondHearingDialog
from package.views.no_plea_bond_dialog_ui import Ui_NoPleaBondDialog
from package.views.probation_violation_bond_dialog_ui import (
    Ui_ProbationViolationBondDialog,
)


class NoPleaBondDialog(CriminalBaseDialog, Ui_NoPleaBondDialog):
    """Dialog builder class for 'Appear on Warrant (No Plea) / Bond' Entry."""

    condition_checkbox_dict = {
        'monitoring_checkBox': ['monitoring_type_box'],
        'specialized_docket_checkBox': ['specialized_docket_type_box'],
    }

    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.additional_conditions_list = [
            (
                'admin_license_suspension_checkBox',
                self.entry_case_information.admin_license_suspension,
            ),
            (
                'domestic_violence_checkBox',
                self.entry_case_information.domestic_violence_conditions,
            ),
            ('no_contact_checkBox', self.entry_case_information.no_contact),
            ('custodial_supervision_checkBox', self.entry_case_information.custodial_supervision),
            ('other_conditions_checkBox', self.entry_case_information.other_conditions),
            ('vehicle_seizure_checkBox', self.entry_case_information.vehicle_seizure),
        ]
        self.dialog_name = 'No Plea Bond Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.entry_case_information.bond_conditions = BondConditions()

    def modify_view(self):
        return NoPleaBondDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = NoPleaBondDialogSlotFunctions(self)

    def connect_signals_to_slots(self):
        return NoPleaBondDialogSignalConnector(self)

    def update_entry_case_information(self):
        """Calls the dialog specific CaseModelUpdater in the grid_case_updaters.py module."""
        return NoPleaBondDialogUpdater(self)

    def load_entry_case_information_model(self):
        self.entry_case_information = NoPleaBondEntryCaseInformation()
        self.entry_case_information.judicial_officer = self.judicial_officer

    def load_cms_data_to_view(self):
        return CmsNoChargeLoader(self)

    def perform_info_checks(self):
        self.dialog_checks = NoPleaBondDialogInfoChecker(self)


class ProbationViolationBondDialog(CriminalBaseDialog, Ui_ProbationViolationBondDialog):
    """Dialog builder class for 'Prelim. Probation Violation / Bond' Entry."""

    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.dialog_name = 'Probation Violation Bond Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.entry_case_information.bond_conditions = CommunityControlViolationBondConditions()

    def modify_view(self):
        return ProbationViolationBondDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = ProbationViolationBondDialogSlotFunctions(self)
        self.functions.hide_bond_conditions()

    def connect_signals_to_slots(self):
        return ProbationViolationBondDialogSignalConnector(self)

    def load_entry_case_information_model(self):
        self.entry_case_information = CommunityControlViolationEntryCaseInformation()
        self.entry_case_information.judicial_officer = self.judicial_officer

    def load_cms_data_to_view(self):
        return CmsNoChargeLoader(self)

    def update_entry_case_information(self):
        return ProbationViolationBondDialogUpdater(self)

    def perform_info_checks(self):
        self.dialog_checks = ProbationViolationBondDialogInfoChecker(self)


class BondHearingDialog(CriminalBaseDialog, Ui_BondHearingDialog):
    """Dialog builder class for 'Bond Modification / Revocation' Entry."""

    condition_checkbox_dict = {
        'monitoring_checkBox': ['monitoring_type_box'],
        'specialized_docket_checkBox': ['specialized_docket_type_box'],
    }

    def __init__(
        self,
        judicial_officer: object,
        cms_case: str = None,
        case_table: str = None,
        parent: object = None,
    ) -> None:
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.additional_conditions_list = [
            (
                'admin_license_suspension_checkBox',
                self.entry_case_information.admin_license_suspension,
            ),
            (
                'domestic_violence_checkBox',
                self.entry_case_information.domestic_violence_conditions,
            ),
            ('no_contact_checkBox', self.entry_case_information.no_contact),
            ('custodial_supervision_checkBox', self.entry_case_information.custodial_supervision),
            ('other_conditions_checkBox', self.entry_case_information.other_conditions),
            ('vehicle_seizure_checkBox', self.entry_case_information.vehicle_seizure),
        ]
        self.dialog_name = 'Bond Hearing Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.entry_case_information.bond_conditions = BondModificationConditions()

    def modify_view(self) -> BondHearingDialogViewModifier:
        return BondHearingDialogViewModifier(self)

    def create_dialog_slot_functions(self) -> None:
        self.functions = BondHearingDialogSlotFunctions(self)

    def connect_signals_to_slots(self) -> BondHearingDialogSignalConnector:
        return BondHearingDialogSignalConnector(self)

    def load_entry_case_information_model(self):
        self.entry_case_information = BondHearingEntryCaseInformation()
        self.entry_case_information.judicial_officer = self.judicial_officer

    def load_cms_data_to_view(self) -> CmsNoChargeLoader:
        return CmsNoChargeLoader(self)

    def update_entry_case_information(self) -> BondHearingDialogUpdater:
        """Calls the dialog specific CaseModelUpdater in the grid_case_updaters.py module."""
        return BondHearingDialogUpdater(self)

    def perform_info_checks(self) -> None:
        self.dialog_checks = BondHearingDialogInfoChecker(self)


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
