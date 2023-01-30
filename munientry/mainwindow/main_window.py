"""Module containing the Main Window of the application."""
from functools import partial

from loguru import logger
from PyQt6.QtWidgets import QInputDialog, QMainWindow

from munientry.appsettings.user_settings import load_user_settings
from munientry.digitalworkflow.workflow_builder import DigitalWorkflow
from munientry.mainwindow import main_window_view
from munientry.mainwindow.dialog_starter import start_dialog
from munientry.mainwindow.main_window_slots import MainWindowSlotFunctionsMixin
from munientry.mainmenu.menu import MainMenu
from munientry.mainwindow.shortcuts import set_mainwindow_shortcuts
from munientry.models.party_types import JudicialOfficer
from munientry.views.main_window_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow, MainWindowSlotFunctionsMixin):
    """The main window of the application that is the launching point for all dialogs."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.modify_view()
        self.digital_workflow = DigitalWorkflow(self)
        self.connect_signals_to_slots()
        self.menu = MainMenu(self)
        self.load_case_lists()
        self.show_hide_daily_case_lists()
        self.judicial_officer = None
        self.dialog = None
        self.daily_case_list = None
        self.user_settings = load_user_settings(self)
        self.set_shortcuts(self)

    def modify_view(self) -> None:
        main_window_view.MainWindowViewModifier(self)

    def connect_signals_to_slots(self) -> None:
        MainWindowSignalConnector(self)

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

    def set_shortcuts(self, mainwindow: 'MainWindow') -> None:
        return set_mainwindow_shortcuts(self)

    def update_judicial_officer(self) -> None:
        self.judicial_officer = self.judicial_officer_buttons_dict.get(self.sender())
        judicial_officer = self.judicial_officer.last_name
        logger.action(f'Judicial Officer set to: {judicial_officer}')


class MainWindowSignalConnector(object):
    """Class for connecting signals to slots of the Main Window."""

    def __init__(self, mainwindow: object) -> None:
        self.mainwindow = mainwindow
        self.connect_general_buttons()
        self.connect_judicial_officers_to_set_officer()
        self.connect_dialog_buttons_to_start_dialog()


    def connect_general_buttons(self):
        self.mainwindow.reload_cases_Button.released.connect(self.mainwindow.reload_case_lists)
        self.mainwindow.random_judge_Button.released.connect(self.mainwindow.assign_judge)
        self.mainwindow.visiting_judge_radioButton.toggled.connect(
            self.mainwindow.set_visiting_judge,
        )
        self.mainwindow.tabWidget.currentChanged.connect(self.mainwindow.set_person_stack_widget)
        self.mainwindow.search_tabWidget.currentChanged.connect(self.mainwindow.set_entries_tab)
        self.mainwindow.get_case_Button.pressed.connect(self.mainwindow.query_case_info)

        self.mainwindow.civil_get_case_Button.pressed.connect(self.mainwindow.query_case_info)

        self.mainwindow.show_docket_Button.pressed.connect(self.mainwindow.show_case_docket)
        self.mainwindow.show_docket_case_list_Button.pressed.connect(
            self.mainwindow.show_case_docket_case_list,
        )

    def connect_judicial_officers_to_set_officer(self) -> None:
        """Updates the judicial officer whenever a judicial officer radio button is selected."""
        for key in self.mainwindow.judicial_officer_buttons_dict:
            key.clicked.connect(self.mainwindow.update_judicial_officer)

    def connect_dialog_buttons_to_start_dialog(self) -> None:
        """Connects all dialog buttons to the appropriate dialog.

        Each dialog button is binded to the start_dialog function with the dialog itself. When
        pressed the start_dialog function starts the dialog load process.
        """
        for button, dialog in self.mainwindow.dialog_buttons_dict.items():
            button.released.connect(partial(start_dialog, dialog, self.mainwindow))
