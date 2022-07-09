"""Module containing the Main Window of the application."""
import os

from loguru import logger
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QComboBox, QMainWindow, QShortcut

from munientry.data.databases import CriminalCaseSQLRetriever
from munientry.mainwindow import (
    main_window_signalconnector,
    main_window_view,
)
from munientry.mainwindow.main_window_slots import MainWindowSlotFunctions
from munientry.models.cms_models import CmsCaseInformation
from munientry.settings import LOG_PATH, USER_LOG_NAME
from munientry.views.main_window_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow, MainWindowSlotFunctions):
    """The main window of the application that is the launching point for all dialogs."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.modify_view()
        self.connect_signals_to_slots()
        self.menu = MainWindowMenu(self)
        self.load_case_lists()
        self.show_hide_daily_case_lists()
        self.judicial_officer = None
        self.dialog = None
        self.case_table = 'None'

    def modify_view(self) -> None:
        main_window_view.MainWindowViewModifier(self)

    def connect_signals_to_slots(self) -> None:
        # self.functions = main_window_slots.MainWindowSlotFunctions(self)
        main_window_signalconnector.MainWindowSignalConnector(self)

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
