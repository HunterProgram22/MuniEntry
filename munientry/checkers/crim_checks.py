"""Checks for Criminal Traffic Dialogs."""
from loguru import logger

from munientry.checkers.base_checks import BaseChecks, RequiredCheck, RequiredConditionCheck, WarningCheck
from munientry.checkers.check_messages import (
    DEF_COUNSEL_MSG,
    DEF_COUNSEL_TITLE,
    DIVERSION_SET_MSG,
    DIVERSION_SET_TITLE,
    LEAP_PAST_MSG,
    LEAP_PAST_TITLE,
    PLEA_PAST_MSG,
    PLEA_PAST_TITLE,
)
from munientry.settings.pyqt_constants import YES_BUTTON_RESPONSE, NO_BUTTON_RESPONSE, \
    CANCEL_BUTTON_RESPONSE
from munientry.widgets.message_boxes import RequiredBox, FAIL, PASS, WarningBox, BLANK, \
    JailWarningBox, TwoChoiceQuestionBox

NO_BOND_AMOUNT_TYPES = ('Recognizance (OR) Bond', 'Continue Existing Bond', 'No Bond')
YES = 'Yes'


class CrimBaseChecks(BaseChecks):
    """Base class for all Criminal Traffic checks."""

    conditions_list: list = []

    @RequiredCheck(PLEA_PAST_TITLE, PLEA_PAST_MSG)
    def check_plea_date(self) -> bool:
        """Returns False (Fails check) if plea date is not set in the past."""
        return self.dialog.plea_date.date() < self.today

    @RequiredCheck(LEAP_PAST_TITLE, LEAP_PAST_MSG)
    def check_leap_plea_date(self) -> bool:
        """Returns False (Fails check) if LEAP plea date is not set in the past."""
        return self.dialog.leap_plea_date.date() < self.today

    @RequiredCheck(DIVERSION_SET_TITLE, DIVERSION_SET_MSG)
    def check_if_diversion_program_selected(self) -> bool:
        diversion_radio_btns = [
            self.dialog.marijuana_diversion_radio_btn,
            self.dialog.theft_diversion_radio_btn,
            self.dialog.other_diversion_radio_btn,
        ]
        return any(btn.isChecked() for btn in diversion_radio_btns)

    def check_additional_conditions_ordered(self) -> str:
        """Hard stops if an additional condition checkbox is checked, but certain data is None.

        This checks to see if the primary condition of an additional condition is set to something
        other than None or Empty. If so the check passes.

        The conditions_list for each dialog provides a tuple of (condition, the primary condition
        that is checked, the formal name of the Condition).
        """
        for condition in self.conditions_list:
            condition_model, primary_condition, condition_name = self._get_condition_info(condition)
            if condition_model.ordered in (False, None):
                continue
            check_status = self.check_primary_condition(primary_condition, condition_name)
            if check_status == False:
                return False
        return PASS

    def _get_condition_info(self, condition_item: tuple[str, str, str]) -> tuple[str, str, str]:
        """The CheckList class for certain classes has conditions_list tuples that are returned.

        The tuple that is returned contains a string model name, the primary condition that is set
        in a model, and the standard name (i.e. 'License Suspension') for the model.
        """
        condition_model = getattr(self.dialog.entry_case_information, condition_item[0])
        primary_condition = getattr(condition_model, condition_item[1])
        condition_name = condition_item[2]
        return condition_model, primary_condition, condition_name

    @RequiredConditionCheck
    def check_primary_condition(self, primary_condition, condition_name) -> bool:
        return primary_condition not in (None, '')


class DefenseCounselChecks(CrimBaseChecks):
    """Class containing checks for defense counsel."""

    @WarningCheck(DEF_COUNSEL_TITLE, DEF_COUNSEL_MSG)
    def check_defense_counsel(self, msg_response=None) -> str:
        if self.dialog.defense_counsel_name_box.currentText().strip() != '':
            if msg_response == YES_BUTTON_RESPONSE:
                self.dialog.defense_counsel_waived_checkBox.setChecked(True)
            return False
        return False
        # if self.dialog.defense_counsel_name_box.currentText().strip() == '':
        #     if msg_response == YES_BUTTON_RESPONSE:
        #         self.dialog.defense_counsel_waived_checkBox.setChecked(True)
        #         return PASS
        #     elif msg_response == NO_BUTTON_RESPONSE:
        #         self.dialog.defense_counsel_waived_checkBox.setChecked(False)
        #         return FAIL
        #     else:
        #         return FAIL
        # return PASS

    # def set_defense_counsel_waived_or_fail_check(self, message_response) -> str:
    #     if message_response == YES_BUTTON_RESPONSE:
    #     return FAIL


class InsuranceChecks(DefenseCounselChecks):
    """Class containing checks for Insurance."""

    def check_insurance(self) -> str:
        if 'TRC' in self.dialog.case_number_lineEdit.text():
            return self.insurance_check_message()
        if 'TRD' in self.dialog.case_number_lineEdit.text():
            return self.insurance_check_message()
        return PASS

    def insurance_check_message(self) -> str:
        if self.dialog.fra_in_file_box.currentText() == 'Yes':
            return PASS
        if self.dialog.fra_in_court_box.currentText() == 'N/A':
            message = (
                'The information provided currently indicates insurance was not shown in the'
                + ' file.\n\nDid the defendant show proof of insurance in court?'
            )
            msg_response = WarningBox(message, 'Insurance Shown Warning').exec()
            return self.set_fra_in_court_box(msg_response)
        return PASS

    def set_fra_in_court_box(self, message_response) -> str:
        if message_response == NO_BUTTON_RESPONSE:
            self.dialog.fra_in_court_box.setCurrentText('No')
        if message_response == YES_BUTTON_RESPONSE:
            self.dialog.fra_in_court_box.setCurrentText('Yes')
        return PASS


class BondChecks(DefenseCounselChecks):
    """Class that checks dialog to make sure the appropriate bond information is entered."""

    def check_if_no_bond_amount(self) -> str:
        bond_type = self.dialog.bond_type_box.currentText()
        if bond_type in NO_BOND_AMOUNT_TYPES:
            return PASS
        if self.dialog.bond_amount_box.currentText() == 'None':
            message = (
                f'The bond type of {bond_type} requires a bond amount. \n\nPlease specify a bond'
                + ' amount other than None.'
            )
            RequiredBox(message, 'Bond Amount Required').exec()
            return FAIL
        return PASS

    def check_if_improper_bond_type(self) -> str:
        bond_type = self.dialog.bond_type_box.currentText()
        if bond_type in NO_BOND_AMOUNT_TYPES:
            if self.dialog.bond_amount_box.currentText() != 'None':
                message = (
                    f'{bond_type} was selected but a bond amount other than None was chosen.'
                    + '\n\nPlease either change the bond type to 10% Deposit Bond,'
                    + ' or a Cash or Surety Bond, or set the bond amount to None.'
                )
                RequiredBox(message, 'Proper Bond Type Required').exec()
                return FAIL
        return PASS

    def check_if_no_bond_modification_decision(self) -> str:
        if self.dialog.bond_modification_decision_box.currentText() == BLANK:
            message = (
                'A decision on bond modification was not selected.'
                + '\n\nPlease choose an option from the Decison on Bond box.'
            )
            RequiredBox(message, 'Bond Modification Decision Required').exec()
            return FAIL
        return PASS

    def check_domestic_violence_bond_condition(self) -> str:
        dv_conditions = self.dialog.entry_case_information.domestic_violence_conditions
        if dv_conditions.ordered is True:
            if dv_conditions.vacate_residence is False:
                if dv_conditions.surrender_weapons is False:
                    message = (
                        'The Special Condition Domestic Violence Restrictions is checked, but'
                        + ' the details of the Domestic Violence Restrictions have not been'
                        + ' selected.\n\nClick the Add Conditions button to add details, or'
                        + ' uncheck the Domestic Violence Restrictions box if there is no'
                        + ' restrictions in this case.'
                    )
                    RequiredBox(message, 'Domestic Violence Data Required').exec()
                    return FAIL
        return PASS


class ChargeGridChecks(InsuranceChecks):
    """Class that checks dialog to make sure the appropriate information is entered."""

    def __init__(self, dialog):
        self.grid = dialog.charges_gridLayout
        super().__init__(dialog)

    def check_if_no_plea_entered(self) -> str:
        """Hard stops the create entry process for any charge that does not have a plea.

        The column (col) starts at 2 to skip label row and increments by 2 because PyQt adds 2
        columns when adding a charge.Try/Except addresses the issue of PyQt not actually deleting a
        column from a grid_layout when it is deleted, it actually just hides the column.

        Try/Except is used instead of an If None check because by setting the col to 2 and
        incrementing by 2, the error is only raised and addressed if charges are added or deleted,
        which is a low occurrence event.
        """
        col = 2
        while col < self.grid.columnCount():
            try:
                offense = self.grid.itemAtPosition(self.grid.row_offense, col).widget().text()
            except AttributeError as error:
                logger.warning(error)
                col += 1
                continue
            plea = self.grid.itemAtPosition(self.grid.row_plea, col).widget().currentText()
            if plea == 'Dismissed':
                col += 2
                continue
            if plea == '':
                message = f'You must enter a plea for {offense}.'
                RequiredBox(message, 'Plea Required').exec()
                return FAIL
            col += 2
        return PASS

    def check_if_no_finding_entered(self) -> str:
        """Hard stops the create entry process for any charge that does not have a finding.

        The column (col) starts at 2 to skip label row and increments by 2 because PyQt adds 2
        columns when adding a charge.Try/Except addresses the issue of PyQt not actually deleting a
        column from a grid_layout when it is deleted, it actually just hides the column.

        Try/Except is used instead of an If None check because by setting the col to 2 and
        incrementing by 2, the error is only raised and addressed if charges are added or deleted,
        which is a low occurrence event.
        """
        col = 2
        while col < self.dialog.charges_gridLayout.columnCount():
            try:
                offense = self.grid.itemAtPosition(self.grid.row_offense, col).widget().text()
            except AttributeError as error:
                logger.warning(error)
                col += 1
                continue
            plea = self.grid.itemAtPosition(self.grid.row_plea, col).widget().currentText()
            finding = self.grid.itemAtPosition(self.grid.row_finding, col).widget().currentText()
            if plea == 'Dismissed':
                col += 2
                continue
            if finding == '':
                message = f'You must enter a finding for {offense}.'
                RequiredBox(message, 'Finding Required').exec()
                return FAIL
            col += 2
        return PASS

    def check_if_jail_suspended_more_than_imposed(self) -> str:
        if self.jail_days_suspended > self.jail_days_imposed:
            message = (
                f'The total number of jail days suspended is {self.jail_days_suspended} which is'
                + f' greater than the total jail days imposed of {self.jail_days_imposed}.'
                + '\n\nPlease correct.'
            )
            RequiredBox(message, 'Suspended Jail Days Exceeds Days Imposed').exec()
            return FAIL
        return PASS

    def check_if_jail_reporting_required(self) -> str:
        """Checks to see if the jails days imposed is greater than jail days suspended and credit.

        If jails days imposed exceed suspended days and credit days triggers ask users if they
        want to set the jail reporting terms.

        If the Driver Intervention Program is imposed then the check is skipped because no jail
        reporting is required.
        """
        if self.model.community_control.driver_intervention_program is True:
            return PASS
        if self.model.jail_terms.ordered is True:
            return PASS
        if self.model.jail_terms.currently_in_jail == YES:
            return PASS
        if self.jail_days_imposed > (self.jail_days_suspended + self.jail_credit):
            message = (
                f'The total jail days imposed of {self.jail_days_imposed} is greater than the total'
                + f' jail days suspended of {self.jail_days_suspended} and the total jail time'
                + f' credit applied to the sentence of {self.jail_credit}, and the Jail'
                + ' Reporting Terms have not been entered. \n\nDo you want to set the Jail'
                + ' Reporting Terms? \n\nPress Yes to set Jail Reporting Terms. \n\nPress No to'
                + ' open the entry with no Jail Reporting Terms. \n\nPress Cancel to return to the'
                + ' Dialog without opening an entry so that you can change the number of jail days'
                + ' imposed/suspended/credited.'
            )
            return self.add_jail_report_terms(JailWarningBox(message, 'Add Jail Reporting').exec())
        return PASS

    def add_jail_report_terms(self, message_response) -> str:
        if message_response == NO_BUTTON_RESPONSE:
            return PASS
        if message_response == YES_BUTTON_RESPONSE:
            self.dialog.jail_checkBox.setChecked(True)
            self.dialog.functions.start_add_jail_report_dialog()
            return PASS
        if message_response == CANCEL_BUTTON_RESPONSE:
            return FAIL
        return PASS

    def check_if_jail_equals_suspended_and_imposed(self) -> str:
        """Checks if jail reporting is set when no jail days remaining to serve."""
        if self.model.jail_terms.ordered is False:
            return PASS
        if self.jail_days_imposed == (self.jail_days_suspended + self.jail_credit):
            if self.model.jail_terms.currently_in_jail != YES:
                message = (
                    f'The total jail days imposed of {self.jail_days_imposed} is equal to the total'
                    + f' jail days suspended of {self.jail_days_suspended} and total jail time'
                    + f' credit of {self.jail_credit}. The Defendant does not appear to have any'
                    + ' jail days left to serve but you set Jail Reporting Terms. \n\nAre you sure'
                    + ' you want to set Jail Reporting Terms?'
                )
                return self.unset_jail_reporting(WarningBox(message, 'Unset Jail Reporting').exec())
        return PASS

    def unset_jail_reporting(self, message_response) -> str:
        if message_response == NO_BUTTON_RESPONSE:
            self.dialog.jail_checkBox.setChecked(False)
            return PASS
        if message_response == YES_BUTTON_RESPONSE:
            return PASS
        return PASS

    def check_if_in_jail_and_reporting_set(self) -> str:
        if self.model.jail_terms.ordered is False:
            return PASS
        if self.model.jail_terms.currently_in_jail != YES:
            return PASS
        if self.jail_days_imposed >= (self.jail_days_suspended + self.jail_credit):
            message = (
                'The Defendant is currently indicated as being in jail, but you set Jail'
                + ' Reporting Terms.\n\nAre you sure you want to set Jail Reporting Terms?'
            )
            return self.unset_jail_reporting(WarningBox(message, 'In Jail Reporting Set').exec())
        return PASS


class JailTimeChecks(ChargeGridChecks):
    """Class with checks for the Jail Time Credit Box on Dialogs with jail options."""

    def __init__(self, dialog) -> None:
        self.model = dialog.entry_case_information
        self.jail_days_imposed = self.model.jail_terms.total_jail_days_imposed
        self.jail_days_suspended = self.model.jail_terms.total_jail_days_suspended
        self.jail_credit = self.model.jail_terms.days_in_jail
        super().__init__(dialog)

    def check_if_days_in_jail_blank_but_in_jail(self) -> str:
        """Requires user to enter data in Days in Jail field if Currently in Jail is Yes."""
        if self.dialog.in_jail_box.currentText() == YES:
            if self.dialog.jail_time_credit_box.text() == BLANK:
                message = (
                    'The Jail Time Credit box indicates Defendant is in Jail, but'
                    + ' the number of Days In Jail is blank. \n\nPlease enter the number of'
                    + ' Days In Jail and choose whether to apply Jail Time Credit to'
                    + ' Sentence or Costs and Fines.'
                )
                RequiredBox(message, 'Days in Jail Required').exec()
                return FAIL
            return PASS
        return PASS

    def check_if_in_jail_blank_but_has_jail_days(self) -> str:
        """Asks user to choose if defendant is in jail if days in jail has data."""
        if self.dialog.jail_time_credit_box.text() != BLANK:
            if self.dialog.in_jail_box.currentText() == BLANK:
                message = (
                    'The Days in Jail has been provided, but the Jail Time Credit'
                    + ' does not indicate whether the Defendant is Currently In Jail.'
                    + '\n\nIs the Defendant currently in jail?'
                )
                return self.set_in_jail_box(WarningBox(message, 'Is Defendant in Jail').exec())
        return PASS

    def set_in_jail_box(self, message_response) -> str:
        if message_response == NO_BUTTON_RESPONSE:
            self.dialog.in_jail_box.setCurrentText('No')
        elif message_response == YES_BUTTON_RESPONSE:
            self.dialog.in_jail_box.setCurrentText(YES)
        return PASS

    def check_if_apply_jail_credit_blank_but_in_jail(self) -> str:
        """Asks user to choose how to apply jail time credit if jail time credit is entered."""
        if self.dialog.jail_time_credit_box.text() != BLANK:
            if self.dialog.jail_time_credit_apply_box.currentText() == BLANK:
                message = (
                    'The Days in Jail has been provided, but the Apply to JTC field is blank.'
                    + '\n\nPlease choose whether to apply Jail Time Credit to Sentence or Costs'
                    + ' and Fines.'
                )
                return self.set_jtc_apply_box(
                    TwoChoiceQuestionBox(
                        message, 'Sentence', 'Costs and Fines', 'Apply Jail Time Credit',
                    ).exec(),
                )
        return PASS

    def set_jtc_apply_box(self, message_response) -> str:
        if message_response == 0:
            self.dialog.jail_time_credit_apply_box.setCurrentText('Sentence')
        elif message_response == 1:
            self.dialog.jail_time_credit_apply_box.setCurrentText('Costs and Fines')
        return PASS

    def check_if_jail_credit_more_than_imposed(self) -> str:
        """Checks to see if more jail time credit is given then jail time imposed."""
        if self.dialog.jail_time_credit_apply_box.currentText() == 'Sentence':
            if self.jail_credit > self.jail_days_imposed:
                message = (
                    f'The Defendant is set to have {self.jail_credit} days of'
                    + ' jail time credit applied to a sentence, but a total of only'
                    + f' {self.jail_days_imposed} are set to be imposed'
                    + ' in the case. The total jail day imposed is less than the jail time credit'
                    + ' that is being applied to the sentence. \n\nPlease impose additional jail'
                    + ' days or change the Apply JTC to box to Costs and Fines.'
                )
                RequiredBox(message, 'Excessive Jail Credit').exec()
                return FAIL
        return PASS
