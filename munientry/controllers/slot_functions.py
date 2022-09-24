"""Module containing all classes that load functions tied to a signal."""

from loguru import logger
from munientry.builders.crimtraffic.base_crimtraffic_builders import BaseDialogSlotFunctions

from munientry.data.sql_lite_functions import query_offense_type
from munientry.models.criminal_charge_models import CriminalCharge


class AddChargeDialogSlotFunctions(BaseDialogSlotFunctions):
    def __init__(self, dialog):
        self.dialog = dialog
        self.main_dialog = dialog.main_dialog

    @logger.catch
    def clear_add_charge_fields(self):
        self.dialog.statute_choice_box.setCurrentText("")
        self.dialog.offense_choice_box.setCurrentText("")
        self.dialog.degree_choice_box.setCurrentText("")

    @logger.catch
    def add_charge_process(self):
        """The order of functions that are called when the add_charge_Button is
        clicked(). The order is important to make sure the information is
        updated before the charge is added and the data cleared from the fields."""
        self.add_charge_to_entry_case_information()
        self.main_dialog.add_charge_to_grid()
        self.close_event()

    @logger.catch
    def add_charge_to_entry_case_information(self):
        self.criminal_charge = CriminalCharge()
        self.criminal_charge.offense = self.dialog.offense_choice_box.currentText()
        self.criminal_charge.statute = self.dialog.statute_choice_box.currentText()
        self.criminal_charge.degree = self.dialog.degree_choice_box.currentText()
        self.criminal_charge.type = self.set_offense_type()
        self.main_dialog.entry_case_information.add_charge_to_list(self.criminal_charge)
        logger.info(f'Added Charge: {self.criminal_charge.offense}, {self.criminal_charge.statute}')

    def set_offense_type(self):
        """This calls the database_statutes and behind the scenes sets the appropriate cms_case type
        for each charge. It does not show up in the view, but is used for calculating costs."""
        key = self.dialog.statute_choice_box.currentText()
        if self.dialog.freeform_entry_checkBox.isChecked():
            return None
        return query_offense_type(key, self.dialog.db_connection)

    def close_event(self):
        self.close_window()


class AmendChargeDialogSlotFunctions(BaseDialogSlotFunctions):
    def __init__(self, dialog):
        self.dialog = dialog
        self.main_dialog = dialog.main_dialog

    def clear_amend_charge_fields(self):
        self.dialog.statute_choice_box.setCurrentText("")
        self.dialog.offense_choice_box.setCurrentText("")
        self.dialog.degree_choice_box.setCurrentText("")

    def amend_offense_process(self):
        """Adds the data entered for the amended offense to the AmendOffenseDetails
        object then points the entry_case_information object to the AmendOffenseDetails
        object."""
        self.set_amended_offense_details()
        if self.dialog.motion_decision_box.currentText() == "Granted":
            self.update_criminal_charge_offense_name()
            self.add_charge_to_amended_charge_list()
            self.update_charges_grid_with_amended_charge()
        self.close_event()

    def update_criminal_charge_offense_name(self):
        setattr(
            self.dialog.charge,
            "offense",
            f"{self.dialog.current_offense_name} - AMENDED to "
            f"{self.dialog.amend_offense_details.amended_charge}",
        )
        logger.info(f'Original Charge: {self.dialog.current_offense_name}')
        logger.info(f'Amended Charge: {self.dialog.amend_offense_details.amended_charge}')

    def update_charges_grid_with_amended_charge(self):
        for columns in range(self.main_dialog.charges_gridLayout.columnCount()):
            if (
                self.main_dialog.charges_gridLayout.itemAtPosition(
                    self.main_dialog.charges_gridLayout.row_offense, columns
                )
                is not None
                and self.main_dialog.charges_gridLayout.itemAtPosition(
                    self.main_dialog.charges_gridLayout.row_offense, columns
                )
                .widget()
                .text()
                == self.dialog.current_offense_name
            ):
                self.main_dialog.charges_gridLayout.itemAtPosition(
                    self.main_dialog.charges_gridLayout.row_offense, columns
                ).widget().setText(
                    f"{self.dialog.current_offense_name} - AMENDED to "
                    f"{self.dialog.amend_offense_details.amended_charge}"
                )
                self.main_dialog.charges_gridLayout.itemAtPosition(
                    self.main_dialog.charges_gridLayout.row_statute, columns
                ).widget().set_up_widget(self.dialog.statute_choice_box.currentText())
                self.main_dialog.charges_gridLayout.itemAtPosition(
                    self.main_dialog.charges_gridLayout.row_degree, columns
                ).widget().setCurrentText(self.dialog.degree_choice_box.currentText())

    def add_charge_to_amended_charge_list(self):
        self.main_dialog.entry_case_information.amended_charges_list.append(
            (
                self.dialog.amend_offense_details.original_charge,
                self.dialog.amend_offense_details.amended_charge,
            )
        )

    def set_amended_offense_details(self):
        self.dialog.amend_offense_details.original_charge = (
            self.dialog.current_offense_name
        )
        self.dialog.amend_offense_details.amended_charge = (
            self.dialog.offense_choice_box.currentText()
        )
        self.dialog.amend_offense_details.motion_disposition = (
            self.dialog.motion_decision_box.currentText()
        )
        self.main_dialog.entry_case_information.amend_offense_details = (
            self.dialog.amend_offense_details
        )

    def close_event(self):
        self.close_window()


class AddConditionsDialogSlotFunctions(BaseDialogSlotFunctions):
    def __init__(self, dialog):
        self.dialog = dialog
        self.main_dialog = dialog.main_dialog

    def add_conditions(self):
        if self.main_dialog.community_service_checkBox.isChecked():
            self.dialog.transfer_view_data_to_model(
                self.main_dialog.entry_case_information.community_service
            )
        if self.main_dialog.license_suspension_checkBox.isChecked():
            self.dialog.transfer_view_data_to_model(
                self.main_dialog.entry_case_information.license_suspension
            )
        if self.main_dialog.other_conditions_checkBox.isChecked():
            self.dialog.transfer_view_data_to_model(
                self.main_dialog.entry_case_information.other_conditions
            )


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
