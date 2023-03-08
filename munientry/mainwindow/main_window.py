"""Module containing the Main Window of the application."""
from functools import partial

from loguru import logger
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QInputDialog, QMainWindow, QTableWidgetItem

from munientry.appsettings.paths import ICON_PATH
from munientry.appsettings.settings import VERSION_NUMBER
from munientry.appsettings.user_settings import load_user_settings
from munientry.builders.administrative import (
    admin_fiscal_dialog,
    driving_privileges_dialog,
    jury_payment_dialog,
)
from munientry.builders.civil import civ_freeform_dialog
from munientry.builders.crimtraffic import (
    arraignment_continue_dialog,
    bond_hearing_dialog,
    criminal_sealing_dialog,
    diversion_dialog,
    failure_to_appear_dialog,
    fine_only_plea_dialog,
    freeform_dialog,
    jail_cc_plea_dialog,
    leap_plea_dialog,
    leap_plea_valid_dialog,
    leap_sentencing_dialog,
    no_plea_bond_dialog,
    not_guilty_bond_dialog,
    plea_only_future_sentence_dialog,
    probation_violation_bond_dialog,
    sentencing_only_dialog,
    trial_sentencing_dialog,
)
from munientry.builders.scheduling import (
    final_jury_hearing_notice_dialog,
    general_hearing_notice_dialog,
    sched_entry_dialogs,
    trial_to_court_hearing_notice_dialog,
)
from munientry.builders.workflows import bunner_dw_dialog as bunner
from munientry.builders.workflows import admin_judge_dw_dialog as hemmeter
from munientry.builders.workflows import probation_dw_dialogs as probation
from munientry.builders.workflows import rohrer_dw_dialog as rohrer
from munientry.digitalworkflow.workflow_builder import DigitalWorkflow
from munientry.helper_functions import set_random_judge, update_crim_case_number
from munientry.mainmenu.menu import MainMenu
from munientry.mainmenu.reports.daily_reports import run_not_guilty_report_today
from munientry.mainwindow.case_lists import CaseListHandler
from munientry.mainwindow.case_search import CaseSearchHandler
from munientry.mainwindow.court_staff import CourtStaffWidget
from munientry.mainwindow.dialog_starter import start_dialog
from munientry.mainwindow.shortcuts import set_mainwindow_shortcuts
from munientry.sqlserver import crim_getters as crim
from munientry.views.main_window_ui import Ui_MainWindow
from munientry.widgets.table_widgets import TableReportWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """The main window of the application that is the launching point for all dialogs."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.modify_view()
        self.digital_workflow = DigitalWorkflow(self)

        self.court_staff = CourtStaffWidget(self)

        self.dialog_buttons_dict = self.create_entry_buttons_dict()

        self.case_search = CaseSearchHandler(self)
        self.case_lists = CaseListHandler(self)

        MainWindowSignalConnector(self)
        self.menu = MainMenu(self)
        self.case_lists.load_case_lists()
        self.case_lists.show_hide_daily_case_lists()
        self.judicial_officer = None
        self.dialog = None
        self.daily_case_list = None
        self.user_settings = load_user_settings(self)
        set_mainwindow_shortcuts(self)

    def modify_view(self) -> None:
        self.setupUi(self)
        self.create_daily_case_lists()
        self.setWindowIcon(QIcon(f'{ICON_PATH}gavel.ico'))
        self.setWindowTitle(f'MuniEntry - Version {VERSION_NUMBER}')
        self.daily_case_lists = [
            self.arraignments_cases_box,
            self.slated_cases_box,
            self.pleas_cases_box,
            self.pcvh_fcvh_cases_box,
            self.final_pretrial_cases_box,
            self.trials_to_court_cases_box,
        ]

    def create_daily_case_lists(self) -> None:
        self.arraignments_cases_box.setup_combo_box(
            'arraignments', self.arraignments_radioButton, self,
        )
        self.slated_cases_box.setup_combo_box('slated', self.slated_radioButton, self)
        self.final_pretrial_cases_box.setup_combo_box(
            'final_pretrials', self.final_pretrial_radioButton, self,
        )
        self.pleas_cases_box.setup_combo_box('pleas', self.pleas_radioButton, self)
        self.trials_to_court_cases_box.setup_combo_box(
            'trials_to_court', self.trials_to_court_radioButton, self,
        )
        self.pcvh_fcvh_cases_box.setup_combo_box('pcvh_fcvh', self.pcvh_fcvh_radioButton, self)

    def create_entry_buttons_dict(self):
        return {
            ###CrimTraffic###
            self.ArraignmentContinueButton: arraignment_continue_dialog.ArraignmentContinueDialog,
            self.FineOnlyPleaButton: fine_only_plea_dialog.FineOnlyPleaDialog,
            self.JailCCPleaButton: jail_cc_plea_dialog.JailCCPleaDialog,
            self.DiversionButton: diversion_dialog.DiversionPleaDialog,
            self.NotGuiltyBondButton: not_guilty_bond_dialog.NotGuiltyBondDialog,
            self.FailureToAppearButton: failure_to_appear_dialog.FailureToAppearDialog,
            self.ProbationViolationBondButton: probation_violation_bond_dialog.ProbationViolationBondDialog,
            self.BondHearingButton: bond_hearing_dialog.BondHearingDialog,
            self.PleaOnlyButton: plea_only_future_sentence_dialog.PleaOnlyDialog,
            self.NoPleaBondButton: no_plea_bond_dialog.NoPleaBondDialog,
            self.LeapAdmissionButton: leap_plea_dialog.LeapAdmissionPleaDialog,
            self.LeapAdmissionValidButton: leap_plea_valid_dialog.LeapPleaValidDialog,
            self.LeapSentencingButton: leap_sentencing_dialog.LeapSentencingDialog,
            self.TrialSentencingButton: trial_sentencing_dialog.TrialSentencingDialog,
            self.SentencingOnlyButton: sentencing_only_dialog.SentencingOnlyDialog,
            self.FreeformEntryButton: freeform_dialog.FreeformDialog,
            self.CriminalSealingButton: criminal_sealing_dialog.CriminalSealingDialog,

            ###Civil###
            self.CivFreeformEntryButton: civ_freeform_dialog.CivFreeformDialog,

            ###Scheduling###
            self.hemmeter_schedulingEntryButton:
                sched_entry_dialogs.SchedulingEntryDialog,
            self.rohrer_schedulingEntryButton:
                sched_entry_dialogs.SchedulingEntryDialog,
            self.hemmeter_final_jury_hearingButton:
                final_jury_hearing_notice_dialog.FinalJuryNoticeHearingDialog,
            self.rohrer_final_jury_hearingButton:
                final_jury_hearing_notice_dialog.FinalJuryNoticeHearingDialog,
            self.hemmeter_general_hearingButton:
                general_hearing_notice_dialog.GeneralNoticeOfHearingDialog,
            self.rohrer_general_hearingButton:
                general_hearing_notice_dialog.GeneralNoticeOfHearingDialog,
            self.hemmeter_trial_court_hearingButton:
                trial_to_court_hearing_notice_dialog.TrialToCourtHearingDialog,
            self.rohrer_trial_court_hearingButton:
                trial_to_court_hearing_notice_dialog.TrialToCourtHearingDialog,

            ###Admin###
            self.limited_driving_privilegesButton:
                driving_privileges_dialog.DrivingPrivilegesDialog,
            self.juror_paymentButton: jury_payment_dialog.JuryPaymentDialog,
            self.fiscal_entriesButton: admin_fiscal_dialog.AdminFiscalDialog,

            ###Workflow###
            self.admin_workflowButton: hemmeter.AdminWorkflowDialog,
            self.rohrer_workflowButton: rohrer.RohrerWorkflowDialog,
            self.bunner_workflowButton: bunner.BunnerWorkflowDialog,
            self.pretrial_workflowButton: probation.PretrialWorkflowDialog,
            self.community_control_workflowButton: probation.ComControlWorkflowDialog,
        }

    def assign_judge(self) -> None:
        assigned_judge, time_now = set_random_judge()
        self.assign_judge_label.setText(assigned_judge)
        self.last_judge_assigned_label.setText(
            f'The last judge assigned was {assigned_judge}.\n'
            + f' The assignment was made at {time_now}.',
            )

    def set_entries_tab(self) -> None:
        logger.action('Search Tab Changed')
        if self.search_tabWidget.currentWidget().objectName() == 'civil_case_search_tab':
            self.tabWidget.setCurrentWidget(self.civil_Tab)

    def show_case_docket_case_list(self):
        """Value Error catch put in to handle if the empty slot of daily case list is selected."""
        try:
            last_name, case_number = self.daily_case_list.currentText().split(' - ')
        except (ValueError, AttributeError) as err:
            logger.warning(err)
            case_number = ''
        self.show_case_docket(case_number)

    def show_case_docket(self, case_number=None):
        if case_number is None:
            case_number = self.case_search_box.text()
            case_number = update_crim_case_number(case_number)
            self.case_search_box.setText(case_number)
        data_list = crim.CrimCaseDocket(case_number).get_docket()
        rows = len(data_list)
        self.window = TableReportWindow(f'Docket Report for {case_number}')
        self.window.table = self.window.add_table(rows, 2, f'Docket Report for {case_number}', self.window)
        header_labels = ['Date', 'Docket Description']
        self.window.table.setHorizontalHeaderLabels(header_labels)
        for row, docket_item in enumerate(data_list):
            docket_item_stripped = ' '.join(docket_item[1].splitlines())
            docket_item_stripped = docket_item_stripped.title()
            docket_date = QTableWidgetItem(docket_item[0])
            docket_descr = QTableWidgetItem()
            docket_descr.setText(docket_item_stripped)
            docket_descr.setToolTip(docket_item[1])
            self.window.table.setItem(row, 0, docket_date)
            self.window.table.setItem(row, 1, docket_descr)
        self.window.show()


class MainWindowSignalConnector(object):
    """Class for connecting signals to slots of the Main Window."""

    def __init__(self, mainwindow: object) -> None:
        self.mainwindow = mainwindow
        self.connect_general_buttons()
        self.connect_court_staff_to_radio_btns()
        self.connect_dialog_buttons_to_start_dialog()

    def connect_general_buttons(self):
        self.mainwindow.reload_cases_Button.released.connect(self.mainwindow.case_lists.reload_case_lists)
        self.mainwindow.random_judge_Button.released.connect(self.mainwindow.assign_judge)
        self.mainwindow.visiting_judge_radio_btn.toggled.connect(
            self.mainwindow.court_staff.set_visiting_judge,
        )
        self.mainwindow.tabWidget.currentChanged.connect(self.mainwindow.court_staff.set_person_stack_widget)
        self.mainwindow.search_tabWidget.currentChanged.connect(self.mainwindow.set_entries_tab)
        self.mainwindow.get_case_Button.pressed.connect(self.mainwindow.case_search.query_case_info)

        self.mainwindow.civil_get_case_Button.pressed.connect(self.mainwindow.case_search.query_case_info)

        self.mainwindow.show_docket_Button.pressed.connect(self.mainwindow.show_case_docket)
        self.mainwindow.show_docket_case_list_Button.pressed.connect(
            self.mainwindow.show_case_docket_case_list,
        )
        self.mainwindow.not_guilty_report_Button.released.connect(lambda: run_not_guilty_report_today(self.mainwindow))

    def connect_court_staff_to_radio_btns(self) -> None:
        """Updates the judicial officer whenever a judicial officer radio button is selected."""
        for key in self.mainwindow.court_staff.court_staff_buttons_dict:
            key.clicked.connect(self.mainwindow.court_staff.update_court_staff)

    def connect_dialog_buttons_to_start_dialog(self) -> None:
        """Connects all dialog buttons to the appropriate dialog.

        Each dialog button is binded to the start_dialog function with the dialog itself. When
        pressed the start_dialog function starts the dialog load process.
        """
        for button, dialog in self.mainwindow.dialog_buttons_dict.items():
            button.released.connect(partial(start_dialog, dialog, self.mainwindow))
