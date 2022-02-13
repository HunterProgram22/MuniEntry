"""The controller module for the LEAP plea dialog."""
from loguru import logger

from package.views.fta_bond_dialog_ui import Ui_FTABondDialog
from package.models.template_types import TEMPLATE_DICT
from package.models.case_information import CriminalCaseInformation, BondConditions
from package.controllers.base_dialogs import BaseDialog


class FTABondDialog(BaseDialog, Ui_FTABondDialog):
    """The dialog inherits from the BaseDialog (controller) and the
    Ui_FTABondDialog (view)."""
    @logger.catch
    def __init__(self, judicial_officer, parent=None):
        super().__init__(parent)
        self.case_information = CriminalCaseInformation(judicial_officer)
        self.dialog_name = "FTA Bond Dialog"
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.fta_bond_conditions = BondConditions()

    @logger.catch
    def update_case_information(self):
        self.set_party_information()
        self.update_fta_conditions()
        self.update_bond_conditions()
        self.case_information.bond_conditions = self.fta_bond_conditions

    @logger.catch
    def update_fta_conditions(self):
        """Updates the fta conditions from the GUI(view) and saves it to the model."""
        self.fta_bond_conditions.appearance_reason = self.appearance_reason_box.currentText()
        self.fta_bond_conditions.forfeit_bond = self.forfeit_bond_box.currentText()
        self.fta_bond_conditions.issue_warrant = self.issue_warrant_box.currentText()
        self.fta_bond_conditions.forfeit_license = self.forfeit_license_box.currentText()
        self.fta_bond_conditions.vehicle_registration_block = self.vehicle_registration_block_box.currentText()

    @logger.catch
    def update_bond_conditions(self):
        """Updates the bond conditions from the GUI(view) and saves it to the model."""
        bond_conditions_list = [
            ("bond_type", "bond_type_box"),
            ("bond_amount", "bond_amount_box"),
            ("no_contact", "no_contact_checkBox"),
            ("no_alcohol_drug", "no_alcohol_drugs_checkBox"),
            ("alcohol_drugs_assessment", "alcohol_drugs_assessment_checkBox"),
            ("alcohol_test_kiosk", "alcohol_test_kiosk_checkBox"),
            ("specialized_docket", "specialized_docket_checkBox"),
            ("monitoring", "monitoring_checkBox"),
            ("monitoring_type", "monitoring_type_box"),
        ]
        self.transfer_field_data_to_model(self.fta_bond_conditions, bond_conditions_list)
        