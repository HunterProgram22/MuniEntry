"""Module containing classes responsible for updating case information anytime a function for
the case is ran. Each main dialog class has a subclass that governs what is updated for the
main class."""
from settings import MOVING_COURT_COSTS, CRIMINAL_COURT_COSTS, NONMOVING_COURT_COSTS


class CaseUpdater:
    """Base class that contains methods used by subclasses and is called by a main entry dialog to update
    the entry_case_information (model data)."""
    def __init__(self, dialog):
        self.dialog = dialog
        self.set_case_number_and_date()
        self.set_party_information()
        self.set_defense_counsel_information()
        self.set_appearance_reason()

    def set_case_number_and_date(self):
        self.dialog.entry_case_information.case_number = (
            self.dialog.case_number_lineEdit.text()
        )
        self.dialog.entry_case_information.plea_trial_date = (
            self.dialog.plea_trial_date.date().toString("MMMM dd, yyyy")
        )

    def set_party_information(self):
        self.dialog.entry_case_information.defendant.first_name = (
            self.dialog.defendant_first_name_lineEdit.text()
        )
        self.dialog.entry_case_information.defendant.last_name = (
            self.dialog.defendant_last_name_lineEdit.text()
        )

    def set_defense_counsel_information(self):
        self.dialog.entry_case_information.defense_counsel = (
            self.dialog.defense_counsel_name_box.currentText()
        )
        self.dialog.entry_case_information.defense_counsel_type = (
            self.dialog.defense_counsel_type_box.currentText()
        )
        self.dialog.entry_case_information.defense_counsel_waived = (
            self.dialog.defense_counsel_waived_checkBox.isChecked()
        )

    def set_appearance_reason(self):
        self.dialog.entry_case_information.appearance_reason = (
            self.dialog.appearance_reason_box.currentText()
        )

    def update_costs_and_fines_information(self):
        self.dialog.entry_case_information.court_costs.ordered = (
            self.dialog.court_costs_box.currentText()
        )
        self.dialog.entry_case_information.court_costs.ability_to_pay_time = (
            self.dialog.ability_to_pay_box.currentText()
        )
        self.dialog.entry_case_information.court_costs.balance_due_date = (
            self.dialog.balance_due_date.date().toString("MMMM dd, yyyy")
        )

    def calculate_costs_and_fines(self):
        self.dialog.entry_case_information.court_costs.amount = (
            self.calculate_court_costs()
        )
        self.dialog.entry_case_information.total_fines = self.calculate_total_fines()
        self.dialog.entry_case_information.total_fines_suspended = (
            self.calculate_total_fines_suspended()
        )

    def calculate_court_costs(self):
        court_costs = 0
        if self.dialog.court_costs_box.currentText() == "Yes":
            for charge in self.dialog.entry_case_information.charges_list:
                if charge.type == "Moving":
                    return MOVING_COURT_COSTS
                if charge.type == "Criminal":
                    court_costs = max(court_costs, CRIMINAL_COURT_COSTS)
                elif charge.type == "Non-moving":
                    court_costs = max(court_costs, NONMOVING_COURT_COSTS)
        return court_costs

    def calculate_total_fines(self):
        total_fines = 0
        for charge in self.dialog.entry_case_information.charges_list:
            try:
                local_charge_fines_amount = int(charge.fines_amount[2:])
            except ValueError:
                local_charge_fines_amount = 0
            total_fines = total_fines + int(local_charge_fines_amount)
        return total_fines

    def calculate_total_fines_suspended(self):
        total_fines_suspended = 0
        for charge in self.dialog.entry_case_information.charges_list:
            try:
                local_charge_fines_suspended = int(charge.fines_suspended[2:])
            except ValueError:
                local_charge_fines_suspended = 0
            total_fines_suspended = total_fines_suspended + int(
                local_charge_fines_suspended
            )
        return total_fines_suspended


class DiversionDialogCaseUpdater(CaseUpdater):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.update_case_information()

    def update_case_information(self):
        self.dialog.add_plea_to_entry_case_information()
        self.dialog.transfer_field_data_to_model(
            self.dialog.entry_case_information.diversion
        )
        self.dialog.entry_case_information.diversion.program_name = (
            self.dialog.entry_case_information.diversion.get_program_name()
        )
        self.dialog.transfer_field_data_to_model(
            self.dialog.entry_case_information.other_conditions
        )


class JailCCDialogCaseUpdater(CaseUpdater):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog.add_plea_to_entry_case_information()
        self.update_costs_and_fines_information()
        self.update_jail_time_credit()
        self.calculate_costs_and_fines()

    def update_jail_time_credit(self):
        self.dialog.entry_case_information.currently_in_jail = (
            self.dialog.in_jail_box.currentText()
        )
        self.dialog.entry_case_information.days_in_jail = (
            self.dialog.jail_time_credit_box.text()
        )
        self.dialog.entry_case_information.apply_jtc = (
            self.dialog.jail_time_credit_apply_box.currentText()
        )


class FineOnlyDialogCaseUpdater(CaseUpdater):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog.add_plea_to_entry_case_information()
        self.update_costs_and_fines_information()
        self.update_jail_time_credit_for_fines()
        self.calculate_costs_and_fines()

    def update_jail_time_credit_for_fines(self):
        self.dialog.entry_case_information.fines_and_costs_jail_credit = (
            self.dialog.credit_for_jail_checkBox.isChecked()
        )
        self.dialog.entry_case_information.days_in_jail = (
            self.dialog.jail_time_credit_box.text()
        )


class NotGuiltyBondDialogCaseUpdater(CaseUpdater):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog.add_plea_to_entry_case_information()
        self.update_bond_conditions()

    def update_bond_conditions(self):
        self.dialog.transfer_field_data_to_model(
            self.dialog.entry_case_information.bond_conditions
        )
