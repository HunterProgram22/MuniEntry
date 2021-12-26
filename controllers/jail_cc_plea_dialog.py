from PyQt5 import QtCore

from controllers.base_dialogs import CriminalBaseDialog, CMS_FRALoader
from loguru import logger
from models.template_types import TEMPLATE_DICT
from views.jail_cc_plea_dialog_ui import Ui_JailCCPleaDialog


class JailCCPleaDialog(CriminalBaseDialog, Ui_JailCCPleaDialog):
    @logger.catch
    def __init__(self, judicial_officer, case=None, parent=None):
        super().__init__(judicial_officer, case, parent)
        self.dialog_name = 'Jail CC Plea Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)

    @logger.catch
    def load_cms_data_to_view(self):
        return CMS_FRALoader(self)

    @logger.catch
    def modify_view(self):
        """Sets the balance due date in the view to today."""
        super().modify_view()
        self.balance_due_date.setDate(QtCore.QDate.currentDate())

    @logger.catch
    def connect_signals_to_slots(self):
        """The method connects additional signals to slots. That are not
        included in the BaseDialog."""
        super().connect_signals_to_slots()
        self.connect_plea_signals_and_slots()

    @logger.catch
    def update_case_information(self):
        """"Docstring needs updating."""
        super().update_case_information()
        self.add_additional_case_information()

    def add_charge_to_grid(self):
        self.charges_gridLayout.jail_add_charge_finding_fines_and_jail_to_grid(self)
        self.statute_choice_box.setFocus()

