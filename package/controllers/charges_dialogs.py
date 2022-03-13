from PyQt5.QtWidgets import QDialog
from db.databases import create_statute_list, create_offense_list
from loguru import logger
from package.controllers.base_dialogs import charges_database
from package.controllers.signal_connectors import AddChargeDialogSignalConnector, AmendChargeDialogSignalConnector
from package.controllers.slot_functions import AddChargeDialogSlotFunctions, AmendChargeDialogSlotFunctions
from package.controllers.view_modifiers import AddChargeDialogViewModifier, AmendChargeDialogViewModifier
from package.models.case_information import AmendOffenseDetails
from package.views.add_charge_dialog_ui import Ui_AddChargeDialog
from package.views.amend_charge_dialog_ui import Ui_AmendChargeDialog


class BaseChargeDialog(QDialog):
    def __init__(self, main_dialog, button_index=None, parent=None):
        super().__init__(parent)
        self.button_index = button_index
        self.main_dialog = main_dialog
        charges_database.open()
        self.modify_view()
        self.create_dialog_slot_functions()
        self.connect_signals_to_slots()
        self.set_statute_and_offense_choice_boxes()

    def set_statute_and_offense_choice_boxes(self):
        self.statute_choice_box.addItems(create_statute_list())
        self.offense_choice_box.addItems(create_offense_list())
        self.statute_choice_box.setCurrentText("")
        self.offense_choice_box.setCurrentText("")


class AddChargeDialog(BaseChargeDialog, Ui_AddChargeDialog):
    def __init__(self, main_dialog, parent=None):
        super().__init__(main_dialog, parent)

    def modify_view(self):
        return AddChargeDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = AddChargeDialogSlotFunctions(self)

    def connect_signals_to_slots(self):
        return AddChargeDialogSignalConnector(self)


class AmendChargeDialog(BaseChargeDialog, Ui_AmendChargeDialog):
    def __init__(self, main_dialog, parent=None):
        super().__init__(main_dialog, parent)
        self.amend_offense_details = AmendOffenseDetails()
        self.charge = self.sender().charge
        self.current_offense_name = self.sender().charge.offense
        self.original_charge_label.setText(self.current_offense_name)

    def modify_view(self):
        return AmendChargeDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = AmendChargeDialogSlotFunctions(self)

    @logger.catch
    def connect_signals_to_slots(self):
        return AmendChargeDialogSignalConnector(self)