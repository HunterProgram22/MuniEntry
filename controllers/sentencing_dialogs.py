from PyQt5 import QtCore
from controllers.base_dialogs import CriminalBaseDialog, CMS_FRALoader
from loguru import logger

from models.template_types import TEMPLATE_DICT
from views.jail_cc_plea_dialog_ui import Ui_JailCCPleaDialog
from views.no_jail_plea_dialog_ui import Ui_NoJailPleaDialog


class CriminalSentencingDialog(CriminalBaseDialog):
    """Subclass for common methods to Sentencing."""
    def __init__(self, judicial_officer, cms_case=None, parent=None):
        super().__init__(judicial_officer, cms_case, parent)
        self.judicial_officer = judicial_officer
        self.cms_case = cms_case

    @logger.catch
    def load_cms_data_to_view(self):
        return CMS_FRALoader(self)

    @logger.catch
    def modify_view(self):
        """Sets the balance due date in the view to today."""
        super().modify_view()
        self.balance_due_date.setDate(QtCore.QDate.currentDate())

    @logger.catch
    def connect_signals_to_slots(self):
        """The method connects additional signals to slots. That are not
        included in the BaseDialog."""
        super().connect_signals_to_slots()
        self.connect_plea_signals_and_slots()

    @logger.catch
    def update_case_information(self):
        """"Docstring needs updating."""
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
        self.add_plea_findings_and_fines_to_entry_case_information()
        self.update_costs_and_fines_information()
        self.check_add_conditions()
        self.calculate_costs_and_fines()

    @logger.catch
    def calculate_costs_and_fines(self):
        """Calculates costs and fines based on the cms_case type (moving, non-moving, criminal) and
        then adds it to any fines that are in the fines_amount box and subtracts fines in the
        fines_suspended box. The loop stops when a cms_case of the highest fine is found because
        court costs are always for the highest charge. The _index is underscored because it is
        not used but is required to unpack enumerate()."""
        self.entry_case_information.court_costs.amount = 0
        if self.court_costs_box.currentText() == "Yes":
            for _index, charge in enumerate(self.entry_case_information.charges_list):
                if self.entry_case_information.court_costs.amount == 124:
                    break
                if charge.type == "Moving Traffic":
                    self.entry_case_information.court_costs.amount = max(self.entry_case_information.court_costs.amount, 124)
                elif charge.type == "Criminal":
                    self.entry_case_information.court_costs.amount = max(self.entry_case_information.court_costs.amount, 114)
                elif charge.type == "Non-moving Traffic":
                    self.entry_case_information.court_costs.amount = max(self.entry_case_information.court_costs.amount, 95)
        total_fines = 0
        try:
            for _index, charge in enumerate(self.entry_case_information.charges_list):
                if charge.fines_amount == '':
                    charge.fines_amount = 0
                total_fines = total_fines + int(charge.fines_amount)
            self.entry_case_information.total_fines = total_fines
            total_fines_suspended = 0
            for _index, charge in enumerate(self.entry_case_information.charges_list):
                if charge.fines_suspended == '':
                    charge.fines_suspended = 0
                total_fines_suspended = total_fines_suspended + int(charge.fines_suspended)
            self.entry_case_information.total_fines_suspended = total_fines_suspended
        except TypeError:
            print("A type error was allowed to pass - this is because of deleted charge.")

    @logger.catch
    def show_costs_and_fines(self, _bool):
        """The _bool is the toggle from the clicked() of the button pressed. No
        action is taken with respect to it."""
        self.update_case_information()
        message = QMessageBox()
        message.setIcon(QMessageBox.Information)
        message.setWindowTitle("Total Costs and Fines")
        # noinspection PyUnresolvedReferences
        message.setInformativeText("Costs: $" + str(self.entry_case_information.court_costs.amount) +
                                   "\nFines: $" + str(self.entry_case_information.total_fines) +
                                   "\nFines Suspended: $" + str(self.entry_case_information.total_fines_suspended) +
                                   "\n\n*Does not include possible bond forfeiture or other costs \n that " +
                                   "may be assessed as a result of prior actions in cms_case. ")
        total_fines_and_costs = \
            (self.entry_case_information.court_costs.amount + self.entry_case_information.total_fines) - \
            self.entry_case_information.total_fines_suspended
        message.setText("Total Costs and Fines Due By Due Date: $" + str(total_fines_and_costs))
        message.setStandardButtons(QMessageBox.Ok)
        message.exec_()



class JailCCPleaDialog(CriminalSentencingDialog, Ui_JailCCPleaDialog):
    @logger.catch
    def __init__(self, judicial_officer, cms_case=None, parent=None):
        super().__init__(judicial_officer, cms_case, parent)
        self.add_conditions_dict = {
            self.license_suspension_checkBox: self.entry_case_information.license_suspension.ordered,
            self.community_service_checkBox: self.entry_case_information.community_service.ordered,
            self.other_conditions_checkBox: self.entry_case_information.other_conditions.ordered,
        }
        self.dialog_name = 'Jail CC Plea Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)

    def add_charge_to_grid(self):
        self.charges_gridLayout.jail_add_charge_finding_fines_and_jail_to_grid(self)
        self.statute_choice_box.setFocus()

    @logger.catch
    def add_plea_findings_and_fines_to_entry_case_information(self):
        return AddPleaFindingsFinesJail(self)

    @logger.catch
    def check_add_conditions(self):
        """TODO: Bug exists where if you uncheck boxes after adding conditions they are still added. This is probably
        because of a dictionary being used. Refactor back away from dictionary?"""
        for key, value in self.add_conditions_dict.items():
            if key.isChecked():
                self.add_conditions_dict[key] = True
            else:
                self.add_conditions_dict[key] = False


class NoJailPleaDialog(CriminalSentencingDialog, Ui_NoJailPleaDialog):
    """The dialog inherits from the CriminalBaseDialog (controller) and the
    Ui_NoJailPleaDialog (view)."""
    @logger.catch
    def __init__(self, judicial_officer, cms_case=None, parent=None):
        super().__init__(judicial_officer, cms_case, parent)
        self.add_conditions_dict = {
            self.license_suspension_checkBox: self.entry_case_information.license_suspension.ordered,
            self.community_service_checkBox: self.entry_case_information.community_service.ordered,
            self.other_conditions_checkBox: self.entry_case_information.other_conditions.ordered,
        }
        self.dialog_name = 'No Jail Plea Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)

    def add_charge_to_grid(self):
        self.charges_gridLayout.no_jail_add_charge_finding_and_fines_to_grid(self)
        self.statute_choice_box.setFocus()

    @logger.catch
    def check_add_conditions(self):
        """TODO: Bug exists where if you uncheck boxes after adding conditions they are still added. This is probably
        because of a dictionary being used. Refactor back away from dictionary?"""
        for key, value in self.add_conditions_dict.items():
            if key.isChecked():
                self.add_conditions_dict[key] = True
            else:
                self.add_conditions_dict[key] = False

    @logger.catch
    def add_plea_findings_and_fines_to_entry_case_information(self):
        return AddPleaFindingsFines(self)


class AddPleaFindingsFines:
    """Row 3 - allied checkbox, Row 4 - plea, 5 - finding, 6 - fine,
    7 fine-suspended. Columns start at 1 because 0 is labels."""
    def __init__(self, dialog):
        self.dialog = dialog
        self.column = 1
        for index, charge in enumerate(self.dialog.entry_case_information.charges_list):
            while self.dialog.charges_gridLayout.itemAtPosition(3, self.column) is None:
                self.column += 1
            charge.plea = self.dialog.charges_gridLayout.itemAtPosition(
                4, self.column).widget().currentText()
            charge.finding = self.dialog.charges_gridLayout.itemAtPosition(
                5, self.column).widget().currentText()
            charge.fines_amount = self.dialog.charges_gridLayout.itemAtPosition(
                6, self.column).widget().text()
            if self.dialog.charges_gridLayout.itemAtPosition(7, self.column).widget().text() == "":
                charge.fines_suspended = "0"
            else:
                charge.fines_suspended = (
                    self.dialog.charges_gridLayout.itemAtPosition(
                        7, self.column).widget().text()
                )
            self.column += 1


class AddPleaFindingsFinesJail:
    def __init__(self, dialog):
        self.dialog = dialog
        self.column = 1
        for index, charge in enumerate(self.dialog.entry_case_information.charges_list):
            while self.dialog.charges_gridLayout.itemAtPosition(3, self.column) is None:
                self.column += 1
            charge.plea = self.dialog.charges_gridLayout.itemAtPosition(
                4, self.column).widget().currentText()
            charge.finding = self.dialog.charges_gridLayout.itemAtPosition(
                5, self.column).widget().currentText()
            charge.fines_amount = self.dialog.charges_gridLayout.itemAtPosition(
                6, self.column).widget().text()
            if self.dialog.charges_gridLayout.itemAtPosition(7, self.column).widget().text() == "":
                charge.fines_suspended = "0"
            else:
                charge.fines_suspended = (
                    self.dialog.charges_gridLayout.itemAtPosition(
                        7, self.column).widget().text()
                )
            if self.dialog.charges_gridLayout.itemAtPosition(8, self.column).widget().text() == "":
                charge.jail_days = "None"
            else:
                charge.jail_days = self.dialog.charges_gridLayout.itemAtPosition(
                    8, self.column).widget().text()
            if self.dialog.charges_gridLayout.itemAtPosition(9, self.column).widget().text() == "":
                charge.jail_days_suspended = "None"
            else:
                charge.jail_days_suspended = self.dialog.charges_gridLayout.itemAtPosition(
                    9, self.column).widget().text()
            self.column += 1


if __name__ == "__main__":
    print("Sentencing Dialogs ran directly")


