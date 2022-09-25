"""Module containing all classes that load functions tied to a signal."""

from loguru import logger
from munientry.builders.crimtraffic.base_crimtraffic_builders import BaseDialogSlotFunctions


class AddCommunityControlDialogSlotFunctions(BaseDialogSlotFunctions):
    def __init__(self, dialog):
        self.dialog = dialog
        self.main_dialog = dialog.main_dialog

    def add_conditions(self):
        if self.main_dialog.community_service_checkBox.isChecked():
            self.dialog.transfer_view_data_to_model(
                self.main_dialog.entry_case_information.community_service
            )
        if self.main_dialog.other_conditions_checkBox.isChecked():
            self.dialog.transfer_view_data_to_model(
                self.main_dialog.entry_case_information.other_conditions
            )
        if self.main_dialog.community_control_checkBox.isChecked():
            self.dialog.transfer_view_data_to_model(
                self.main_dialog.entry_case_information.community_control
            )
        if self.main_dialog.license_suspension_checkBox.isChecked():
            self.dialog.transfer_view_data_to_model(
                self.main_dialog.entry_case_information.license_suspension
            )
        if self.main_dialog.impoundment_checkBox.isChecked():
            self.dialog.transfer_view_data_to_model(
                self.main_dialog.entry_case_information.impoundment
            )
        if self.main_dialog.victim_notification_checkBox.isChecked():
            self.dialog.transfer_view_data_to_model(
                self.main_dialog.entry_case_information.victim_notification
            )


class AddSpecialBondConditionsDialogSlotFunctions(BaseDialogSlotFunctions):
    def __init__(self, dialog):
        self.dialog = dialog
        self.main_dialog = dialog.main_dialog

    def add_conditions(self):
        if self.main_dialog.domestic_violence_checkBox.isChecked():
            self.dialog.transfer_view_data_to_model(
                self.main_dialog.entry_case_information.domestic_violence_conditions
            )
        if self.main_dialog.admin_license_suspension_checkBox.isChecked():
            self.dialog.transfer_view_data_to_model(
                self.main_dialog.entry_case_information.admin_license_suspension
            )
        if self.main_dialog.no_contact_checkBox.isChecked():
            self.dialog.transfer_view_data_to_model(
                self.main_dialog.entry_case_information.no_contact
            )
        if self.main_dialog.custodial_supervision_checkBox.isChecked():
            self.dialog.transfer_view_data_to_model(
                self.main_dialog.entry_case_information.custodial_supervision
            )
        if self.main_dialog.other_conditions_checkBox.isChecked():
            self.dialog.transfer_view_data_to_model(
                self.main_dialog.entry_case_information.other_conditions
            )
        if self.main_dialog.vehicle_seizure_checkBox.isChecked():
            self.dialog.transfer_view_data_to_model(
                self.main_dialog.entry_case_information.vehicle_seizure
            )


class AddJailOnlyDialogSlotFunctions(BaseDialogSlotFunctions):
    def __init__(self, dialog):
        self.dialog = dialog
        self.main_dialog = dialog.main_dialog

    def add_conditions(self):
        if self.main_dialog.jail_checkBox.isChecked():
            self.dialog.transfer_view_data_to_model(
                self.main_dialog.entry_case_information.jail_terms
            )


if __name__ == "__main__":
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
    # charges_database = open_db_connection("con_charges")
