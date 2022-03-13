"""Module containing classes responsible for updating case information anytime a function for
the case is ran. Each main dialog class has a subclass that governs what is updated for the
main class."""

class CaseUpdater:
    def __init__(self, dialog):
        self.dialog = dialog
        self.set_case_number_and_date(dialog)
        self.set_party_information(dialog)
        self.set_defense_counsel_information(dialog)
        self.set_appearance_reason(dialog)

    def set_case_number_and_date(self, dialog):
        dialog.entry_case_information.case_number = dialog.case_number_lineEdit.text()
        dialog.entry_case_information.plea_trial_date = dialog.plea_trial_date.date().toString("MMMM dd, yyyy")

    def set_party_information(self, dialog):
        dialog.entry_case_information.defendant.first_name = dialog.defendant_first_name_lineEdit.text()
        dialog.entry_case_information.defendant.last_name = dialog.defendant_last_name_lineEdit.text()

    def set_defense_counsel_information(self, dialog):
        dialog.entry_case_information.defense_counsel = dialog.defense_counsel_name_box.currentText()
        dialog.entry_case_information.defense_counsel_type = dialog.defense_counsel_type_box.currentText()
        dialog.entry_case_information.defense_counsel_waived = dialog.defense_counsel_waived_checkBox.isChecked()

    def set_appearance_reason(self, dialog):
        dialog.entry_case_information.appearance_reason = dialog.appearance_reason_box.currentText()

    def update_costs_and_fines_information(self, dialog):
        dialog.entry_case_information.court_costs.ordered = dialog.court_costs_box.currentText()
        dialog.entry_case_information.court_costs.ability_to_pay_time = dialog.ability_to_pay_box.currentText()
        dialog.entry_case_information.court_costs.balance_due_date = dialog.balance_due_date.date(
            ).toString("MMMM dd, yyyy")

    def calculate_costs_and_fines(self, dialog):
        dialog.entry_case_information.court_costs.amount = self.calculate_court_costs(dialog)
        total_fines = 0
        try:
            for charge in dialog.entry_case_information.charges_list:
                try:
                    local_charge_fines_amount = int(charge.fines_amount[2:])
                except ValueError:
                    local_charge_fines_amount = 0
                if local_charge_fines_amount == '':
                    local_charge_fines_amount = 0
                try:
                    total_fines = total_fines + int(local_charge_fines_amount)
                except ValueError:  # This error catches the " " (space) that is placed if a charge is dismissed.
                    pass
            dialog.entry_case_information.total_fines = total_fines
            total_fines_suspended = 0
            for  charge in dialog.entry_case_information.charges_list:
                try:
                    local_charge_fines_suspended = int(charge.fines_suspended[2:])
                except ValueError:
                    local_charge_fines_suspended = 0
                if local_charge_fines_suspended == '':
                    local_charge_fines_suspended = 0
                try:
                    total_fines_suspended = total_fines_suspended + int(local_charge_fines_suspended)
                except ValueError:  # This error catches the " " (space) that is placed if a charge is dismissed.
                    pass
            dialog.entry_case_information.total_fines_suspended = total_fines_suspended
        except TypeError:
            print("A type error was allowed to pass - this is because of deleted charge.")

    def calculate_court_costs(self, dialog):
        dialog.entry_case_information.court_costs.amount = 0
        if dialog.court_costs_box.currentText() == "Yes":
            for charge in dialog.entry_case_information.charges_list:
                if dialog.entry_case_information.court_costs.amount == 137:
                    break
                if charge.type == "Moving":
                    dialog.entry_case_information.court_costs.amount = max(
                        dialog.entry_case_information.court_costs.amount, 137)
                elif charge.type == "Criminal":
                    dialog.entry_case_information.court_costs.amount = max(
                        dialog.entry_case_information.court_costs.amount, 127)
                elif charge.type == "Non-moving":
                    dialog.entry_case_information.court_costs.amount = max(
                        dialog.entry_case_information.court_costs.amount, 108)
        return dialog.entry_case_information.court_costs.amount


class DiversionDialogCaseUpdater(CaseUpdater):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.update_case_information(dialog)

    def update_case_information(self, dialog):
        dialog.add_plea_findings_and_fines_to_entry_case_information()
        dialog.transfer_field_data_to_model(dialog.entry_case_information.diversion)
        dialog.entry_case_information.diversion.program_name = \
            dialog.entry_case_information.diversion.get_program_name()
        dialog.transfer_field_data_to_model(dialog.entry_case_information.other_conditions)


class JailCCDialogCaseUpdater(CaseUpdater):
    def __init__(self, dialog):
        super().__init__(dialog)
        dialog.add_plea_findings_and_fines_to_entry_case_information()
        self.update_costs_and_fines_information(dialog)
        self.update_jail_time_credit(dialog)
        self.calculate_costs_and_fines(dialog)

    def update_jail_time_credit(self, dialog):
        dialog.entry_case_information.currently_in_jail = dialog.in_jail_box.currentText()
        dialog.entry_case_information.days_in_jail = dialog.jail_time_credit_box.text()
        dialog.entry_case_information.apply_jtc = dialog.jail_time_credit_apply_box.currentText()


class FineOnlyDialogCaseUpdater(CaseUpdater):
    def __init__(self, dialog):
        super().__init__(dialog)
        dialog.add_plea_findings_and_fines_to_entry_case_information()
        self.update_costs_and_fines_information(dialog)
        self.update_jail_time_credit(dialog)
        self.calculate_costs_and_fines(dialog)

    def update_jail_time_credit(self, dialog):
        dialog.entry_case_information.fines_and_costs_jail_credit = dialog.credit_for_jail_checkBox.isChecked()
        dialog.entry_case_information.days_in_jail = dialog.jail_time_credit_box.text()


class NotGuiltyBondDialogCaseUpdater(CaseUpdater):
    def __init__(self, dialog):
        super().__init__(dialog)
        dialog.add_plea_to_entry_case_information()
        self.update_bond_conditions(dialog)

    def update_bond_conditions(self, dialog):
        dialog.transfer_field_data_to_model(dialog.entry_case_information.bond_conditions)
