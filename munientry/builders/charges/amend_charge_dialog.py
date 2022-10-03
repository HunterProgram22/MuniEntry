"""Builder module for Amend Charge Dialog."""
from loguru import logger

from munientry.builders.charges import base_charge_builders as charge
from munientry.models.criminal_charge_models import AmendOffenseDetails
from munientry.views.amend_charge_dialog_ui import Ui_AmendChargeDialog


class AmendChargeDialogSlotFunctions(charge.ChargeDialogsSlotFunctions):
    """Additional functions for Amend Charge Dialog."""

    def amend_offense_process(self):
        """Adds the data entered for the amended offense to the AmendOffenseDetails.

        Points the entry_case_information object to the AmendOffenseDetails object.
        """
        self.set_amended_offense_details()
        if self.dialog.motion_decision_box.currentText() == 'Granted':
            self.update_criminal_charge_offense_name()
            self.add_charge_to_amended_charge_list()
            self.update_charges_grid_with_amended_charge()
        self.dialog.close()

    def update_criminal_charge_offense_name(self):
        offense_name = self.dialog.current_offense_name
        amended_charge = self.dialog.amend_offense_details.amended_charge
        setattr(
            self.dialog.charge,
            charge.OFFENSE,
            f'{offense_name} - AMENDED to {amended_charge}',
        )
        logger.info(f'Original Charge: {offense_name}')
        logger.info(f'Amended Charge: {amended_charge}')

    def update_charges_grid_with_amended_charge(self):
        grid = self.main_dialog.charges_gridLayout
        offense = self.dialog.current_offense_name
        statute = self.dialog.statute_choice_box.currentText()
        degree = self.dialog.degree_choice_box.currentText()
        amended_charge = self.dialog.amend_offense_details.amended_charge
        for col in range(grid.columnCount()):
            if grid.itemAtPosition(grid.row_offense, col) is None:
                continue
            if grid.itemAtPosition(grid.row_offense, col).widget().text() != offense:
                continue
            grid.itemAtPosition(grid.row_offense, col).widget().setText(
                f'{offense} - AMENDED to {amended_charge}',
            )
            grid.itemAtPosition(grid.row_statute, col).widget().set_up_widget(statute)
            grid.itemAtPosition(grid.row_degree, col).widget().setCurrentText(degree)

    def add_charge_to_amended_charge_list(self):
        self.main_dialog.entry_case_information.amended_charges_list.append(
            (
                self.dialog.amend_offense_details.original_charge,
                self.dialog.amend_offense_details.amended_charge,
            ),
        )

    def set_amended_offense_details(self):
        self.dialog.amend_offense_details.original_charge = (
            self.dialog.current_offense_name
        )
        self.dialog.amend_offense_details.amended_charge = (
            self.dialog.offense_choice_box.currentText()
        )
        self.dialog.amend_offense_details.motion_disposition = (
            self.dialog.motion_decision_box.currentText()
        )
        self.main_dialog.entry_case_information.amend_offense_details = (
            self.dialog.amend_offense_details
        )


class AmendChargeDialogBuilder(charge.ChargeDialogBuilder, Ui_AmendChargeDialog):
    """Updates the charge that is being amended.

    Updates the view and the charge in the entry_case_information (model data). In
    AmendChargeDialogSlotFunctions it adds the charge to an amended charge list for use
    in the template of the dialog.
    """

    build_dict = {
        'dialog_name': 'Amend Charge Dialog',
        'view': charge.ChargeDialogsViewModifier,
        'slots': AmendChargeDialogSlotFunctions,
        'signals': charge.ChargeDialogsSignalConnector,
        'db_connection_string': 'con_charges',
    }

    def additional_setup(self):
        self.amend_charge_Button.released.connect(self.functions.amend_offense_process)
        self.amend_offense_details = AmendOffenseDetails()
        self.charge = self.sender().charge
        self.current_offense_name = self.sender().charge.offense
        self.original_charge_label.setText(self.current_offense_name)


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
