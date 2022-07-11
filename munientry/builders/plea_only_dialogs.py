"""Module containing classes to build Plea Only Dialogs."""
from loguru import logger

from munientry.builders.base_dialogs import CriminalBaseDialog
from munientry.checkers.plea_only_checkers import (
    LeapAdmissionPleaDialogInfoChecker,
    NotGuiltyBondDialogInfoChecker,
    PleaOnlyDialogInfoChecker,
)
from munientry.controllers.signal_connectors import (
    LeapAdmissionPleaDialogSignalConnector,
    LeapAdmissionPleaValidDialogSignalConnector,
    NotGuiltyBondDialogSignalConnector,
    PleaOnlyDialogSignalConnector,
)
from munientry.controllers.slot_functions import (
    LeapAdmissionPleaDialogSlotFunctions,
    NotGuiltyBondDialogSlotFunctions,
    PleaOnlyDialogSlotFunctions,
)
from munientry.controllers.view_modifiers import (
    LeapAdmissionPleaDialogViewModifier,
    NotGuiltyBondDialogViewModifier,
    PleaOnlyDialogViewModifier,
)
from munientry.data.cms_case_loaders import CmsChargeLoader
from munientry.models.case_information.plea_entries import (
    LeapAdmissionEntryCaseInformation,
    NotGuiltyBondEntryCaseInformation,
    PleaOnlyEntryCaseInformation,
)
from munientry.models.conditions_models import BondConditions
from munientry.models.template_types import TEMPLATE_DICT
from munientry.updaters.grid_case_updaters import (
    LeapAdmissionPleaDialogUpdater,
    NotGuiltyBondDialogUpdater,
    PleaOnlyDialogUpdater,
)
from munientry.views.leap_admission_plea_dialog_ui import Ui_LeapAdmissionPleaDialog
from munientry.views.leap_plea_valid_dialog_ui import Ui_LeapPleaValidDialog
from munientry.views.not_guilty_bond_dialog_ui import Ui_NotGuiltyBondDialog
from munientry.views.plea_only_dialog_ui import Ui_PleaOnlyDialog


class PleaOnlyDialog(CriminalBaseDialog, Ui_PleaOnlyDialog):
    """Dialog builder class for 'Plea Only - Future Sentencing' dialog."""

    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.dialog_name = 'Plea Only Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)

    def modify_view(self) -> None:
        PleaOnlyDialogViewModifier(self)

    def connect_signals_to_slots(self) -> None:
        self.functions = PleaOnlyDialogSlotFunctions(self)
        PleaOnlyDialogSignalConnector(self)

    def load_entry_case_information_model(self) -> None:
        self.entry_case_information = PleaOnlyEntryCaseInformation()
        self.entry_case_information.judicial_officer = self.judicial_officer

    def load_cms_data_to_view(self) -> None:
        CmsChargeLoader(self)

    def update_entry_case_information(self) -> None:
        PleaOnlyDialogUpdater(self)

    def perform_info_checks(self) -> None:
        self.dialog_checks = PleaOnlyDialogInfoChecker(self)


class NotGuiltyBondDialog(CriminalBaseDialog, Ui_NotGuiltyBondDialog):
    """Dialog builder class for 'Not Guilty Plea / Bond' dialog."""

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
        self.dialog_name = 'Not Guilty Bond Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.entry_case_information.bond_conditions = BondConditions()
        self.charges_gridLayout.set_all_pleas('Not Guilty')

    def modify_view(self) -> None:
        NotGuiltyBondDialogViewModifier(self)

    def connect_signals_to_slots(self) -> None:
        self.functions = NotGuiltyBondDialogSlotFunctions(self)
        NotGuiltyBondDialogSignalConnector(self)

    def load_entry_case_information_model(self) -> None:
        self.entry_case_information = NotGuiltyBondEntryCaseInformation()
        self.entry_case_information.judicial_officer = self.judicial_officer

    def load_cms_data_to_view(self) -> None:
        CmsChargeLoader(self)

    def update_entry_case_information(self) -> NotGuiltyBondDialogUpdater:
        return NotGuiltyBondDialogUpdater(self)

    def perform_info_checks(self) -> None:
        self.dialog_checks = NotGuiltyBondDialogInfoChecker(self)


class LeapAdmissionPleaDialog(CriminalBaseDialog, Ui_LeapAdmissionPleaDialog):
    """Dialog builder class for 'LEAP Admission Plea' dialog."""

    def __init__(
        self,
        judicial_officer: object,
        cms_case: str = None,
        case_table: str = None,
        parent: object = None,
    ) -> None:
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.dialog_name = 'Leap Admission Plea Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.functions.set_leap_sentencing_date('120 days')

    def modify_view(self) -> None:
        LeapAdmissionPleaDialogViewModifier(self)

    def connect_signals_to_slots(self) -> None:
        self.functions = LeapAdmissionPleaDialogSlotFunctions(self)
        LeapAdmissionPleaDialogSignalConnector(self)

    def load_entry_case_information_model(self):
        self.entry_case_information = LeapAdmissionEntryCaseInformation()
        self.entry_case_information.judicial_officer = self.judicial_officer

    def load_cms_data_to_view(self) -> None:
        CmsChargeLoader(self)

    def update_entry_case_information(self) -> LeapAdmissionPleaDialogUpdater:
        return LeapAdmissionPleaDialogUpdater(self)

    def perform_info_checks(self) -> LeapAdmissionPleaDialogInfoChecker:
        self.dialog_checks = LeapAdmissionPleaDialogInfoChecker(self)


class LeapPleaValidDialog(CriminalBaseDialog, Ui_LeapPleaValidDialog):
    """Dialog builder class for 'LEAP Admission Plea - Already Valid' dialog."""

    def __init__(
        self,
        judicial_officer: object,
        cms_case: str = None,
        case_table: str = None,
        parent: object = None,
    ) -> None:
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.dialog_name = 'Leap Admission Plea Already Valid Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)

    def modify_view(self) -> None:
        LeapAdmissionPleaDialogViewModifier(self)

    def connect_signals_to_slots(self) -> None:
        self.functions = LeapAdmissionPleaDialogSlotFunctions(self)
        LeapAdmissionPleaValidDialogSignalConnector(self)

    def load_entry_case_information_model(self):
        self.entry_case_information = LeapAdmissionEntryCaseInformation()
        self.entry_case_information.judicial_officer = self.judicial_officer

    def load_cms_data_to_view(self) -> None:
        CmsChargeLoader(self)

    def update_entry_case_information(self) -> LeapAdmissionPleaDialogUpdater:
        return LeapAdmissionPleaDialogUpdater(self)

    def perform_info_checks(self) -> LeapAdmissionPleaDialogInfoChecker:
        self.dialog_checks = LeapAdmissionPleaDialogInfoChecker(self)


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
