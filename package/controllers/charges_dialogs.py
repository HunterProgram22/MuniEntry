"""The charges dialogs module contains 'secondary' dialogs that are opened from a
main entry dialog when a charge needs to be added or amended."""
from PyQt5.QtWidgets import QDialog

from package.database_controllers.databases import (
    query_offense_statute_data,
    open_db_connection,
)
from package.models.case_information import AmendOffenseDetails
from package.views.add_charge_dialog_ui import Ui_AddChargeDialog
from package.views.amend_charge_dialog_ui import Ui_AmendChargeDialog
from package.controllers.signal_connectors import (
    AddChargeDialogSignalConnector,
    AmendChargeDialogSignalConnector,
)
from package.controllers.slot_functions import (
    AddChargeDialogSlotFunctions,
    AmendChargeDialogSlotFunctions,
)
from package.controllers.view_modifiers import (
    AddChargeDialogViewModifier,
    AmendChargeDialogViewModifier,
)


class BaseChargeDialog(QDialog):
    """The Base Charge Dialog loads the statutes and offenses from the database as
    both subclasses require access to the statutes and offenses."""

    def __init__(self, main_dialog, parent=None):
        super().__init__(parent)
        self.main_dialog = main_dialog
        self.set_database()
        self.modify_view()
        self.functions = self.create_dialog_slot_functions()
        self.connect_signals_to_slots()
        self.load_statute_and_offense_choice_boxes()

    def set_database(self):
        self.charges_database = open_db_connection("con_charges")

    def load_statute_and_offense_choice_boxes(self):
        """Loads the choice boxes and adds a blank item to set fields to blank on open."""
        self.statute_choice_box.addItems(query_offense_statute_data("statute"))
        self.offense_choice_box.addItems(query_offense_statute_data("offense"))
        self.statute_choice_box.insertItem(0, "")
        self.offense_choice_box.insertItem(0, "")
        self.degree_choice_box.insertItem(0, "")
        self.statute_choice_box.setCurrentText("")
        self.offense_choice_box.setCurrentText("")
        self.degree_choice_box.setCurrentText("")


class AddChargeDialog(BaseChargeDialog, Ui_AddChargeDialog):
    """This class does not need its own init method since it usess the BaseChargeDialog
    init method."""

    def modify_view(self):
        return AddChargeDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        return AddChargeDialogSlotFunctions(self)

    def connect_signals_to_slots(self):
        return AddChargeDialogSignalConnector(self)


class AmendChargeDialog(BaseChargeDialog, Ui_AmendChargeDialog):
    """The amend charge dialog class takes the charge that is being amended and updates
    both the view and the charge in the entry_case_information (model data). In
    AmendChargeDialogSlotFunctions it adds the charge to an amended charge list for use
    in the template of the dialog."""

    def __init__(self, main_dialog, parent=None):
        super().__init__(main_dialog, parent)
        self.amend_offense_details = AmendOffenseDetails()
        self.charge = self.sender().charge
        self.current_offense_name = self.sender().charge.offense
        self.original_charge_label.setText(self.current_offense_name)

    def modify_view(self):
        return AmendChargeDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        return AmendChargeDialogSlotFunctions(self)

    def connect_signals_to_slots(self):
        return AmendChargeDialogSignalConnector(self)
