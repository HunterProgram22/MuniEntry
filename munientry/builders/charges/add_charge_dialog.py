"""Builder module for Add Charge Dialog."""
from loguru import logger

from munientry.builders.charges import base_charge_builders as charge
from munientry.sqllite.sql_lite_functions import query_offense_type
from munientry.models.criminal_charge_models import CriminalCharge
from munientry.views.add_charge_dialog_ui import Ui_AddChargeDialog


class AddChargeDialogSlotFunctions(charge.ChargeDialogsSlotFunctions):
    """Additional functions for Add Charge Dialog."""

    def add_charge_process(self):
        """The order of functions that are called when the add_charge_Button is clicked().

        The order is important to make sure the information is updated before the charge is added
        and the data cleared from the fields.
        """
        self.add_charge_to_entry_case_information()
        self.add_charge_to_grid()
        self.dialog.close()

    def add_charge_to_entry_case_information(self):
        criminal_charge = CriminalCharge()
        offense = self.dialog.offense_choice_box.currentText()
        statute = self.dialog.statute_choice_box.currentText()
        degree = self.dialog.degree_choice_box.currentText()
        criminal_charge.offense = offense
        criminal_charge.statute = statute
        criminal_charge.degree = degree
        criminal_charge.type = self.set_offense_type()
        self.main_dialog.entry_case_information.add_charge_to_list(criminal_charge)
        logger.info(f'Added Charge: {offense}, {statute}, {degree}')

    def add_charge_to_grid(self):
        self.main_dialog.charges_gridLayout.add_fields_to_charges_grid(self.main_dialog)

    def set_offense_type(self):
        """This calls the internal database and sets the appropriate cms_case type for each charge.

        It does not show up in the view, but is used for calculating costs.
        """
        key = self.dialog.statute_choice_box.currentText()
        if self.dialog.freeform_entry_checkBox.isChecked():
            return None
        return query_offense_type(key, self.dialog.db_connection)


class AddChargeDialogBuilder(charge.ChargeDialogBuilder, Ui_AddChargeDialog):
    """Adds a charge to the ChargeGrid for the dialog."""

    _signal_connector = charge.ChargeDialogsSignalConnector
    _slots = AddChargeDialogSlotFunctions
    _view_modifier = charge.ChargeDialogsViewModifier
    dialog_name = 'Add Charge Dialog'

    def additional_setup(self):
        self.add_charge_Button.released.connect(self.functions.add_charge_process)


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
