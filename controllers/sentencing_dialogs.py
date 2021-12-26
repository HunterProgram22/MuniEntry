from loguru import logger

from controllers.base_dialogs import CriminalSentencingDialog
from models.template_types import TEMPLATE_DICT
from views.jail_cc_plea_dialog_ui import Ui_JailCCPleaDialog
from views.no_jail_plea_dialog_ui import Ui_NoJailPleaDialog


class JailCCPleaDialog(CriminalSentencingDialog, Ui_JailCCPleaDialog):
    @logger.catch
    def __init__(self, judicial_officer, cms_case=None, parent=None):
        super().__init__(judicial_officer, cms_case, parent)
        self.dialog_name = 'Jail CC Plea Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)

    def add_charge_to_grid(self):
        self.charges_gridLayout.jail_add_charge_finding_fines_and_jail_to_grid(self)
        self.statute_choice_box.setFocus()


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


class AddPleaFindingsFines:
    """Row 3 - allied checkbox, Row 4 - plea, 5 - finding, 6 - fine,
    7 fine-suspended. Columns start at 1 because 0 is labels."""
    def __init__(self, dialog):
        self.dialog = dialog
        column = 1
        for index, charge in enumerate(self.dialog.entry_case_information.charges_list):
            while self.dialog.charges_gridLayout.itemAtPosition(3, column) is None:
                column += 1
            charge.plea = self.dialog.charges_gridLayout.itemAtPosition(
                4, column).widget().currentText()
            charge.finding = self.dialog.charges_gridLayout.itemAtPosition(
                5, column).widget().currentText()
            charge.fines_amount = self.dialog.charges_gridLayout.itemAtPosition(
                6, column).widget().text()
            if self.dialog.charges_gridLayout.itemAtPosition(7, column).widget().text() == "":
                charge.fines_suspended = "0"
            else:
                charge.fines_suspended = (
                    self.dialog.charges_gridLayout.itemAtPosition(
                        7, column).widget().text()
                )
            column += 1

if __name__ == "__main__":
    print("Sentencing Dialogs ran directly")


