"""Module containing all classes that load functions tied to a signal."""
from os import startfile

from docxtpl import DocxTemplate
from loguru import logger
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtCore import QDate

from munientry.views.custom_widgets import InfoBox
from munientry.data.databases import sql_query_offense_type
from munientry.controllers.helper_functions import set_future_date
from munientry.models.criminal_charge_models import CriminalCharge
from munientry.views.custom_widgets import RequiredBox
from munientry.settings import SAVE_PATH

SPECIAL_DOCKETS_COSTS = [
    'while on the OVI Docket',
    'while on Mission Court',
    'while on the Mental Health Docket',
]

class BaseDialogSlotFunctions(object):
    def __init__(self, dialog):
        self.dialog = dialog

    def start_add_charge_dialog(self):
        from munientry.builders.charges_dialogs import AddChargeDialog

        self.dialog.update_entry_case_information()
        self.dialog.popup_dialog = AddChargeDialog(self.dialog)
        self.dialog.popup_dialog.exec()

    def start_amend_offense_dialog(self):
        from munientry.builders.charges_dialogs import AmendChargeDialog

        self.dialog.update_entry_case_information()
        self.dialog.popup_dialog = AmendChargeDialog(self.dialog)
        self.dialog.popup_dialog.exec()

    def close_window(self):
        """Closes window by calling closeEvent in BaseDialog.

        Event is logged in BaseDialog closeEvent.

        Function connected to a button to close the window. Can be connected
        to any button press/click/release to close a window. This can also be called
        at the end of the close_event process to close the dialog.
        """
        self.dialog.close()

    def clear_case_information_fields(self):
        self.dialog.defendant_first_name_lineEdit.clear()
        self.dialog.defendant_last_name_lineEdit.clear()
        self.dialog.case_number_lineEdit.clear()
        self.dialog.defendant_first_name_lineEdit.setFocus()

    def create_entry(self):
        """Loads the proper template and creates the entry."""
        self.dialog.update_entry_case_information()
        doc = DocxTemplate(self.dialog.template.template_path)
        case_data = self.dialog.entry_case_information.get_case_information()
        # extract_data(case_data)
        doc.render(case_data)
        docname = self.set_document_name()
        logger.info(f'Entry Created: {docname}')
        try:
            doc.save(SAVE_PATH + docname)
            startfile(SAVE_PATH + docname)
        except PermissionError as error:
            logger.warning(error)
            self.dialog.message_box = RequiredBox(
                "An entry for this case is already open in Word."
                " You must close the Word document first."
            )
            self.dialog.message_box.exec()

    def create_entry_process(self):
        """The info_checks variable is either "Pass" or "Fail" based on the checks performed by the
        update_info_and_perform_checks method."""
        if self.update_info_and_perform_checks() == "Pass":
            self.create_entry()

    def set_document_name(self):
        """Returns a name for the document in the format CaseNumber_TemplateName.docx
        (i.e. 21CRB1234_Crim_Traffic Judgment Entry.docx"""
        return (
            f"{self.dialog.entry_case_information.case_number}"
            f"_{self.dialog.template.template_name}.docx"
        )

    def set_fines_costs_pay_date(self, days_to_add_string):
        """Sets the sentencing date to the Tuesday after the number of days added."""
        if days_to_add_string == "forthwith":
            self.dialog.balance_due_date.setHidden(False)
            self.dialog.balance_due_date.setDate(QDate.currentDate())
        elif days_to_add_string in SPECIAL_DOCKETS_COSTS:
            self.dialog.balance_due_date.setHidden(True)
        else:
            self.dialog.balance_due_date.setHidden(False)
            days_to_add = self.get_days_to_add(days_to_add_string)
            total_days_to_add = set_future_date(days_to_add, "Tuesday")
            self.dialog.balance_due_date.setDate(
                QDate.currentDate().addDays(total_days_to_add)
            )

    def get_days_to_add(self, days_to_add_string):
        pay_date_dict = {
            "within 30 days": 30,
            "within 60 days": 60,
            "within 90 days": 90,
        }
        return pay_date_dict.get(days_to_add_string)

    @logger.catch
    def update_info_and_perform_checks(self):
        """This method performs an update then calls to the main_entry_dialog's InfoChecker class to run
        the checks for that dialog. The InfoChecker check_status will return as "Fail" if any of the
        checks are hard stops - meaning the warning message doesn't allow immediate correction.

        The dialog.update_entry_case_information is called a second time to update the model with any changes
        to information that was made by the InfoChecker checks."""
        self.dialog.update_entry_case_information()
        self.dialog.perform_info_checks()
        if self.dialog.dialog_checks.check_status == "Fail":
            return "Fail"
        self.dialog.update_entry_case_information()
        return "Pass"

    def set_defense_counsel(self):
        if self.dialog.defense_counsel_waived_checkBox.isChecked():
            self.dialog.defense_counsel_name_box.setEnabled(False)
            self.dialog.defense_counsel_type_box.setEnabled(False)
        else:
            self.dialog.defense_counsel_name_box.setEnabled(True)
            self.dialog.defense_counsel_type_box.setEnabled(True)

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

    def set_fra_in_court(self, current_text):
        """Sets the FRA (proof of insurance) to true if the view indicates 'yes'
        that the FRA was shown in court."""
        if current_text == "Yes":
            self.dialog.entry_case_information.fra_in_court = True
        elif current_text == "No":
            self.dialog.entry_case_information.fra_in_court = False
        else:
            self.dialog.entry_case_information.fra_in_court = None

    @logger.catch
    def show_costs_and_fines(self):
        self.dialog.update_entry_case_information()
        message = InfoBox()
        message.setWindowTitle("Total Costs and Fines")
        message.setInformativeText(
            f"Costs: $ {str(self.dialog.entry_case_information.court_costs.amount)}"
            f"\nFines: $ {str(self.dialog.entry_case_information.total_fines)}"
            f"\nFines Suspended: $ {str(self.dialog.entry_case_information.total_fines_suspended)}"
            f"\n\n*Does not include possible bond forfeiture or other costs \n that "
            f"may be assessed as a result of prior actions in the case. "
        )
        total_fines_and_costs = (
            self.dialog.entry_case_information.court_costs.amount
            + self.dialog.entry_case_information.total_fines
        ) - self.dialog.entry_case_information.total_fines_suspended
        message.setText(
            f"Total Costs and Fines Due By Due Date: $ {str(total_fines_and_costs)}"
        )
        message.exec_()

    def update_community_service_due_date(self, _index=None):
        days_to_complete = int(
            self.dialog.community_service_days_to_complete_box.currentText()
        )
        self.dialog.community_service_date_to_complete_box.setDate(
            QDate.currentDate().addDays(days_to_complete)
        )

    def set_offense(self, key):
        if self.dialog.freeform_entry_checkBox.isChecked():
            return None
        field = 'statute'
        offense, statute, degree = self.query_charges_database(key, field)
        if statute == key:
            self.dialog.offense_choice_box.setCurrentText(offense)
        self.dialog.degree_choice_box.setCurrentText(degree)

    def set_statute(self, key):
        if self.dialog.freeform_entry_checkBox.isChecked():
            return None
        field = 'offense'
        offense, statute, degree = self.query_charges_database(key, field)
        if offense == key:
            self.dialog.statute_choice_box.setCurrentText(statute)
        self.dialog.degree_choice_box.setCurrentText(degree)

    def query_charges_database(self, key, field):
        query_string = f"SELECT * FROM charges WHERE {field} LIKE '%' || :key || '%'"
        query = QSqlQuery(self.dialog.db_connection)
        query.prepare(query_string)
        query.bindValue(":key", key)
        query.bindValue(field, field)
        query.exec()
        query.next()
        offense = query.value(1)
        statute = query.value(2)
        degree = query.value(3)
        query.finish()
        return offense, statute, degree

    def conditions_checkbox_toggle(self):
        logger.log('BUTTON', f'{self.dialog.sender().text()} Checkbox Set: {self.dialog.sender().isChecked()}')
        if self.dialog.sender().isChecked():
            for items in self.dialog.additional_conditions_list:
                if items[0] == self.dialog.sender().objectName():
                    setattr(items[1], "ordered", True)
        else:
            for items in self.dialog.additional_conditions_list:
                if items[0] == self.dialog.sender().objectName():
                    setattr(items[1], "ordered", False)

    def set_report_date(self):
        if (
            self.dialog.report_type_box.currentText()
            == "date set by Office of Community Control"
        ):
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
        if (
            self.dialog.jail_sentence_execution_type_box.currentText()
            == "consecutive days"
        ):
            self.dialog.jail_report_days_notes_box.setDisabled(True)
            self.dialog.jail_report_days_notes_box.setHidden(True)
        else:
            self.dialog.jail_report_days_notes_box.setDisabled(False)
            self.dialog.jail_report_days_notes_box.setHidden(False)

    def show_hide_checkbox_connected_fields(self):
        """Gets list of boxes tied to condition checkbox and sets to show or hidden based on
        whether the box is checked or not."""
        checkbox = self.dialog.sender()
        boxes = self.dialog.condition_checkbox_dict.get(checkbox.objectName())
        for item in boxes:
            if checkbox.isChecked():
                getattr(self.dialog, item).setEnabled(True)
                getattr(self.dialog, item).setHidden(False)
                getattr(self.dialog, item).setFocus(True)
            else:
                getattr(self.dialog, item).setEnabled(False)
                getattr(self.dialog, item).setHidden(True)

    def set_freeform_entry(self):
        if self.dialog.freeform_entry_checkBox.isChecked():
            self.dialog.statute_choice_box.setEditable(True)
            self.dialog.offense_choice_box.setEditable(True)
            self.dialog.statute_choice_box.clearEditText()
            self.dialog.offense_choice_box.clearEditText()
            self.dialog.degree_choice_box.setCurrentText("")
        else:
            self.dialog.statute_choice_box.setEditable(False)
            self.dialog.offense_choice_box.setEditable(False)
            self.dialog.statute_choice_box.setCurrentText("")
            self.dialog.offense_choice_box.setCurrentText("")
            self.dialog.degree_choice_box.setCurrentText("")

    def show_bond_boxes(self, bond_mod_string):
        if bond_mod_string == "request to modify bond is granted":
            self.dialog.bond_frame.setHidden(False)
            self.dialog.bond_conditions_frame.setHidden(False)
            self.dialog.special_bond_conditions_frame.setHidden(False)
        else:
            self.dialog.bond_frame.setHidden(True)
            self.dialog.bond_conditions_frame.setHidden(True)
            self.dialog.special_bond_conditions_frame.setHidden(True)


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
        return sql_query_offense_type(key, self.dialog.db_connection)

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


class LeapAdmissionPleaDialogSlotFunctions(BaseDialogSlotFunctions):
    def __init__(self, dialog):
        self.dialog = dialog

    def set_leap_sentencing_date(self, days_to_add_string):
        """Sets the sentencing date to the Monday after the number of days added."""
        if days_to_add_string == "forthwith":
            self.dialog.sentencing_date.setDate(QDate.currentDate())
        else:
            days_to_add = self.get_days_to_add(days_to_add_string)
            total_days_to_add = set_future_date(days_to_add, "Monday")
            self.dialog.sentencing_date.setDate(
                QDate.currentDate().addDays(total_days_to_add)
            )

    def get_days_to_add(self, days_to_add_string):
        leap_sentence_date_dict = {
            "120 days": 120,
        }
        return leap_sentence_date_dict.get(days_to_add_string)


class PleaOnlyDialogSlotFunctions(BaseDialogSlotFunctions):
    def __init__(self, dialog):
        self.dialog = dialog


class LeapSentencingDialogSlotFunctions(BaseDialogSlotFunctions):
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

    def start_add_conditions_dialog(self):
        from munientry.builders.conditions_dialogs import AddConditionsDialog

        self.dialog.update_entry_case_information()
        self.dialog.popup_dialog = AddConditionsDialog(self.dialog)
        self.dialog.popup_dialog.exec()


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

    def start_add_conditions_dialog(self):
        from munientry.builders.conditions_dialogs import AddConditionsDialog

        self.dialog.update_entry_case_information()
        self.dialog.popup_dialog = AddConditionsDialog(self.dialog)
        self.dialog.popup_dialog.exec()


class JailCCDialogSlotFunctions(BaseDialogSlotFunctions):
    def __init__(self, dialog):
        self.dialog = dialog

    def show_companion_case_fields(self):
        if self.dialog.add_companion_cases_checkBox.isChecked():
            self.dialog.companion_cases_box.setHidden(False)
            self.dialog.companion_cases_sentence_box.setHidden(False)
            self.dialog.companion_cases_sentence_label.setHidden(False)
        else:
            self.dialog.companion_cases_box.setHidden(True)
            self.dialog.companion_cases_sentence_box.setHidden(True)
            self.dialog.companion_cases_sentence_label.setHidden(True)

    @logger.catch
    def start_add_jail_report_dialog(self):
        from munientry.builders.conditions_dialogs import AddJailOnlyDialog

        self.dialog.update_entry_case_information()
        self.dialog.popup_dialog = AddJailOnlyDialog(self.dialog)
        self.dialog.popup_dialog.exec()

    @logger.catch
    def start_add_conditions_dialog(self):
        from munientry.builders.conditions_dialogs import AddCommunityControlDialog

        self.dialog.update_entry_case_information()
        self.dialog.popup_dialog = AddCommunityControlDialog(self.dialog)
        self.dialog.popup_dialog.exec()


class SentencingOnlyDialogSlotFunctions(JailCCDialogSlotFunctions):
    """Inherits from JailCCDialogSlotFunctions because all the functions are the same.

        The only difference between dialogs is the template has a plea date field.
        """

    def __init__(self, dialog):
        super().__init__(dialog)


class TrialSentencingDialogSlotFunctions(JailCCDialogSlotFunctions):
    """Inherits from JailCCDialogSlotFunctions because all the functions are the same.

    The only difference between dialogs is the template used and the charge grid does not
    have a plea field.
    """
    def __init__(self, dialog):
        super().__init__(dialog)

    def set_all_findings_process(self):
        self.dialog.charges_gridLayout.set_all_trial_findings()


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
            self.dialog.jail_report_date_note_label.setHidden(False)
        else:
            self.dialog.diversion_jail_report_date_box.setHidden(True)
            self.dialog.diversion_jail_report_date_label.setHidden(True)
            self.dialog.jail_report_date_note_label.setHidden(True)

    def show_restitution_boxes(self):
        if self.dialog.pay_restitution_checkBox.isChecked():
            self.dialog.pay_restitution_to_box.setHidden(False)
            self.dialog.pay_restitution_amount_box.setHidden(False)
            self.dialog.pay_restitution_to_label.setHidden(False)
            self.dialog.pay_restitution_amount_label.setHidden(False)
        else:
            self.dialog.pay_restitution_to_box.setHidden(True)
            self.dialog.pay_restitution_amount_box.setHidden(True)
            self.dialog.pay_restitution_to_label.setHidden(True)
            self.dialog.pay_restitution_amount_label.setHidden(True)


class ProbationViolationBondDialogSlotFunctions(BaseDialogSlotFunctions):
    def __init__(self, dialog):
        self.dialog = dialog

    def hide_bond_conditions(self):
        if self.dialog.bond_type_box.currentText() == "No Bond":
            self.dialog.bond_conditions_frame.setHidden(True)
        else:
            self.dialog.bond_conditions_frame.setHidden(False)

    def set_if_no_bond(self, dialog):
        if self.dialog.bond_type_box.currentText() == "No Bond":
            self.dialog.bond_amount_box.setCurrentText("None")


class FreeformDialogSlotFunctions(BaseDialogSlotFunctions):
    def __init__(self, dialog):
        self.dialog = dialog


class FailureToAppearDialogSlotFunctions(BaseDialogSlotFunctions):
    def __init__(self, dialog):
        self.dialog = dialog

    def hide_warrant_radius(self):
        if self.dialog.arrest_warrant_checkBox.isChecked():
            self.dialog.arrest_warrant_radius_label.setHidden(False)
            self.dialog.arrest_warrant_radius_box.setHidden(False)
        else:
            self.dialog.arrest_warrant_radius_label.setHidden(True)
            self.dialog.arrest_warrant_radius_box.setHidden(True)

    def hide_bond_boxes(self):
        if self.dialog.set_bond_checkBox.isChecked():
            self.dialog.bond_type_box.setHidden(False)
            self.dialog.bond_amount_box.setHidden(False)
            self.dialog.bond_type_label.setHidden(False)
            self.dialog.bond_amount_label.setHidden(False)
        else:
            self.dialog.bond_type_box.setHidden(True)
            self.dialog.bond_amount_box.setHidden(True)
            self.dialog.bond_type_label.setHidden(True)
            self.dialog.bond_amount_label.setHidden(True)

    def set_bond_amount_box(self):
        if self.dialog.bond_type_box.currentText() == "No Bond":
            self.dialog.bond_amount_box.setHidden(True)
            self.dialog.bond_amount_label.setHidden(True)
        elif self.dialog.bond_type_box.currentText() == "Recognizance (OR) Bond":
            self.dialog.bond_amount_box.setHidden(True)
            self.dialog.bond_amount_label.setHidden(True)
        else:
            self.dialog.bond_amount_box.setHidden(False)
            self.dialog.bond_amount_label.setHidden(False)


class NotGuiltyBondDialogSlotFunctions(BaseDialogSlotFunctions):
    def __init__(self, dialog):
        self.dialog = dialog

    def start_add_special_bond_conditions_dialog(self):
        from munientry.builders.conditions_dialogs import (
            AddSpecialBondConditionsDialog,
        )

        self.dialog.update_entry_case_information()
        AddSpecialBondConditionsDialog(self.dialog).exec()

    def hide_boxes(self):
        """This method is called from modify_view as part of the init to hide all optional boxes on load."""
        for item in self.dialog.condition_checkbox_dict:
            (condition_checkbox, condition_field) = item
            if hasattr(self.dialog, condition_checkbox):
                getattr(self.dialog, condition_field).setEnabled(False)
                getattr(self.dialog, condition_field).setHidden(True)

    def show_hide_bond_conditions(self):
        if self.dialog.bond_type_box.currentText() == "Continue Existing Bond":
            self.dialog.bond_conditions_frame.setHidden(True)
            self.dialog.special_bond_conditions_frame.setHidden(True)
        else:
            self.dialog.bond_conditions_frame.setHidden(False)
            self.dialog.special_bond_conditions_frame.setHidden(False)


class NoPleaBondDialogSlotFunctions(BaseDialogSlotFunctions):
    def __init__(self, dialog):
        self.dialog = dialog

    def start_add_special_bond_conditions_dialog(self):
        from munientry.builders.conditions_dialogs import (
            AddSpecialBondConditionsDialog,
        )

        self.dialog.update_entry_case_information()
        AddSpecialBondConditionsDialog(self.dialog).exec()

    def hide_boxes(self):
        """This method is called from modify_view as part of the init to hide all optional boxes on load."""
        for item in self.dialog.condition_checkbox_dict:
            (condition_checkbox, condition_field) = item
            if hasattr(self.dialog, condition_checkbox):
                getattr(self.dialog, condition_field).setEnabled(False)
                getattr(self.dialog, condition_field).setHidden(True)


class BondHearingDialogSlotFunctions(NotGuiltyBondDialogSlotFunctions):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.show_bond_boxes("None")


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
