"""Module containing classes responsible for updating case information.
Each main dialog class has a subclass that governs what
is updated for the main class. The classes take the data from the view (GUI) and transfer
it to the appropriate model object."""
from settings import MOVING_COURT_COSTS, CRIMINAL_COURT_COSTS, NONMOVING_COURT_COSTS


class CaseModelUpdater:
    """Base class that contains methods used by subclasses and is called by a main
    entry dialog to update the entry_case_information (model data)."""

    def __init__(self, dialog):
        self.dialog = dialog
        self.model = dialog.entry_case_information
        self.set_case_number_and_date()
        self.set_party_information()
        self.set_defense_counsel_information()
        self.set_appearance_reason()

    def set_case_number_and_date(self):
        self.model.case_number = self.dialog.case_number_lineEdit.text()
        self.model.plea_trial_date = self.dialog.plea_trial_date.date().toString("MMMM dd, yyyy")

    def set_party_information(self):
        self.model.defendant.first_name = self.dialog.defendant_first_name_lineEdit.text()
        self.model.defendant.last_name = self.dialog.defendant_last_name_lineEdit.text()

    def set_defense_counsel_information(self):
        self.model.defense_counsel = self.dialog.defense_counsel_name_box.currentText()
        self.model.defense_counsel_type = self.dialog.defense_counsel_type_box.currentText()
        self.model.defense_counsel_waived = self.dialog.defense_counsel_waived_checkBox.isChecked()

    def set_appearance_reason(self):
        self.model.appearance_reason = self.dialog.appearance_reason_box.currentText()

    def update_costs_and_fines_information(self):
        self.model.court_costs.ordered = self.dialog.court_costs_box.currentText()
        self.model.court_costs.ability_to_pay_time = self.dialog.ability_to_pay_box.currentText()
        self.model.court_costs.balance_due_date = self.dialog.balance_due_date.date().toString(
            "MMMM dd, yyyy"
        )

    def calculate_costs_and_fines(self):
        self.model.court_costs.amount = self.calculate_court_costs()
        self.model.total_fines = self.calculate_total_fines()
        self.model.total_fines_suspended = self.calculate_total_fines_suspended()

    def calculate_court_costs(self):
        court_costs = 0
        if self.dialog.court_costs_box.currentText() == "Yes":
            for charge in self.model.charges_list:
                if charge.type == "Moving":
                    return MOVING_COURT_COSTS
                if charge.type == "Criminal":
                    court_costs = max(court_costs, CRIMINAL_COURT_COSTS)
                elif charge.type == "Non-moving":
                    court_costs = max(court_costs, NONMOVING_COURT_COSTS)
        return court_costs

    def calculate_total_fines(self):
        total_fines = 0
        for charge in self.model.charges_list:
            try:
                local_charge_fines_amount = int(charge.fines_amount[2:])
            except ValueError:
                local_charge_fines_amount = 0
            total_fines = total_fines + int(local_charge_fines_amount)
        return total_fines

    def calculate_total_fines_suspended(self):
        total_fines_suspended = 0
        for charge in self.model.charges_list:
            try:
                local_charge_fines_suspended = int(charge.fines_suspended[2:])
            except ValueError:
                local_charge_fines_suspended = 0
            total_fines_suspended = total_fines_suspended + int(local_charge_fines_suspended)
        return total_fines_suspended


class DiversionDialogCaseUpdater(CaseModelUpdater):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.update_case_information()

    def update_case_information(self):
        self.dialog.add_plea_to_entry_case_information()
        self.dialog.transfer_field_data_to_model(self.model.diversion)
        self.model.diversion.program_name = self.model.diversion.get_program_name()
        self.dialog.transfer_field_data_to_model(self.model.other_conditions)


class JailCCDialogCaseUpdater(CaseModelUpdater):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog.add_plea_to_entry_case_information()
        self.update_costs_and_fines_information()
        self.update_jail_time_credit()
        self.calculate_total_jail_days_to_serve()
        self.calculate_costs_and_fines()

    def update_jail_time_credit(self):
        self.model.currently_in_jail = self.dialog.in_jail_box.currentText()
        self.model.days_in_jail = self.set_jail_time_credit()
        self.model.apply_jtc = self.dialog.jail_time_credit_apply_box.currentText()

    def set_jail_time_credit(self):
        if self.dialog.jail_time_credit_box.text() == "":
            return 0
        return int(self.dialog.jail_time_credit_box.text())

    def calculate_total_jail_days_to_serve(self):
        self.model.total_jail_days_imposed = self.calculate_total_jail_days_imposed()
        self.model.total_jail_days_suspended = self.calculate_total_jail_days_suspended()
        self.model.total_jail_days_to_serve = int(self.model.total_jail_days_imposed) - int(
            self.model.total_jail_days_suspended
        )

    def calculate_total_jail_days_imposed(self):
        total_jail_days_imposed = 0
        for charge in self.model.charges_list:
            try:
                local_jail_days_imposed = int(charge.jail_days)
            except ValueError:
                local_jail_days_imposed = 0
            total_jail_days_imposed = total_jail_days_imposed + local_jail_days_imposed
        return total_jail_days_imposed

    def calculate_total_jail_days_suspended(self):
        total_jail_days_suspended = 0
        for charge in self.model.charges_list:
            try:
                local_jail_days_suspended = int(charge.jail_days_suspended)
            except ValueError:
                local_jail_days_suspended = 0
            total_jail_days_suspended = total_jail_days_suspended + local_jail_days_suspended
        return total_jail_days_suspended


class FineOnlyDialogCaseUpdater(CaseModelUpdater):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog.add_plea_to_entry_case_information()
        self.update_costs_and_fines_information()
        self.update_jail_time_credit_for_fines()
        self.calculate_costs_and_fines()

    def update_jail_time_credit_for_fines(self):
        self.model.fines_and_costs_jail_credit = self.dialog.credit_for_jail_checkBox.isChecked()
        self.model.days_in_jail = self.dialog.jail_time_credit_box.text()


class NotGuiltyBondDialogCaseUpdater(CaseModelUpdater):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog.add_plea_to_entry_case_information()
        self.update_bond_conditions()

    def update_bond_conditions(self):
        self.dialog.transfer_field_data_to_model(self.model.bond_conditions)
