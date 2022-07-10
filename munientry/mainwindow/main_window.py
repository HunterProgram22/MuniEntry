"""Module containing the Main Window of the application."""
import os

from loguru import logger
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QComboBox, QInputDialog, QMainWindow, QShortcut

from munientry.data.databases import CriminalCaseSQLRetriever
from munientry.mainwindow import main_window_signalconnector, main_window_view
from munientry.mainwindow.main_window_slots import MainWindowSlotFunctionsMixin
from munientry.models.cms_models import CmsCaseInformation
from munientry.models.party_types import JudicialOfficer
from munientry.settings import LOG_PATH, USER_LOG_NAME
from munientry.views.main_window_ui import Ui_MainWindow


def open_current_log(signal=None) -> None:
    """Menu function that opens the user logs directly or with keyboard shortcut."""
    if signal is False:
        signal = 'Menu'
    else:
        signal = 'Keyboard Shortcut'
    logger.info(f'Log opened from {signal}.')
    os.startfile(f'{LOG_PATH}{USER_LOG_NAME}')


def connect_menu_functions(main_window) -> None:
    """Connects all menu functions from the main window."""
    main_window.log_shortcut = QShortcut(QKeySequence('Ctrl+L'), main_window)
    main_window.log_shortcut.activated.connect(open_current_log)
    main_window.actionOpen_Current_Log.triggered.connect(open_current_log)


class MainWindow(QMainWindow, Ui_MainWindow, MainWindowSlotFunctionsMixin):
    """The main window of the application that is the launching point for all dialogs."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.modify_view()
        self.connect_signals_to_slots()
        connect_menu_functions(self)
        self.load_case_lists()
        self.show_hide_daily_case_lists()
        self.judicial_officer = None
        self.dialog = None
        self.case_table = 'None'

    def modify_view(self) -> None:
        main_window_view.MainWindowViewModifier(self)

    def connect_signals_to_slots(self) -> None:
        main_window_signalconnector.MainWindowSignalConnector(self)

    def set_selected_case_list_table(self) -> None:
        self.case_table = self.daily_case_list_buttons_dict.get(self.sender(), 'None')

    def set_visiting_judge(self):
        if self.visiting_judge_radioButton.isChecked():
            first_name, response_ok = QInputDialog.getText(
                self, 'Set Visiting Judge', 'Enter Judge First Name:',
            )
            last_name, response_ok = QInputDialog.getText(
                self, 'Set Visiting Judge', 'Enter Judge Last Name:',
            )
            if response_ok:
                update_dict = {
                    self.visiting_judge_radioButton: JudicialOfficer(
                        f'{first_name}', f'{last_name}', 'Judge',
                    ),
                }
                self.judicial_officer_buttons_dict.update(update_dict)
                self.visiting_judge_radioButton.setText(f'Judge {last_name}')

    def update_judicial_officer(self) -> None:
        self.judicial_officer = self.judicial_officer_buttons_dict.get(self.sender())
        judicial_officer = self.judicial_officer.last_name
        logger.action(f'Judicial Officer set to: {judicial_officer}')

    def set_case_to_load(self, selected_case_table: QComboBox) -> CmsCaseInformation:
        """Returns an empty CmsCaseInformation object if no case is selected.

        Otherwise returns a CmsCaseInformation object via CriminalCaseSQLRetriever().load_case()
        that contains all data from the Cms daily case list reports.
        """
        if selected_case_table.currentText() == '':
            return CmsCaseInformation()
        case_number = selected_case_table.currentText().split('- ')[1]
        return CriminalCaseSQLRetriever(case_number, self.case_table).load_case()
