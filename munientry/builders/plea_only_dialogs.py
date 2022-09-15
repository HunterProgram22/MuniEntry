"""Module containing classes to build Plea Only Dialogs."""
from loguru import logger

from munientry.builders.base_dialogs import CriminalBaseDialog, CriminalDialogBuilder
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

class PleaOnlyDialog(CriminalDialogBuilder, Ui_PleaOnlyDialog):
    """Dialog builder class for 'Plea Only - Future Sentencing' dialog."""
    build_dict = {
        'view': PleaOnlyDialogViewModifier,
        'slots': PleaOnlyDialogSlotFunctions,
        'signals': PleaOnlyDialogSignalConnector,
        'case_information_model': PleaOnlyEntryCaseInformation,
        'loader': CmsChargeLoader,
        'updater': PleaOnlyDialogUpdater,
        'info_checker': PleaOnlyDialogInfoChecker,
    }

    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.dialog_name = 'Plea Only Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.entry_case_information.judicial_officer = self.judicial_officer


class NotGuiltyBondDialog(CriminalDialogBuilder, Ui_NotGuiltyBondDialog):
    """Dialog builder class for 'Not Guilty Plea / Bond' dialog."""
    build_dict = {
        'view': NotGuiltyBondDialogViewModifier,
        'slots': NotGuiltyBondDialogSlotFunctions,
        'signals': NotGuiltyBondDialogSignalConnector,
        'case_information_model': NotGuiltyBondEntryCaseInformation,
        'loader': CmsChargeLoader,
        'updater': NotGuiltyBondDialogUpdater,
        'info_checker': NotGuiltyBondDialogInfoChecker,
    }

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
        self.entry_case_information.judicial_officer = self.judicial_officer
        self.charges_gridLayout.set_all_pleas('Not Guilty')


class LeapAdmissionPleaDialog(CriminalDialogBuilder, Ui_LeapAdmissionPleaDialog):
    """Dialog builder class for 'LEAP Admission Plea' dialog."""
    build_dict = {
        'view': LeapAdmissionPleaDialogViewModifier,
        'slots': LeapAdmissionPleaDialogSlotFunctions,
        'signals': LeapAdmissionPleaDialogSignalConnector,
        'case_information_model': LeapAdmissionEntryCaseInformation,
        'loader': CmsChargeLoader,
        'updater': LeapAdmissionPleaDialogUpdater,
        'info_checker': LeapAdmissionPleaDialogInfoChecker,
    }

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
        self.entry_case_information.judicial_officer = self.judicial_officer


class LeapPleaValidDialog(CriminalDialogBuilder, Ui_LeapPleaValidDialog):
    """Dialog builder class for 'LEAP Admission Plea - Already Valid' dialog."""
    build_dict = {
        'view': LeapAdmissionPleaDialogViewModifier,
        'slots': LeapAdmissionPleaDialogSlotFunctions,
        'signals': LeapAdmissionPleaValidDialogSignalConnector,
        'case_information_model': LeapAdmissionEntryCaseInformation,
        'loader': CmsChargeLoader,
        'updater': LeapAdmissionPleaDialogUpdater,
        'info_checker': LeapAdmissionPleaDialogInfoChecker,
    }

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
        self.entry_case_information.judicial_officer = self.judicial_officer


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
