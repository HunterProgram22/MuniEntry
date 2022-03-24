"""Module containing classes responsible for updating case information.
Each main dialog class has a subclass that governs what
is updated for the main class. The classes take the data from the view (GUI) and transfer
it to the appropriate model object."""
from loguru import logger
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
        self.update_case_information()

    def update_case_information(self):
        self.view.add_plea_to_entry_case_information()
        self.transfer_view_data_to_model(self.model.diversion)
        self.model.diversion.program_name = self.model.diversion.get_program_name()
        self.transfer_view_data_to_model(self.model.other_conditions)


class JailCCDialogCaseModelUpdater(CaseModelUpdater):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.update_model_with_case_information_frame_data()
        self.view.add_plea_to_entry_case_information()
        self.update_costs_and_fines_information()
        self.update_jail_time_credit()
        self.calculate_total_jail_days_to_serve()
        self.calculate_costs_and_fines()

    def update_jail_time_credit(self):
        self.model.currently_in_jail = self.view.in_jail_box.currentText()
        self.model.days_in_jail = self.set_jail_time_credit()
        self.model.apply_jtc = self.view.jail_time_credit_apply_box.currentText()

    def set_jail_time_credit(self):
        if self.view.jail_time_credit_box.text() == "":
            return 0
        return int(self.view.jail_time_credit_box.text())

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


class FineOnlyDialogCaseModelUpdater(CaseModelUpdater):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.update_model_with_case_information_frame_data()
        self.view.add_plea_to_entry_case_information()
        self.update_costs_and_fines_information()
        self.update_jail_time_credit_for_fines()
        self.calculate_costs_and_fines()

    def update_jail_time_credit_for_fines(self):
        self.model.fines_and_costs_jail_credit = self.view.credit_for_jail_checkBox.isChecked()
        self.model.days_in_jail = self.view.jail_time_credit_box.text()


class NotGuiltyBondDialogCaseModelUpdater(CaseModelUpdater):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.update_model_with_case_information_frame_data()
        self.add_plea_to_model()
        self.update_bond_conditions()

    def update_bond_conditions(self):
        self.transfer_view_data_to_model(self.model.bond_conditions)

    def add_plea_to_model(self):
        return NotGuiltyPleaAdder(self.view, self.model)


class PleaAdder:
    row_offense = 0
    row_statute = 1
    row_degree = 2

    def __init__(self, view, model):
        self.grid = view.charges_gridLayout
        self.model = model


class NotGuiltyPleaAdder(PleaAdder):
    row_plea = 3

    def __init__(self, view, model):
        super().__init__(view, model)
        self.update_and_add_plea()

    @logger.catch
    def update_and_add_plea(self):
        """This method updates any changes to the statute and degree that were made in the grid and
        adds the plea that is entered for each charge."""
        col = 1
        for charge in self.model.charges_list:
            print(self.grid.columnCount())
            try:
                if self.grid.itemAtPosition(self.row_offense, col) is None:
                    col += 1
            except AttributeError:
                col += 1
            charge.statute = self.grid.itemAtPosition(self.row_statute, col).widget().text()
            charge.degree = self.grid.itemAtPosition(self.row_degree, col).widget().currentText()
            charge.plea = self.grid.itemAtPosition(self.row_plea, col).widget().currentText()
            col += 1


class NoJailPleaFindingFines:
    row_dismissed_box = 3
    row_allied_box = 4
    row_plea = 5
    row_finding = 6
    row_fine = 7
    row_fine_suspended = 8
    row_amend_button = 9
    row_delete_button = 10

    @classmethod
    def add(cls, dialog):
        column = 1
        for index, charge in enumerate(dialog.entry_case_information.charges_list):
            while dialog.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_offense, column) is None:
                column += 1
            charge.statute = dialog.charges_gridLayout.itemAtPosition(
                NoJailPleaFindingFines.row_statute, column).widget().text()
            charge.degree = dialog.charges_gridLayout.itemAtPosition(
                NoJailPleaFindingFines.row_degree, column).widget().currentText()
            charge.plea = dialog.charges_gridLayout.itemAtPosition(
                NoJailPleaFindingFines.row_plea, column).widget().currentText()
            if dialog.charges_gridLayout.itemAtPosition(
                    NoJailPleaFindingFines.row_plea, column).widget().currentText() == "Dismissed":
                charge.finding = ""
                charge.fines_amount = " " # A space is used here b/c otherwise puts 0
                charge.fines_suspended = " " # A space is used here b/c otherwise puts 0
            else:
                charge.finding = dialog.charges_gridLayout.itemAtPosition(
                    NoJailPleaFindingFines.row_finding, column).widget().currentText()
                if dialog.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_fine, column).widget().text() == "":
                    charge.fines_amount = 0
                    charge.fines_amount = f"$ {charge.fines_amount}"
                else:
                    charge.fines_amount = (
                        dialog.charges_gridLayout.itemAtPosition(
                            NoJailPleaFindingFines.row_fine, column).widget().text()
                    )
                    charge.fines_amount = f"$ {charge.fines_amount}"
                if dialog.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_fine_suspended, column).widget().text() == "":
                    charge.fines_suspended = 0
                    charge.fines_suspended = f"$ {charge.fines_suspended}"
                else:
                    charge.fines_suspended = (
                        dialog.charges_gridLayout.itemAtPosition(
                            NoJailPleaFindingFines.row_fine_suspended, column).widget().text()
                    )
                    charge.fines_suspended = f"$ {charge.fines_suspended}"
            column += 1


class JailAddPleaFindingsFinesJail:
    row_offense = 0
    row_statute = 1
    row_degree = 2
    row_dismissed_box = 3
    row_allied_box = 4
    row_plea = 5
    row_finding = 6
    row_fine = 7
    row_fine_suspended = 8
    row_jail_days = 9
    row_jail_days_suspended = 10
    row_amend_button = 11
    row_delete_button = 12

    @classmethod
    def add(cls, dialog):
        column = 1
        for index, charge in enumerate(dialog.entry_case_information.charges_list):
            while dialog.charges_gridLayout.itemAtPosition(JailAddPleaFindingsFinesJail.row_offense, column) is None:
                column += 1
            charge.statute = dialog.charges_gridLayout.itemAtPosition(
                JailAddPleaFindingsFinesJail.row_statute, column).widget().text()
            charge.degree = dialog.charges_gridLayout.itemAtPosition(
                JailAddPleaFindingsFinesJail.row_degree, column).widget().currentText()
            charge.plea = dialog.charges_gridLayout.itemAtPosition(
                JailAddPleaFindingsFinesJail.row_plea, column).widget().currentText()
            if dialog.charges_gridLayout.itemAtPosition(
                    JailAddPleaFindingsFinesJail.row_plea, column).widget().currentText() == "Dismissed":
                charge.finding = ""
                charge.fines_amount = " " # A space is used here b/c otherwise puts 0
                charge.fines_suspended = " " # A space is used here b/c otherwise puts 0
                charge.jail_days = " " # A space is used here b/c otherwise puts None
                charge.jail_days_suspended = " " # A space is used here b/c otherwise puts None
            else:
                charge.finding = dialog.charges_gridLayout.itemAtPosition(
                    JailAddPleaFindingsFinesJail.row_finding, column).widget().currentText()
                if dialog.charges_gridLayout.itemAtPosition(JailAddPleaFindingsFinesJail.row_fine,
                                                            column).widget().text() == "":
                    charge.fines_amount = 0
                    charge.fines_amount = f"$ {charge.fines_amount}"
                else:
                    charge.fines_amount = (
                        dialog.charges_gridLayout.itemAtPosition(
                            JailAddPleaFindingsFinesJail.row_fine, column).widget().text()
                    )
                    charge.fines_amount = f"$ {charge.fines_amount}"
                if dialog.charges_gridLayout.itemAtPosition(JailAddPleaFindingsFinesJail.row_fine_suspended, column).widget().text() == "":
                    charge.fines_suspended = 0
                    charge.fines_suspended = f"$ {charge.fines_suspended}"
                else:
                    charge.fines_suspended = (
                        dialog.charges_gridLayout.itemAtPosition(
                            JailAddPleaFindingsFinesJail.row_fine_suspended, column).widget().text()
                    )
                    charge.fines_suspended = f"$ {charge.fines_suspended}"
                if dialog.charges_gridLayout.itemAtPosition(JailAddPleaFindingsFinesJail.row_jail_days, column).widget().text() == "":
                    charge.jail_days = "None"
                else:
                    charge.jail_days = dialog.charges_gridLayout.itemAtPosition(
                        JailAddPleaFindingsFinesJail.row_jail_days, column).widget().text()
                if dialog.charges_gridLayout.itemAtPosition(JailAddPleaFindingsFinesJail.row_jail_days_suspended, column).widget().text() == "":
                    charge.jail_days_suspended = "None"
                else:
                    charge.jail_days_suspended = dialog.charges_gridLayout.itemAtPosition(
                        JailAddPleaFindingsFinesJail.row_jail_days_suspended, column).widget().text()
            column += 1


