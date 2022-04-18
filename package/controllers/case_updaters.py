"""Module containing classes responsible for updating case information.
Each main dialog class has a subclass that governs what
is updated for the main class. The classes take the data from the view (GUI) and transfer
it to the appropriate model object."""
from PyQt5.QtWidgets import (
    QDialog,
    QComboBox,
    QCheckBox,
    QLineEdit,
    QTextEdit,
    QDateEdit,
    QTimeEdit,
    QRadioButton,
)

from settings import MOVING_COURT_COSTS, CRIMINAL_COURT_COSTS, NONMOVING_COURT_COSTS


class CaseModelUpdater:
    """Base class that contains methods used by subclasses and is called by a main
    entry dialog to update the entry_case_information (model data)."""

    def __init__(self, dialog):
        self.view = dialog
        self.model = dialog.entry_case_information

    def update_model_with_case_information_frame_data(self):
        """Calls the methods that update all model with all fields in the case information (top
        frame) in all main entry dialogs."""
        self.set_case_number_and_date()
        self.set_party_information()
        self.set_defense_counsel_information()
        self.set_appearance_reason()

    def set_case_number_and_date(self):
        self.model.case_number = self.view.case_number_lineEdit.text()
        self.model.plea_trial_date = self.view.plea_trial_date.date().toString("MMMM dd, yyyy")

    def set_party_information(self):
        self.model.defendant.first_name = self.view.defendant_first_name_lineEdit.text()
        self.model.defendant.last_name = self.view.defendant_last_name_lineEdit.text()

    def set_defense_counsel_information(self):
        self.model.defense_counsel = self.view.defense_counsel_name_box.currentText()
        self.model.defense_counsel_type = self.view.defense_counsel_type_box.currentText()
        self.model.defense_counsel_waived = self.view.defense_counsel_waived_checkBox.isChecked()

    def set_appearance_reason(self):
        self.model.appearance_reason = self.view.appearance_reason_box.currentText()

    def update_costs_and_fines_information(self):
        self.model.court_costs.ordered = self.view.court_costs_box.currentText()
        self.model.court_costs.ability_to_pay_time = self.view.ability_to_pay_box.currentText()
        self.model.court_costs.balance_due_date = self.view.balance_due_date.date().toString(
            "MMMM dd, yyyy"
        )

    def calculate_costs_and_fines(self):
        self.model.court_costs.amount = self.calculate_court_costs()
        self.model.total_fines = self.calculate_total_fines()
        self.model.total_fines_suspended = self.calculate_total_fines_suspended()

    def calculate_court_costs(self):
        court_costs = 0
        if self.view.court_costs_box.currentText() == "Yes":
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

    def transfer_view_data_to_model(self, terms_object):
        """Function that loops through a list of fields and transfers the data in the field
        to the appropriate model attribute. The function uses the appropriate pyqt method for
        the field type. Format of item in terms_list is a list of tuples (item[0] = model data,
        item[1] = view field that contains the data)."""
        terms_list = getattr(terms_object, "terms_list")
        for item in terms_list:
            (model_attribute, view_field) = item
            if isinstance(getattr(self.view, view_field), QComboBox):
                setattr(
                    terms_object,
                    model_attribute,
                    getattr(self.view, view_field).currentText(),
                )
            elif isinstance(getattr(self.view, view_field), QCheckBox):
                setattr(
                    terms_object,
                    model_attribute,
                    getattr(self.view, view_field).isChecked(),
                )
            elif isinstance(getattr(self.view, view_field), QRadioButton):
                setattr(
                    terms_object,
                    model_attribute,
                    getattr(self.view, view_field).isChecked(),
                )
            elif isinstance(getattr(self.view, view_field), QLineEdit):
                setattr(terms_object, model_attribute, getattr(self.view, view_field).text())
            elif isinstance(getattr(self.view, view_field), QTextEdit):
                plain_text = getattr(self.view, view_field).toPlainText()
                try:
                    if plain_text[-1] == ".":
                        plain_text = plain_text[:-1]
                except IndexError:
                    pass
                setattr(terms_object, model_attribute, plain_text)
            elif isinstance(getattr(self.view, view_field), QDateEdit):
                setattr(
                    terms_object,
                    model_attribute,
                    getattr(self.view, view_field).date().toString("MMMM dd, yyyy"),
                )
            elif isinstance(getattr(self.view, view_field), QTimeEdit):
                setattr(
                    terms_object,
                    model_attribute,
                    getattr(self.view, view_field).time().toString("hh:mm A"),
                )


class DiversionDialogCaseModelUpdater(CaseModelUpdater):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.update_model_with_case_information_frame_data()
        self.update_model_with_charge_grid_data()
        self.update_case_information()

    def update_case_information(self):
        self.transfer_view_data_to_model(self.model.diversion)
        self.model.diversion.program_name = self.model.diversion.get_program_name()
        self.transfer_view_data_to_model(self.model.other_conditions)

    def update_model_with_charge_grid_data(self):
        return DiversionGridModelUpdater(self.view, self.model)


class JailCCDialogCaseModelUpdater(CaseModelUpdater):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.update_model_with_case_information_frame_data()
        self.update_model_with_charge_grid_data()
        self.update_costs_and_fines_information()
        self.update_jail_time_credit()
        self.calculate_total_jail_days_to_serve()
        self.calculate_costs_and_fines()
        self.update_offense_of_violence()

    def update_model_with_charge_grid_data(self):
        return JailCCGridModelUpdater(self.view, self.model)

    def update_jail_time_credit(self):
        self.model.jail_terms.currently_in_jail = self.view.in_jail_box.currentText()
        self.model.jail_terms.days_in_jail = self.set_jail_time_credit()
        self.model.jail_terms.apply_jtc = self.view.jail_time_credit_apply_box.currentText()
        self.model.jail_terms.companion_cases_exist = self.view.add_companion_cases_checkBox.isChecked()
        self.model.jail_terms.companion_cases_numbers = self.view.companion_cases_box.text()
        self.model.jail_terms.companion_cases_sentence_type = self.view.companion_cases_sentence_box.currentText()

    def set_jail_time_credit(self):
        if self.view.jail_time_credit_box.text() == "":
            return 0
        return int(self.view.jail_time_credit_box.text())

    def calculate_total_jail_days_to_serve(self):
        self.model.jail_terms.total_jail_days_imposed = self.calculate_total_jail_days_imposed()
        self.model.jail_terms.total_jail_days_suspended = self.calculate_total_jail_days_suspended()
        self.model.jail_terms.total_jail_days_to_serve = int(self.model.jail_terms.total_jail_days_imposed) - int(
            self.model.jail_terms.total_jail_days_suspended
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

    def update_offense_of_violence(self):
        if self.view.offense_of_violence_checkBox.isChecked():
            self.model.offense_of_violence = True
        else:
            self.model.offense_of_violence = False


class FineOnlyDialogCaseModelUpdater(CaseModelUpdater):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.update_model_with_case_information_frame_data()
        self.update_model_with_charge_grid_data()
        self.update_costs_and_fines_information()
        self.update_jail_time_credit_for_fines()
        self.calculate_costs_and_fines()

    def update_jail_time_credit_for_fines(self):
        self.model.fines_and_costs_jail_credit = self.view.credit_for_jail_checkBox.isChecked()
        self.model.fine_jail_days = self.view.jail_time_credit_box.text()

    def update_model_with_charge_grid_data(self):
        return FineOnlyGridModelUpdater(self.view, self.model)


class PleaOnlyDialogCaseModelUpdater(CaseModelUpdater):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.update_model_with_case_information_frame_data()
        self.update_model_with_charge_grid_data()
        self.update_model_with_future_sentencing()

    def update_model_with_charge_grid_data(self):
        return PleaOnlyGridModelUpdater(self.view, self.model)

    def update_model_with_future_sentencing(self):
        self.transfer_view_data_to_model(self.model.future_sentencing)


class NotGuiltyBondDialogCaseModelUpdater(CaseModelUpdater):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.update_model_with_case_information_frame_data()
        self.update_model_with_charge_grid_data()
        self.update_bond_conditions()

    def update_bond_conditions(self):
        self.transfer_view_data_to_model(self.model.bond_conditions)

    def update_model_with_charge_grid_data(self):
        return NotGuiltyGridModelUpdater(self.view, self.model)


class BondHearingDialogCaseModelUpdater(CaseModelUpdater):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.update_model_with_case_information_frame_data()
        self.update_bond_conditions()

    def update_bond_conditions(self):
        self.transfer_view_data_to_model(self.model.bond_conditions)


class FailureToAppearDialogCaseModelUpdater(CaseModelUpdater):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.update_model_with_case_information_frame_data()
        self.update_fta_conditions()

    def update_fta_conditions(self):
        self.transfer_view_data_to_model(self.model.fta_conditions)


class ProbationViolationBondDialogCaseModelUpdater(CaseModelUpdater):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.update_model_with_case_information_frame_data()
        self.update_model_with_probable_cause_information()
        self.update_bond_conditions()

    def update_model_with_probable_cause_information(self):
        self.model.cc_violation_probable_cause = self.view.probable_cause_finding_box.currentText()

    def update_bond_conditions(self):
        """This uses a cc_bond_conditions instead of bond_conditions because a separate model
        was created. TODO: Refactor models"""
        self.transfer_view_data_to_model(self.model.cc_bond_conditions)


class GridModelUpdater:
    row_offense = 0
    row_statute = 1
    row_degree = 2

    def __init__(self, view, model):
        self.grid = view.charges_gridLayout
        self.model = model

    def update_model_with_plea_finding_grid_data(self):
        """This method updates any changes to the statute and degree that were made in the grid and
        adds the plea that is entered for each charge. TODO: This should be refactored b/c dismissed
        does not apply to Not Guilty - did a Hotfix to fix NotGuilty."""
        col = 1
        for charge in self.model.charges_list:
            while self.grid.itemAtPosition(self.row_offense, col) is None:
                col += 1
            charge.statute = self.grid.itemAtPosition(self.row_statute, col).widget().text()
            charge.degree = self.grid.itemAtPosition(self.row_degree, col).widget().currentText()
            charge.plea = self.grid.itemAtPosition(self.row_plea, col).widget().currentText()
            if self.grid.itemAtPosition(self.row_plea, col).widget().currentText() == "Dismissed":
                charge.finding = ""
            else:
                charge.finding = (
                    self.grid.itemAtPosition(self.row_finding, col).widget().currentText()
                )
            col += 1


class NotGuiltyGridModelUpdater(GridModelUpdater):
    row_plea = 3

    def __init__(self, view, model):
        super().__init__(view, model)
        self.update_model_with_plea_grid_data()

    def update_model_with_plea_grid_data(self):
        """This method updates any changes to the statute and degree that were made in the grid and
        adds the plea that is entered for each charge."""
        col = 1
        for charge in self.model.charges_list:
            while self.grid.itemAtPosition(self.row_offense, col) is None:
                col += 1
            charge.statute = self.grid.itemAtPosition(self.row_statute, col).widget().text()
            charge.degree = self.grid.itemAtPosition(self.row_degree, col).widget().currentText()
            charge.plea = self.grid.itemAtPosition(self.row_plea, col).widget().currentText()
            col += 1


class PleaOnlyGridModelUpdater(GridModelUpdater):
    row_dismissed_box = 3
    row_allied_box = 4
    row_plea = 5
    row_finding = 6
    row_amend_button = 7
    row_delete_button = 8

    def __init__(self, view, model):
        super().__init__(view, model)
        self.update_model_with_plea_finding_grid_data()


class FineOnlyGridModelUpdater(GridModelUpdater):
    row_dismissed_box = 3
    row_allied_box = 4
    row_plea = 5
    row_finding = 6
    row_fine = 7
    row_fine_suspended = 8
    row_amend_button = 9
    row_delete_button = 10

    def __init__(self, view, model):
        super().__init__(view, model)
        self.update_model_with_plea_finding_grid_data()
        self.update_model_with_fine_grid_data()

    def update_model_with_fine_grid_data(self):
        col = 1
        for charge in self.model.charges_list:
            while self.grid.itemAtPosition(self.row_offense, col) is None:
                col += 1
            if self.grid.itemAtPosition(self.row_plea, col).widget().currentText() == "Dismissed":
                charge.fines_amount = " "  # A space is used here b/c otherwise puts 0
                charge.fines_suspended = " "  # A space is used here b/c otherwise puts 0
            else:
                self.update_model_with_fines(charge, col)
                self.update_model_with_fines_suspended(charge, col)
            col += 1

    def update_model_with_fines(self, charge, col):
        if self.grid.itemAtPosition(self.row_fine, col).widget().text() == "":
            charge.fines_amount = 0
            charge.fines_amount = f"$ {charge.fines_amount}"
        else:
            charge.fines_amount = self.grid.itemAtPosition(self.row_fine, col).widget().text()
            charge.fines_amount = f"$ {charge.fines_amount}"

    def update_model_with_fines_suspended(self, charge, col):
        if self.grid.itemAtPosition(self.row_fine_suspended, col).widget().text() == "":
            charge.fines_suspended = 0
            charge.fines_suspended = f"$ {charge.fines_suspended}"
        else:
            charge.fines_suspended = (
                self.grid.itemAtPosition(self.row_fine_suspended, col).widget().text()
            )
            charge.fines_suspended = f"$ {charge.fines_suspended}"


class JailCCGridModelUpdater(FineOnlyGridModelUpdater):
    row_jail_days = 9
    row_jail_days_suspended = 10
    row_amend_button = 11
    row_delete_button = 12

    def __init__(self, view, model):
        """The call to super init of JailCCGridModelUpdater calls the updates
        to plea and findings of FinesOnlyGridModelUpdater."""
        super().__init__(view, model)
        self.update_model_with_jail_grid_data()

    def update_model_with_jail_grid_data(self):
        col = 1
        for charge in self.model.charges_list:
            while self.grid.itemAtPosition(self.row_offense, col) is None:
                col += 1
            if self.grid.itemAtPosition(self.row_plea, col).widget().currentText() == "Dismissed":
                charge.jail_days = " "  # A space is used here b/c otherwise puts None
                charge.jail_days_suspended = " "  # A space is used here b/c otherwise puts None
            else:
                self.update_model_with_jail_imposed(charge, col)
                self.update_model_with_jail_suspended(charge, col)
            col += 1

    def update_model_with_jail_imposed(self, charge, col):
        if self.grid.itemAtPosition(self.row_jail_days, col).widget().text() == "":
            charge.jail_days = "None"
        else:
            charge.jail_days = self.grid.itemAtPosition(self.row_jail_days, col).widget().text()

    def update_model_with_jail_suspended(self, charge, col):
        if self.grid.itemAtPosition(self.row_jail_days_suspended, col).widget().text() == "":
            charge.jail_days_suspended = "None"
        else:
            charge.jail_days_suspended = (
                self.grid.itemAtPosition(self.row_jail_days_suspended, col).widget().text()
            )


class DiversionGridModelUpdater(JailCCGridModelUpdater):
    def __init__(self, view, model):
        """The call to super init of DiversionGridModelUpdater calls the updates
        to plea and findings and jail of JailCCGridModelUpdater."""
        super().__init__(view, model)
