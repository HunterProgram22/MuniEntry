"""Module that contains general dialogs for specific parts of a dialog dialog."""
from typing import Any

from loguru import logger

from munientry.settings.business_constants import MOVING_COURT_COSTS, CRIMINAL_COURT_COSTS, \
    NONMOVING_COURT_COSTS, SPECIAL_DOCKETS_COSTS
from munientry.updaters.base_updaters import BaseDialogUpdater


### WARNING - FRA (INSURANCE) - fra_in_court and fra_in_file
### NOTICE - the FRA (insurance) is updated through the base_crimtraffic_builders.py method
### set_fra_in_court and set_fra_in_file which is triggered to run any time one of the fields
### is changed/updated.
### TODO: This should be moved to an updater.
### Alternative is wholesale rewrite to somehow trigger model updates on any UI change - but that
### is a lot more work.


class CaseInformationUpdater(BaseDialogUpdater):
    """Updates the model data with the case information fram (top frame on dialogs)."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.model.case_number = self.dialog.case_number_lineEdit.text()
        self.model.plea_trial_date = self.dialog.plea_trial_date.get_date_as_string()
        try:
            self.model.appearance_reason = self.dialog.appearance_reason_box.currentText()
        except AttributeError as error:
            logger.warning(error)
        self.update_defendant()
        try:
            self.update_defense_counsel()
        except AttributeError as err:
            logger.warning(err)

    def update_defendant(self) -> None:
        self.model.defendant.first_name = self.dialog.defendant_first_name_lineEdit.text()
        self.model.defendant.last_name = self.dialog.defendant_last_name_lineEdit.text()

    def update_defense_counsel(self) -> None:
        self.model.defense_counsel = self.dialog.defense_counsel_name_box.currentText()
        try:
            self.model.defense_counsel_type = self.dialog.defense_counsel_type_box.currentText()
        except AttributeError as error:
            logger.warning(error)
        try:
            self.model.defense_counsel_waived = (
                self.dialog.defense_counsel_waived_checkBox.isChecked()
            )
        except AttributeError as error_two:
            logger.warning(error_two)


class CourtCostsUpdater(BaseDialogUpdater):
    """Updates the court costs for a case by determining the highest charge type."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.model.court_costs.ordered = self.dialog.court_costs_box.currentText()
        self.model.court_costs.ability_to_pay_time = self.dialog.ability_to_pay_box.currentText()
        self.model.court_costs.balance_due_date = self.set_balance_due_date()
        self.model.court_costs.amount = self.calculate_court_costs()
        self.model.court_costs.pay_today_amount = self.dialog.pay_today_box.text()
        self.model.court_costs.monthly_pay_amount = self.dialog.monthly_pay_box.text()

    def set_balance_due_date(self) -> str:
        """Sets the balance due date to the name of the specialized docket or specific due date."""
        if self.dialog.ability_to_pay_box.currentText() in SPECIAL_DOCKETS_COSTS:
            return self.dialog.ability_to_pay_box.currentText()
        return self.dialog.balance_due_date.get_date_as_string()

    def calculate_court_costs(self) -> int:
        court_costs = 0
        if self.dialog.court_costs_box.currentText() == 'Yes':
            for charge in self.model.charges_list:
                court_costs = self.set_max_court_costs(charge, court_costs)
        return court_costs

    def set_max_court_costs(self, charge: type[Any], court_costs: int) -> int:
        if charge.type == 'Moving':
            return MOVING_COURT_COSTS
        if charge.type == 'Criminal':
            return max(court_costs, CRIMINAL_COURT_COSTS)
        if charge.type == 'Non-moving':
            return max(court_costs, NONMOVING_COURT_COSTS)
        return 0


class FinesUpdater(BaseDialogUpdater):
    """Updates the total fines owed and fines suspended in a case."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.model.total_fines = self.calculate_total_fines()
        self.model.total_fines_suspended = self.calculate_total_fines_suspended()

    def calculate_total_fines(self) -> int:
        total_fines = 0
        for charge in self.model.charges_list:
            try:
                local_charge_fines_amount = int(charge.fines_amount[2:])
            except ValueError:
                local_charge_fines_amount = 0
            total_fines = total_fines + int(local_charge_fines_amount)
        return total_fines

    def calculate_total_fines_suspended(self) -> int:
        total_fines_suspended = 0
        for charge in self.model.charges_list:
            try:
                local_charge_fines_suspended = int(charge.fines_suspended[2:])
            except ValueError:
                local_charge_fines_suspended = 0
            total_fines_suspended = total_fines_suspended + int(local_charge_fines_suspended)
        return total_fines_suspended


class JailDataUpdater(BaseDialogUpdater):
    """Updates the jail days, jail suspended days and jail credit."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.update_jail_time_credit()
        self.set_all_jail_day_totals()

    def update_jail_time_credit(self) -> None:
        self.model.jail_terms.currently_in_jail = self.dialog.in_jail_box.currentText()
        self.model.jail_terms.days_in_jail = self.set_jail_time_credit()
        self.model.jail_terms.apply_jtc = self.dialog.jail_time_credit_apply_box.currentText()

        self.model.jail_terms.companion_cases_exist = (
            self.dialog.add_companion_cases_checkBox.isChecked()
        )
        self.model.jail_terms.companion_cases_numbers = self.dialog.companion_cases_box.text()
        self.model.jail_terms.companion_cases_sentence_type = (
            self.dialog.companion_cases_sentence_box.currentText()
        )

    def set_jail_time_credit(self) -> int:
        if self.dialog.jail_time_credit_box.text() == '':
            return 0
        return int(self.dialog.jail_time_credit_box.text())

    def set_all_jail_day_totals(self) -> None:
        self.model.jail_terms.total_jail_days_imposed = self.calculate_total_jail_days_imposed()
        self.model.jail_terms.total_jail_days_suspended = self.calculate_total_jail_days_suspended()
        self.model.jail_terms.total_jail_days_to_serve = self.calculate_total_jail_days_to_serve()

    def calculate_total_jail_days_to_serve(self) -> int:
        return (self.model.jail_terms.total_jail_days_imposed) - (
            self.model.jail_terms.total_jail_days_suspended
        )

    def calculate_total_jail_days_imposed(self) -> int:
        total_jail_days_imposed = 0
        for charge in self.model.charges_list:
            try:
                local_jail_days_imposed = int(charge.jail_days)
            except ValueError:
                local_jail_days_imposed = 0
            total_jail_days_imposed += local_jail_days_imposed
        return total_jail_days_imposed

    def calculate_total_jail_days_suspended(self) -> int:
        total_jail_days_suspended = 0
        for charge in self.model.charges_list:
            try:
                local_jail_days_suspended = int(charge.jail_days_suspended)
            except ValueError:
                local_jail_days_suspended = 0
            total_jail_days_suspended += local_jail_days_suspended
        return total_jail_days_suspended


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
