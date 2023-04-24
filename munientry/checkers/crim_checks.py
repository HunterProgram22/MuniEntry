# flake8: noqa: WPS110, WPS214
"""Checks for Criminal Traffic Dialogs."""
from typing import Any, Optional

from PyQt6.QtWidgets import QComboBox, QLabel

from munientry.checkers import check_messages as cm
from munientry.checkers.base_checks import (
    BaseChecks,
    jail_warning_check,
    required_check,
    required_condition_check,
    warning_check,
)
from munientry.models.conditions_models import ConditionsModel
from munientry.settings.pyqt_constants import NO_BUTTON_RESPONSE, YES_BUTTON_RESPONSE
from munientry.widgets.message_boxes import TwoChoiceQuestionBox

BLANK = ''
DISMISSED = 'Dismissed'
NO = 'No'
NO_BOND_AMOUNT_TYPES = ('Recognizance (OR) Bond', 'Continue Existing Bond', 'No Bond')
NONE = 'None'
YES = 'Yes'
TRAFFIC_CODES = ('TRC', 'TRD')


class CrimBaseChecks(BaseChecks):
    """Base class for all Criminal Traffic checks."""

    conditions_list: list = []

    @required_check(cm.PLEA_PAST_TITLE, cm.PLEA_PAST_MSG)
    def check_plea_date(self) -> bool:
        """Returns False (Fails) if plea date is not set in the past."""
        return self.dialog.plea_date.date() < self.today

    @required_check(cm.LEAP_PAST_TITLE, cm.LEAP_PAST_MSG)
    def check_leap_plea_date(self) -> bool:
        """Returns False (Fails) if LEAP plea date is not set in the past."""
        return self.dialog.leap_plea_date.date() < self.today

    @required_check(cm.DIVERSION_SET_TITLE, cm.DIVERSION_SET_MSG)
    def check_if_diversion_program_selected(self) -> bool:
        """Returns False (Fails) if no diversion radio button is checked."""
        diversion_radio_btns = [
            self.dialog.marijuana_diversion_radio_btn,
            self.dialog.theft_diversion_radio_btn,
            self.dialog.other_diversion_radio_btn,
        ]
        return any(btn.isChecked() for btn in diversion_radio_btns)

    @required_condition_check
    def check_additional_conditions_ordered(self) -> tuple[bool, list[str]]:
        """Hard stops if an additional condition checkbox is checked, but certain data is None.

        This checks to see if the primary condition of an additional condition is set to something
        other than None or Empty. If so the check passes.

        The conditions_list for each dialog provides a tuple of (condition, the primary condition
        that is checked, the formal name of the Condition).
        """
        for condition in self.conditions_list:
            condition_model, primary_condition, condition_name = self._get_condition_info(condition)
            if condition_model.ordered in {False, None}:
                continue
            if primary_condition in {None, BLANK}:
                return False, [condition_name]
        return True, [condition_name]

    def _get_condition_info(
        self,
        condition_item: tuple[str, str, str]
    ) -> tuple[ConditionsModel, str, str]:
        """The CheckList class for certain classes has conditions_list tuples that are returned.

        The tuple that is returned contains a string model name, the primary condition that is set
        in a model, and the standard name (i.e. 'License Suspension') for the model.
        """
        condition_model = getattr(self.dialog.entry_case_information, condition_item[0])
        primary_condition = getattr(condition_model, condition_item[1])
        condition_name = condition_item[2]
        return condition_model, primary_condition, condition_name


class DefenseCounselChecks(CrimBaseChecks):
    """Class containing checks for defense counsel."""

    @warning_check(cm.DEF_COUNSEL_TITLE, cm.DEF_COUNSEL_MSG)
    def check_defense_counsel(self, msg_response: int = None) -> bool:
        """Returns False (Fails) with choice to set defense counsel waived if no counsel set."""
        if self.dialog.defense_counsel_waived_checkBox.isChecked():
            return True
        if msg_response == YES_BUTTON_RESPONSE:
            self.dialog.defense_counsel_waived_checkBox.setChecked(True)
            return True
        return self.dialog.defense_counsel_name_box.currentText().strip() != BLANK


class InsuranceChecks(DefenseCounselChecks):
    """Class containing checks for Insurance."""

    @warning_check(cm.INSURANCE_TITLE, cm.INSURANCE_MSG)
    def check_insurance(self, msg_response: int = None) -> bool:
        """Returns False (Fails) if insurance in Traffic cases not shown in file or in court."""
        if msg_response is not None:
            return self.set_insurance(msg_response)
        if self.dialog.fra_in_file_box.currentText() == YES:
            return True
        if any(code in self.dialog.case_number_lineEdit.text() for code in TRAFFIC_CODES):
            return self.dialog.fra_in_court_box.currentText() in {YES, NO}
        return True

    def set_insurance(self, msg_response: int) -> bool:
        if msg_response == YES_BUTTON_RESPONSE:
            self.dialog.fra_in_court_box.setCurrentText(YES)
        elif msg_response == NO_BUTTON_RESPONSE:
            self.dialog.fra_in_court_box.setCurrentText(NO)
        return True


class BondChecks(DefenseCounselChecks):
    """Class that checks dialog to make sure the appropriate bond information is entered."""

    @required_check(cm.BOND_REQUIRED_TITLE, cm.BOND_REQUIRED_MSG)
    def check_if_no_bond_amount(self) -> bool:
        """Returns False (Fails) when bond type requires a bond amount but no bond set."""
        if self.dialog.bond_type_box.currentText() in NO_BOND_AMOUNT_TYPES:
            return True
        return self.dialog.bond_amount_box.currentText() != NONE

    @required_check(cm.BOND_AMOUNT_TITLE, cm.BOND_AMOUNT_MSG)
    def check_if_improper_bond_type(self) -> bool:
        """Returns False (Fails) if bond amount set, but bond type is no bond amount type."""
        if self.dialog.bond_type_box.currentText() not in NO_BOND_AMOUNT_TYPES:
            return True
        return self.dialog.bond_amount_box.currentText() == NONE

    @required_check(cm.BOND_MODIFICATION_TITLE, cm.BOND_MODIFICATION_MSG)
    def check_if_no_bond_modification_decision(self) -> bool:
        """Returns False (Fails) if bond modification decision is not set."""
        return self.dialog.bond_modification_decision_box.currentText() != BLANK

    @required_check(cm.DV_BOND_TITLE, cm.DV_BOND_MSG)
    def check_domestic_violence_bond_condition(self) -> bool:
        """Returns False (Fails) if either vacate residence or surrender weapons is not set.

        This check is used because there are two 'primary conditions' for the Domestic Violence
        Bond Conditions so the check primary condition for check additional conditions ordered
        will not suffice.
        """
        dv_conditions = self.dialog.entry_case_information.domestic_violence_conditions
        if dv_conditions.ordered is True:
            return dv_conditions.vacate_residence or dv_conditions.surrender_weapons
        return True


class ChargeGridChecks(InsuranceChecks):
    """Class that checks dialog to make sure the appropriate information is entered."""

    def __init__(self, dialog):
        self.grid = dialog.charges_gridLayout
        super().__init__(dialog)

    def get_widget_text(self, row: int, col: int) -> Optional[str]:
        """Returns the text of a widget based on the type of widget."""
        try:
            widget = self.grid.itemAtPosition(row, col).widget()
        except AttributeError:
            widget = None
        if isinstance(widget, QLabel):
            return widget.text()
        if isinstance(widget, QComboBox):
            return widget.currentText()
        return None

    def should_skip_charge(self, col: int) -> bool:
        """Returns True if charge in the specified column should be skipped, False otherwise."""
        offense = self.get_widget_text(self.grid.row_offense, col)
        plea = self.get_widget_text(self.grid.row_plea, col)
        if offense is None:
            return True
        return plea == DISMISSED

    @required_check(cm.MISSING_PLEA_TITLE, cm.MISSING_PLEA_MSG)
    def check_if_no_plea_entered(self) -> tuple[bool, list[Optional[str]]]:
        """Stops the create entry process for any charge without a plea.

        The column (col) starts at 1 to skip the label column (col 0) of the charge grid.
        """
        col = 1
        while col < self.grid.columnCount():
            if self.should_skip_charge(col):
                col += 1
                continue
            plea = self.get_widget_text(self.grid.row_plea, col)
            if plea == BLANK:
                offense = self.get_widget_text(self.grid.row_offense, col)
                return False, [offense]
            col += 1
        return True, []

    @required_check(cm.MISSING_FINDING_TITLE, cm.MISSING_FINDING_MSG)
    def check_if_no_finding_entered(self) -> tuple[bool, list[Optional[str]]]:
        """Stops the create entry process for any charge without a finding.

        The column (col) starts at 1 to skip the label column (col 0) of the charge grid.
        """
        col = 1
        while col < self.dialog.charges_gridLayout.columnCount():
            if self.should_skip_charge(col):
                col += 1
                continue
            finding = self.get_widget_text(self.grid.row_finding, col)
            if finding == BLANK:
                offense = self.get_widget_text(self.grid.row_offense, col)
                return False, [offense]
            col += 1
        return True, []


class JailTimeChecks(ChargeGridChecks):
    """Class with checks for the Jail Time Credit Box on Dialogs with jail options."""

    def __init__(self, dialog) -> None:
        self.model = dialog.entry_case_information
        self.jail_days_imposed = self.model.jail_terms.total_jail_days_imposed
        self.jail_days_suspended = self.model.jail_terms.total_jail_days_suspended
        self.jail_credit = self.model.jail_terms.days_in_jail
        super().__init__(dialog)

    @required_check(cm.EXCESS_JAIL_SUSP_TITLE, cm.EXCESS_JAIL_SUSP_MSG)
    def check_if_jail_suspended_more_than_imposed(self) -> tuple[bool, list[Any]]:
        """Returns False (Fails) if jail days suspended are greater than jail days imposed."""
        return (
            self.jail_days_suspended <= self.jail_days_imposed,
            [self.jail_days_suspended, self.jail_days_imposed],
        )

    @jail_warning_check(cm.ADD_JAIL_TITLE, cm.ADD_JAIL_MSG)
    def check_if_jail_reporting_required(self, msg_response: int = None) -> tuple[bool, list[Any]]:
        """Checks to see if the jails days imposed is greater than jail days suspended and credit.

        If jails days imposed exceed suspended days and credit days triggers ask users if they
        want to set the jail reporting terms.

        If the Driver Intervention Program is imposed then the check is skipped because no jail
        reporting is required.
        """
        if msg_response is not None:
            return self.add_jail_report_terms(msg_response)
        if self.skip_jail_check():
            return True, []
        if self.jail_days_imposed > (self.jail_days_suspended + self.jail_credit):
            return False, [self.jail_days_imposed, self.jail_days_suspended, self.jail_credit]
        return True, []

    def skip_jail_check(self) -> bool:
        if self.model.community_control.driver_intervention_program is True:
            return True
        if self.model.jail_terms.ordered is True:
            return True
        return self.model.jail_terms.currently_in_jail == YES

    def add_jail_report_terms(self, msg_response: int) -> tuple[bool, list[Any]]:
        """Asks user if Jail Reporting needs to be set and sets reporting if answer is Yes."""
        if msg_response == YES_BUTTON_RESPONSE:
            self.dialog.jail_checkBox.setChecked(True)
            self.dialog.functions.start_add_jail_report_dialog()
            return True, []
        else:
            return True, []

    @warning_check(cm.JAIL_SET_NO_JAIL_TITLE, cm.JAIL_SET_NO_JAIL_MSG)
    def check_if_jail_equals_suspended_and_imposed(self, msg_response: int = None) -> bool:
        """Returns False (Check fails) if set to report to jail but no jail days left to serve."""
        if msg_response is not None:
            return self.handle_jail_message(msg_response)
        if self.model.jail_terms.ordered is True:
            return self.jail_days_imposed != (self.jail_days_suspended + self.jail_credit)
        return True

    @warning_check(cm.DEF_IN_JAIL_TITLE, cm.DEF_IN_JAIL_MSG)
    def check_if_in_jail_and_reporting_set(self, msg_response: int = None) -> bool:
        """Returns False (Check fails) if defendant in jail but reporting to jail terms are set."""
        if msg_response is not None:
            return self.handle_jail_message(msg_response)
        if self.model.jail_terms.currently_in_jail != YES:
            return True
        if self.model.jail_terms.ordered is False:
            return True
        return self.jail_days_imposed >= (self.jail_days_suspended + self.jail_credit)

    def handle_jail_message(self, msg_response: int) -> bool:
        if msg_response == NO_BUTTON_RESPONSE:
            self.dialog.jail_checkBox.setChecked(False)
            return True
        return msg_response == YES_BUTTON_RESPONSE

    @required_check(cm.JAIL_DAYS_REQUIRED_TITLE, cm.JAIL_DAYS_REQUIRED_MSG)
    def check_if_days_in_jail_blank_but_in_jail(self) -> bool:
        """Returns False (Fails) if Defendant is in jail, but days in jail is blank."""
        if self.dialog.in_jail_box.currentText() == YES:
            return self.dialog.jail_time_credit_box.text() != BLANK
        return True

    @required_check(cm.EXCESS_JAIL_CREDIT_TITLE, cm.EXCESS_JAIL_CREDIT_MSG)
    def check_if_jail_credit_more_than_imposed(self) -> tuple[bool, list[Any]]:
        """Returns False (Fails) if more jail time credit is given than jail time imposed."""
        if self.dialog.jail_time_credit_apply_box.currentText() == 'Sentence':
            return (
                self.jail_credit <= self.jail_days_imposed,
                [self.jail_credit, self.jail_days_imposed],
            )
        return True, []

    @warning_check(cm.SET_JAIL_STATUS_TITLE, cm.SET_JAIL_STATUS_MSG)
    def check_if_in_jail_blank_but_has_jail_days(self, msg_response: int = None) -> bool:
        """Returns False (Fails) if jail time credit is set but no indication if in jail."""
        if msg_response is not None:
            return self.set_in_jail_box(msg_response)
        if self.dialog.jail_time_credit_box.text() != BLANK:
            if self.dialog.in_jail_box.currentText() == BLANK:
                return False
        return True

    def set_in_jail_box(self, msg_response: int) -> bool:
        if msg_response == NO_BUTTON_RESPONSE:
            self.dialog.in_jail_box.setCurrentText(NO)
        elif msg_response == YES_BUTTON_RESPONSE:
            self.dialog.in_jail_box.setCurrentText(YES)
        return True

    def check_if_apply_jail_credit_blank_but_in_jail(self) -> bool:
        """Asks user to choose how to apply jail time credit if jail time credit is entered."""
        if self.dialog.jail_time_credit_box.text() != BLANK:
            if self.dialog.jail_time_credit_apply_box.currentText() == BLANK:
                return self.set_jtc_apply_box(
                    TwoChoiceQuestionBox(
                        cm.APPLY_JTC_MSG, 'Sentence', 'Costs and Fines', cm.APPLY_JTC_TITLE,
                    ).exec(),
                )
        return True

    def set_jtc_apply_box(self, message_response) -> bool:
        if message_response == 0:
            self.dialog.jail_time_credit_apply_box.setCurrentText('Sentence')
        elif message_response == 1:
            self.dialog.jail_time_credit_apply_box.setCurrentText('Costs and Fines')
        return True
