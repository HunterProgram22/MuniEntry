"""Module containing custom widget Combo Boxes.

If using QtDesigner for creation of the Ui file you must promote the widget to one of the custom
widgets that is used. The header file for this module must then be added in QtDesigner so that
when the file is converted using 'pyuic6 -o {python_view_file.py} {qt_ui_file.ui}' this
module will be imported as part of the python_view_file.py.
"""
from loguru import logger
from PyQt6.QtWidgets import QComboBox, QMenu

from munientry.data.connections import close_db_connection, open_db_connection
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

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFocusPolicy(STRONG_FOCUS)

    def load_attorneys(self):
        db_connection = open_db_connection('con_munientry_db')
        attorney_list = query_attorney_list(db_connection)
        attorney_count = len(attorney_list)
        logger.info(f'{attorney_count} attorneys loaded.')
        for attorney in attorney_list:
            self.addItem(attorney)
        close_db_connection(db_connection)
        # self.insertItem(0, '')
        # self.setCurrentIndex(0)


class DegreeComboBox(NoScrollComboBox):
    """Custom ComboBox used for charges grid degree boxes."""

    def __init__(self, degree, parent=None):
        super().__init__(parent)
        self.set_up_widget(degree)

    def set_up_widget(self, degree):
        self.setMinimumSize(COMBO_BOX_MIN_SIZE)
        self.setMaximumSize(COMBO_BOX_MAX_SIZE)
        self.setStyleSheet(WHITE_BACKGROUND_STYLE_SHEET)
        self.setEditable(False)
        self.setFocusPolicy(STRONG_FOCUS)
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


class PleaComboBox(NoScrollComboBox):
    """Custom ComboBox used for charges grid plea boxes."""

    def __init__(self, column, dialog=None, parent=None):
        super().__init__(parent)
        self.column = column
        self.dialog = dialog
        self.set_up_widget()

    def set_up_widget(self):
        self.setMinimumSize(COMBO_BOX_MIN_SIZE)
        self.setMaximumSize(COMBO_BOX_MAX_SIZE)
        self.setStyleSheet(WHITE_BACKGROUND_STYLE_SHEET)
        self.setEditable(False)
        self.setFocusPolicy(STRONG_FOCUS)
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


class FindingComboBox(NoScrollComboBox):
    """Custom ComboBox used for charges grid finding boxes."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.set_up_widget()

    def set_up_widget(self):
        self.setMinimumSize(COMBO_BOX_MIN_SIZE)
        self.setMaximumSize(COMBO_BOX_MAX_SIZE)
        self.setStyleSheet(WHITE_BACKGROUND_STYLE_SHEET)
        self.setEditable(False)
        self.setFocusPolicy(STRONG_FOCUS)
        self.setObjectName('finding_choice_box')
        self.add_finding_box_items()

    def add_finding_box_items(self):
        self.addItem('')
        self.addItem('Guilty')
        self.addItem('Not Guilty')
        self.addItem('Lesser Included')
        self.addItem('Guilty - Allied Offense')
        self.addItem('Not Guilty - Allied Offense')
