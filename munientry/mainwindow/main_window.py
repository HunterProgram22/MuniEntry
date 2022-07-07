"""Module containing the Main Window of the application."""
import os

from loguru import logger
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QComboBox, QMainWindow, QShortcut

from munientry.builders.sched_entry_dialogs import SchedulingEntryDialog
from munientry.controllers.helper_functions import (
    check_case_list_selected,
    check_judicial_officer,
    set_random_judge,
)
from munientry.data.databases import CriminalCaseSQLRetriever
from munientry.mainwindow.main_window_signalconnector import MainWindowSignalConnector
from munientry.mainwindow.main_window_slots import MainWindowSlotFunctions
from munientry.mainwindow.main_window_view import MainWindowViewModifier
from munientry.models.cms_models import CmsCaseInformation
from munientry.settings import LOG_PATH, USER_LOG_NAME
from munientry.views.main_window_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """The main window of the application that is the launching point for all dialogs."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.modify_view()
        self.connect_signals_to_slots()
        self.menu = MainWindowMenu(self)
        self.functions.load_case_lists()
        self.functions.show_hide_daily_case_lists()
        self.judicial_officer = None
        self.dialog = None
        self.case_table = 'None'

    def modify_view(self) -> None:
        MainWindowViewModifier(self)

    def connect_signals_to_slots(self) -> None:
        self.functions = MainWindowSlotFunctions(self)
        MainWindowSignalConnector(self)

    def set_selected_case_list_table(self) -> None:
        self.case_table = self.daily_case_list_buttons_dict.get(self.sender(), 'None')

    def update_judicial_officer(self) -> None:
        self.judicial_officer = self.judicial_officer_buttons_dict.get(self.sender())

    def set_case_to_load(self, selected_case_table: QComboBox) -> CmsCaseInformation:
        """Returns an empty CmsCaseInformation object if no case is selected.

        Otherwise returns a CmsCaseInformation object via CriminalCaseSQLRetriever().load_case()
        that contains all data from the Cms daily case list reports.
        """
        if selected_case_table.currentText() == '':
            return CmsCaseInformation()
        case_number = selected_case_table.currentText().split('- ')[1]
        return CriminalCaseSQLRetriever(case_number, self.case_table).load_case()

    @check_judicial_officer
    @check_case_list_selected
    def start_dialog_from_entry_button(self) -> None:
        """The decorator checks prevent the dialog execution unless compliant.

        :check_judicial_officer: Requires that a judicial officer is selected.

        'check_case_list_selected: Requires that a daily case list is selected, if no case
        is needed then must select a case list with the field blank.
        """
        selected_case_table = self.database_table_dict.get(self.case_table, QComboBox)
        cms_case_data = self.set_case_to_load(selected_case_table)
        self.dialog = self.dialog_buttons_dict[self.sender()](
            self.judicial_officer,
            cms_case=cms_case_data,
            case_table=self.case_table,
        )
        dialog_name = self.dialog.objectName()
        logger.log('DIALOG', f'{dialog_name} Opened')
        self.dialog.exec()

    @check_case_list_selected
    def start_scheduling_entry(self) -> None:
        selected_case_table = self.database_table_dict.get(self.case_table, QComboBox)
        dialog_name = self.set_scheduling_dialog_name()
        cms_case_data = self.set_case_to_load(selected_case_table)
        self.dialog = SchedulingEntryDialog(
            dialog_name=dialog_name,
            cms_case=cms_case_data,
            case_table=self.case_table,
        )
        logger.log('DIALOG', f'{dialog_name} Opened')
        self.dialog.exec()

    def set_scheduling_dialog_name(self) -> str:
        if self.sender().objectName() == 'rohrer_schedulingEntryButton':
            return 'Rohrer Scheduling Entry'
        if self.sender().objectName() == 'hemmeter_schedulingEntryButton':
            return 'Hemmeter Scheduling Entry'
        return 'None'

    def assign_judge(self):
        assigned_judge, time_now = set_random_judge()
        self.assign_judge_label.setText(assigned_judge)
        self.last_judge_assigned_label.setText(
            f'The last judge assigned was {assigned_judge}.\n'
            + f' The assignment was made at {time_now}.',
        )


class MainWindowMenu(object):
    """Class that builds and connects all signals and functions for the mainwindow menu."""

    def __init__(self, window):
        self.window = window
        self.connect_menu_functions()

    def connect_menu_functions(self) -> None:
        self.window.log_shortcut = QShortcut(QKeySequence('Ctrl+L'), self.window)
        self.window.log_shortcut.activated.connect(self.open_current_log)
        self.window.actionOpen_Current_Log.triggered.connect(self.open_current_log)

    def open_current_log(self, signal=None) -> None:
        os.startfile(f'{LOG_PATH}{USER_LOG_NAME}')
