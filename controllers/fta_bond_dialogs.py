"""The controller module for the LEAP plea dialog."""
from loguru import logger

from PyQt5.QtCore import QDate

from views.fta_bond_dialog_ui import Ui_FTABondDialog
from models.template_types import TEMPLATE_DICT
from models.case_information import CaseInformation, FTABondConditions
from controllers.criminal_dialogs import BaseCriminalDialog


class FTABondDialog(BaseCriminalDialog, Ui_FTABondDialog):
    """The dialog inherits from the BaseCriminalDialog (controller) and the
    Ui_FTABondDialog (view)."""
    @logger.catch
    def __init__(self, judicial_officer, parent=None):
        super().__init__(parent)
        self.case_information = CaseInformation(judicial_officer)
        self.dialog_name = "FTA Bond Dialog"
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.fta_bond_conditions = FTABondConditions()

    @logger.catch
    def modify_view(self):
        super().modify_view()

    @logger.catch
    def connect_signals_to_slots(self):
        super().connect_signals_to_slots()

    @logger.catch
    def update_case_information(self):
        self.update_party_information()
        self.update_fta_conditions()
        self.case_information.fta_bond_conditions = self.fta_bond_conditions

    @logger.catch
    def update_party_information(self):
        super().update_party_information()

    @logger.catch
    def update_fta_conditions(self):
        """Updates the fta conditions from the GUI(view) and saves it to the model."""
        self.fta_bond_conditions.appearance_reason = self.appearance_reason_box.currentText()
        self.fta_bond_conditions.forefeit_bond = self.forefeit_bond_box.currentText()
        self.fta_bond_conditions.issue_warrant = self.issue_warrant_box.currentText()
        self.fta_bond_conditions.forfeit_license = self.forfeit_license_box.currentText()
        self.fta_bond_conditions.vehicle_registration_block = self.vehicle_registration_block.currentText()
