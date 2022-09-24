"""Module for building main entry bond dialogs."""
from loguru import logger

from munientry.builders.base_dialogs import CriminalBaseDialog
from munientry.checkers.bond_checkers import (
    BondHearingDialogInfoChecker,
    ProbationViolationBondDialogInfoChecker,
)
from munientry.controllers.signal_connectors import (
    BondHearingDialogSignalConnector,
    ProbationViolationBondDialogSignalConnector,
)
from munientry.controllers.slot_functions import (
    BondHearingDialogSlotFunctions,
    ProbationViolationBondDialogSlotFunctions,
)
from munientry.controllers.view_modifiers import (
    BondHearingDialogViewModifier,
    ProbationViolationBondDialogViewModifier,
)
from munientry.data.cms_case_loaders import CmsNoChargeLoader
from munientry.models.case_information.plea_entries import (
    BondHearingEntryCaseInformation,
    CommunityControlViolationEntryCaseInformation,
)
from munientry.models.conditions_models import (
    BondModificationConditions,
    CommunityControlViolationBondConditions,
)
from munientry.models.template_types import TEMPLATE_DICT
from munientry.updaters.no_grid_case_updaters import (
    BondHearingDialogUpdater,
    ProbationViolationBondDialogUpdater,
)
from munientry.views.bond_hearing_dialog_ui import Ui_BondHearingDialog
from munientry.views.probation_violation_bond_dialog_ui import (
    Ui_ProbationViolationBondDialog,
)


class ProbationViolationBondDialog(CriminalBaseDialog, Ui_ProbationViolationBondDialog):
    """Dialog builder class for 'Prelim. Probation Violation / Bond' Entry."""

    def __init__(
        self,
        judicial_officer: object,
        cms_case: str = None,
        case_table: str = None,
        parent: object = None,
    ) -> None:
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.dialog_name = 'Probation Violation Bond Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.entry_case_information.bond_conditions = CommunityControlViolationBondConditions()

    def _modify_view(self) -> ProbationViolationBondDialogViewModifier:
        return ProbationViolationBondDialogViewModifier(self)

    def _connect_signals_to_slots(self) -> None:
        self.functions = ProbationViolationBondDialogSlotFunctions(self)
        self.functions.hide_bond_conditions()
        ProbationViolationBondDialogSignalConnector(self)

    def load_entry_case_information_model(self) -> None:
        self.entry_case_information = CommunityControlViolationEntryCaseInformation()
        self.entry_case_information.judicial_officer = self.judicial_officer

    def load_cms_data_to_view(self) -> CmsNoChargeLoader:
        return CmsNoChargeLoader(self)

    def update_entry_case_information(self) -> ProbationViolationBondDialogUpdater:
        return ProbationViolationBondDialogUpdater(self)

    def perform_info_checks(self) -> None:
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

    def _modify_view(self) -> BondHearingDialogViewModifier:
        return BondHearingDialogViewModifier(self)

    def _connect_signals_to_slots(self) -> None:
        self.functions = BondHearingDialogSlotFunctions(self)
        BondHearingDialogSignalConnector(self)

    def load_entry_case_information_model(self):
        self.entry_case_information = BondHearingEntryCaseInformation()
        self.entry_case_information.judicial_officer = self.judicial_officer

    def load_cms_data_to_view(self) -> CmsNoChargeLoader:
        return CmsNoChargeLoader(self)

    def update_entry_case_information(self) -> BondHearingDialogUpdater:
        return BondHearingDialogUpdater(self)

    def perform_info_checks(self) -> None:
        self.dialog_checks = BondHearingDialogInfoChecker(self)


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
