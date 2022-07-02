"""Secondary dialogs opened from a main entry dialog when a charge needs to be added or amended."""
from typing import TypeVar

from loguru import logger
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QDialog

from package.builders.base_dialogs import CriminalBaseDialog
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
from package.database_controllers.databases import (
    close_db_connection,
    open_db_connection,
    query_offense_statute_data,
)
from package.models.criminal_charge_models import AmendOffenseDetails
from package.views.add_charge_dialog_ui import Ui_AddChargeDialog
from package.views.amend_charge_dialog_ui import Ui_AmendChargeDialog

CBD = TypeVar('CBD', bound=CriminalBaseDialog)


class BaseChargeDialog(QDialog):
    """The Base Charge Dialog loads the statutes and offenses from the database."""

    def __init__(self, main_dialog: CBD, parent: QDialog = None) -> None:
        super().__init__(parent)
        self.main_dialog = main_dialog
        self.db_connection = open_db_connection('con_charges')
        self.modify_view()
        self.functions = self.create_dialog_slot_functions()
        self.connect_signals_to_slots()
        self.load_offense_choice_boxes()
        self.load_statute_choice_boxes()
        self.set_offense_statute_degree_boxes_to_blank()

    def load_offense_choice_boxes(self) -> None:
        offense_list = query_offense_statute_data(self.db_connection, 'offense')
        self.offense_choice_box.addItems(offense_list)
        offense_count = len(offense_list)
        logger.info(f'{offense_count} offenses loaded.')
        self.offense_choice_box.insertItem(0, '')

    def load_statute_choice_boxes(self) -> None:
        statute_list = query_offense_statute_data(self.db_connection, 'statute')
        self.statute_choice_box.addItems(statute_list)
        statute_count = len(statute_list)
        logger.info(f'{statute_count} statutes loaded.')
        self.statute_choice_box.insertItem(0, '')

    def set_offense_statute_degree_boxes_to_blank(self) -> None:
        """Degree choices are loaded in the view, so do not need to be loaded in this method."""
        self.offense_choice_box.setCurrentText('')
        self.statute_choice_box.setCurrentText('')
        self.degree_choice_box.insertItem(0, '')
        self.degree_choice_box.setCurrentText('')

    def closeEvent(self, event: QCloseEvent) -> None:
        logger.log('DIALOG', f'{self.objectName()} Closed')
        close_db_connection(self.db_connection)


class AddChargeDialog(BaseChargeDialog, Ui_AddChargeDialog):
    """Adds a charge to the ChargeGrid for the dialog."""

    def __init__(self, main_dialog: CBD, parent: QDialog = None) -> None:
        super().__init__(main_dialog, parent)
        logger.log('DIALOG', f'{self.objectName()} Opened')

    def modify_view(self) -> AddChargeDialogViewModifier:
        return AddChargeDialogViewModifier(self)

    def connect_signals_to_slots(self) -> None:
        AddChargeDialogSlotFunctions(self)
        AddChargeDialogSignalConnector(self)


class AmendChargeDialog(BaseChargeDialog, Ui_AmendChargeDialog):
    """Updates the charge that is being amended.

    Updates the view and the charge in the entry_case_information (model data). In
    AmendChargeDialogSlotFunctions it adds the charge to an amended charge list for use
    in the template of the dialog.
    """

    def __init__(self, main_dialog: CBD, parent: QDialog = None) -> None:
        super().__init__(main_dialog, parent)
        logger.log('DIALOG', f'{self.objectName()} Opened')
        self.amend_offense_details = AmendOffenseDetails()
        self.charge = self.sender().charge
        self.current_offense_name = self.sender().charge.offense
        self.original_charge_label.setText(self.current_offense_name)

    def modify_view(self) -> AmendChargeDialogViewModifier:
        return AmendChargeDialogViewModifier(self)

    def connect_signals_to_slots(self) -> None:
        AmendChargeDialogSlotFunctions(self)
        AmendChargeDialogSignalConnector(self)


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
