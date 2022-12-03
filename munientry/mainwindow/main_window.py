"""Module containing the Main Window of the application."""
from loguru import logger
from PyQt6.QtWidgets import QInputDialog, QMainWindow

from munientry.settings import load_user_settings
from munientry.digitalworkflow.workflow_builder import DigitalWorkflow
from munientry.mainwindow import main_window_signalconnector, main_window_view
from munientry.mainwindow.main_window_slots import MainWindowSlotFunctionsMixin
from munientry.menu.menu import MainWindowMenu
from munientry.mainwindow.shortcuts import Shortcuts
from munientry.models.party_types import JudicialOfficer
from munientry.views.main_window_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow, MainWindowSlotFunctionsMixin):
    """The main window of the application that is the launching point for all dialogs."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.modify_view()
        self.digital_workflow = DigitalWorkflow(self)
        self.connect_signals_to_slots()
        self.menu = MainWindowMenu(self)
        self.load_case_lists()
        self.show_hide_daily_case_lists()
        self.judicial_officer = None
        self.dialog = None
        self.daily_case_list = None
        self.user_settings = load_user_settings(self)
        self.shorcuts = Shortcuts(self)

    def modify_view(self) -> None:
        main_window_view.MainWindowViewModifier(self)

    def connect_signals_to_slots(self) -> None:
        main_window_signalconnector.MainWindowSignalConnector(self)

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
