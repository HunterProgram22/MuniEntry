import os

from docxtpl import DocxTemplate
from loguru import logger
from PyQt5.QtSql import QSqlQuery

from db.databases import open_charges_db_connection, extract_data
from package.controllers.helper_functions import InfoChecker, check_if_diversion_program_selected, set_document_name
from package.models.case_information import CriminalCharge, AmendOffenseDetails
from package.views.custom_widgets import RequiredBox
from settings import SAVE_PATH


class BaseDialogSlotFunctions(object):
    def __init__(self, dialog):
        self.dialog = dialog

    def start_add_charge_dialog(self):
        from package.controllers.base_dialogs import AddChargeDialog
        self.dialog.update_case_information()
        AddChargeDialog(self.dialog).exec()

    def start_amend_offense_dialog(self):
        from package.controllers.base_dialogs import AmendChargeDialog
        self.dialog.update_case_information()
        AmendChargeDialog(self.dialog).exec()

    def close_event(self):
        self.close_window()

    def close_window(self):
        """Function connected to a button to close the window. Can be connected
        to any button press/click/release to close a window. This can also be called
        at the end of the close_event process to close the dialog."""
        self.dialog.close()

    @logger.catch
    def clear_case_information_fields(self):
        self.dialog.defendant_first_name_lineEdit.clear()
        self.dialog.defendant_last_name_lineEdit.clear()
        self.dialog.case_number_lineEdit.clear()
        self.dialog.defendant_first_name_lineEdit.setFocus()

    @logger.catch
    def create_entry(self):
        """Loads the proper template and creates the entry."""
        doc = DocxTemplate(self.dialog.template.template_path)
        case_data = self.dialog.entry_case_information.get_case_information()
        extract_data(case_data)
        doc.render(case_data)
        docname = set_document_name(self.dialog)
        try:
            doc.save(SAVE_PATH + docname)
            os.startfile(SAVE_PATH + docname)
        except PermissionError:
            message = RequiredBox("An entry for this case is already open in Word."
                                  " You must close the Word document first.")
            message.exec()

    @logger.catch
    def create_entry_process(self):
        """The info_checks variable is either "Pass" or "Fail" based on the checks performed by the
        update_info_and_perform_checks method (found in helper_functions.py)."""
        info_checks = self.update_info_and_perform_checks()
        if info_checks == "Pass":
            self.create_entry()

    @logger.catch
    def update_info_and_perform_checks(self):
        self.dialog.update_case_information()
        if InfoChecker.check_defense_counsel(self.dialog) == "Fail":
            return "Fail"
        if check_if_diversion_program_selected(self.dialog) is False:
            return "Fail"
        if InfoChecker.check_plea_and_findings(self.dialog) == "Fail":
            return "Fail"
        if InfoChecker.check_insurance(self.dialog) == "Fail":
            return "Fail"
        if InfoChecker.check_bond_amount(self.dialog) == "Fail":
            return "Fail"
        if InfoChecker.check_additional_conditions_ordered(self.dialog) == "Fail":
            return "Fail"
        if InfoChecker.check_jail_days(self.dialog) == "Fail":
            return "Fail"
        self.dialog.update_case_information()
        return "Pass"

    def set_defense_counsel(self):
        if self.dialog.defense_counsel_waived_checkBox.isChecked():
            self.dialog.defense_counsel_name_box.setEnabled(False)
            self.dialog.defense_counsel_type_box.setEnabled(False)
        else:
            self.dialog.defense_counsel_name_box.setEnabled(True)
            self.dialog.defense_counsel_type_box.setEnabled(True)

    @logger.catch
    def set_fra_in_file(self, current_text):
        """Sets the FRA (proof of insurance) to true if the view indicates 'yes'
        that the FRA was shown in the complaint of file."""
        if current_text == "Yes":
            self.dialog.entry_case_information.fra_in_file = True
            self.dialog.fra_in_court_box.setCurrentText("No")
        elif current_text == "No":
            self.dialog.entry_case_information.fra_in_file = False
        else:
            self.dialog.entry_case_information.fra_in_file = None

    @logger.catch
    def set_fra_in_court(self, current_text):
        """Sets the FRA (proof of insurance) to true if the view indicates 'yes'
        that the FRA was shown in court."""
        if current_text == "Yes":
            self.dialog.entry_case_information.fra_in_court = True
        elif current_text == "No":
            self.dialog.entry_case_information.fra_in_court = False
        else:
            self.dialog.entry_case_information.fra_in_court = None

    def close_dialog(self):
        self.dialog.close_event()

    @classmethod
    @logger.catch
    def set_statute_and_offense(cls, key, dialog):
        """:key: is the string that is passed by the function each time the field
        is changed on the view."""
        charges_database = open_charges_db_connection()
        field = None
        if dialog.freeform_entry_checkBox.isChecked():
            return None
        if dialog.sender() == dialog.statute_choice_box:
            field = 'statute'
        elif dialog.sender() == dialog.offense_choice_box:
            field = 'offense'
        query = QSqlQuery(charges_database)
        query_string = f"SELECT * FROM charges WHERE {field} LIKE '%' || :key || '%'"
        query.prepare(query_string)
        query.bindValue(":key", key)
        query.bindValue(field, field)
        query.exec()
        while query.next():
            offense = query.value(1)
            statute = query.value(2)
            degree = query.value(3)
            if field == 'offense':
                if offense == key:
                    dialog.statute_choice_box.setCurrentText(statute)
            elif field == 'statute':
                if statute == key:
                    dialog.offense_choice_box.setCurrentText(offense)
            dialog.degree_choice_box.setCurrentText(degree)
            query.finish()
            break

    def conditions_checkbox_toggle(self):
        if self.dialog.sender().isChecked():
            for items in self.dialog.additional_conditions_list:
                if items[0] == self.dialog.sender().objectName():
                    setattr(items[1], "ordered", True)
        else:
            for items in self.dialog.additional_conditions_list:
                if items[0] == self.dialog.sender().objectName():
                    setattr(items[1], "ordered", False)

    def set_report_date(self):
        if self.dialog.report_type_box.currentText() == "date set by Office of Community Control":
            self.dialog.report_date_box.setDisabled(True)
            self.dialog.report_date_box.setHidden(True)
            self.dialog.report_time_box.setDisabled(True)
            self.dialog.report_time_box.setHidden(True)
            self.dialog.report_date_label.setHidden(True)
            self.dialog.report_time_label.setHidden(True)
        elif self.dialog.report_type_box.currentText() == "forthwith":
            self.dialog.report_date_box.setDisabled(True)
            self.dialog.report_date_box.setHidden(True)
            self.dialog.report_time_box.setDisabled(True)
            self.dialog.report_time_box.setHidden(True)
            self.dialog.report_date_label.setHidden(True)
            self.dialog.report_time_label.setHidden(True)
        else:
            self.dialog.report_date_box.setEnabled(True)
            self.dialog.report_date_box.setHidden(False)
            self.dialog.report_time_box.setEnabled(True)
            self.dialog.report_time_box.setHidden(False)
            self.dialog.report_date_label.setHidden(False)
            self.dialog.report_time_label.setHidden(False)

    def show_report_days_notes_box(self):
        if self.dialog.jail_sentence_execution_type_box.currentText() == "consecutive days":
            self.dialog.jail_report_days_notes_box.setDisabled(True)
            self.dialog.jail_report_days_notes_box.setHidden(True)
        else:
            self.dialog.jail_report_days_notes_box.setDisabled(False)
            self.dialog.jail_report_days_notes_box.setHidden(False)

    def set_field_enabled(self):
        """Loops through the conditions_checkbox_list and if the box is checked for the condition it will show
        any additional fields that are required for that condition."""
        for item in self.dialog.condition_checkbox_list:
            (condition_checkbox, condition_field) = item
            if hasattr(self.dialog, condition_checkbox):
                if getattr(self.dialog, condition_checkbox).isChecked():
                    getattr(self.dialog, condition_field).setEnabled(True)
                    getattr(self.dialog, condition_field).setHidden(False)
                    getattr(self.dialog, condition_field).setFocus(True)
                else:
                    getattr(self.dialog, condition_field).setEnabled(False)
                    getattr(self.dialog, condition_field).setHidden(True)


class AddChargeDialogSlotFunctions(BaseDialogSlotFunctions):
    def __init__(self, dialog):
        self.dialog = dialog
        self.main_dialog = dialog.main_dialog

    @logger.catch
    def clear_add_charge_fields(self):
        self.dialog.statute_choice_box.clearEditText()
        self.dialog.offense_choice_box.clearEditText()

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
        """TODO: self.criminal_charge_type needs to be fixed to add back in to get costs calculator to work
        again eventually."""
        self.criminal_charge = CriminalCharge()
        self.criminal_charge.offense = self.dialog.offense_choice_box.currentText()
        self.criminal_charge.statute = self.dialog.statute_choice_box.currentText()
        self.criminal_charge.degree = self.dialog.degree_choice_box.currentText()
        # self.criminal_charge.type = self.set_offense_type()
        self.main_dialog.entry_case_information.add_charge_to_list(self.criminal_charge)


class AmendChargeDialogSlotFunctions(BaseDialogSlotFunctions):
    def __init__(self, dialog):
        self.dialog = dialog
        self.main_dialog = dialog.main_dialog

    def clear_amend_charge_fields(self):
        """Clears the fields in the view."""
        self.dialog.statute_choice_box.clearEditText()
        self.dialog.offense_choice_box.clearEditText()

    def amend_offense(self):
        """Adds the data entered for the amended ofdialog.fense to the AmendOffenseDetails
        object then points the entry_case_information object to the AmendOffenseDetails
        object."""
        self.dialog.amend_offense_details.original_charge = self.dialog.current_offense_name
        self.dialog.amend_offense_details.amended_charge = self.dialog.offense_choice_box.currentText()
        self.dialog.amend_offense_details.motion_disposition = self.dialog.motion_decision_box.currentText()
        self.main_dialog.entry_case_information.amend_offense_details = self.dialog.amend_offense_details
        if self.dialog.motion_decision_box.currentText() == "Granted":
            amended_charge = f"{self.dialog.current_offense_name} - AMENDED to {self.dialog.amend_offense_details.amended_charge}"
            setattr(self.dialog.charge, 'offense', amended_charge)
            self.main_dialog.entry_case_information.amended_charges_list.append(
                (self.dialog.amend_offense_details.original_charge, self.dialog.amend_offense_details.amended_charge)
            )
            for columns in range(self.main_dialog.charges_gridLayout.columnCount()):
                if (
                    self.main_dialog.charges_gridLayout.itemAtPosition(0, columns) is not None
                    and self.main_dialog.charges_gridLayout.itemAtPosition(
                        0, columns).widget().text() == self.dialog.current_offense_name
                ):
                    self.main_dialog.charges_gridLayout.itemAtPosition(0, columns).widget().setText(amended_charge)
                    self.main_dialog.charges_gridLayout.itemAtPosition(1, columns).widget().setText(self.dialog.statute_choice_box.currentText())
                    self.main_dialog.charges_gridLayout.itemAtPosition(2, columns).widget().setCurrentText(self.dialog.degree_choice_box.currentText())
        self.close_event()


class FineOnlyDialogSlotFunctions(BaseDialogSlotFunctions):
    def __init__(self, dialog):
        self.dialog = dialog

    def set_fines_credit_for_jail_field(self):
        if self.dialog.credit_for_jail_checkBox.isChecked():
            self.dialog.jail_time_credit_box.setEnabled(True)
            self.dialog.jail_time_credit_box.setHidden(False)
            self.dialog.jail_time_credit_box.setFocus()
        else:
            self.dialog.jail_time_credit_box.setEnabled(False)
            self.dialog.jail_time_credit_box.setHidden(True)

    @logger.catch
    def start_add_conditions_dialog(self):
        from package.controllers.conditions_dialogs import AddConditionsDialog
        self.dialog.update_case_information()
        AddConditionsDialog(self.dialog).exec()


class JailCCDialogSlotFunctions(BaseDialogSlotFunctions):
    def __init__(self, dialog):
        self.dialog = dialog

    @logger.catch
    def start_add_conditions_dialog(self):
        from package.controllers.conditions_dialogs import AddCommunityControlDialog
        self.dialog.update_case_information()
        AddCommunityControlDialog(self.dialog).exec()


class DiversionDialogSlotFunctions(BaseDialogSlotFunctions):
    def __init__(self, dialog):
        self.dialog = dialog

    def show_other_conditions_box(self):
        if self.dialog.other_conditions_checkBox.isChecked():
            self.dialog.other_conditions_textEdit.setHidden(False)
            self.dialog.other_conditions_textEdit.setFocus()
        else:
            self.dialog.other_conditions_textEdit.setHidden(True)

    def show_jail_report_date_box(self):
        if self.dialog.diversion_jail_imposed_checkBox.isChecked():
            self.dialog.diversion_jail_report_date_box.setHidden(False)
            self.dialog.diversion_jail_report_date_label.setHidden(False)
        else:
            self.dialog.diversion_jail_report_date_box.setHidden(True)
            self.dialog.diversion_jail_report_date_label.setHidden(True)


class NotGuiltyBondDialogSlotFunctions(BaseDialogSlotFunctions):
    def __init__(self, dialog):
        self.dialog = dialog

    def start_add_special_bond_conditions_dialog(self):
        from package.controllers.conditions_dialogs import AddSpecialBondConditionsDialog
        self.dialog.update_case_information()
        AddSpecialBondConditionsDialog(self.dialog).exec()

    def conditions_checkbox_toggle(self):
        if self.dialog.sender().isChecked():
            for items in self.dialog.additional_conditions_list:
                if items[0] == self.dialog.sender().objectName():
                    setattr(items[1], "ordered", True)
        else:
            for items in self.dialog.additional_conditions_list:
                if items[0] == self.dialog.sender().objectName():
                    setattr(items[1], "ordered", False)

    def hide_boxes(self):
        """This method is called from modify_view as part of the init to hide all optional boxes on load."""
        for item in self.dialog.condition_checkbox_list:
            (condition_checkbox, condition_field) = item
            if hasattr(self.dialog, condition_checkbox):
                getattr(self.dialog, condition_field).setEnabled(False)
                getattr(self.dialog, condition_field).setHidden(True)

    def set_field_enabled(self):
        """Loops through the conditions_checkbox_list and if the box is checked for the condition it will show
        any additional fields that are required for that condition."""
        for item in self.dialog.condition_checkbox_list:
            (condition_checkbox, condition_field) = item
            if hasattr(self.dialog, condition_checkbox):
                if getattr(self.dialog, condition_checkbox).isChecked():
                    getattr(self.dialog, condition_field).setEnabled(True)
                    getattr(self.dialog, condition_field).setHidden(False)
                    getattr(self.dialog, condition_field).setFocus(True)
                else:
                    getattr(self.dialog, condition_field).setEnabled(False)
                    getattr(self.dialog, condition_field).setHidden(True)


class AddConditionsDialogSlotFunctions(BaseDialogSlotFunctions):
    def __init__(self, dialog):
        self.dialog = dialog
        self.main_dialog = dialog.main_dialog

    def add_conditions(self):
        if self.main_dialog.community_service_checkBox.isChecked():
            self.dialog.transfer_field_data_to_model(self.main_dialog.entry_case_information.community_service)
        if self.main_dialog.license_suspension_checkBox.isChecked():
            self.dialog.transfer_field_data_to_model(self.main_dialog.entry_case_information.license_suspension)
        if self.main_dialog.other_conditions_checkBox.isChecked():
            self.dialog.transfer_field_data_to_model(self.main_dialog.entry_case_information.other_conditions)


class AddCommunityControlDialogSlotFunctions(BaseDialogSlotFunctions):
    def __init__(self, dialog):
        self.dialog = dialog
        self.main_dialog = dialog.main_dialog

    def add_conditions(self):
        if self.main_dialog.community_service_checkBox.isChecked():
            self.dialog.transfer_field_data_to_model(self.main_dialog.entry_case_information.community_service)
        if self.main_dialog.license_suspension_checkBox.isChecked():
            self.dialog.transfer_field_data_to_model(self.main_dialog.entry_case_information.license_suspension)
        if self.main_dialog.other_conditions_checkBox.isChecked():
            self.dialog.transfer_field_data_to_model(self.main_dialog.entry_case_information.other_conditions)
        if self.main_dialog.community_control_checkBox.isChecked():
            self.dialog.transfer_field_data_to_model(self.main_dialog.entry_case_information.community_control)
        if self.main_dialog.jail_checkBox.isChecked():
            self.dialog.transfer_field_data_to_model(self.main_dialog.entry_case_information.jail_terms)
        if self.main_dialog.impoundment_checkBox.isChecked():
            self.dialog.transfer_field_data_to_model(self.main_dialog.entry_case_information.impoundment)
        if self.main_dialog.victim_notification_checkBox.isChecked():
            self.dialog.transfer_field_data_to_model(self.main_dialog.entry_case_information.victim_notification)


class AddSpecialBondConditionsDialogSlotFunctions(BaseDialogSlotFunctions):
    def __init__(self, dialog):
        self.dialog = dialog
        self.main_dialog = dialog.main_dialog

    def add_conditions(self):
        if self.main_dialog.domestic_violence_checkBox.isChecked():
            self.dialog.transfer_field_data_to_model(self.main_dialog.entry_case_information.domestic_violence_conditions)
        if self.main_dialog.admin_license_suspension_checkBox.isChecked():
            self.dialog.transfer_field_data_to_model(self.main_dialog.entry_case_information.admin_license_suspension)
        if self.main_dialog.no_contact_checkBox.isChecked():
            self.dialog.transfer_field_data_to_model(self.main_dialog.entry_case_information.no_contact)
        if self.main_dialog.custodial_supervision_checkBox.isChecked():
            self.dialog.transfer_field_data_to_model(self.main_dialog.entry_case_information.custodial_supervision)
        if self.main_dialog.other_conditions_checkBox.isChecked():
            self.dialog.transfer_field_data_to_model(self.main_dialog.entry_case_information.other_conditions)
        if self.main_dialog.vehicle_seizure_checkBox.isChecked():
            self.dialog.transfer_field_data_to_model(self.main_dialog.entry_case_information.vehicle_seizure)


class AddJailOnlyDialogSlotFunctions(BaseDialogSlotFunctions):
    def __init__(self, dialog):
        self.dialog = dialog
        self.main_dialog = dialog.main_dialog

    def add_conditions(self):
        if self.main_dialog.jail_checkBox.isChecked():
            self.dialog.transfer_field_data_to_model(self.main_dialog.entry_case_information.jail_terms)


def close_databases():
    """This function is duplicate of the one in base_dialogs.py"""
    charges_database.close()
    charges_database.removeDatabase("QSQLITE")


if __name__ == "__main__":
    print("Slot Functions ran directly")
else:
    print("Slot Functions imported")
    charges_database = open_charges_db_connection()


