"""The controller module for the LEAP plea dialog."""
from loguru import logger

from views.not_guilty_bond_dialog_ui import Ui_NotGuiltyBondDialog
from models.template_types import TEMPLATE_DICT
from models.case_information import FTABondConditions
from controllers.criminal_dialogs import CriminalPleaDialog
from controllers.conditions_dialogs import AddSpecialBondConditionsDialog


class NotGuiltyBondDialog(CriminalPleaDialog, Ui_NotGuiltyBondDialog):
    """The dialog inherits from the CriminalPleaDialog (controller) and the
    Ui_NotGuiltyBondDialog (view)."""
    @logger.catch
    def __init__(self, judicial_officer, case=None, parent=None):
        super().__init__(judicial_officer, case, parent)
        self.add_special_conditions_dict = {
            self.admin_license_suspension_checkBox:
                self.case_information.admin_license_suspension.ordered,
            self.domestic_violence_checkBox:
                self.case_information.domestic_violence_conditions.ordered,
            self.no_contact_checkBox:
                self.case_information.no_contact.ordered,
            self.custodial_supervision_checkBox:
                self.case_information.custodial_supervision.ordered,
            self.other_conditions_checkBox:
                self.case_information.other_conditions.ordered,
            self.vehicle_seizure_checkBox:
                self.case_information.vehicle_seizure.ordered,
        }
        self.dialog_name = "Not Guilty Bond Dialog"
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.case_information.fta_bond_conditions = FTABondConditions()

    @logger.catch
    def add_charge_to_grid(self):
        self.charges_gridLayout.add_charge_only_to_grid(
            self, add_allied_box=False, add_delete_button=True)
        self.statute_choice_box.setFocus()

    @logger.catch
    def update_case_information(self):
        self.update_party_information()
        self.update_not_guilty_conditions()
        self.update_bond_conditions()
        self.check_add_special_conditions()

    @logger.catch
    def connect_signals_to_slots(self):
        """The method connects additional signals to slots. That are not
        included in the BaseDialog."""
        super().connect_signals_to_slots()
        self.not_guilty_all_Button.pressed.connect(self.set_plea_and_findings_process)
        self.add_special_conditions_Button.pressed.connect(self.start_add_special_bond_conditions_dialog)

    @logger.catch
    def update_not_guilty_conditions(self):
        self.case_information.appearance_reason = self.appearance_reason_box.currentText()
        self.add_dispositions_and_fines()

    @logger.catch
    def update_bond_conditions(self):
        """Updates the bond conditions from the GUI(view) and saves it to the model."""
        self.case_information.fta_bond_conditions.bond_type = \
            self.bond_type_box.currentText()
        self.case_information.fta_bond_conditions.bond_amount = \
            self.bond_amount_box.currentText()
        self.case_information.fta_bond_conditions.no_alcohol_drugs = \
            self.no_alcohol_drugs_checkBox.isChecked()
        self.case_information.fta_bond_conditions.alcohol_drugs_assessment = \
            self.alcohol_drugs_assessment_checkBox.isChecked()
        self.case_information.fta_bond_conditions.alcohol_test_kiosk = \
            self.alcohol_test_kiosk_checkBox.isChecked()
        self.case_information.fta_bond_conditions.specialized_docket = \
            self.specialized_docket_checkBox.isChecked()
        self.case_information.fta_bond_conditions.specialized_docket_type = \
            self.specialized_docket_type_box.currentText()

    @logger.catch
    def check_add_special_conditions(self):
        """Checks to see what conditions in the Add Conditions box are checked and then
        transfers the information from the conditions to case_information model if the
        box is checked.
        TODO: Bug that also exists in check_add_conditions in no_jail_plea dialog
        likely exists here."""
        for key, value in self.add_special_conditions_dict.items():
            if key.isChecked():
                self.add_special_conditions_dict[key] = True
            else:
                self.add_special_conditions_dict[key] = False

    @logger.catch
    def start_add_special_bond_conditions_dialog(self):
        """Opens special conditions for bond."""
        self.check_add_special_conditions()
        AddSpecialBondConditionsDialog(self).exec()
