"""Secondary dialogs opened from a main entry dialog when a charge needs to be added or amended."""
from loguru import logger
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QDialog

from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.data.connections import close_db_connection, open_db_connection
from munientry.data.sql_lite_functions import (
    query_offense_statute_data,
    query_offense_type,
)
from munientry.data.sql_lite_queries import select_off_stat_deg_from_charges_query
from munientry.models.criminal_charge_models import AmendOffenseDetails, CriminalCharge
from munientry.views.add_charge_dialog_ui import Ui_AddChargeDialog
from munientry.views.amend_charge_dialog_ui import Ui_AmendChargeDialog

OFFENSE = 'offense'
STATUTE = 'statute'
DEGREE = 'degree'


class ChargeDialogsViewModifier(crim.CrimTrafficViewModifier):
    """View builder for both Add and Amend Charge Dialogs."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.load_offense_choice_boxes()
        self.load_statute_choice_boxes()
        self.set_offense_statute_degree_boxes_to_blank()
        self.set_case_information_banner()

    def load_offense_choice_boxes(self) -> None:
        offense_list = query_offense_statute_data(self.dialog.db_connection, OFFENSE)
        self.dialog.offense_choice_box.addItems(offense_list)
        offense_count = len(offense_list)
        logger.info(f'{offense_count} offenses loaded.')
        self.dialog.offense_choice_box.insertItem(0, '')

    def load_statute_choice_boxes(self) -> None:
        statute_list = query_offense_statute_data(self.dialog.db_connection, STATUTE)
        self.dialog.statute_choice_box.addItems(statute_list)
        statute_count = len(statute_list)
        logger.info(f'{statute_count} statutes loaded.')
        self.dialog.statute_choice_box.insertItem(0, '')

    def set_offense_statute_degree_boxes_to_blank(self) -> None:
        """Degree choices are loaded in the view, so do not need to be loaded in this method."""
        self.dialog.offense_choice_box.setCurrentText('')
        self.dialog.statute_choice_box.setCurrentText('')
        self.dialog.degree_choice_box.insertItem(0, '')
        self.dialog.degree_choice_box.setCurrentText('')


class BaseChargeDialogsSlotFunctions(object):
    """Base set of functions for Charge Dialogs."""

    def __init__(self, dialog):
        self.dialog = dialog
        self.main_dialog = dialog.main_dialog

    def set_offense(self, key) -> int:
        """Sets the offense and degree for a charge based on the statute.

        Returns 0 if the freeform box is checked so database is not queried.
        """
        if self.dialog.freeform_entry_checkBox.isChecked():
            return 0
        field = STATUTE
        offense, statute, degree = self.query_charges_database(key, field)
        if statute == key:
            self.dialog.offense_choice_box.setCurrentText(offense)
            self.dialog.degree_choice_box.setCurrentText(degree)
        return 1

    def set_statute(self, key) -> int:
        """Sets the statute and degree for a charge based on the offense.

        Returns 0 if the freeform box is checked so database is not queried.
        """
        if self.dialog.freeform_entry_checkBox.isChecked():
            return 0
        field = OFFENSE
        offense, statute, degree = self.query_charges_database(key, field)
        if offense == key:
            self.dialog.statute_choice_box.setCurrentText(statute)
            self.dialog.degree_choice_box.setCurrentText(degree)
        return 1

    def query_charges_database(self, key: str, field: str) -> tuple:
        query_string = select_off_stat_deg_from_charges_query(key, field)
        query = QSqlQuery(self.dialog.db_connection)
        query.prepare(query_string)
        query.exec()
        query.next()
        offense = query.value(OFFENSE)
        statute = query.value(STATUTE)
        degree = query.value(DEGREE)
        query.finish()
        return offense, statute, degree

    def set_freeform_entry(self):
        if self.dialog.freeform_entry_checkBox.isChecked():
            self.dialog.statute_choice_box.setEditable(True)
            self.dialog.offense_choice_box.setEditable(True)
            self.dialog.statute_choice_box.clearEditText()
            self.dialog.offense_choice_box.clearEditText()
            self.dialog.degree_choice_box.setCurrentText('')
        else:
            self.dialog.statute_choice_box.setEditable(False)
            self.dialog.offense_choice_box.setEditable(False)
            self.dialog.statute_choice_box.setCurrentText('')
            self.dialog.offense_choice_box.setCurrentText('')
            self.dialog.degree_choice_box.setCurrentText('')

    def close_window(self):
        self.dialog.close()


class AmendChargeDialogSlotFunctions(BaseChargeDialogsSlotFunctions):
    """Additional functions for Amend Charge Dialog."""

    def clear_amend_charge_fields(self):
        self.dialog.statute_choice_box.setCurrentText('')
        self.dialog.offense_choice_box.setCurrentText('')
        self.dialog.degree_choice_box.setCurrentText('')

    def amend_offense_process(self):
        """Adds the data entered for the amended offense to the AmendOffenseDetails.

        Points the entry_case_information object to the AmendOffenseDetails object.
        """
        self.set_amended_offense_details()
        if self.dialog.motion_decision_box.currentText() == 'Granted':
            self.update_criminal_charge_offense_name()
            self.add_charge_to_amended_charge_list()
            self.update_charges_grid_with_amended_charge()
        self.dialog.functions.close_window()

    def update_criminal_charge_offense_name(self):
        offense_name = self.dialog.current_offense_name
        amended_charge = self.dialog.amend_offense_details.amended_charge
        setattr(
            self.dialog.charge,
            OFFENSE,
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


class AddChargeDialogSlotFunctions(BaseChargeDialogsSlotFunctions):
    """Additional functions for Add Charge Dialog."""

    def clear_add_charge_fields(self):
        self.dialog.statute_choice_box.setCurrentText('')
        self.dialog.offense_choice_box.setCurrentText('')
        self.dialog.degree_choice_box.setCurrentText('')

    def add_charge_process(self):
        """The order of functions that are called when the add_charge_Button is clicked().

        The order is important to make sure the information is updated before the charge is added
        and the data cleared from the fields.
        """
        self.add_charge_to_entry_case_information()
        self.main_dialog.add_charge_to_grid()
        self.dialog.functions.close_window()

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

    def set_offense_type(self):
        """This calls the internal database and sets the appropriate cms_case type for each charge.

        It does not show up in the view, but is used for calculating costs.
        """
        key = self.dialog.statute_choice_box.currentText()
        if self.dialog.freeform_entry_checkBox.isChecked():
            return None
        return query_offense_type(key, self.dialog.db_connection)


class ChargeDialogsSignalConnector(object):
    """Signal Connector for Add and Amend Charge Dialogs."""

    def __init__(self, dialog):
        self.dialog = dialog
        self.connect_common_signals()
        self.connect_statute_and_offense_boxes()

    def connect_common_signals(self):
        self.dialog.cancel_Button.released.connect(self.dialog.functions.close_window)
        self.dialog.freeform_entry_checkBox.toggled.connect(
            self.dialog.functions.set_freeform_entry,
        )

    def connect_statute_and_offense_boxes(self):
        self.dialog.statute_choice_box.currentTextChanged.connect(
            self.dialog.functions.set_offense,
        )
        self.dialog.offense_choice_box.currentTextChanged.connect(
            self.dialog.functions.set_statute,
        )


class BaseChargeDialogBuilder(QDialog):
    """The Base Charge Dialog loads the statutes and offenses from the database."""

    def __init__(self, main_dialog: QDialog, parent: QDialog = None) -> None:
        super().__init__(parent)
        self.main_dialog = main_dialog
        self.build_attrs = self._get_dialog_attributes()
        self.db_connection_string = self.build_attrs.get('db_connection_string')
        self.db_connection = open_db_connection(self.db_connection_string)
        self._modify_view()
        self._connect_signals_to_slots()
        self.dialog_name = self.build_attrs.get('dialog_name')
        self.additional_setup()
        logger.dialog(f'{self.dialog_name} Opened')

    def additional_setup(self):
        """Abstract base method used in subclasses for additional setup after init."""

    def closeEvent(self, _event) -> None:
        """Extends QDialog closeEvent to log and close database connection."""
        logger.dialog(f'{self.objectName()} Closed')
        close_db_connection(self.db_connection)

    def _get_dialog_attributes(self) -> dict:
        return self.build_dict

    def _modify_view(self) -> None:
        self.build_attrs.get('view')(self)

    def _connect_signals_to_slots(self) -> None:
        self.functions = self.build_attrs.get('slots')(self)
        self.build_attrs.get('signals')(self)


class AddChargeDialog(BaseChargeDialogBuilder, Ui_AddChargeDialog):
    """Adds a charge to the ChargeGrid for the dialog."""

    build_dict = {
        'dialog_name': 'Add Charge Dialog',
        'view': ChargeDialogsViewModifier,
        'slots': AddChargeDialogSlotFunctions,
        'signals': ChargeDialogsSignalConnector,
        'db_connection_string': 'con_charges',
    }

    def additional_setup(self):
        self.clear_fields_Button.released.connect(self.functions.clear_add_charge_fields)
        self.add_charge_Button.released.connect(self.functions.add_charge_process)


class AmendChargeDialog(BaseChargeDialogBuilder, Ui_AmendChargeDialog):
    """Updates the charge that is being amended.

    Updates the view and the charge in the entry_case_information (model data). In
    AmendChargeDialogSlotFunctions it adds the charge to an amended charge list for use
    in the template of the dialog.
    """

    build_dict = {
        'dialog_name': 'Amend Charge Dialog',
        'view': ChargeDialogsViewModifier,
        'slots': AmendChargeDialogSlotFunctions,
        'signals': ChargeDialogsSignalConnector,
        'db_connection_string': 'con_charges',
    }

    def additional_setup(self):
        self.clear_fields_Button.released.connect(self.functions.clear_amend_charge_fields)
        self.amend_charge_Button.released.connect(self.functions.amend_offense_process)
        self.amend_offense_details = AmendOffenseDetails()
        self.charge = self.sender().charge
        self.current_offense_name = self.sender().charge.offense
        self.original_charge_label.setText(self.current_offense_name)


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
