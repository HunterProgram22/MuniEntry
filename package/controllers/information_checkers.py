"""Module that contains various data checks that are ran when a user creates an entry."""
from PyQt5.QtWidgets import QMessageBox
from package.views.custom_widgets import (
    WarningBox,
    RequiredBox,
    TwoChoiceQuestionBox,
    JailWarningBox,
)


# InfoChecker Wrappers
def check_judicial_officer(func):
    def wrapper(self):
        if self.judicial_officer is None:
            RequiredBox("You must select a judicial officer.").exec()
        else:
            func(self)

    return wrapper


def check_case_list_selected(func):
    def wrapper(self):
        if any(key.isChecked() for key in self.daily_case_list_buttons.keys()):
            func(self)
        else:
            RequiredBox(
                "You must select a case list to load. If loading a "
                "blank template choose any case list and leave dropdown menu blank."
            ).exec()

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
        if self.dialog.defense_counsel_name_box.currentText().strip() == "":
            message = WarningBox(
                f"There is no attorney listed. Did the Defendant appear without or waive his right "
                f"to counsel?\n\nIf you select 'No' you must enter a name for Defense Counsel."
            )
            return self.set_defense_counsel_waived_or_fail_check(message.exec())

    def set_defense_counsel_waived_or_fail_check(self, message_response):
        if message_response == QMessageBox.Yes:
            self.dialog.defense_counsel_waived_checkBox.setChecked(True)
            return "Pass"
        elif message_response == QMessageBox.No:
            return "Fail"

    def check_if_no_plea_entered(self):
        """The column (col) starts at 2 to skip label row and increments by 2 because PyQt adds 2
        columns when adding a charge.Try/Except addresses the issue of PyQt not actually deleting a
        column from a grid_layout when it is deleted, it actually just hides the column."""
        col = 2
        loop_counter = 0
        while loop_counter < self.dialog.charges_gridLayout.columnCount():
            try:
                offense = (
                    self.dialog.charges_gridLayout.itemAtPosition(
                        self.dialog.charges_gridLayout.row_offense, col
                    )
                    .widget()
                    .text()
                )
                plea = (
                    self.dialog.charges_gridLayout.itemAtPosition(
                        self.dialog.charges_gridLayout.row_plea, col
                    )
                    .widget()
                    .currentText()
                )
            except AttributeError:
                offense, plea = None, None
            if plea == "Dismissed":
                col += 2
                loop_counter += 1
                continue
            elif plea == "":
                RequiredBox(f"You must enter a plea for {offense}.").exec()
                return "Fail"
            col += 2
            loop_counter += 1
        return "Pass"

    def check_if_no_finding_entered(self):
        """The column (col) starts at 2 to skip label row and increments by 2 because PyQt adds 2
        columns when adding a charge.Try/Except addresses the issue of PyQt not actually deleting a
        column from a grid_layout when it is deleted, it actually just hides the column."""
        col = 2
        loop_counter = 0
        while loop_counter < self.dialog.charges_gridLayout.columnCount():
            try:
                offense = (
                    self.dialog.charges_gridLayout.itemAtPosition(
                        self.dialog.charges_gridLayout.row_offense, col
                    )
                    .widget()
                    .text()
                )
                plea = (
                    self.dialog.charges_gridLayout.itemAtPosition(
                        self.dialog.charges_gridLayout.row_plea, col
                    )
                    .widget()
                    .currentText()
                )
                finding = (
                    self.dialog.charges_gridLayout.itemAtPosition(
                        self.dialog.charges_gridLayout.row_finding, col
                    )
                    .widget()
                    .currentText()
                )
            except AttributeError:
                offense, plea, finding = None, None, None
            if plea == "Dismissed":
                col += 2
                loop_counter += 1
                continue
            elif finding == "":
                RequiredBox(f"You must enter a finding for {offense}.").exec()
                return "Fail"
            col += 2
            loop_counter += 1
        return "Pass"

    def check_insurance(self):
        if (
            self.dialog.fra_in_file_box.currentText() == "No"
            and self.dialog.fra_in_court_box.currentText() == "N/A"
        ):
            message = WarningBox(
                "The information provided currently "
                "indicates insurance was not shown in the file. "
                "\n\nDid the defendant show proof of insurance "
                "in court?"
            )
            return self.set_fra_in_court_box(message.exec())

    def set_fra_in_court_box(self, message_response):
        if message_response == QMessageBox.No:
            self.dialog.fra_in_court_box.setCurrentText("No")
            return "Pass"
        elif message_response == QMessageBox.Yes:
            self.dialog.fra_in_court_box.setCurrentText("Yes")
            return "Pass"

    def check_additional_conditions_ordered(self):
        for condition_item in self.conditions_list:
            condition = getattr(self.dialog.entry_case_information, condition_item[0])
            condition_ordered = getattr(condition, "ordered")
            main_condition_set = getattr(condition, condition_item[1])
            condition_name = condition_item[2]
            if condition_ordered is True and main_condition_set is None:
                message = RequiredBox(
                    f"The additional condition {condition_name} is checked, but "
                    f"the details of the {condition_name} have not been entered.\n\n"
                    f"Click the Add Conditions button to add details, or uncheck the "
                    f"{condition_name} box if there is no {condition_name} in this case."
                )
                message.exec()
                return "Fail"


class FineOnlyDialogInfoChecker(BaseInfoChecker):
    conditions_list = [
        ("license_suspension", "license_type", "License Suspension"),
        ("community_service", "hours_of_service", "Community Service"),
        ("other_conditions", "terms", "Other Conditions"),
    ]

    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog_check_list = [
            "check_defense_counsel",
            "check_if_no_plea_entered",
            "check_if_no_finding_entered",
            "check_insurance",
            "check_additional_conditions_ordered",
        ]
        self.check_status = self.perform_check_list()


class NotGuiltyBondDialogInfoChecker(BaseInfoChecker):
    conditions_list = [
        ("admin_license_suspension", "disposition", "Admin License Suspension"),
        ("vehicle_seizure", "vehicle_make_model", "Vehicle Seizure"),
        ("no_contact", "name", "No Contact"),
        ("custodial_supervision", "supervisor", "Custodial Supervision"),
        ("other_conditions", "terms", "Other Conditions"),
    ]

    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog_check_list = [
            "check_defense_counsel",
            "check_if_no_plea_entered",
            "check_if_no_bond_amount",
            "check_if_improper_bond_type",
            "check_additional_conditions_ordered",
            "check_domestic_violence_bond_condition",
        ]
        self.check_status = self.perform_check_list()

    def check_if_no_bond_amount(self):
        if (
            self.dialog.bond_type_box.currentText() != "Recognizance (OR) Bond"
            and self.dialog.bond_amount_box.currentText() == "None (OR Bond)"
        ):
            message = (
                "A bond type requiring a bond amount was selected, but a bond amount was "
                "not selected. \n\nPlease specify the bond amount."
            )
            RequiredBox(message).exec()
            return "Fail"

    def check_if_improper_bond_type(self):
        if (
            self.dialog.bond_type_box.currentText() == "Recognizance (OR) Bond"
            and self.dialog.bond_amount_box.currentText() != "None (OR Bond)"
        ):
            message = (
                "A Recognizance (OR) Bond was selected but a bond amount other than "
                "None(OR Bond) was chosen. \n\nPlease either change bond type to 10% "
                "or Cash or Surety, or set bond amount to None (OR Bond)."
            )
            RequiredBox(message).exec()
            return "Fail"

    def check_domestic_violence_bond_condition(self):
        dv_bond_conditions_list = [
            (
                self.dialog.entry_case_information.domestic_violence_conditions.ordered,
                self.dialog.entry_case_information.domestic_violence_conditions.vacate_residence,
                self.dialog.entry_case_information.domestic_violence_conditions.surrender_weapons,
                "Domestic Violence Restrictions",
            ),
        ]
        for item in dv_bond_conditions_list:
            if item[0] is True and item[1] is False and item[2] is False:
                description = item[3]
                message = RequiredBox(
                    f"The Additional Condition {description} is checked, but "
                    f"the details of the {description} have not been selected. "
                    f"Click the Add Conditions button to add details, or uncheck the "
                    f"{description} box if there is no {description} in this case."
                )
                message.exec()
                return "Fail"


class DiversionDialogInfoChecker(BaseInfoChecker):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog_check_list = [
            "check_defense_counsel",
            "check_if_no_plea_entered",
            "check_if_no_finding_entered",
            "check_if_diversion_program_selected",
            "check_insurance",
        ]
        self.check_status = self.perform_check_list()

    def check_if_diversion_program_selected(self):
        diversion_program_list = [
            "marijuana_diversion",
            "theft_diversion",
            "other_diversion",
        ]
        for program in diversion_program_list:
            if (
                getattr(
                    self.dialog.entry_case_information.diversion,
                    program,
                )
                is True
            ):
                return "Pass"
        message = RequiredBox(
            f"No Diversion Program was selected. \n\n" f"Please select a Diversion Program."
        )
        message.exec()
        return "Fail"


class JailCCPleaDialogInfoChecker(BaseInfoChecker):
    conditions_list = [
        ("license_suspension", "license_type", "License Suspension"),
        ("community_service", "hours_of_service", "Community Service"),
        ("other_conditions", "terms", "Other Conditions"),
        ("community_control", "term_of_control", "Community Control"),
        ("impoundment", "vehicle_make_model", "Immobilize/Impound"),
    ]

    def __init__(self, dialog):
        super().__init__(dialog)
        # self.total_jail_days = self.calculate_total_jail_days()
        # self.total_jail_days_suspended = self.calculate_total_jail_days_suspended()
        # self.total_jail_days_credit = self.calculate_jail_days_credit()
        self.case_info = self.dialog.entry_case_information
        self.dialog_check_list = [
            "check_defense_counsel",
            "check_if_no_plea_entered",
            "check_if_no_finding_entered",
            "check_insurance",
            "check_additional_conditions_ordered",
            "check_dv_and_victim_notifications_ordered",
            "check_if_jail_days_suspended_greater_than_jail_imposed",
            "check_jail_time_credit_fields",
            "check_if_jail_days_imposed_greater_than_suspended_and_credit",
            "check_if_jail_days_equals_suspended_and_imposed_days",
            "check_if_jails_days_left_and_defendant_in_jail_and_reporting_ordered",
            "check_if_jtc_applied_to_sentence_is_greater_than_jail_imposed",
        ]
        self.check_status = self.perform_check_list()

    def check_dv_and_victim_notifications_ordered(self):
        pass

    def check_jail_time_credit_fields(self):
        """Generates warning messages if certain required jail time credit fields have data, but
        other required fields do not contain data. If currenlty in jail is no, but other days in
        jail is blank no warning is generated because a user may enter no for currently in jail,
        but there may not be jail time credit."""
        if self.case_info.currently_in_jail == "Yes":
            if self.check_if_days_in_jail_blank():
                return "Fail"
            self.check_if_apply_jtc_blank()
        elif self.case_info.days_in_jail != "":
            if self.case_info.days_in_jail == 0:
                return "Pass"
            self.check_if_currently_in_jail_blank()
            self.check_if_apply_jtc_blank()

    def check_if_days_in_jail_blank(self):
        if self.case_info.days_in_jail == "":
            message = RequiredBox(
                f"The Jail Time Credit box indicates Defendant is in Jail, but "
                f"the number of Days In Jail is blank. \n\nPlease enter the number of "
                f"Days In Jail and select whether to apply Jail Time Credit to "
                f"Sentence or Costs and Fines."
            )
            message.exec()
            return True
        return False

    def check_if_currently_in_jail_blank(self):
        if self.case_info.currently_in_jail == "":
            message = WarningBox(
                f"The Days in Jail has been provided, but the Jail Time Credit "
                f"does not indicate whether the Defendant is Currently In Jail. "
                f"\n\nIs the Defendant currently in jail?"
            )
            return self.set_in_jail_box(message.exec())

    def set_in_jail_box(self, message_response):
        if message_response == QMessageBox.No:
            self.dialog.in_jail_box.setCurrentText("No")
        elif message_response == QMessageBox.Yes:
            self.dialog.in_jail_box.setCurrentText("Yes")

    def check_if_apply_jtc_blank(self):
        if self.case_info.apply_jtc == "":
            message = TwoChoiceQuestionBox(
                f"The Days in Jail has been provided, but the Apply to JTC field is blank. "
                f"\n\nPlease select whether to apply Jail Time Credit to Sentence or Costs and "
                f"Fines.",
                "Sentence",
                "Costs and Fines",
            )
            return self.set_jtc_apply_box(message.exec())

    def set_jtc_apply_box(self, message_response):
        if message_response == 0:
            self.dialog.jail_time_credit_apply_box.setCurrentText("Sentence")
        elif message_response == 1:
            self.dialog.jail_time_credit_apply_box.setCurrentText("Costs and Fines")

    def calculate_jail_days_credit(self):
        if self.case_info.days_in_jail == "":
            return 0
        else:
            return int(self.case_info.days_in_jail)

    def check_if_jail_days_suspended_greater_than_jail_imposed(self):
        if self.case_info.total_jail_days_suspended > self.case_info.total_jail_days_imposed:
            message = RequiredBox(
                f"The total number of jail days suspended is {self.case_info.total_jail_days_suspended} "
                f"which is greater than the total jail days imposed of {self.case_info.total_jail_days_imposed}. "
                f"Please correct."
            )
            message.exec()
            return "Fail"
        return False

    def check_if_jail_days_imposed_greater_than_suspended_and_credit(self):
        if (
            self.case_info.total_jail_days_imposed > (self.case_info.total_jail_days_suspended + self.case_info.days_in_jail)
            and self.case_info.jail_terms.ordered is False
            and (
                self.case_info.currently_in_jail == "No"
                or self.case_info.currently_in_jail == ""
            )
            and self.case_info.community_control.driver_intervention_program
            is False
        ):
            message = JailWarningBox(
                f"The total jail days imposed of {self.case_info.total_jail_days_imposed} is greater than the total "
                f"jail days suspended of {self.case_info.total_jail_days_suspended} and the total jail time "
                f"credit applied to the sentence of {self.case_info.days_in_jail}, and the Jail "
                f"Reporting Terms have not been entered. \n\nDo you want to set the Jail "
                f"Reporting Terms? \n\nPress 'Yes' to set Jail Reporting Terms. \n\nPress 'No' to "
                f"open the entry with no Jail Reporting Terms. \n\nPress 'Cancel' to return to the "
                f"Dialog without opening an entry so that you can change the number of jail days "
                f"imposed/suspended/credited."
            )
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
            self.case_info.total_jail_days_imposed == (self.case_info.total_jail_days_suspended + self.case_info.days_in_jail)
            and self.case_info.jail_terms.ordered is True
            and (
                self.case_info.currently_in_jail == "No"
                or self.case_info.currently_in_jail == ""
            )
        ):
            message = WarningBox(
                f"The total jail days imposed of {self.case_info.total_jail_days_imposed} is equal to the total jail "
                f"days suspended of {self.case_info.total_jail_days_suspended} and total jail time credit of "
                f"{self.case_info.days_in_jail}. The Defendant does not appear to have any jail "
                f"days left to serve but you set Jail Reporting Terms. \n\nAre you sure you want "
                f"to set Jail Reporting Terms?"
            )
            return self.unset_jail_reporting_terms(message.exec())

    def unset_jail_reporting_terms(self, message_response):
        if message_response == QMessageBox.No:
            self.dialog.jail_checkBox.setChecked(False)
            return "Pass"
        elif message_response == QMessageBox.Yes:
            return "Pass"

    def check_if_jails_days_left_and_defendant_in_jail_and_reporting_ordered(self):
        if (
            self.case_info.total_jail_days_imposed >= (self.case_info.total_jail_days_suspended + self.case_info.days_in_jail)
            and self.case_info.jail_terms.ordered is True
            and self.case_info.currently_in_jail == "Yes"
        ):
            message = WarningBox(
                f"The Defendant is currently indicated as being in jail, "
                f"but you set Jail Reporting Terms. \n\nAre you sure you want "
                f"to set Jail Reporting Terms?"
            )
            return self.unset_jail_reporting_terms(message.exec())

    def check_if_jtc_applied_to_sentence_is_greater_than_jail_imposed(self):
        if (
            self.case_info.days_in_jail > self.case_info.total_jail_days_imposed
            and self.dialog.jail_time_credit_apply_box.currentText() == "Sentence"
        ):
            message = RequiredBox(
                f"The Defendant is set to have {self.case_info.days_in_jail} days of jail time "
                f"credit applied to a sentence, but a total of only {self.case_info.total_jail_days_imposed} are set "
                f"to be imposed in the case. The total jail day imposed is less than the jail time "
                f"credit that is being applied to the sentence. \n\nPlease impose additional jails "
                f"days or change the Apply JTC to box to 'Costs and Fines'."
            )
            message.exec()
            return "Fail"
