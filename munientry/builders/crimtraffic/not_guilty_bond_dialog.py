"""Builder module for the Not Guilty Bond Dialog."""
from loguru import logger

from munientry.builders.conditions_dialogs import AddSpecialBondConditionsDialog
from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.checkers.plea_only_checkers import NotGuiltyBondDialogInfoChecker
from munientry.controllers import charges_grids as cg
from munientry.data.cms_case_loaders import CmsChargeLoader
from munientry.models.case_information.plea_entries import (
    NotGuiltyBondEntryCaseInformation,
)
from munientry.updaters.grid_case_updaters import NotGuiltyBondDialogUpdater
from munientry.views.not_guilty_bond_dialog_ui import Ui_NotGuiltyBondDialog


class NotGuiltyBondDialogViewModifier(crim.BaseDialogViewModifier):
    """View builder for Not Guilty Bond Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog.charges_gridLayout.__class__ = cg.NotGuiltyPleaGrid
        self.set_appearance_reason()
        self.dialog.monitoring_type_box.setHidden(True)
        self.dialog.specialized_docket_type_box.setHidden(True)


class NotGuiltyBondDialogSlotFunctions(crim.BaseDialogSlotFunctions):
    """Additional functions for Not Guilty Bond Dialog."""

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


class NotGuiltyBondDialogSignalConnector(crim.BaseDialogSignalConnector_Refactor):
    """Signal Connector for Not Guilty Bond Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()
        self.connect_not_guilty_all_button()
        self.connect_add_charge_button()
        self.add_special_conditions_signals()
        self.connect_bond_condition_signals()

    def connect_bond_condition_signals(self):
        """Hides the bond condition boxes if 'Continue Existing Bond' is selected."""
        self.dialog.bond_type_box.currentTextChanged.connect(
            self.dialog.functions.show_hide_bond_conditions,
        )

    def add_special_conditions_signals(self):
        self.dialog.add_special_conditions_Button.pressed.connect(
            self.dialog.functions.start_add_special_bond_conditions_dialog,
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


class NotGuiltyBondDialog(crim.CriminalDialogBuilder, Ui_NotGuiltyBondDialog):
    """Dialog builder class for 'Not Guilty Plea / Bond' dialog."""

    build_dict = {
        'dialog_name': 'Not Guilty Bond Dialog',
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

    def additional_setup(self):
        """The self.additional_conditions list is called in the base_crimtraffic_builders module.

        TODO: This needs refactoring along with the conditions_checkbox_toggle method in
        BaseDialogSlotFunctions in base_crimtraffic_builder. It is too complex.

        TODO: Ultimately want to tie a checbox to the 'ordered' attribute of a conditions model.
        """
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
        self.charges_gridLayout.set_all_pleas('Not Guilty')


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
