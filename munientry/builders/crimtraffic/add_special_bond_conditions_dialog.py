"""Module builder for Add Conditions Secondary Dialog."""
from loguru import logger
from PyQt5.QtWidgets import QLabel

from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.views.add_special_bond_conditions_dialog_ui import (
    Ui_AddSpecialBondConditionsDialog,
)


class AddSpecialBondConditionsDialogViewModifier(crim.BaseDialogViewModifier):
    """View builder for Add Special Bond Conditions Dialog."""

    condition_classes = [
        ('other_conditions_checkBox', 'other_conditions'),
        ('admin_license_suspension_checkBox', 'admin_license_suspension'),
        ('domestic_violence_checkBox', 'domestic_violence_conditions'),
        ('vehicle_seizure_checkBox', 'vehicle_seizure'),
        ('no_contact_checkBox', 'no_contact'),
        ('custodial_supervision_checkBox', 'custodial_supervision'),
    ]

    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_bond_cond_case_information_banner()
        self.load_existing_data_to_dialog()

    def set_bond_cond_case_information_banner(self):
        column = self.dialog.charges_gridLayout.columnCount() + 1
        for charge in self.dialog.charges_list:
            self.dialog.charges_gridLayout.addWidget(QLabel(charge.offense), 0, column)
            self.dialog.charges_gridLayout.addWidget(QLabel(charge.statute), 1, column)
            column += 1


class AddSpecialBondConditionsDialogSlotFunctions(crim.BaseDialogSlotFunctions):
    """Additional functions for Add Special Bond Conditions Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.main_dialog = dialog.main_dialog

    def add_conditions(self):
        if self.main_dialog.domestic_violence_checkBox.isChecked():
            self.dialog.transfer_view_data_to_model(
                self.main_dialog.entry_case_information.domestic_violence_conditions,
            )
        if self.main_dialog.admin_license_suspension_checkBox.isChecked():
            self.dialog.transfer_view_data_to_model(
                self.main_dialog.entry_case_information.admin_license_suspension,
            )
        if self.main_dialog.no_contact_checkBox.isChecked():
            self.dialog.transfer_view_data_to_model(
                self.main_dialog.entry_case_information.no_contact,
            )
        if self.main_dialog.custodial_supervision_checkBox.isChecked():
            self.dialog.transfer_view_data_to_model(
                self.main_dialog.entry_case_information.custodial_supervision,
            )
        if self.main_dialog.other_conditions_checkBox.isChecked():
            self.dialog.transfer_view_data_to_model(
                self.main_dialog.entry_case_information.other_conditions,
            )
        if self.main_dialog.vehicle_seizure_checkBox.isChecked():
            self.dialog.transfer_view_data_to_model(
                self.main_dialog.entry_case_information.vehicle_seizure,
            )


class AddSpecialBondConditionsDialogSignalConnector(crim.BaseDialogSignalConnector):
    """Signal Connector for Add Special Bond Conditions Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_condition_dialog_main_signals()


class AddSpecialBondConditionsDialog(crim.BaseDialogBuilder, Ui_AddSpecialBondConditionsDialog):
    """The secondary dialog for adding special bond conditions.

    Dialogs that use: NotGuiltyBondDialog, BondHearingDialog, NoPleaBondDialog.
    """

    build_dict = {
        'dialog_name': 'Add Special Bond Conditions Dialog',
        'view': AddSpecialBondConditionsDialogViewModifier,
        'slots': AddSpecialBondConditionsDialogSlotFunctions,
        'signals': AddSpecialBondConditionsDialogSignalConnector,
    }

    conditions_frames = [
        ('other_conditions_checkBox', 'other_conditions_frame'),
        ('admin_license_suspension_checkBox', 'admin_license_suspension_frame'),
        ('domestic_violence_checkBox', 'domestic_violence_frame'),
        ('vehicle_seizure_checkBox', 'vehicle_seizure_frame'),
        ('no_contact_checkBox', 'no_contact_frame'),
        ('custodial_supervision_checkBox', 'custodial_supervision_frame'),
    ]

    def __init__(self, main_dialog, parent=None) -> None:
        self.charges_list = main_dialog.entry_case_information.charges_list
        self.main_dialog = main_dialog
        super().__init__(parent)
        logger.dialog(f'{self.dialog_name} Opened')
        crim.enable_condition_frames(self, main_dialog)


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
