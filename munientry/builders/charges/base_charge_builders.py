"""Secondary dialogs opened from a main entry dialog when a charge needs to be added or amended."""
from loguru import logger
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QDialog

from munientry.builders import base_builders as base
from munientry.data.connections import close_db_connection, open_db_connection
from munientry.data.sql_lite_functions import (
    query_offense_statute_data,
)
from munientry.data.sql_lite_queries import select_off_stat_deg_from_charges_query

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


class ChargeDialogsSignalConnector(object):
    """Signal Connector for Add and Amend Charge Dialogs."""

    def __init__(self, dialog):
        self.dialog = dialog
        self.connect_common_signals()
        self.connect_statute_and_offense_boxes()

    def connect_common_signals(self):
        self.dialog.cancel_Button.released.connect(self.dialog.functions.close_window)
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


class ChargeDialogBuilder(QDialog):
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


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
