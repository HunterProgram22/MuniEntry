"""Builder module for the Not Guilty Bond Dialog."""

from munientry.builders.base_dialogs import CriminalDialogBuilder
from munientry.checkers.plea_only_checkers import NotGuiltyBondDialogInfoChecker
from munientry.controllers import charges_grids as cg
from munientry.controllers.signal_connectors import BaseDialogSignalConnector
from munientry.controllers.slot_functions import BaseDialogSlotFunctions
from munientry.controllers.view_modifiers import BaseDialogViewModifier
from munientry.data.cms_case_loaders import CmsChargeLoader
from munientry.models.case_information.plea_entries import (
    NotGuiltyBondEntryCaseInformation,
)
from munientry.models.conditions_models import BondConditions
from munientry.updaters.grid_case_updaters import NotGuiltyBondDialogUpdater
from munientry.views.not_guilty_bond_dialog_ui import Ui_NotGuiltyBondDialog


class NotGuiltyBondDialogViewModifier(BaseDialogViewModifier):
    """View builder for Not Guilty Bond Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog.charges_gridLayout.__class__ = cg.NotGuiltyPleaGrid
        self.set_appearance_reason()
        self.dialog.monitoring_type_box.setHidden(True)
        self.dialog.specialized_docket_type_box.setHidden(True)


class NotGuiltyBondDialogSignalConnector(BaseDialogSignalConnector):
    """Signal Connector for Not Guilty Bond Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals(dialog)
        self.connect_not_guilty_all_button(dialog)
        dialog.bond_type_box.currentTextChanged.connect(dialog.functions.show_hide_bond_conditions)
        dialog.add_charge_Button.released.connect(dialog.functions.start_add_charge_dialog)
        self.add_special_conditions_signals(dialog)

    def add_special_conditions_signals(self, dialog):
        dialog.add_special_conditions_Button.pressed.connect(
            dialog.functions.start_add_special_bond_conditions_dialog,
        )
        dialog.admin_license_suspension_checkBox.toggled.connect(
            dialog.functions.conditions_checkbox_toggle,
        )
        dialog.domestic_violence_checkBox.toggled.connect(
            dialog.functions.conditions_checkbox_toggle,
        )
        dialog.no_contact_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.custodial_supervision_checkBox.toggled.connect(
            dialog.functions.conditions_checkbox_toggle,
        )
        dialog.other_conditions_checkBox.toggled.connect(
            dialog.functions.conditions_checkbox_toggle,
        )
        dialog.vehicle_seizure_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.monitoring_checkBox.toggled.connect(
            dialog.functions.show_hide_checkbox_connected_fields,
        )
        dialog.specialized_docket_checkBox.toggled.connect(
            dialog.functions.show_hide_checkbox_connected_fields,
        )


class NotGuiltyBondDialogSlotFunctions(BaseDialogSlotFunctions):
    """Additional functions for Not Guilty Bond Dialog."""

    def start_add_special_bond_conditions_dialog(self):
        from munientry.builders.conditions_dialogs import AddSpecialBondConditionsDialog

        self.dialog.update_entry_case_information()
        AddSpecialBondConditionsDialog(self.dialog).exec()

    def hide_boxes(self):
        """This method is called from modify_view as part of the init.

        This method hides all optional boxes on load.
        """
        for condition in self.dialog.condition_checkbox_dict:
            (condition_checkbox, condition_field) = condition
            getattr(self.dialog, condition_field).setEnabled(False)
            getattr(self.dialog, condition_field).setHidden(True)

    def show_hide_bond_conditions(self):
        if self.dialog.bond_type_box.currentText() == 'Continue Existing Bond':
            self.dialog.bond_conditions_frame.setHidden(True)
            self.dialog.special_bond_conditions_frame.setHidden(True)
        else:
            self.dialog.bond_conditions_frame.setHidden(False)
            self.dialog.special_bond_conditions_frame.setHidden(False)


class NotGuiltyBondDialog(CriminalDialogBuilder, Ui_NotGuiltyBondDialog):
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
        self.entry_case_information.bond_conditions = BondConditions()
        self.entry_case_information.judicial_officer = self.judicial_officer
        self.charges_gridLayout.set_all_pleas('Not Guilty')
