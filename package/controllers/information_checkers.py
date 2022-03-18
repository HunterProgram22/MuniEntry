from PyQt5.QtWidgets import QMessageBox
from package.views.custom_widgets import WarningBox, RequiredBox, TwoChoiceQuestionBox, JailWarningBox


# InfoChecker Wrappers
def check_judicial_officer(func):
    def wrapper(self):
        if self.judicial_officer is None:
            message = RequiredBox("You must select a judicial officer.")
            message.exec()
        else:
            func(self)
    return wrapper


def check_case_list_selected(func):
    def wrapper(self):
        if any(key.isChecked() for key in self.daily_case_list_buttons.keys()):
            func(self)
        else:
            message = RequiredBox("You must select a case list to load. If loading a "
                                  "blank template choose any case list and leave dropdown menu blank.")
            message.exec()
    return wrapper


class BaseInfoChecker(object):
    """Class that checks dialog to make sure the appropriate information is entered."""
    def __init__(self, dialog):
        self.dialog = dialog

    def perform_check_list(self):
        for item in self.dialog_check_list:
            if getattr(self, item)() == "Fail":
                return "Fail"

    def check_defense_counsel(self):
        if self.dialog.defense_counsel_waived_checkBox.isChecked():
            return "Pass"
        elif self.dialog.defense_counsel_name_box.currentText().strip() == "":
            message = WarningBox("There is no attorney listed. Did "
                                 "the Defendant waive his right to counsel?"
                                 "\n\nIf you select 'No' you must enter a name "
                                 "for Def. Counsel.")
            message_response = message.exec()
            if message_response == QMessageBox.Yes:
                self.dialog.defense_counsel_waived_checkBox.setChecked(True)
                return "Pass"
            elif message_response == QMessageBox.No:
                return "Fail"

    def check_plea_and_findings(self):
        """Shows warning if no plea or findings are entered. Checks one at a time so unless all
        fields have a plea and finding you will get the warning until they are filled in."""
        row_plea, row_finding = self.dialog.charges_gridLayout.set_plea_and_finding_rows()
        column = 2
        loop_counter = 0
        while loop_counter < self.dialog.charges_gridLayout.columnCount():
            try:
                offense = self.dialog.charges_gridLayout.itemAtPosition(0, column).widget().text()
                if self.dialog.charges_gridLayout.itemAtPosition(row_plea, column).widget().currentText() == "Dismissed":
                    column += 2
                    loop_counter += 1
                    continue
                elif self.dialog.charges_gridLayout.itemAtPosition(row_plea, column).widget().currentText() == "":
                    message = RequiredBox(f"You must enter a plea for {offense}.")
                    message.exec()
                    return "Fail"
                elif self.dialog.charges_gridLayout.itemAtPosition(row_finding, column).widget().currentText() == "":
                    message = RequiredBox(f"You must enter a finding for {offense}.")
                    message.exec()
                    return "Fail"
            except AttributeError:
                pass
            column += 2
            loop_counter += 1
        return "Pass"

    def check_insurance(self):
        if (self.dialog.fra_in_file_box.currentText() == "No"
            and self.dialog.fra_in_court_box.currentText() == "N/A"
        ):
            message = WarningBox("The information provided currently "
                                 "indicates insurance was not shown in the file. "
                                 "\n\nDid the defendant show proof of insurance in court?")
            return self.set_fra_in_court_box(message.exec())

    def set_fra_in_court_box(self, message_response):
        if message_response == QMessageBox.No:
            self.dialog.fra_in_court_box.setCurrentText("No")
            return "Pass"
        elif message_response == QMessageBox.Yes:
            self.dialog.fra_in_court_box.setCurrentText("Yes")
            return "Pass"

    def check_additional_conditions_ordered(self):
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
            # Domestic Violence Special Bond Condition needs to be added - but conditions don't work for method
        ]
        for condition_item in conditions_list:
            # Because dialog.entry_case_information is a model with all case conditions there is
            # apparently no need to check if it has that attribute (hasattr).
            condition = getattr(self.dialog.entry_case_information, condition_item[0])
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
        """The bond_conditions_list for Victim Notification and Domestic Violence is used because of two checkboxes as only options, no 
        ordered option like other conditions. TODO: figure out way to make it part of standard conditions list."""
        bool_conditions_list = [
            # Refactored out because added third notifcation condition for DV and 18 USC gun prohibitions - TODO: Fix
            # (dialog.entry_case_information.victim_notification.ordered,
            #  dialog.entry_case_information.victim_notification.victim_reparation_notice,
            #  dialog.entry_case_information.victim_notification.victim_prosecutor_notice,
            #  "Victim Notification"),
            (self.dialog.entry_case_information.domestic_violence_conditions.ordered,
             self.dialog.entry_case_information.domestic_violence_conditions.vacate_residence,
             self.dialog.entry_case_information.domestic_violence_conditions.surrender_weapons,
             "Domestic Violence Restrictions"),
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


class FineOnlyDialogInfoChecker(BaseInfoChecker):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog_check_list = [
            "check_defense_counsel",
            "check_plea_and_findings",
            "check_insurance",
            "check_additional_conditions_ordered",
        ]
        self.check_status = self.perform_check_list()


class NotGuiltyBondDialogInfoChecker(BaseInfoChecker):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog_check_list = [
            "check_defense_counsel",
            "check_plea_and_findings",
            "check_if_no_bond_amount",
            "check_if_improper_bond_type",
            "check_additional_conditions_ordered",
        ]
        self.check_status = self.perform_check_list()

    def check_if_no_bond_amount(self):
        if (    self.dialog.bond_type_box.currentText() != 'Recognizance (OR) Bond'
                and self.dialog.bond_amount_box.currentText() == 'None (OR Bond)'
        ):
            message = RequiredBox("A bond type requiring a bond amount was selected, but a bond amount was "
                                  "not selected. \n\nPlease specify the bond amount.")
            message.exec()
            return "Fail"

    def check_if_improper_bond_type(self):
        if (    self.dialog.bond_type_box.currentText() == 'Recognizance (OR) Bond'
                and self.dialog.bond_amount_box.currentText() != 'None (OR Bond)'
        ):
            message = RequiredBox(
                "A Recognizance (OR) Bond was selected but a bond amount other than None(OR Bond) "
                "was chosen. \n\nPlease either change bond type to 10% or Cash or Surety, or set "
                "bond amount to None (OR Bond).")
            message.exec()
            return "Fail"


class DiversionDialogInfoChecker(BaseInfoChecker):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog_check_list = [
            "check_defense_counsel",
            "check_plea_and_findings",
            "check_if_diversion_program_selected",
        ]
        self.check_status = self.perform_check_list()

    def check_if_diversion_program_selected(self):
        diversion_program_list = [
            'marijuana_diversion',
            'theft_diversion',
            'other_diversion',
        ]
        for program in diversion_program_list:
            if getattr(self.dialog.entry_case_information.diversion, program) is True:
                return "Pass"
        message = RequiredBox(f"No Diversion Program was selected. \n\n"
                              f"Please select a Diversion Program.")
        message.exec()
        return "Fail"


class JailCCPleaDialogInfoChecker(BaseInfoChecker):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.total_jail_days = self.calculate_total_jail_days()
        self.total_jail_days_suspended = self.calculate_total_jail_days_suspended()
        self.total_jail_days_credit = self.calculate_jail_days_credit()
        self.dialog_check_list = [
            "check_defense_counsel",
            "check_plea_and_findings",
            "check_insurance",
            "check_additional_conditions_ordered",
            "check_if_jail_days_suspended_greater_than_jail_imposed",
            "check_jail_time_credit_fields",
            "check_if_jail_days_imposed_greater_than_suspended_and_credit",
            "check_if_jail_days_equals_suspended_and_imposed_days",
            "check_if_jails_days_left_and_defendant_in_jail_and_reporting_ordered",
            "check_if_jtc_applied_to_sentence_is_greater_than_jail_imposed",
        ]
        self.check_status = self.perform_check_list()

    def check_jail_time_credit_fields(self):
        """Generates warning messages if certain required jail time credit fields have data, but other required
        fields do not contain data. If currenlty in jail is no, but other days in jail is blank no warning is
        generated because a user may enter no for currently in jail, but there may not be jail time credit."""
        if self.dialog.entry_case_information.currently_in_jail == "Yes":
            if self.check_if_days_in_jail_blank():
                return "Fail"
            self.check_if_apply_jtc_blank()
        elif self.dialog.entry_case_information.days_in_jail != "":
            self.check_if_currently_in_jail_blank()
            self.check_if_apply_jtc_blank()

    def check_if_days_in_jail_blank(self):
        if self.dialog.entry_case_information.days_in_jail == "":
            message = RequiredBox(f"The Jail Time Credit box indicates Defendant is in Jail, but "
                                  f"the number of Days In Jail is blank. \n\nPlease enter the number of "
                                  f"Days In Jail and select whether to apply Jail Time Credit to "
                                  f"Sentence or Costs and Fines.")
            message.exec()
            return True
        return False

    def check_if_currently_in_jail_blank(self):
        if self.dialog.entry_case_information.currently_in_jail == '':
            message = WarningBox(f"The Days in Jail has been provided, but the Jail Time Credit "
                                 f"does not indicate whether the Defendant is Currently In Jail. "
                                 f"\n\nIs the Defendant currently in jail?")
            return self.set_in_jail_box(message.exec())

    def set_in_jail_box(self, message_response):
        if message_response == QMessageBox.No:
            self.dialog.in_jail_box.setCurrentText("No")
        elif message_response == QMessageBox.Yes:
            self.dialog.in_jail_box.setCurrentText("Yes")

    def check_if_apply_jtc_blank(self):
        if self.dialog.entry_case_information.apply_jtc == '':
            message = TwoChoiceQuestionBox(
                f"The Days in Jail has been provided, but the Apply to JTC field is blank. "
                f"\n\nPlease select whether to apply Jail Time Credit to Sentence or Costs and Fines.",
                "Sentence",
                "Costs and Fines"
            )
            return self.set_jtc_apply_box(message.exec())

    def set_jtc_apply_box(self, message_response):
        if message_response == 0:
            self.dialog.jail_time_credit_apply_box.setCurrentText("Sentence")
        elif message_response == 1:
            self.dialog.jail_time_credit_apply_box.setCurrentText("Costs and Fines")

    def calculate_jail_days_credit(self):
        if self.dialog.entry_case_information.days_in_jail.strip() == "":
            return 0
        else:
            return int(self.dialog.entry_case_information.days_in_jail)

    def calculate_total_jail_days(self):
        self.total_jail_days = 0
        for charge in self.dialog.entry_case_information.charges_list:
            try:
                self.total_jail_days += int(charge.jail_days)
            except ValueError:
                pass
        return self.total_jail_days

    def calculate_total_jail_days_suspended(self):
        self.total_jail_days_suspended = 0
        for charge in self.dialog.entry_case_information.charges_list:
            try:
                self.total_jail_days_suspended += int(charge.jail_days_suspended)
            except ValueError:
                pass
        return self.total_jail_days_suspended

    def check_if_jail_days_suspended_greater_than_jail_imposed(self):
        if self.total_jail_days_suspended > self.total_jail_days:
            message = RequiredBox(
                f"The total number of jail days suspended is {self.total_jail_days_suspended} which is "
                f"greater than the total jail days imposed of {self.total_jail_days}. Please correct.")
            message.exec()
            return "Fail"
        return False

    def check_if_jail_days_imposed_greater_than_suspended_and_credit(self):
        if (
                self.total_jail_days > (self.total_jail_days_suspended + self.total_jail_days_credit)
                and self.dialog.entry_case_information.jail_terms.ordered is False
                and
                (
                self.dialog.entry_case_information.currently_in_jail == 'No'
                or self.dialog.entry_case_information.currently_in_jail == ''
                )
                and self.dialog.entry_case_information.community_control.driver_intervention_program is False
        ):
            message = JailWarningBox(
                f"The total jail days imposed of {self.total_jail_days} is greater than the total "
                f"jail days suspended of {self.total_jail_days_suspended} and the total jail time credit applied "
                f"to the sentence of {self.total_jail_days_credit}, and the Jail Reporting Terms "
                f"have not been entered. \n\nDo you want to set the Jail Reporting Terms? \n\n"
                f"Press 'Yes' to set Jail Reporting Terms. \n\nPress 'No' to open the entry with no "
                f"Jail Reporting Terms. \n\nPress 'Cancel' to return to the Dialog without opening an "
                f"entry so that you can change the number of jail days imposed/suspended/credited.")
            return self.add_jail_reporting_terms(message.exec())

    def add_jail_reporting_terms(self, message_response):
        if message_response == QMessageBox.No:
            return "Pass"
        elif message_response == QMessageBox.Yes:
            self.dialog.jail_checkBox.setChecked(True)
            self.dialog.start_jail_only_dialog()
            return "Pass"
        elif message_response == QMessageBox.Cancel:
            return "Fail"

    def check_if_jail_days_equals_suspended_and_imposed_days(self):
        if (
                self.total_jail_days == (self.total_jail_days_suspended + self.total_jail_days_credit)
                and self.dialog.entry_case_information.jail_terms.ordered is True
                and (self.dialog.entry_case_information.currently_in_jail == "No" or self.dialog.entry_case_information.currently_in_jail == "")
        ):
            message = WarningBox(f"The total jail days imposed of {self.total_jail_days} is equal to the total jail days "
                                 f"suspended of {self.total_jail_days_suspended} and total jail time credit of "
                                 f"{self.total_jail_days_credit}. The Defendant does not appear to have any jail days left "
                                 f"to serve but you set Jail Reporting Terms. \n\nAre you sure you want to set "
                                 f"Jail Reporting Terms?")
            return self.unset_jail_reporting_terms(message.exec())

    def unset_jail_reporting_terms(self, message_response):
        if message_response == QMessageBox.No:
            self.dialog.jail_checkBox.setChecked(False)
            return "Pass"
        elif message_response == QMessageBox.Yes:
            return "Pass"

    def check_if_jails_days_left_and_defendant_in_jail_and_reporting_ordered(self):
        if (
                self.total_jail_days >= (self.total_jail_days_suspended + self.total_jail_days_credit)
                and self.dialog.entry_case_information.jail_terms.ordered is True
                and self.dialog.entry_case_information.currently_in_jail == 'Yes'
        ):
            message = WarningBox(f"The Defendant is currently indicated as being in jail, "
                                 f"but you set Jail Reporting Terms. \n\nAre you sure you want "
                                 f"to set Jail Reporting Terms?")
            return self.unset_jail_reporting_terms(message.exec())

    def check_if_jtc_applied_to_sentence_is_greater_than_jail_imposed(self):
        if (
            self.total_jail_days_credit > self.total_jail_days
            and self.dialog.jail_time_credit_apply_box.currentText() == "Sentence"
        ):
            message = RequiredBox(f"The Defendant is set to have {self.total_jail_days_credit} days of jail time "
                                  f"credit applied to a sentence, but a total of only {self.total_jail_days} are set "
                                  f"to be imposed in the case. The total jail day imposed is less than the jail time "
                                  f"credit that is being applied to the sentence. \n\nPlease impose additional jails "
                                  f"days or change the Apply JTC to box to 'Costs and Fines'.")
            message.exec()
            return "Fail"