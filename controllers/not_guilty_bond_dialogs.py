"""The controller module for the LEAP plea dialog."""
from loguru import logger

from views.not_guilty_bond_dialog_ui import Ui_NotGuiltyBondDialog
from models.template_types import TEMPLATE_DICT
from models.case_information import FTABondConditions
from controllers.criminal_dialogs import CriminalPleaDialog, AddSpecialBondConditionsDialog
from .helper_functions import create_entry


class NotGuiltyBondDialog(CriminalPleaDialog, Ui_NotGuiltyBondDialog):
    """The dialog inherits from the CriminalPleaDialog (controller) and the
    Ui_NotGuiltyBondDialog (view)."""
    @logger.catch
    def __init__(self, judicial_officer, case, parent=None):
        super().__init__(judicial_officer, case, parent)
        self.dialog_name = "Not Guilty Bond Dialog"
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.fta_bond_conditions = FTABondConditions()

    @logger.catch
    def add_charge_to_grid(self):
        self.charges_gridLayout.add_charge_only_to_grid(
            self, add_allied_box=False, add_delete_button=True)
        self.statute_choice_box.setFocus()

    @logger.catch
    def create_entry_process(self):
        """The order of functions that are called when the create_entry_Button is pressed()
        on a criminal dialog. The order is important to make sure the information is
        updated before the entry is created."""
        self.update_case_information()
        create_entry(self)
        self.close_event()

    @logger.catch
    def connect_signals_to_slots(self):
        super().connect_signals_to_slots()
        self.not_guilty_all_Button.pressed.connect(self.set_plea_and_findings_process)
        self.add_special_conditions_Button.pressed.connect(self.start_add_special_bond_conditions_dialog)

    @logger.catch
    def update_case_information(self):
        self.update_party_information()
        self.update_not_guilty_conditions()
        self.update_bond_conditions()
        self.case_information.fta_bond_conditions = self.fta_bond_conditions

    @logger.catch
    def update_not_guilty_conditions(self):
        self.case_information.appearance_reason = self.appearance_reason_box.currentText()
        self.add_dispositions_and_fines()

    @logger.catch
    def update_bond_conditions(self):
        """Updates the bond conditions from the GUI(view) and saves it to the model."""
        self.fta_bond_conditions.bond_type = self.bond_type_box.currentText()
        self.fta_bond_conditions.bond_amount = self.bond_amount_box.currentText()
        self.fta_bond_conditions.no_alcohol_drugs = self.no_alcohol_drugs_checkBox.isChecked()
        self.fta_bond_conditions.alcohol_drugs_assessment = self.alcohol_drugs_assessment_checkBox.isChecked()
        self.fta_bond_conditions.alcohol_test_kiosk = self.alcohol_test_kiosk_checkBox.isChecked()
        self.fta_bond_conditions.specialized_docket = self.specialized_docket_checkBox.isChecked()
        self.fta_bond_conditions.specialized_docket_type = self.specialized_docket_type_box.currentText()

    @logger.catch
    def start_add_special_bond_conditions_dialog(self):
        """Opens special conditions for bond."""
        self.update_case_information()
        AddSpecialBondConditionsDialog(self).exec()
