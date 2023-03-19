"""Module that contains data checks for dialogs that potentially impose jail time."""
from loguru import logger

from munientry.checkers.base_checks import (
    BLANK,
    FAIL,
    PASS,
    BaseChecker,
    ChargeGridInfoChecker,
    InsuranceInfoChecker,
)
from munientry.settings.pyqt_constants import YES_BUTTON_RESPONSE, NO_BUTTON_RESPONSE, \
    CANCEL_BUTTON_RESPONSE
from munientry.widgets.message_boxes import (
    JailWarningBox,
    RequiredBox,
    TwoChoiceQuestionBox,
    WarningBox,
)

YES = 'Yes'


class JailTimeCreditChecker(BaseChecker):
    """Class with checks for the Jail Time Credit Box on Dialogs with jail options."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.model = self.view.entry_case_information
        self.jail_days_imposed = self.model.jail_terms.total_jail_days_imposed
        self.jail_days_suspended = self.model.jail_terms.total_jail_days_suspended
        self.jail_credit = self.model.jail_terms.days_in_jail

    def check_if_days_in_jail_blank_but_in_jail(self) -> str:
        """Requires user to enter data in Days in Jail field if Currently in Jail is Yes."""
        if self.view.in_jail_box.currentText() == YES:
            if self.view.jail_time_credit_box.text() == BLANK:
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
        if self.view.jail_time_credit_box.text() != BLANK:
            if self.view.in_jail_box.currentText() == BLANK:
                message = (
                    'The Days in Jail has been provided, but the Jail Time Credit'
                    + ' does not indicate whether the Defendant is Currently In Jail.'
                    + '\n\nIs the Defendant currently in jail?'
                )
                return self.set_in_jail_box(WarningBox(message, 'Is Defendant in Jail').exec())
        return PASS

    def set_in_jail_box(self, message_response) -> str:
        if message_response == NO_BUTTON_RESPONSE:
            self.view.in_jail_box.setCurrentText('No')
        elif message_response == YES_BUTTON_RESPONSE:
            self.view.in_jail_box.setCurrentText(YES)
        return PASS

    def check_if_apply_jail_credit_blank_but_in_jail(self) -> str:
        """Asks user to choose how to apply jail time credit if jail time credit is entered."""
        if self.view.jail_time_credit_box.text() != BLANK:
            if self.view.jail_time_credit_apply_box.currentText() == BLANK:
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
            self.view.jail_time_credit_apply_box.setCurrentText('Sentence')
        elif message_response == 1:
            self.view.jail_time_credit_apply_box.setCurrentText('Costs and Fines')
        return PASS

    def check_if_jail_credit_more_than_imposed(self) -> str:
        """Checks to see if more jail time credit is given then jail time imposed."""
        if self.view.jail_time_credit_apply_box.currentText() == 'Sentence':
            if self.jail_credit > self.jail_days_imposed:
                message = (
                    f'The Defendant is set to have {self.jail_credit} days of'
                    + ' jail time credit applied to a sentence, but a total of only'
                    + f'{self.jail_days_imposed} are set to be imposed'
                    + ' in the case. The total jail day imposed is less than the jail time credit'
                    + ' that is being applied to the sentence. \n\nPlease impose additional jail'
                    + ' days or change the Apply JTC to box to Costs and Fines.'
                )
                RequiredBox(message, 'Excessive Jail Credit').exec()
                return FAIL
        return PASS


class JailCCPleaDialogInfoChecker(
    ChargeGridInfoChecker, InsuranceInfoChecker, JailTimeCreditChecker,
):
    """Class with checks for the Jail CC Plea Dialog."""

    conditions_list = [
        ('license_suspension', 'license_type', 'License Suspension'),
        ('community_service', 'hours_of_service', 'Community Service'),
        ('other_conditions', 'terms', 'Other Conditions'),
        ('community_control', 'term_of_control', 'Community Control'),
        ('impoundment', 'vehicle_make_model', 'Immobilize/Impound'),
    ]

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.model = self.view.entry_case_information
        self.jail_days_imposed = self.model.jail_terms.total_jail_days_imposed
        self.jail_days_suspended = self.model.jail_terms.total_jail_days_suspended
        self.jail_credit = self.model.jail_terms.days_in_jail
        self.dialog_check_list = [
            'check_defense_counsel',
            'check_if_no_plea_entered',
            'check_if_no_finding_entered',
            'check_insurance',
            'check_additional_conditions_ordered',
            'check_if_jail_suspended_more_than_imposed',
            'check_if_days_in_jail_blank_but_in_jail',
            'check_if_in_jail_blank_but_has_jail_days',
            'check_if_apply_jail_credit_blank_but_in_jail',
            'check_if_jail_reporting_required',
            'check_if_jail_equals_suspended_and_imposed',
            'check_if_jail_credit_more_than_imposed',
            'check_if_in_jail_and_reporting_set',
        ]
        self.check_status = self.perform_check_list()

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
            self.view.jail_checkBox.setChecked(True)
            self.view.functions.start_add_jail_report_dialog()
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
            self.view.jail_checkBox.setChecked(False)
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


class SentencingOnlyDialogInfoChecker(JailCCPleaDialogInfoChecker):
    """Class for Sentencing Only Checks, same as JailCCPlea, but plea check is different."""

    conditions_list = [
        ('license_suspension', 'license_type', 'License Suspension'),
        ('community_service', 'hours_of_service', 'Community Service'),
        ('other_conditions', 'terms', 'Other Conditions'),
        ('community_control', 'term_of_control', 'Community Control'),
        ('impoundment', 'vehicle_make_model', 'Immobilize/Impound'),
    ]

    def __init__(self, dialog):
        super().__init__(dialog)
        self.case_info = self.view.entry_case_information
        self.dialog_check_list = [
            'check_defense_counsel',
            'check_if_plea_date_is_today',
            'check_if_no_finding_entered',
            'check_insurance',
            'check_additional_conditions_ordered',
            'check_if_jail_suspended_more_than_imposed',
            'check_if_days_in_jail_blank_but_in_jail',
            'check_if_in_jail_blank_but_has_jail_days',
            'check_if_apply_jail_credit_blank_but_in_jail',
            'check_if_jail_reporting_required',
            'check_if_jail_equals_suspended_and_imposed',
            'check_if_jail_credit_more_than_imposed',
            'check_if_in_jail_and_reporting_set',
        ]
        self.check_status = self.perform_check_list()


class TrialSentencingDialogInfoChecker(JailCCPleaDialogInfoChecker):
    """Class for Trial Sentencing Checks, same as JailCCPlea, but there is no plea check."""

    conditions_list = [
        ('license_suspension', 'license_type', 'License Suspension'),
        ('community_service', 'hours_of_service', 'Community Service'),
        ('other_conditions', 'terms', 'Other Conditions'),
        ('community_control', 'term_of_control', 'Community Control'),
        ('impoundment', 'vehicle_make_model', 'Immobilize/Impound'),
    ]

    def __init__(self, dialog):
        super().__init__(dialog)
        self.case_info = self.view.entry_case_information
        self.dialog_check_list = [
            'check_defense_counsel',
            'check_if_no_finding_entered',
            'check_insurance',
            'check_additional_conditions_ordered',
            'check_if_jail_suspended_more_than_imposed',
            'check_if_days_in_jail_blank_but_in_jail',
            'check_if_in_jail_blank_but_has_jail_days',
            'check_if_apply_jail_credit_blank_but_in_jail',
            'check_if_jail_reporting_required',
            'check_if_jail_equals_suspended_and_imposed',
            'check_if_jail_credit_more_than_imposed',
            'check_if_in_jail_and_reporting_set',
        ]
        self.check_status = self.perform_check_list()


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
