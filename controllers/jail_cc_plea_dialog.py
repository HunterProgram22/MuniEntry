from PyQt5 import QtCore

from controllers.base_dialogs import CriminalBaseDialog, CMS_FRALoader, CriminalSentencingDialog
from loguru import logger
from models.template_types import TEMPLATE_DICT
from views.jail_cc_plea_dialog_ui import Ui_JailCCPleaDialog


class JailCCPleaDialog(CriminalSentencingDialog, Ui_JailCCPleaDialog):
    @logger.catch
    def __init__(self, judicial_officer, cms_case=None, parent=None):
        super().__init__(judicial_officer, cms_case, parent)
        self.dialog_name = 'Jail CC Plea Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)

    def add_charge_to_grid(self):
        self.charges_gridLayout.jail_add_charge_finding_fines_and_jail_to_grid(self)
        self.statute_choice_box.setFocus()
