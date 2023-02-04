"""Secondary dialogs opened from a main entry dialog when a charge needs to be added or amended."""
from loguru import logger

from munientry.builders import base_builders as base
from munientry.sqllite import sql_lite_functions as sql_lite
from munientry.data.connections import close_db_connection, open_db_connection

OFFENSE = 'offense'
STATUTE = 'statute'
DEGREE = 'degree'


class ChargeDialogsViewModifier(base.BaseDialogViewModifier):
    """View builder for both Add and Amend Charge Dialogs."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.load_offense_choice_boxes()
        self.load_statute_choice_boxes()
        self.set_offense_statute_degree_boxes_to_blank()
        self.set_case_information_banner()

    def load_offense_choice_boxes(self) -> None:
        offense_list = sql_lite.query_offense_statute_data(self.dialog.db_connection, OFFENSE)
        self.dialog.offense_choice_box.addItems(offense_list)
        offense_count = len(offense_list)
        logger.info(f'{offense_count} offenses loaded.')
        self.dialog.offense_choice_box.insertItem(0, '')

    def load_statute_choice_boxes(self) -> None:
        statute_list = sql_lite.query_offense_statute_data(self.dialog.db_connection, STATUTE)
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

    def set_case_information_banner(self):
        defendant = self.dialog.main_dialog.entry_case_information.defendant
        defendant_name = f'{defendant.first_name} {defendant.last_name}'
        self.dialog.defendant_name_label.setText(f'State of Ohio v. {defendant_name}')
        self.dialog.case_number_label.setText(
            self.dialog.main_dialog.entry_case_information.case_number,
        )


class ChargeDialogsSlotFunctions(object):
    """Base set of functions for Charge Dialogs."""

    def __init__(self, dialog):
        self.dialog = dialog
        self.main_dialog = dialog.main_dialog

    def clear_charge_fields(self):
        self.dialog.statute_choice_box.setCurrentText('')
        self.dialog.offense_choice_box.setCurrentText('')
        self.dialog.degree_choice_box.setCurrentText('')

    def set_offense(self, key) -> int:
        """Sets the offense and degree for a charge based on the statute.

        Returns 0 if the freeform box is checked so database is not queried.
        """
        if self.dialog.freeform_entry_checkBox.isChecked():
            return 0
        field = STATUTE
        offense, statute, degree = sql_lite.query_charges_database(
            self.dialog.db_connection, key, field,
        )
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
        offense, statute, degree = sql_lite.query_charges_database(
            self.dialog.db_connection, key, field,
        )
        if offense == key:
            self.dialog.statute_choice_box.setCurrentText(statute)
            self.dialog.degree_choice_box.setCurrentText(degree)
        return 1

    def set_freeform_entry(self):
        if self.dialog.freeform_entry_checkBox.isChecked():
            self._enable_freeform()
        else:
            self._disable_freeform()

    def _enable_freeform(self):
        self.dialog.statute_choice_box.setEditable(True)
        self.dialog.offense_choice_box.setEditable(True)
        self.dialog.statute_choice_box.clearEditText()
        self.dialog.offense_choice_box.clearEditText()
        self.dialog.degree_choice_box.setCurrentText('')

    def _disable_freeform(self):
        self.dialog.statute_choice_box.setEditable(False)
        self.dialog.offense_choice_box.setEditable(False)
        self.dialog.statute_choice_box.setCurrentText('')
        self.dialog.offense_choice_box.setCurrentText('')
        self.dialog.degree_choice_box.setCurrentText('')


class ChargeDialogsSignalConnector(object):
    """Signal Connector for Add and Amend Charge Dialogs."""

    def __init__(self, dialog):
        self.dialog = dialog
        self.connect_common_signals()
        self.connect_statute_and_offense_boxes()

    def connect_common_signals(self):
        self.dialog.cancel_Button.released.connect(self.dialog.close)
        self.dialog.clear_fields_Button.released.connect(self.dialog.functions.clear_charge_fields)
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


class ChargeDialogBuilder(base.BaseDialogBuilder):
    """The Base Charge Dialog loads the statutes and offenses from the database."""

    def __init__(self, main_dialog, parent=None) -> None:
        self.main_dialog = main_dialog
        self.db_connection_string = 'con_munientry_db'
        self.db_connection = open_db_connection(self.db_connection_string)
        super().__init__(parent)
        if self.db_connection == 'NO_Connection':
            self.freeform_entry_checkBox.setChecked((True))
        self.additional_setup()
        logger.dialog(f'{self.dialog_name} Opened')

    def additional_setup(self):
        """Abstract base method used in subclasses for additional setup after init."""

    def close(self) -> bool:
        """Extends the close function to close database connection."""
        close_db_connection(self.db_connection)
        super().close()


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
