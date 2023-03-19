"""Module containing the Main Window of the application."""
from functools import partial
import os

from loguru import logger
from PyQt6.QtCore import pyqtSignal, pyqtSlot
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow

from munientry.appsettings.paths import GAVEL_PATH
from munientry.appsettings.settings import VERSION_NUMBER
from munientry.appsettings.user_settings import load_user_settings
from munientry.digitalworkflow.workflow_builder import DigitalWorkflow
from munientry.helper_functions import (
    set_random_judge,
    update_civil_case_number,
    update_crim_case_number,
)
from munientry.mainmenu.menu import MainMenu
from munientry.mainmenu.reports.daily_reports import run_not_guilty_report_today
from munientry.mainwindow.case_search import CaseDocketHandler, CaseListHandler, CaseSearchHandler
from munientry.mainwindow.court_staff import CourtStaffManager
from munientry.mainwindow.shortcuts import set_mainwindow_shortcuts
from munientry.views.main_window_ui import Ui_MainWindow
from munientry.widgets.table_widgets import TableReportWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """The main window of the application that is the launching point for all dialogs."""

    crim_case_docket_requested = pyqtSignal(str)
    crim_case_data_requested = pyqtSignal(str)
    civil_case_data_requested = pyqtSignal(str)

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setup_view()
        self.digital_workflow = DigitalWorkflow(self)
        self.court_staff = CourtStaffManager(self)
        self.main_menu = MainMenu(self)
        self.user_settings = load_user_settings(self)
        set_mainwindow_shortcuts(self)
        self.judicial_officer = None
        self.dialog = None
        self.daily_case_list = None
        self.daily_case_lists = [
            self.arraignments_cases_box,
            self.slated_cases_box,
            self.pleas_cases_box,
            self.pcvh_fcvh_cases_box,
            self.final_pretrial_cases_box,
            self.trials_to_court_cases_box,
        ]
        self.connect_daily_case_lists()
        self.case_docket = CaseDocketHandler(self)
        self.case_search = CaseSearchHandler(self)
        self.case_lists = CaseListHandler(self.daily_case_lists)
        self.connect_signals_to_slots()

    def connect_daily_case_lists(self) -> None:
        self.arraignments_cases_box.setup_combo_box(
            'arraignments', self.arraignments_radio_btn, self,
        )
        self.slated_cases_box.setup_combo_box('slated', self.slated_radio_btn, self)
        self.final_pretrial_cases_box.setup_combo_box(
            'final_pretrials', self.final_pretrial_radio_btn, self,
        )
        self.pleas_cases_box.setup_combo_box('pleas', self.pleas_radio_btn, self)
        self.trials_to_court_cases_box.setup_combo_box(
            'trials_to_court', self.trials_to_court_radio_btn, self,
        )
        self.pcvh_fcvh_cases_box.setup_combo_box('pcvh_fcvh', self.pcvh_fcvh_radio_btn, self)

    def setup_view(self) -> None:
        self.setupUi(self)
        self.setWindowIcon(QIcon(GAVEL_PATH))
        self.setWindowTitle(f'MuniEntry - Version {VERSION_NUMBER}')

    def connect_signals_to_slots(self):
        self.reload_cases_Button.released.connect(self.case_lists.reload_case_lists)

        self.visiting_judge_radio_btn.toggled.connect(self.court_staff.set_visiting_judge)
        self.entries_tab_widget.currentChanged.connect(self.court_staff.set_person_stack_widget)

        self.random_judge_Button.released.connect(self.assign_judge)
        self.cases_tab_widget.currentChanged.connect(self.cases_tab_changed)
        self.crim_get_case_btn.released.connect(self.crim_case_search)
        self.civil_get_case_btn.released.connect(self.civil_case_search)
        self.crim_show_docket_case_search_btn.released.connect(self.crim_show_docket_case_search)
        self.crim_show_docket_case_list_btn.released.connect(self.crim_show_docket_case_list)
        self.case_docket.docket_report_delivered.connect(self.display_docket_report)
        self.case_search.crim_case_data_delivered.connect(self.display_crim_search_data)
        self.case_search.civil_case_data_delivered.connect(self.display_civil_search_data)

        self.not_guilty_report_Button.released.connect(lambda: run_not_guilty_report_today(self))
        self.connect_court_staff_to_radio_btns()

    def connect_court_staff_to_radio_btns(self) -> None:
        """Updates the judicial officer whenever a judicial officer radio button is selected."""
        for key in self.court_staff.court_staff_buttons_dict:
            key.clicked.connect(self.court_staff.update_court_staff)

    @pyqtSlot(TableReportWindow)
    def display_docket_report(self, docket_report: TableReportWindow) -> None:
        self.docket_report = docket_report
        self.docket_report.show()

    @pyqtSlot(tuple)
    def display_crim_search_data(self, display_data: tuple) -> None:
        case_number, case_name, case_charges = display_data
        self.crim_case_number_label.setText(case_number)
        self.crim_case_name_label.setText(case_name)
        self.crim_case_charges_label.setText(case_charges)

    @pyqtSlot(tuple)
    def display_civil_search_data(self, display_data: tuple) -> None:
        case_number, case_name, case_type = display_data
        self.civil_case_number_label.setText(case_number)
        self.civil_case_name_label.setText(case_name)
        self.civil_case_type_label.setText(case_type)

    def cases_tab_changed(self) -> None:
        logger.info('Search Tab Changed')
        if self.cases_tab_widget.currentWidget().objectName() == 'civil_case_search_tab':
            self.entries_tab_widget.setCurrentWidget(self.civil_tab)

    def get_case_number(self, search_type: str) -> str:
        if search_type == 'criminal':
            case_number = self.crim_case_search_box.text()
            case_number = update_crim_case_number(case_number)
        elif search_type == 'civil':
            case_number = self.civil_case_search_box.text()
            case_number = update_civil_case_number(case_number)
        return case_number

    def crim_case_search(self):
        case_number = self.get_case_number('criminal')
        self.crim_case_search_box.setText(case_number)
        self.crim_case_data_requested.emit(case_number)

    def crim_show_docket_case_search(self) -> None:
        case_number = self.get_case_number()
        self.crim_case_docket_requested.emit(case_number)

    def crim_show_docket_case_list(self) -> None:
        try:
            _last_name, case_number = self.daily_case_list.currentText().split(' - ')
        except (ValueError, AttributeError) as err:
            logger.warning(err)
            case_number = ''
        self.crim_case_docket_requested.emit(case_number)

    def civil_case_search(self):
        case_number = self.get_case_number('civil')
        self.civil_case_search_box.setText(case_number)
        self.civil_case_data_requested.emit(case_number)

    def assign_judge(self) -> None:
        assigned_judge, time_now = set_random_judge()
        self.assign_judge_label.setText(assigned_judge)
        self.last_judge_assigned_label.setText(
            f'The last judge assigned was {assigned_judge}.\n'
            + f' The assignment was made at {time_now}.',
        )
