"""Module containing common information checks used on multiple dialogs."""
from loguru import logger
from PyQt6.QtCore import QDate

from munientry.settings.pyqt_constants import (
    NO_BUTTON_RESPONSE,
    YES_BUTTON_RESPONSE,
)
from munientry.widgets.message_boxes import BLANK, FAIL, PASS, RequiredBox, WarningBox

NO_BOND_AMOUNT_TYPES = ('Recognizance (OR) Bond', 'Continue Existing Bond', 'No Bond')


class BaseChecker(object):
    """Class for initializing InfoChecker objects."""

    conditions_list = []

    def __init__(self, dialog) -> None:
        self.view = dialog
        self.dialog_check_list: list = []
        self.today = QDate.currentDate()

    def perform_check_list(self) -> str:
        for item_to_check in self.dialog_check_list:
            if getattr(self, item_to_check)() == FAIL:
                logger.checkfail(item_to_check)
                return FAIL
        return PASS

    def check_if_plea_date_is_today(self) -> str:
        if self.view.plea_date.date() == self.today:
            message = (
                'The Plea Date is Today, but must be a date prior to Today. Please enter'
                + ' a date in the Plea Date box prior to today.'
            )
            RequiredBox(message).exec()
            return FAIL
        return PASS

    def check_if_trial_date_is_today(self) -> str:
        """Scheduling date checker to make sure trial date is not set to today."""
        if self.view.trial_date.date() == self.today:
            message = (
                    'The Trial Date is Today, but must be a date in the future. Please enter'
                    + ' a date in the Trial Date box after today.'
            )
            RequiredBox(message).exec()
            return FAIL
        return PASS

    def check_if_final_pretrial_date_is_today(self) -> str:
        """Scheduling date checker to make sure final pretrial date is not set to today."""
        if self.view.jury_trial_only_no_radioButton.isChecked():
            if self.view.final_pretrial_dateEdit.date() == self.today:
                message = (
                        'The Final Pretrial Date is Today, but must be a date in the future. Please'
                        + ' enter a date in the Final Pretrial Date box after today.'
                )
                RequiredBox(message).exec()
                return FAIL
            return PASS
        return PASS

    def check_if_leap_plea_date_is_today(self) -> str:
        if self.view.leap_plea_date.date() == self.today:
            message = (
                'The Leap Plea Date is Today, but must be a date prior to Today. Please enter'
                + ' a date in the Leap Plea Date box prior to today.'
            )
            RequiredBox(message, 'LEAP Plea Date Before Today Required').exec()
            return FAIL
        return PASS

    def check_additional_conditions_ordered(self) -> str:
        """Hard stops if an additional condition checkbox is checked, but certain data is None.

        This checks to see if the primary condition of an additional condition is set to something
        other than None. If so the check passes. This only prevents checking a condition checkbox
        on the main dialog without opening the secondary dialog to add the conditions.

        Once the additional conditions dialog is opened, then the field that was being checked
        would be set to an empty string if no data is entered and this check would pass.

        The conditions_list for each dialog provides a tuple of (condition, the primary condition
        that is checked, the formal name of the Condition).
        """
        for condition_item in self.conditions_list:
            condition = getattr(self.view.entry_case_information, condition_item[0])
            main_condition_set = getattr(condition, condition_item[1])
            condition_name = condition_item[2]
            if condition.ordered is True and main_condition_set is None:
                message = (
                    f'The additional condition {condition_name} is checked, but the details of'
                    + f' the {condition_name} have not been entered.\n\nClick the Add Conditions'
                    + f' button to add details, or uncheck the {condition_name} box if there is'
                    + f' no {condition_name} in this case.'
                )
                RequiredBox(message, 'Additional Condition Info Required').exec()
                return FAIL
        return PASS


class DefenseCounselChecker(BaseChecker):
    """Class containing checks for defense counsel."""

    def check_defense_counsel(self) -> str:
        if self.view.defense_counsel_waived_checkBox.isChecked():
            return PASS
        if self.view.defense_counsel_name_box.currentText().strip() == '':
            message = (
                'There is no attorney selected for the Defendant.\n\nDid the Defendant'
                + ' appear without or waive his right to counsel?\n\nIf you select No you'
                + ' must enter a name for Defense Counsel.'
            )
            msg_response = WarningBox(message, 'Does Defendant Have Counsel').exec()
            return self.set_defense_counsel_waived_or_fail_check(msg_response)
        return PASS

    def set_defense_counsel_waived_or_fail_check(self, message_response) -> str:
        if message_response == YES_BUTTON_RESPONSE:
            self.view.defense_counsel_waived_checkBox.setChecked(True)
            return PASS
        return FAIL


class InsuranceInfoChecker(BaseChecker):
    """Class containing checks for Insurance."""

    def check_insurance(self) -> str:
        if 'TRC' in self.view.case_number_lineEdit.text():
            return self.insurance_check_message()
        if 'TRD' in self.view.case_number_lineEdit.text():
            return self.insurance_check_message()
        return PASS

    def insurance_check_message(self) -> str:
        if self.view.fra_in_file_box.currentText() == 'Yes':
            return PASS
        if self.view.fra_in_court_box.currentText() == 'N/A':
            message = (
                'The information provided currently indicates insurance was not shown in the'
                + ' file.\n\nDid the defendant show proof of insurance in court?'
            )
            msg_response = WarningBox(message, 'Insurance Shown Warning').exec()
            return self.set_fra_in_court_box(msg_response)
        return PASS

    def set_fra_in_court_box(self, message_response) -> str:
        if message_response == NO_BUTTON_RESPONSE:
            self.view.fra_in_court_box.setCurrentText('No')
        if message_response == YES_BUTTON_RESPONSE:
            self.view.fra_in_court_box.setCurrentText('Yes')
        return PASS


class BondInfoChecker(DefenseCounselChecker):
    """Class that checks dialog to make sure the appropriate bond information is entered."""

    def check_if_no_bond_amount(self) -> str:
        bond_type = self.view.bond_type_box.currentText()
        if bond_type in NO_BOND_AMOUNT_TYPES:
            return PASS
        if self.view.bond_amount_box.currentText() == 'None':
            message = (
                f'The bond type of {bond_type} requires a bond amount. \n\nPlease specify a bond'
                + ' amount other than None.'
            )
            RequiredBox(message, 'Bond Amount Required').exec()
            return FAIL
        return PASS

    def check_if_improper_bond_type(self) -> str:
        bond_type = self.view.bond_type_box.currentText()
        if bond_type in NO_BOND_AMOUNT_TYPES:
            if self.view.bond_amount_box.currentText() != 'None':
                message = (
                    f'{bond_type} was selected but a bond amount other than None was chosen.'
                    + '\n\nPlease either change the bond type to 10% Deposit Bond,'
                    + ' or a Cash or Surety Bond, or set the bond amount to None.'
                )
                RequiredBox(message, 'Proper Bond Type Required').exec()
                return FAIL
        return PASS

    def check_if_no_bond_modification_decision(self) -> str:
        if self.view.bond_modification_decision_box.currentText() == BLANK:
            message = (
                'A decision on bond modification was not selected.'
                + '\n\nPlease choose an option from the Decison on Bond box.'
            )
            RequiredBox(message, 'Bond Modification Decision Required').exec()
            return FAIL
        return PASS

    def check_domestic_violence_bond_condition(self) -> str:
        dv_conditions = self.view.entry_case_information.domestic_violence_conditions
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


class ChargeGridInfoChecker(DefenseCounselChecker):
    """Class that checks dialog to make sure the appropriate information is entered."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.grid = dialog.charges_gridLayout

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
        while col < self.view.charges_gridLayout.columnCount():
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


class FailureToAppearDialogInfoChecker(DefenseCounselChecker):
    """Class with all checks for Failure to Appear Dialog."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.dialog_check_list = [
            'check_defense_counsel',
        ]
        self.check_status = self.perform_check_list()


class ArraignmentContinueDialogInfoChecker(DefenseCounselChecker):
    """Class with all checks for Arriagnment Continuance Dialog."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.dialog_check_list = [
            'check_defense_counsel',
        ]
        self.check_status = self.perform_check_list()


class FreeformDialogInfoChecker(DefenseCounselChecker):
    """Class with all checks for Freeform Entry Dialog."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.dialog_check_list = [
            'check_defense_counsel',
        ]
        self.check_status = self.perform_check_list()


class CriminalSealingDialogInfoChecker(DefenseCounselChecker):
    """Class with all checks for Criminal Sealing Entry Dialog."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.dialog_check_list = [
            'check_defense_counsel',
        ]
        self.check_status = self.perform_check_list()


class CivilFreeformDialogInfoChecker(BaseChecker):
    """Class with all checks for Civil Freeform Entry Dialog."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.dialog_check_list = [
        ]
        self.check_status = self.perform_check_list()
