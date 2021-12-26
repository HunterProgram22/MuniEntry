from controllers.base_dialogs import CriminalBaseDialog
from loguru import logger
from models.template_types import TEMPLATE_DICT
from views.jail_cc_plea_dialog_ui import Ui_JailCCPleaDialog


class JailCCPleaDialog(CriminalBaseDialog, Ui_JailCCPleaDialog):
    @logger.catch
    def __init__(self, judicial_officer, case=None, parent=None):
        super().__init__(judicial_officer, case, parent)
        self.dialog_name = 'Jail CC Plea Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)

    def add_charge_to_grid(self):
        self.charges_gridLayout.jail_add_charge_finding_fines_and_jail_to_grid(self)
        self.statute_choice_box.setFocus()


    @logger.catch
    def start_amend_offense_dialog(self, _bool):
        """Opens the amend offense dialog as a modal window. The
        entry_case_information is passed to the dialog class in order to populate
        the cms_case information banner. The _bool is from clicked and not used."""
        self.update_case_information()
        button_index = self.amend_button_list.index(self.sender())
        AmendOffenseDialog(self, self.entry_case_information, button_index).exec()