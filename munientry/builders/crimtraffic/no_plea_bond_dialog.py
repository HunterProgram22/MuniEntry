"""Builder module for the No Plea Bond Dialog."""
import munientry.builders.base_dialogs
from loguru import logger

from munientry.builders.crimtraffic.add_special_bond_conditions_dialog import \
    AddSpecialBondConditionsDialog
from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.checkers.bond_checkers import NoPleaBondDialogInfoChecker
from munientry.data.cms_case_loaders import CmsNoChargeLoader
from munientry.models.case_information.plea_entries import (
    NoPleaBondEntryCaseInformation,
)
from munientry.models.conditions_models import BondConditions
from munientry.updaters.no_grid_case_updaters import NoPleaBondDialogUpdater
from munientry.views.no_plea_bond_dialog_ui import Ui_NoPleaBondDialog


class NoPleaBondDialogViewModifier(crim.BaseDialogViewModifier):
    """View builder for No Plea Bond Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_appearance_reason()
        self.dialog.monitoring_type_box.setHidden(True)
        self.dialog.specialized_docket_type_box.setHidden(True)


class NoPleaBondDialogSlotFunctions(crim.BaseDialogSlotFunctions):
    """Additional functions for No Plea Bond Dialog."""

    def start_add_special_bond_conditions_dialog(self):
        self.dialog.update_entry_case_information()
        AddSpecialBondConditionsDialog(self.dialog).exec()

    def hide_boxes(self):
        """This method is called on load to hide all optional boxes."""
        for conditions in self.dialog.condition_checkbox_dict:
            (_condition_checkbox, condition_field) = conditions
            getattr(self.dialog, condition_field).setEnabled(False)
            getattr(self.dialog, condition_field).setHidden(True)


class NoPleaBondDialogSignalConnector(crim.CrimTrafficSignalConnector):
    """Signal connector for No Plea Bond Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()
        self.connect_dialog_specific_signals()

    def connect_dialog_specific_signals(self):
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


class NoPleaBondDialog(crim.CriminalDialogBuilder, Ui_NoPleaBondDialog):
    """Dialog builder class for 'Appear on Warrant (No Plea) / Bond' Entry."""

    build_dict = {
        'dialog_name': 'No Plea Bond Dialog',
        'view': NoPleaBondDialogViewModifier,
        'slots': NoPleaBondDialogSlotFunctions,
        'signals': NoPleaBondDialogSignalConnector,
        'case_information_model': NoPleaBondEntryCaseInformation,
        'loader': CmsNoChargeLoader,
        'updater': NoPleaBondDialogUpdater,
        'info_checker': NoPleaBondDialogInfoChecker,
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
        self.entry_case_information.bond_conditions = BondConditions()


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
