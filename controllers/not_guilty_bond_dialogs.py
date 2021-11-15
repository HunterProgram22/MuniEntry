"""The controller module for the LEAP plea dialog."""
from loguru import logger

from PyQt5.QtCore import QDate

from views.not_guilty_bond_dialog_ui import Ui_NotGuiltyBondDialog
from models.template_types import TEMPLATE_DICT
from models.case_information import CaseInformation, FTABondConditions, NotGuiltyConditions
from controllers.criminal_dialogs import BaseCriminalDialog


class NotGuiltyBondDialog(BaseCriminalDialog, Ui_NotGuiltyBondDialog):
    """The dialog inherits from the BaseCriminalDialog (controller) and the
    Ui_NotGuiltyBondDialog (view)."""
    @logger.catch
    def __init__(self, judicial_officer, case, parent=None):
        super().__init__(judicial_officer, case, parent)
        self.case_information = CaseInformation(judicial_officer)
        self.dialog_name = "Not Guilty Bond Dialog"
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.not_guilty_conditions = NotGuiltyConditions()
        self.fta_bond_conditions = FTABondConditions()
        self.load_arraignment_data()

    @logger.catch
    def load_arraignment_data(self):
        if self.case.case_number != None:
            self.case_number_lineEdit.setText(self.case.case_number)
            self.defendant_first_name_lineEdit.setText(self.case.defendant_first_name)
            self.defendant_last_name_lineEdit.setText(self.case.defendant_last_name)

    @logger.catch
    def modify_view(self):
        super().modify_view()

    @logger.catch
    def connect_signals_to_slots(self):
        super().connect_signals_to_slots()

    @logger.catch
    def update_case_information(self):
        self.update_party_information()
        self.update_not_guilty_conditions()
        self.update_bond_conditions()
        self.case_information.fta_bond_conditions = self.fta_bond_conditions
        self.case_information.not_guilty_conditions = self.not_guilty_conditions

    @logger.catch
    def update_party_information(self):
        super().update_party_information()

    @logger.catch
    def update_not_guilty_conditions(self):
        self.not_guilty_conditions.appearance_reason = self.appearance_reason_box.currentText()
        self.not_guilty_conditions.plea = self.plea_box.currentText()
        if self.speedy_trial_box.currentText() == "Yes":
            self.not_guilty_conditions.waive_speedy_trial = True
        else:
            self.not_guilty_conditions.waive_speedy_trial = False

    @logger.catch
    def update_bond_conditions(self):
        """Updates the bond conditions from the GUI(view) and saves it to the model."""
        self.fta_bond_conditions.bond_type = self.bond_type_box.currentText()
        self.fta_bond_conditions.bond_amount = self.bond_amount_box.currentText()
        self.fta_bond_conditions.no_contact = self.no_contact_checkBox.isChecked()
        self.fta_bond_conditions.no_alcohol_drugs = self.no_alcohol_drugs_checkBox.isChecked()
        self.fta_bond_conditions.alcohol_drugs_assessment = self.alcohol_drugs_assessment_checkBox.isChecked()
        self.fta_bond_conditions.alcohol_test_kiosk = self.alcohol_test_kiosk_checkBox.isChecked()
        self.fta_bond_conditions.specialized_docket = self.specialized_docket_checkBox.isChecked()
        self.fta_bond_conditions.specialized_docket_type = self.specialized_docket_type_box.currentText()
        self.fta_bond_conditions.monitoring = self.monitoring_checkBox.isChecked()
        self.fta_bond_conditions.monitoring_type = self.monitoring_type_box.currentText()
