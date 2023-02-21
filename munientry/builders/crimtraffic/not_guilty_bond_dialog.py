"""Builder module for the Not Guilty Bond Dialog."""
from loguru import logger

from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.builders.secondary.add_special_bond_conditions_dialog import (
    AddSpecialBondConditionsDialog,
)
from munientry.checkers.plea_only_checkers import NotGuiltyBondDialogInfoChecker
from munientry.loaders.cms_case_loaders import CmsChargeLoader
from munientry.models.case_information.plea_entries import (
    NotGuiltyBondEntryCaseInformation,
)
from munientry.updaters.grid_case_updaters import NotGuiltyBondDialogUpdater
from munientry.views.not_guilty_bond_dialog_ui import Ui_NotGuiltyBondDialog


class NotGuiltyBondDialogViewModifier(crim.CrimTrafficViewModifier):
    """View builder for Not Guilty Bond Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_appearance_reason()
        self.dialog.monitoring_type_box.setHidden(True)
        self.dialog.specialized_docket_type_box.setHidden(True)


class NotGuiltyBondDialogSlotFunctions(crim.CrimTrafficSlotFunctions):
    """Additional functions for Not Guilty Bond Dialog."""

    def start_add_special_bond_conditions_dialog(self):
        self.dialog.update_entry_case_information()
        self.dialog.popup_dialog = AddSpecialBondConditionsDialog(self.dialog)
        self.dialog.popup_dialog.exec()

    def show_hide_bond_conditions(self):
        """
        Shows or hides the bond conditions frames based on the selected bond type.

        If the bond type is 'Continue Existing Bond', the bond conditions frames are hidden.
        Otherwise, they are shown.
        """
        bond_type = self.dialog.bond_type_box.currentText()
        hide_boxes = bond_type in {'Continue Existing Bond'}
        self.dialog.bond_conditions_frame.setHidden(hide_boxes)
        self.dialog.special_bond_conditions_frame.setHidden(hide_boxes)


class NotGuiltyBondDialogSignalConnector(crim.CrimTrafficSignalConnector):
    """Signal Connector for Not Guilty Bond Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()
        self.connect_not_guilty_all_button()
        self.connect_add_charge_button()
        self.add_special_conditions_signals()
        self.connect_condition_checkbox_signals()
        self.connect_hidden_boxes_to_checkboxes()
        self.connect_bond_condition_signals()

    def connect_not_guilty_all_button(self):
        self.dialog.not_guilty_all_Button.pressed.connect(
            self.dialog.charges_gridLayout.set_pleas_to_not_guilty,
        )

    def connect_bond_condition_signals(self):
        self.dialog.bond_type_box.currentTextChanged.connect(
            self.dialog.functions.show_hide_bond_conditions,
        )

    def connect_condition_checkbox_signals(self):
        checkboxes = [
            self.dialog.admin_license_suspension_checkBox,
            self.dialog.domestic_violence_checkBox,
            self.dialog.no_contact_checkBox,
            self.dialog.custodial_supervision_checkBox,
            self.dialog.other_conditions_checkBox,
            self.dialog.vehicle_seizure_checkBox,
        ]
        for checkbox in checkboxes:
            checkbox.toggled.connect(self.dialog.functions.conditions_checkbox_toggle)

    def add_special_conditions_signals(self):
        self.dialog.add_special_conditions_Button.pressed.connect(
            self.dialog.functions.start_add_special_bond_conditions_dialog,
        )

    def connect_hidden_boxes_to_checkboxes(self):
        checkboxes = [
            self.dialog.monitoring_checkBox,
            self.dialog.specialized_docket_checkBox,
        ]
        for checkbox in checkboxes:
            checkbox.toggled.connect(self.dialog.functions.show_hide_checkbox_connected_fields)


class NotGuiltyBondDialog(crim.CrimTrafficDialogBuilder, Ui_NotGuiltyBondDialog):
    """Dialog builder class for 'Not Guilty Plea / Bond' dialog."""

    _case_information_model = NotGuiltyBondEntryCaseInformation
    _case_loader = CmsChargeLoader
    _info_checker = NotGuiltyBondDialogInfoChecker
    _model_updater = NotGuiltyBondDialogUpdater
    _signal_connector = NotGuiltyBondDialogSignalConnector
    _slots = NotGuiltyBondDialogSlotFunctions
    _view_modifier = NotGuiltyBondDialogViewModifier
    dialog_name = 'Not Guilty Bond Dialog'

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
        self.charges_gridLayout.set_pleas_to_not_guilty()


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
