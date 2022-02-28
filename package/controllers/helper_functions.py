"""Helper functions that are used throughout the application."""
from datetime import date, timedelta

from PyQt5.QtWidgets import QMessageBox
from loguru import logger

from MuniEntry.package.views.custom_widgets import WarningBox, RequiredBox, JailWarningBox, TwoChoiceQuestionBox


def set_document_name(dialog):
    """Sets document name based on the cms_case number and name of the template
    must include '.docx' to make it a Word document."""
    return dialog.entry_case_information.case_number + "_" + dialog.template.template_name + ".docx"


@logger.catch
def set_future_date(days_to_add, days_to_add_dict, next_day):
    """This is a general helper function that will accept the numbers of days to
    add to the current date and set a new date.
    :days_to_add: A string from the view.
    :days_to_add_dict: A dict that has the different date options available in
    the view.
    :next_day: The next day of the week to set the date after the days to add.
    For example 0 days sets it to the next Monday after the added days, 1 sets
    it to the next Tuesday after the added days, etc."""
    if days_to_add_dict is None:
        days_to_add = days_to_add
    else:
        days_to_add = days_to_add_dict[days_to_add]
    future_date = date.today() + timedelta(days_to_add)
    today = date.today()

    def next_court_day(future_date, weekday):
        """This function returns the number of days to add to today to set
        the actual date needed. If it is 1 it would be Tuesday, 3 would
        be Wednesday, etc."""
        days_ahead = weekday - future_date.weekday()
        if days_ahead <= 0:  # Target day already happened this week
            days_ahead += 7
        return future_date + timedelta(days_ahead)

    future_date = next_court_day(future_date, next_day)
    total_days_to_add = (future_date - today).days
    return total_days_to_add


class InfoChecker(object):
    """Class that checks dialog to make sure the appropriate information is entered.
    Methods are class methods because this is a factory method to perform checks and
    no object is instantiated."""
    @classmethod
    def check_defense_counsel(cls, dialog):
        if (dialog.defense_counsel_name_box.currentText() == ""
                and not dialog.defense_counsel_waived_checkBox.isChecked()):
            message = WarningBox("There is no attorney listed. Did "
                                 "the Defendant waive his right to counsel?"
                                 "\n\nIf you select 'No' you must enter a name "
                                 "for Def. Counsel.")
            return_value = message.exec()
            if return_value == QMessageBox.Yes:
                dialog.defense_counsel_waived_checkBox.setChecked(True)
                return "Pass"
            elif return_value == QMessageBox.No:
                return "Fail"
        else:
            return "Pass"

    @classmethod
    def check_plea_and_findings(cls, dialog):
        """Shows warning if no plea or findings are entered. Checks one at a time so unless all
        fields have a plea and finding you will get the warning until they are filled in."""
        row_plea, row_finding = dialog.charges_gridLayout.set_plea_and_finding_rows()
        column = 2
        loop_counter = 0
        while loop_counter < dialog.charges_gridLayout.columnCount():
            try:
                offense = dialog.charges_gridLayout.itemAtPosition(0, column).widget().text()
                if dialog.charges_gridLayout.itemAtPosition(row_plea, column).widget().currentText() == "":
                    message = RequiredBox(f"You must enter a plea for {offense}.")
                    message.exec()
                    return "Fail"
                elif dialog.charges_gridLayout.itemAtPosition(row_plea, column).widget().currentText() == "Dismissed":
                    column += 2
                    loop_counter += 1
                    continue
                elif dialog.charges_gridLayout.itemAtPosition(row_finding, column).widget().currentText() == "":
                    message = RequiredBox(f"You must enter a finding for {offense}.")
                    message.exec()
                    return "Fail"
            except AttributeError:
                pass
            column += 2
            loop_counter += 1
        return "Pass"

    @classmethod
    def check_insurance(cls, dialog):
        if (
            hasattr(dialog, 'fra_in_file_box')
            and dialog.fra_in_file_box.currentText() == "No"
            and dialog.fra_in_court_box.currentText() == "N/A"
        ):
            message = WarningBox("The information provided currently "
                                 "indicates insurance was not shown in the file. "
                                 "\n\nDid the defendant show proof of insurance in court?")
            return_value = message.exec()
            if return_value == QMessageBox.No:
                dialog.fra_in_court_box.setCurrentText("No")
                return "Pass"
            elif return_value == QMessageBox.Yes:
                dialog.fra_in_court_box.setCurrentText("Yes")
                return "Pass"
        else:
            return "Pass"

    @classmethod
    def check_bond_amount(cls, dialog):
        if(
            hasattr(dialog, 'bond_type_box')
            and dialog.bond_type_box.currentText() != 'Recognizance (OR) Bond'
            and dialog.bond_amount_box.currentText() == 'None (OR Bond)'
        ):
            message = RequiredBox("A bond type requiring a bond amount was selected, but a bond amount was not selected. Please specify the bond amount.")
            message.exec()
            return "Fail"
        if (
                hasattr(dialog, 'bond_type_box')
                and dialog.bond_type_box.currentText() == 'Recognizance (OR) Bond'
                and dialog.bond_amount_box.currentText() != 'None (OR Bond)'
        ):
            message = RequiredBox(
                "A Recognizance (OR) Bond was selected but a bond amount other than None(OR Bond) "
                "was chosen. Please either change bond type to 10% or Cash or Surety, or set bond amount to None (OR Bond).")
            message.exec()
            return "Fail"

    @classmethod
    def check_additional_conditions_ordered(cls, dialog):
        """TODO: This should be a method and the conditions_list should be passed based on the dialog so it only
        loops over the items in that dialog."""
        conditions_list = [
            ("license_suspension", "license_type", "License Suspension"),
            ("community_service", "hours_of_service", "Community Service"),
            ("other_conditions", "terms", "Other Conditions"),
            ("community_control", "term_of_control", "Community Control"),
            ("impoundment", "vehicle_make_model", "Immobilize/Impound"),
            ("admin_license_suspension", "disposition", "Admin License Suspension"),
            ("vehicle_seizure", "vehicle_make_model", "Vehicle Seizure"),
            ("no_contact", "name", "No Contact"),
            ("custodial_supervision", "supervisor", "Custodial Supervision"),
            ("diversion", "program_name", "Diversion"),
            # Domestic Violence Special Bond Condition needs to be added - but conditions don't work for method
        ]
        for condition_item in conditions_list:
            # Because dialog.entry_case_information is a model with all case conditions there is
            # apparently no need to check if it has that attribute (hasattr).
            condition = getattr(dialog.entry_case_information, condition_item[0])
            condition_ordered = getattr(condition, "ordered")
            main_condition_set = getattr(condition, condition_item[1])
            description = condition_item[2]
            if (
                condition_ordered is True
                and main_condition_set is None
            ):
                message = RequiredBox(f"The Additional Condition {description} is checked, but "
                                      f"the details of the {description} have not been entered.\n\n"
                                      f"Click the Add Conditions button to add details, or uncheck the "
                                      f"{description} box if there is no {description} in this case.")
                message.exec()
                return "Fail"
        """The bond_conditions_list for Victim Notification is used because of two checkboxes as only options, no 
        ordered option like other conditions. TODO: figure out way to make it part of standard conditions list."""
        bool_conditions_list = [
            (dialog.entry_case_information.victim_notification.ordered,
             dialog.entry_case_information.victim_notification.victim_reparation_notice,
             dialog.entry_case_information.victim_notification.victim_prosecutor_notice,
             "Victim Notification"),
        ]
        for bool_condition_item in bool_conditions_list:
            (bool_condition_ordered, bool_condition_one, bool_condition_two, description) = bool_condition_item
            if (
                bool_condition_ordered is True
                and bool_condition_one is False
                and bool_condition_two is False
            ):
                message = RequiredBox(f"The Additional Condition {description} is checked, but "
                                      f"the details of the {description} have not been selected. "
                                      f"Click the Add Conditions button to add details, or uncheck the "
                                      f"{description} box if there is no {description} in this case.")
                message.exec()
                return "Fail"
        return "Pass"

    @classmethod
    def check_jail_days(cls, dialog):
        if dialog.entry_case_information.diversion.ordered is True:
            return "Pass"
        if dialog.entry_case_information.community_control.driver_intervention_program is True:
            return "Pass"
        if dialog.dialog_name != 'Jail CC Plea Dialog':
            return "Pass"
        InfoChecker.check_jail_time_credit_fields(dialog)
        total_jail_days = 0
        total_jail_days_suspended = 0
        if dialog.entry_case_information.days_in_jail == "":
            total_jail_days_credit = 0
        else:
            total_jail_days_credit = int(dialog.entry_case_information.days_in_jail)
        for charge in dialog.entry_case_information.charges_list:
            try:
                if charge.jail_days == 'None':
                    charge.jail_days = 0
            except ValueError:
                charge.jail_days = 0
            try:
                if charge.jail_days_suspended == 'None':
                    charge.jail_days_suspended = 0
            except ValueError:
                charge.jail_days_suspended = 0
            try:
                total_jail_days += int(charge.jail_days)
            except ValueError:
                pass
            try:
                total_jail_days_suspended += int(charge.jail_days_suspended)
            except ValueError:
                pass
        if total_jail_days_suspended > total_jail_days:
            message = RequiredBox(
                f"The total number of jail days suspended is {total_jail_days_suspended} which is "
                f"greater than the total jail days imposed of {total_jail_days}. Please correct.")
            message.exec()
            return "Fail"
        if (
            total_jail_days > (total_jail_days_suspended + total_jail_days_credit)
            and dialog.entry_case_information.jail_terms.ordered is False
            and (dialog.entry_case_information.currently_in_jail == 'No' or dialog.entry_case_information.currently_in_jail == '')
        ):
            message = JailWarningBox(
                f"The total jail days imposed of {total_jail_days} is greater than the total "
                f"jail days suspended of {total_jail_days_suspended} and the total jail time credit applied "
                f"to the sentence of {total_jail_days_credit}, and the Jail Reporting Terms "
                f"have not been entered. \n\nDo you want to set the Jail Reporting Terms? \n\n"
                f"Press 'Yes' to set Jail Reporting Terms. \n\nPress 'No' to open the entry with no "
                f"Jail Reporting Terms. \n\nPress 'Cancel' to return to the Dialog without opening an "
                f"entry so that you can change the number of jail days imposed/suspended/credited.")
            return_value = message.exec()
            if return_value == QMessageBox.No:
                return "Pass"
            elif return_value == QMessageBox.Yes:
                dialog.jail_checkBox.setChecked(True)
                dialog.start_jail_only_dialog()
            elif return_value == QMessageBox.Cancel:
                return "Fail"
        if (
                total_jail_days > (total_jail_days_suspended + total_jail_days_credit)
                and dialog.entry_case_information.jail_terms.ordered is True
                and dialog.entry_case_information.currently_in_jail == 'Yes'
        ):
            message = WarningBox(f"The Defendant is currently indicated as being in jail, "
                                 f"but you set Jail Reporting Terms. \n\nAre you sure you want "
                                 f"to set Jail Reporting Terms?")
            return_value = message.exec()
            if return_value == QMessageBox.No:
                dialog.jail_checkBox.setChecked(False)
                return "Pass"
            elif return_value == QMessageBox.Yes:
                return "Pass"
        return "Pass"

    @classmethod
    def check_jail_time_credit_fields(cls, dialog):
        if dialog.entry_case_information.currently_in_jail == 'Yes':

            if dialog.entry_case_information.days_in_jail == '':
                message = RequiredBox(f"The Jail Time Credit box indicates Defendant is in Jail, but "
                                      f"the number of Days In Jail is blank. \n\nPlease enter the number of "
                                      f"Days In Jail and select whether to apply Jail Time Credit to "
                                      f"Sentence or Costs and Fines.")
                message.exec()
                return "Fail"

            elif dialog.entry_case_information.apply_jtc == '':
                message = TwoChoiceQuestionBox(
                    f"The Days in Jail has been provided, but the Apply to JTC field is blank. "
                    f"\n\nPlease select whether to apply Jail Time Credit to Sentence or Costs and Fines.",
                    "Sentence",
                    "Costs and Fines"
                )
                return_value = message.exec()
                if return_value == QMessageBox.Yes:
                    dialog.jail_time_credit_apply_box.setCurrentText("Sentence")
                elif return_value == QMessageBox.Yes:
                    dialog.jail_time_credit_apply_box.setCurrentText("Costs and Fines")

        elif dialog.entry_case_information.days_in_jail != '':

            if dialog.entry_case_information.currently_in_jail == '':
                message = WarningBox(f"The Days in Jail has been provided, but the Jail Time Credit "
                                     f"does not indicate whether the Defendant is Currently In Jail. "
                                     f"\n\nIs the Defendant currently in jail?")
                return_value = message.exec()
                print(f"Currently in jail return value is: {return_value}")
                if return_value == QMessageBox.No:
                    dialog.in_jail_box.setCurrentText("No")
                elif return_value == QMessageBox.Yes:
                    dialog.in_jail_box.setCurrentText("Yes")

            if dialog.entry_case_information.apply_jtc == '':
                message = TwoChoiceQuestionBox(
                    f"The Days in Jail has been provided, but the Apply to JTC field is blank. "
                    f"\n\nPlease select whether to apply Jail Time Credit to Sentence or Costs and Fines.",
                    "Sentence",
                    "Costs and Fines"
                )
                return_value = message.exec()  # Sentence (YesRole) returns 0, Costs and Fines (NoRole) returns 1
                if return_value == 0:
                    dialog.jail_time_credit_apply_box.setCurrentText("Sentence")
                elif return_value == 1:
                    dialog.jail_time_credit_apply_box.setCurrentText("Costs and Fines")
