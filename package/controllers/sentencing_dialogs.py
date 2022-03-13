from package.controllers.conditions_dialogs import AddJailOnlyDialog
from package.controllers.base_dialogs import CriminalBaseDialog, CMS_FRALoader
from package.controllers.slot_functions import *


class CriminalSentencingDialog(CriminalBaseDialog):
    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.judicial_officer = judicial_officer
        self.cms_case = cms_case

    def add_charge_to_grid(self):
        self.charges_gridLayout.add_charge_only_to_grid(self)
        self.defense_counsel_name_box.setFocus()

    @logger.catch
    def load_cms_data_to_view(self):
        return CMS_FRALoader(self)

    @logger.catch
    def update_case_information(self):
        super().update_case_information()
        self.add_additional_case_information()

    @logger.catch
    def update_costs_and_fines_information(self):
        """Updates the costs and fines from the GUI(view) and saves it to the model."""
        self.entry_case_information.court_costs.ordered = self.court_costs_box.currentText()
        self.entry_case_information.court_costs.ability_to_pay_time = self.ability_to_pay_box.currentText()
        self.entry_case_information.court_costs.balance_due_date = \
            self.balance_due_date.date().toString("MMMM dd, yyyy")

    def add_additional_case_information(self):
        """The additional conditions are set by the toggling of the Additional Conditions checkbox.
        If the box is checked, but Additional Conditions is not pressed, then conditions will appear
        with None for details. TODO: Add warning box."""
        self.add_plea_findings_and_fines_to_entry_case_information()
        self.update_costs_and_fines_information()
        self.update_jail_time_credit()
        self.calculate_costs_and_fines()

    @logger.catch
    def calculate_costs_and_fines(self):
        """Calculates costs and fines based on the cms_case type (moving, non-moving, criminal) and
        then adds it to any fines that are in the fines_amount box and subtracts fines in the
        fines_suspended box. The loop stops when a cms_case of the highest fine is found because
        court costs are always for the highest charge. The _index is underscored because it is
        not used but is required to unpack enumerate().

        TODO: This needs to be refactored and fixed - code in the AddPlea functions for each dialog have code
        that exists just to deal with this function setting the charge fines/fines_suspended to 0."""
        self.entry_case_information.court_costs.amount = self.calculate_court_costs()
        total_fines = 0
        try:
            for charge in self.entry_case_information.charges_list:
                try:
                    local_charge_fines_amount = int(charge.fines_amount[2:])
                except ValueError:
                    local_charge_fines_amount = 0
                if local_charge_fines_amount == '':
                    local_charge_fines_amount = 0
                try:
                    total_fines = total_fines + int(local_charge_fines_amount)
                except ValueError: # This error catches the " " (space) that is placed if a charge is dismissed.
                    pass
            self.entry_case_information.total_fines = total_fines
            total_fines_suspended = 0
            for _index, charge in enumerate(self.entry_case_information.charges_list):
                try:
                    local_charge_fines_suspended = int(charge.fines_suspended[2:])
                except ValueError:
                    local_charge_fines_suspended = 0
                if local_charge_fines_suspended == '':
                    local_charge_fines_suspended = 0
                try:
                    total_fines_suspended = total_fines_suspended + int(local_charge_fines_suspended)
                except ValueError: # This error catches the " " (space) that is placed if a charge is dismissed.
                    pass
            self.entry_case_information.total_fines_suspended = total_fines_suspended
        except TypeError:
            print("A type error was allowed to pass - this is because of deleted charge.")

    def calculate_court_costs(self):
        self.entry_case_information.court_costs.amount = 0
        if self.court_costs_box.currentText() == "Yes":
            for charge in self.entry_case_information.charges_list:
                if self.entry_case_information.court_costs.amount == 124:
                    break
                if charge.type == "Moving":
                    self.entry_case_information.court_costs.amount = max(
                        self.entry_case_information.court_costs.amount, 124)
                elif charge.type == "Criminal":
                    self.entry_case_information.court_costs.amount = max(
                        self.entry_case_information.court_costs.amount, 114)
                elif charge.type == "Non-moving":
                    self.entry_case_information.court_costs.amount = max(
                        self.entry_case_information.court_costs.amount, 95)
        return self.entry_case_information.court_costs.amount

    @logger.catch
    def start_jail_only_dialog(self):
        self.update_case_information()
        AddJailOnlyDialog(self).exec()


class NoJailPleaFindingFines:
    row_offense = 0
    row_statute = 1
    row_degree = 2
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


if __name__ == "__main__":
    print("Sentencing Dialogs ran directly")
