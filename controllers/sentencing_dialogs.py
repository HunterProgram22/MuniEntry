from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox
from controllers.conditions_dialogs import AddConditionsDialog, AddCommunityControlDialog
from views.custom_widgets import JailChargesGrid, NoJailChargesGrid

from loguru import logger

from models.template_types import TEMPLATE_DICT
from views.jail_cc_plea_dialog_ui import Ui_JailCCPleaDialog
from views.no_jail_plea_dialog_ui import Ui_NoJailPleaDialog
from controllers.base_dialogs import CriminalBaseDialog, CMS_FRALoader


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

    def connect_plea_signals_and_slots(self):
        self.guilty_all_Button.pressed.connect(self.set_plea_and_findings_process)
        self.add_conditions_Button.pressed.connect(self.start_add_conditions_dialog)
        self.fra_in_file_box.currentTextChanged.connect(self.set_fra_in_file)
        self.fra_in_court_box.currentTextChanged.connect(self.set_fra_in_court)
        self.ability_to_pay_box.currentTextChanged.connect(self.set_pay_date)
        self.no_contest_all_Button.pressed.connect(self.set_plea_and_findings_process)
        self.costs_and_fines_Button.clicked.connect(self.show_costs_and_fines)

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
                    self.entry_case_information.court_costs.amount = max(
                        self.entry_case_information.court_costs.amount, 124)
                elif charge.type == "Criminal":
                    self.entry_case_information.court_costs.amount = max(
                        self.entry_case_information.court_costs.amount, 114)
                elif charge.type == "Non-moving Traffic":
                    self.entry_case_information.court_costs.amount = max(
                        self.entry_case_information.court_costs.amount, 95)
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
    def set_fra_in_file(self, current_text):
        """Sets the FRA (proof of insurance) to true if the view indicates 'yes'
        that the FRA was shown in the complaint of file."""
        if current_text == "Yes":
            self.entry_case_information.fra_in_file = True
            self.fra_in_court_box.setCurrentText("No")
        elif current_text == "No":
            self.entry_case_information.fra_in_file = False
        else:
            self.entry_case_information.fra_in_file = None

    @logger.catch
    def set_fra_in_court(self, current_text):
        """Sets the FRA (proof of insurance) to true if the view indicates 'yes'
        that the FRA was shown in court."""
        if current_text == "Yes":
            self.entry_case_information.fra_in_court = True
        elif current_text == "No":
            self.entry_case_information.fra_in_court = False
        else:
            self.entry_case_information.fra_in_court = None

    @logger.catch
    def start_add_conditions_dialog(self):
        """Opens the add conditions dialog as a modal window. It passes the
        instance of the NoJailPleaDialog class (self) as an argument
        so that the AddConditionsDialog can access all data from the
        NoJailPleaDialog when working in the AddConditionsDialog."""
        self.update_case_information()
        AddConditionsDialog(self).exec()


class JailCCPleaDialog(CriminalSentencingDialog, Ui_JailCCPleaDialog):
    @logger.catch
    def __init__(self, judicial_officer, cms_case=None, parent=None):
        super().__init__(judicial_officer, cms_case, parent)
        self.charges_gridLayout.__class__ = JailChargesGrid
        self.add_conditions_dict = {
            self.community_control_checkBox: self.entry_case_information.community_control.ordered,
            self.license_suspension_checkBox: self.entry_case_information.license_suspension.ordered,
            self.community_service_checkBox: self.entry_case_information.community_service.ordered,
            self.jail_checkBox: self.entry_case_information.jail_terms.ordered,
            self.other_conditions_checkBox: self.entry_case_information.other_conditions.ordered,
        }
        self.dialog_name = 'Jail CC Plea Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.load_cms_data_to_view()

    def add_charge_to_grid(self):
        self.charges_gridLayout.add_charge_only_to_grid(self)
        self.statute_choice_box.setFocus()

    def add_additional_case_information(self):
        """This adds jail time credit to the base method."""
        super().add_additional_case_information()
        self.update_jail_time_credit()

    def update_jail_time_credit(self):
        self.entry_case_information.days_in_jail = self.jail_time_credit_box.text()
        self.entry_case_information.apply_jtc = self.jail_time_credit_apply_box.currentText()

    @logger.catch
    def add_plea_findings_and_fines_to_entry_case_information(self):
        return AddPleaFindingsFinesJail(self)

    @logger.catch
    def start_add_conditions_dialog(self):
        """Opens the add conditions dialog as a modal window. It passes the
        instance of the NoJailPleaDialog class (self) as an argument
        so that the AddConditionsDialog can access all data from the
        NoJailPleaDialog when working in the AddConditionsDialog."""
        self.update_case_information()
        AddCommunityControlDialog(self).exec()


class NoJailPleaDialog(CriminalSentencingDialog, Ui_NoJailPleaDialog):
    """The dialog inherits from the CriminalBaseDialog (controller) and the
    Ui_NoJailPleaDialog (view)."""
    @logger.catch
    def __init__(self, judicial_officer, cms_case=None, parent=None):
        super().__init__(judicial_officer, cms_case, parent)
        self.charges_gridLayout.__class__ = NoJailChargesGrid
        self.add_conditions_dict = {
            self.license_suspension_checkBox: self.entry_case_information.license_suspension.ordered,
            self.community_service_checkBox: self.entry_case_information.community_service.ordered,
            self.other_conditions_checkBox: self.entry_case_information.other_conditions.ordered,
        }

        self.dialog_name = 'No Jail Plea Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.load_cms_data_to_view()

    def add_charge_to_grid(self):
        self.charges_gridLayout.add_charge_only_to_grid(self)
        self.statute_choice_box.setFocus()

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
            charge.statute = self.dialog.charges_gridLayout.itemAtPosition(
                1, self.column).widget().text()
            charge.degree = self.dialog.charges_gridLayout.itemAtPosition(
                2, self.column).widget().currentText()
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
            charge.statute = self.dialog.charges_gridLayout.itemAtPosition(
                1, self.column).widget().text()
            charge.degree = self.dialog.charges_gridLayout.itemAtPosition(
                2, self.column).widget().currentText()
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
