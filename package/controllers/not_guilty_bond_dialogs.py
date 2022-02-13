"""The controller module for the LEAP plea dialog."""
from package.controllers.base_dialogs import CriminalBaseDialog
from loguru import logger
from package.views.charges_grids import NotGuiltyPleaGrid

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
        self.additional_conditions_list = [
            ("admin_license_suspension_checkBox", self.entry_case_information.admin_license_suspension),
            ("domestic_violence_checkBox", self.entry_case_information.domestic_violence_conditions),
            ("no_contact_checkBox", self.entry_case_information.no_contact),
            ("custodial_supervision_checkBox", self.entry_case_information.custodial_supervision),
            ("other_conditions_checkBox", self.entry_case_information.other_conditions),
            ("vehicle_seizure_checkBox", self.entry_case_information.vehicle_seizure),
        ]
        self.dialog_name = "Not Guilty Bond Dialog"
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.entry_case_information.fta_bond_conditions = FTABondConditions()
        self.load_cms_data_to_view()

    @logger.catch
    def add_charge_to_grid(self):
        self.charges_gridLayout.add_charge_only_to_grid(self)
        self.defense_counsel_name_box.setFocus()

    @logger.catch
    def add_plea_to_entry_case_information(self):
        return NotGuiltyAddPlea.add(self) # self is the dialog

    @logger.catch
    def update_case_information(self):
        super().update_case_information()
        self.update_not_guilty_conditions()
        self.update_bond_conditions()

    @logger.catch
    def connect_signals_to_slots(self):
        """The method connects additional signals to slots. That are not
        included in the BaseDialog."""
        super().connect_signals_to_slots()
        self.not_guilty_all_Button.pressed.connect(self.set_plea_and_findings_process)
        self.add_special_conditions_Button.pressed.connect(self.start_add_special_bond_conditions_dialog)
        self.admin_license_suspension_checkBox.toggled.connect(self.conditions_checkbox_toggle)
        self.domestic_violence_checkBox.toggled.connect(self.conditions_checkbox_toggle)
        self.no_contact_checkBox.toggled.connect(self.conditions_checkbox_toggle)
        self.custodial_supervision_checkBox.toggled.connect(self.conditions_checkbox_toggle)
        self.other_conditions_checkBox.toggled.connect(self.conditions_checkbox_toggle)
        self.vehicle_seizure_checkBox.toggled.connect(self.conditions_checkbox_toggle)


    @logger.catch
    def update_not_guilty_conditions(self):
        self.entry_case_information.appearance_reason = self.appearance_reason_box.currentText()
        self.add_plea_to_entry_case_information()

    @logger.catch
    def update_bond_conditions(self):
        """TODO: Refactor this like other conditions.
        Updates the bond conditions from the GUI(view) and saves it to the model."""
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
        self.transfer_field_data_to_model(self.entry_case_information.fta_bond_conditions, bond_conditions_terms_list)

    def conditions_checkbox_toggle(self):
        if self.sender().isChecked():
            for items in self.additional_conditions_list:
                if items[0] == self.sender().objectName():
                    setattr(items[1], "ordered", True)
        else:
            for items in self.additional_conditions_list:
                if items[0] == self.sender().objectName():
                    setattr(items[1], "ordered", False)

    @logger.catch
    def start_add_special_bond_conditions_dialog(self):
        """Opens special conditions for bond."""
        self.update_case_information()
        AddSpecialBondConditionsDialog(self).exec()


class NotGuiltyAddPlea:
    row_offense = 0
    row_statute = 1
    row_degree = 2
    row_plea = 3

    @classmethod
    def add(cls, dialog):
        column = 1
        for index, charge in enumerate(dialog.entry_case_information.charges_list):
            while dialog.charges_gridLayout.itemAtPosition(NotGuiltyAddPlea.row_offense, column) is None:
                column += 1
            charge.statute = dialog.charges_gridLayout.itemAtPosition(
                NotGuiltyAddPlea.row_statute, column).widget().text()
            charge.degree = dialog.charges_gridLayout.itemAtPosition(
                NotGuiltyAddPlea.row_degree, column).widget().currentText()
            charge.plea = dialog.charges_gridLayout.itemAtPosition(
                NotGuiltyAddPlea.row_plea, column).widget().currentText()
            column += 1
