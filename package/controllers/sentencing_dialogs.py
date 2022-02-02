from PyQt5 import QtCore
from loguru import logger

from package.controllers.conditions_dialogs import AddConditionsDialog, AddCommunityControlDialog
from package.views.charges_grids import NoJailChargesGrid, JailChargesGrid
from package.models.template_types import TEMPLATE_DICT
from package.views.custom_widgets import InfoBox
from package.views.jail_cc_plea_dialog_ui import Ui_JailCCPleaDialog
from package.views.no_jail_plea_dialog_ui import Ui_NoJailPleaDialog
from package.controllers.base_dialogs import CriminalBaseDialog, CMS_FRALoader


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
                try:
                    total_fines = total_fines + int(charge.fines_amount)
                except ValueError: # This error catches the " " (space) that is placed if a charge is dismissed.
                    pass
            self.entry_case_information.total_fines = total_fines
            total_fines_suspended = 0
            for _index, charge in enumerate(self.entry_case_information.charges_list):
                if charge.fines_suspended == '':
                    charge.fines_suspended = 0
                try:
                    total_fines_suspended = total_fines_suspended + int(charge.fines_suspended)
                except ValueError: # This error catches the " " (space) that is placed if a charge is dismissed.
                    pass
            self.entry_case_information.total_fines_suspended = total_fines_suspended
        except TypeError:
            print("A type error was allowed to pass - this is because of deleted charge.")

    @logger.catch
    def show_costs_and_fines(self, _bool):
        """The _bool is the toggle from the clicked() of the button pressed. No
        action is taken with respect to it."""
        self.update_case_information()
        message = InfoBox()
        message.setWindowTitle("Total Costs and Fines")
        # noinspection PyUnresolvedReferences
        message.setInformativeText("Costs: $" + str(self.entry_case_information.court_costs.amount) +
                                   "\nFines: $" + str(self.entry_case_information.total_fines) +
                                   "\nFines Suspended: $" + str(self.entry_case_information.total_fines_suspended) +
                                   "\n\n*Does not include possible bond forfeiture or other costs \n that " +
                                   "may be assessed as a result of prior actions in the case. ")
        total_fines_and_costs = \
            (self.entry_case_information.court_costs.amount + self.entry_case_information.total_fines) - \
            self.entry_case_information.total_fines_suspended
        message.setText("Total Costs and Fines Due By Due Date: $" + str(total_fines_and_costs))
        message.exec_()

    @logger.catch
    def check_add_conditions(self):
        """TODO: Bug exists where if you uncheck boxes after adding conditions they are still added. This is probably
        because of a dictionary being used. Refactor back away from dictionary?"""
        for items in self.add_conditions_list:
            if items[0].isChecked():
                items[1] = True
            else:
                items[1] = False

        # for key, value in self.add_conditions_dict.items():
        #     if key.isChecked():
        #         self.add_conditions_dict[key] = True
        #         print(value)
        #     else:
        #         self.add_conditions_dict[key] = False
        #         print(value)

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

    def update_jail_time_credit(self):
        self.entry_case_information.days_in_jail = self.jail_time_credit_box.text()
        self.entry_case_information.apply_jtc = self.jail_time_credit_apply_box.currentText()

    @logger.catch
    def add_plea_findings_and_fines_to_entry_case_information(self):
        return JailAddPleaFindingsFinesJail.add(self) # self is dialog

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
        self.add_conditions_list = [
            (self.license_suspension_checkBox, self.entry_case_information.license_suspension.ordered),
            (self.community_service_checkBox, self.entry_case_information.community_service.ordered),
            (self.other_conditions_checkBox, self.entry_case_information.other_conditions.ordered),
        ]

        self.dialog_name = 'No Jail Plea Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.load_cms_data_to_view()
        self.set_fines_credit_for_jail_field()

    @logger.catch
    def connect_signals_to_slots(self):
        """The method connects additional signals to slots. That are not
        included in the BaseDialog or CriminalSentencingDialog."""
        super().connect_signals_to_slots()
        self.credit_for_jail_checkBox.toggled.connect(self.set_fines_credit_for_jail_field)

    def set_fines_credit_for_jail_field(self):
        if self.credit_for_jail_checkBox.isChecked():
            self.jail_time_credit_box.setEnabled(True)
            self.jail_time_credit_box.setHidden(False)
            self.days_in_jail_label.setHidden(False)
        else:
            self.jail_time_credit_box.setEnabled(False)
            self.jail_time_credit_box.setHidden(True)
            self.days_in_jail_label.setHidden(True)

    def add_charge_to_grid(self):
        self.charges_gridLayout.add_charge_only_to_grid(self)
        self.statute_choice_box.setFocus()

    def update_jail_time_credit(self):
        self.entry_case_information.fines_and_costs_jail_credit = self.credit_for_jail_checkBox.isChecked()
        self.entry_case_information.days_in_jail = self.jail_time_credit_box.text()

    @logger.catch
    def add_plea_findings_and_fines_to_entry_case_information(self):
        return NoJailPleaFindingFines.add(self) # self is the dialog


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
