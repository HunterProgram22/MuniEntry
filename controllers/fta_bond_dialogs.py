"""The controller module for the LEAP plea dialog."""
from loguru import logger

from PyQt5.QtCore import QDate

from views.fta_bond_dialog_ui import Ui_FTABondDialog
from models.template_types import TEMPLATE_DICT
from models.case_information import CaseInformation
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
