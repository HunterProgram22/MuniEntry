class CaseUpdater(object):
    """Class responsible for updating case number, date, appearance reasons and party information. Top frame
    on primary dialogs."""
    def __init__(self, dialog):
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
        dialog.entry_case_information.court_costs.balance_due_date = dialog.balance_due_date.date().toString("MMMM dd, yyyy")


    #         NEED TO ADD THIS SOMEWHERE and REFACTOR the METHOD in Criminal Base
    #         self.calculate_costs_and_fines()
    #     except AttributeError:
    #         print("Fix this it exists because of refactoring and not Guilty and add_additional_case_information")
    #         pass


class DiversionDialogCaseUpdater(CaseUpdater):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.update_case_information(dialog)

    def update_case_information(self, dialog):
        dialog.add_plea_findings_and_fines_to_entry_case_information()
        dialog.transfer_field_data_to_model(dialog.entry_case_information.diversion)
        dialog.entry_case_information.diversion.program_name = dialog.entry_case_information.diversion.get_program_name()
        dialog.transfer_field_data_to_model(dialog.entry_case_information.other_conditions)


class JailCCDialogCaseUpdater(CaseUpdater):
    def __init__(self, dialog):
        super().__init__(dialog)
        dialog.add_plea_findings_and_fines_to_entry_case_information()
        self.update_costs_and_fines_information(dialog)
        self.update_jail_time_credit(dialog)

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

    def update_jail_time_credit(self, dialog):
        dialog.entry_case_information.fines_and_costs_jail_credit = dialog.credit_for_jail_checkBox.isChecked()
        dialog.entry_case_information.days_in_jail = dialog.jail_time_credit_box.text()


class NotGuiltyBondDialogCaseUpdater(CaseUpdater):
    def __init__(self, dialog):
        super().__init__(dialog)
        dialog.add_plea_to_entry_case_information()
        self.update_bond_conditions(dialog)

    def update_bond_conditions(self, dialog):
        """Updates the bond conditions from the GUI(view) and saves it to the model."""
        dialog.transfer_field_data_to_model(dialog.entry_case_information.bond_conditions)
