"""Builder module for Bond Hearing Dialog."""
import munientry.builders.base_dialogs
from loguru import logger

from munientry.builders.crimtraffic.add_special_bond_conditions_dialog import \
    AddSpecialBondConditionsDialog
from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.checkers.bond_checkers import BondHearingDialogInfoChecker
from munientry.data.cms_case_loaders import CmsNoChargeLoader
from munientry.models.case_information.plea_entries import (
    BondHearingEntryCaseInformation,
)
from munientry.models.conditions_models import BondModificationConditions
from munientry.updaters.no_grid_case_updaters import BondHearingDialogUpdater
from munientry.views.bond_hearing_dialog_ui import Ui_BondHearingDialog


class BondHearingDialogViewModifier(crim.BaseDialogViewModifier):
    """View builder for Bond Hearing Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog.monitoring_type_box.setHidden(True)
        self.dialog.specialized_docket_type_box.setHidden(True)


class BondHearingDialogSlotFunctions(crim.BaseDialogSlotFunctions):
    """Additional functions for Bond Hearing Dialog."""

    def start_add_special_bond_conditions_dialog(self):
        self.dialog.update_entry_case_information()
        AddSpecialBondConditionsDialog(self.dialog).exec()

    def show_hide_bond_conditions(self):
        if self.dialog.bond_type_box.currentText() == 'Continue Existing Bond':
            self.dialog.bond_conditions_frame.setHidden(True)
            self.dialog.special_bond_conditions_frame.setHidden(True)
        else:
            self.dialog.bond_conditions_frame.setHidden(False)
            self.dialog.special_bond_conditions_frame.setHidden(False)


class BondHearingDialogSignalConnector(crim.CrimTrafficSignalConnector):
    """Signal connector for Bond Hearing Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()
        self.dialog.add_special_conditions_Button.pressed.connect(
            self.dialog.functions.start_add_special_bond_conditions_dialog,
        )
        self.connect_dialog_specific_signals()

    def connect_dialog_specific_signals(self):
        self.dialog.bond_modification_decision_box.currentTextChanged.connect(
            self.dialog.functions.show_bond_boxes,
        )
        self.dialog.admin_license_suspension_checkBox.toggled.connect(
            self.dialog.functions.conditions_checkbox_toggle,
        )
        self.dialog.domestic_violence_checkBox.toggled.connect(
            self.dialog.functions.conditions_checkbox_toggle,
        )
        self.dialog.no_contact_checkBox.toggled.connect(
            self.dialog.functions.conditions_checkbox_toggle,
        )
        self.dialog.custodial_supervision_checkBox.toggled.connect(
            self.dialog.functions.conditions_checkbox_toggle,
        )
        self.dialog.other_conditions_checkBox.toggled.connect(
            self.dialog.functions.conditions_checkbox_toggle,
        )
        self.dialog.vehicle_seizure_checkBox.toggled.connect(
            self.dialog.functions.conditions_checkbox_toggle,
        )
        self.dialog.monitoring_checkBox.toggled.connect(
            self.dialog.functions.show_hide_checkbox_connected_fields,
        )
        self.dialog.specialized_docket_checkBox.toggled.connect(
            self.dialog.functions.show_hide_checkbox_connected_fields,
        )


class BondHearingDialog(crim.CriminalDialogBuilder, Ui_BondHearingDialog):
    """Dialog builder class for 'Bond Modification / Revocation' Entry."""

    build_dict = {
        'dialog_name': 'Bond Hearing Dialog',
        'view': BondHearingDialogViewModifier,
        'slots': BondHearingDialogSlotFunctions,
        'signals': BondHearingDialogSignalConnector,
        'case_information_model': BondHearingEntryCaseInformation,
        'loader': CmsNoChargeLoader,
        'updater': BondHearingDialogUpdater,
        'info_checker': BondHearingDialogInfoChecker,
    }

    condition_checkbox_dict = {
        'monitoring_checkBox': ['monitoring_type_box'],
        'specialized_docket_checkBox': ['specialized_docket_type_box'],
    }

    def additional_setup(self):
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
        self.entry_case_information.bond_conditions = BondModificationConditions()


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
