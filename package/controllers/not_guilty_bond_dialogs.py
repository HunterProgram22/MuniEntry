"""The controller module for the LEAP plea dialog."""
from package.controllers.base_dialogs import CriminalBaseDialog
from loguru import logger
from package.views.custom_widgets import NotGuiltyPleaGrid

from package.views.not_guilty_bond_dialog_ui import Ui_NotGuiltyBondDialog
from package.models.template_types import TEMPLATE_DICT
from package.models.case_information import FTABondConditions
from package.controllers.conditions_dialogs import AddSpecialBondConditionsDialog


class NotGuiltyBondDialog(CriminalBaseDialog, Ui_NotGuiltyBondDialog):
    """The dialog inherits from the CriminalBaseDialog (controller) and the
    Ui_NotGuiltyBondDialog (view)."""
    @logger.catch
    def __init__(self, judicial_officer, case=None, parent=None):
        super().__init__(judicial_officer, case, parent)
        self.charges_gridLayout.__class__ = NotGuiltyPleaGrid
        self.add_special_conditions_dict = {
            self.admin_license_suspension_checkBox:
                self.entry_case_information.admin_license_suspension.ordered,
            self.domestic_violence_checkBox:
                self.entry_case_information.domestic_violence_conditions.ordered,
            self.no_contact_checkBox:
                self.entry_case_information.no_contact.ordered,
            self.custodial_supervision_checkBox:
                self.entry_case_information.custodial_supervision.ordered,
            self.other_conditions_checkBox:
                self.entry_case_information.other_conditions.ordered,
            self.vehicle_seizure_checkBox:
                self.entry_case_information.vehicle_seizure.ordered,
        }
        self.dialog_name = "Not Guilty Bond Dialog"
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.entry_case_information.fta_bond_conditions = FTABondConditions()
        self.load_cms_data_to_view()

    @logger.catch
    def add_charge_to_grid(self):
        self.charges_gridLayout.add_charge_only_to_grid(self)
        self.statute_choice_box.setFocus()

    @logger.catch
    def update_case_information(self):
        super().update_case_information()
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
        self.entry_case_information.appearance_reason = self.appearance_reason_box.currentText()
        self.add_plea_to_entry_case_information()

    @logger.catch
    def update_bond_conditions(self):
        """Updates the bond conditions from the GUI(view) and saves it to the model."""
        bond_conditions_terms_list = [
            ("bond_type", "bond_type_box"),
            ("bond_amount", "bond_amount_box"),
            ("no_alcohol_drugs", "no_alcohol_drugs_checkBox"),
            ("alcohol_drugs_assessment", "alcohol_drugs_assessment_checkBox"),
            ("alcohol_test_kiosk", "alcohol_test_kiosk_checkBox"),
            ("specialized_docket", "specialized_docket_checkBox"),
            ("specialized_docket_type", "specialized_docket_type_box"),
            ("monitoring", "monitoring_checkBox"),
            ("monitoring_type", "monitoring_type_box"),
        ]
        self.widget_type_check_set(self.entry_case_information.fta_bond_conditions, bond_conditions_terms_list)

    @logger.catch
    def check_add_special_conditions(self):
        """Checks to see what conditions in the Add Conditions box are checked and then
        transfers the information from the conditions to entry_case_information model if the
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
