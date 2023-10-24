"""Module containing custom widget Combo Boxes.

If using QtDesigner for creation of the Ui file you must promote the widget to one of the custom
widgets that is used. The header file for this module must then be added in QtDesigner so that
when the file is converted using 'pyuic6 -o {python_view_file.py} {qt_ui_file.ui}' this
module will be imported as part of the python_view_file.py.
"""
from loguru import logger
from PyQt6.QtWidgets import QComboBox, QMenu

from munientry.data.connections import MUNIENTRY_DB_CONN, database_connection
from munientry.sqllite.sql_lite_functions import query_attorney_list
from munientry.widgets.widget_settings import (
    CASE_LIST_BOX_MIN_SIZE,
    COMBO_BOX_MAX_SIZE,
    COMBO_BOX_MIN_SIZE,
    CONTEXT_MENU_POLICY,
    EVENT_KEY_DELETE,
    EVENT_WHEEL_EVENT,
    STRONG_FOCUS,
    WHITE_BACKGROUND_STYLE_SHEET,
)

FIRST_OVI_DESCR_LIST = ['OVI Alcohol / Drugs 1st', 'OVI 1st']
TEXT_DESCR_LIST = ['Driving while texting', 'Text or Access Internet while Driving']


class DailyCaseListComboBox(QComboBox):
    """Custom ComboBox used for Daily Case Lists on Main Window."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFocusPolicy(STRONG_FOCUS)
        self.setEnabled(False)
        self.setMinimumSize(CASE_LIST_BOX_MIN_SIZE)
        self.setStyleSheet(
            'background-color: rgb(255, 255, 255);'
            + 'selection-background-color: rgb(85, 170, 255);',
        )
        self.setEditable(False)
        self.setContextMenuPolicy(CONTEXT_MENU_POLICY)
        self.customContextMenuRequested.connect(self.show_menu)

    def setup_combo_box(self, name, radio_button, main_window):
        self.name = name
        self.radio_button = radio_button
        self.main_window = main_window
        self.radio_button.clicked.connect(self.set_daily_case_list)
        self.radio_button.toggled.connect(self.show_hide_case_list)

    def show_hide_case_list(self):
        if self.radio_button.isChecked():
            self.setEnabled(True)
            self.setHidden(False)
            self.setFocus()
        else:
            self.setCurrentText('')
            self.setEnabled(False)
            self.setHidden(True)

    def set_daily_case_list(self):
        self.main_window.daily_case_list = self

    def show_menu(self, pos):
        menu = QMenu()
        menu.addAction('Delete Case', self.delete_case)
        menu.exec(self.mapToGlobal(pos))

    def delete_case(self):
        index = self.currentIndex()
        case = self.itemText(index)
        self.removeItem(index)
        logger.action(f'Case {case} deleted from {self.objectName()}.')

    def all_items(self) -> list:
        return [self.itemText(index) for index in range(self.count())]

    def keyPressEvent(self, event) -> None:
        super().keyPressEvent(event)
        if event.key() == EVENT_KEY_DELETE:
            self.delete_case()


class NoScrollComboBox(QComboBox):
    """Custom ComboBox used to ignore scroll wheel when mouse hovers over a ComboBox."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFocusPolicy(STRONG_FOCUS)

    def wheelEvent(self, event):
        if event == EVENT_WHEEL_EVENT:
            event.ignore()


class DefenseCounselComboBox(NoScrollComboBox):
    """Custom ComboBox for loading attorneys from internal DB (MuniEntryDB.sqlite)."""

    @database_connection(MUNIENTRY_DB_CONN)
    def load_attorneys(self, db_connection: str):
        attorney_list = query_attorney_list(db_connection)
        attorney_count = len(attorney_list)
        logger.info(f'{attorney_count} attorneys loaded.')
        for attorney in attorney_list:
            self.addItem(attorney)
        self.insertItem(0, '')
        self.setCurrentIndex(0)


class ChargeGridComboBox(NoScrollComboBox):
    """Base Class for Combo Boxes used in the Charges Grid."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(COMBO_BOX_MIN_SIZE)
        self.setMaximumSize(COMBO_BOX_MAX_SIZE)
        self.setStyleSheet(WHITE_BACKGROUND_STYLE_SHEET)
        self.setEditable(False)
        self.setFocusPolicy(STRONG_FOCUS)


class DegreeComboBox(ChargeGridComboBox):
    """Custom ComboBox used for charges grid degree boxes."""

    def __init__(self, degree: str, parent=None) -> None:
        super().__init__(parent)
        self.set_up_widget(degree)

    def set_up_widget(self, degree: str) -> None:
        self.setObjectName('degree_choice_box')
        self.add_degree_box_items(degree)

    def add_degree_box_items(self, degree):
        self.addItem('')
        self.addItem('M1')
        self.addItem('M2')
        self.addItem('M3')
        self.addItem('M4')
        self.addItem('MM')
        self.addItem('UCM')
        self.addItem('No Data')
        self.setCurrentText(degree)


class PleaComboBox(ChargeGridComboBox):
    """Custom ComboBox used for charges grid plea boxes."""

    def __init__(self, column, dialog=None, parent=None):
        super().__init__(parent)
        self.column = column
        self.dialog = dialog
        self.set_up_widget()

    def set_up_widget(self):
        self.setObjectName('plea_choice_box')
        self.add_plea_box_items()

    def add_plea_box_items(self):
        if self.dialog.objectName() == 'TrialSentencingDialog':
            self.addItem('Court')
            self.addItem('Jury')
            self.addItem('Dismissed')
        else:
            self.addItem('')
            self.addItem('Guilty')
            self.addItem('No Contest')
            self.addItem('Not Guilty')
            self.addItem('Dismissed')


class FindingComboBox(ChargeGridComboBox):
    """Custom ComboBox used for charges grid finding boxes."""

    def __init__(self, column, dialog=None, parent=None):
        super().__init__()
        self.column = column
        self.dialog = dialog
        self.charge_grid = self.dialog.charges_gridLayout
        self.case_information = self.dialog.entry_case_information
        self.set_up_widget()
        self.currentTextChanged.connect(self.check_charge)

    def set_up_widget(self):
        self.setObjectName('finding_choice_box')
        self.add_finding_box_items()

    def add_finding_box_items(self):
        self.addItem('')
        self.addItem('Guilty')
        self.addItem('Not Guilty')
        self.addItem('Lesser Included')
        self.addItem('Guilty - Allied Offense')
        self.addItem('Not Guilty - Allied Offense')

    def check_charge(self, text: str):
        """Checks the text of the Finding Box to determine the type of charge to process."""
        charge = self.get_offense_box_text()
        if text == 'Guilty' and charge in FIRST_OVI_DESCR_LIST:
            # charge = 'OVI Alcohol / Drugs 1st'
            self.process_ovi_one_charge(charge)
        elif text == 'Guilty' and charge in TEXT_DESCR_LIST:
            self.process_distracted_driving_charge(charge)

    def get_offense_box_text(self) -> str:
        """Returns the text of an offense box as a string."""
        return self.charge_grid.itemAtPosition(
            self.charge_grid.row_offense, self.column,
        ).widget().text()

    def process_ovi_one_charge(self, charge: str):
        """Runs the process for asking the user if they one to set 1st OVI minimums.

        The ovi_one_mins returns one of 3 options. Yes set mins and dismiss other charges returns 0;
        Yes set mins and do not disimss other charges returns 1; and No returns 2.

        The try/except block is used in case the user uses a dialog that has a finding box, but that
        does not impose jail time (i.e. Fine Only Dialog).
        """
        try:
            bool_response, msg_response = self.case_information.ovi_one_mins()
        except AttributeError as error:
            logger.warning(error)
            return None
        logger.info('OVI Mins message')
        if msg_response == 2:
            return None
        self.update_grid()
        if msg_response == 0:
            self.charge_grid.dismiss_other_charges(charge)

    def process_distracted_driving_charge(self, charge: str):
        logger.debug('Distracted Driving Course Language')

    def update_grid(self) -> None:
        """Updates the UI if the user choses to set the OVI Mins.

        TODO: Refactor out different values based on judicial officer.

        TODO: This should be a general function that updates grid based on the charge.
        """
        self.dialog.community_control_checkBox.setChecked(True)
        self.dialog.license_suspension_checkBox.setChecked(True)
        self.dialog.victim_notification_checkBox.setChecked(True)
        self.charge_grid.itemAtPosition(self.charge_grid.row_jail_days, self.column).widget().setText('180')
        self.charge_grid.itemAtPosition(self.charge_grid.row_jail_days_suspended, self.column).widget().setText('177')
        if self.dialog.entry_case_information.judicial_officer.last_name == 'Hemmeter':
            self.charge_grid.itemAtPosition(self.charge_grid.row_fine, self.column).widget().setText('450')
        else:
            self.charge_grid.itemAtPosition(self.charge_grid.row_fine, self.column).widget().setText('375')
        self.charge_grid.itemAtPosition(self.charge_grid.row_fine_suspended, self.column).widget().setText('0')
