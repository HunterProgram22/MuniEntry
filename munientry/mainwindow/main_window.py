"""Module containing the Main Window of the application."""
from functools import partial

from PyQt6.QtGui import QIcon
from PyQt6.QtSql import QSqlQuery
from loguru import logger
from PyQt6.QtWidgets import QInputDialog, QMainWindow, QTableWidgetItem
from munientry.appsettings.paths import ICON_PATH
from munientry.appsettings.settings import VERSION_NUMBER

from munientry.appsettings.user_settings import load_user_settings
from munientry.builders.administrative import driving_privileges_dialog, jury_payment_dialog, \
    admin_fiscal_dialog
from munientry.builders.civil import civ_freeform_dialog
from munientry.builders.crimtraffic import arraignment_continue_dialog, fine_only_plea_dialog, \
    jail_cc_plea_dialog, diversion_dialog, not_guilty_bond_dialog, failure_to_appear_dialog, \
    probation_violation_bond_dialog, bond_hearing_dialog, plea_only_future_sentence_dialog, \
    no_plea_bond_dialog, leap_plea_dialog, leap_plea_valid_dialog, leap_sentencing_dialog, \
    trial_sentencing_dialog, sentencing_only_dialog, freeform_dialog
from munientry.builders.scheduling import sched_entry_dialogs, final_jury_hearing_notice_dialog, \
    general_hearing_notice_dialog, trial_to_court_hearing_notice_dialog
from munientry.builders.workflows import hemmeter_dw_dialog as hemmeter, rohrer_dw_dialog as rohrer, \
    bunner_dw_dialog as bunner, probation_dw_dialogs as probation
from munientry.data.connections import open_db_connection, close_db_connection
from munientry.data.data_cleaners import clean_last_name
from munientry.digitalworkflow.workflow_builder import DigitalWorkflow
from munientry.helper_functions import set_random_judge, update_crimtraffic_case_number, \
    update_civil_case_number
from munientry.mainwindow.dialog_starter import start_dialog
from munientry.mainmenu.menu import MainMenu
from munientry.mainwindow.shortcuts import set_mainwindow_shortcuts
from munientry.models.party_types import JudicialOfficer
from munientry.sqlserver import sql_server_queries as sql_query, sql_server_getters as sql_server, \
    civil_getters as civil
from munientry.views.main_window_ui import Ui_MainWindow
from munientry.widgets.table_widgets import TableReportWindow


class MainWindowSlotFunctionsMixin(object):
    """Class that contains common functions for the main window."""

    def load_case_lists(self) -> None:
        """Loads the cms_case numbers of all the cases that are in the daily_case_list databases.

        This does not load the cms_case data for each cms_case.

        The case count is one less than length of list because a blank line is inserted at the
        top of the case list. The case count becomes actual number of cases loaded.
        """
        db_connection = open_db_connection('con_authority_court')
        STORED_PROC_DICT = {
            self.arraignments_cases_box: '[reports].[DMCMuniEntryArraignment]',
            self.slated_cases_box: '[reports].[DMCMuniEntrySlated]',
            self.pleas_cases_box: '[reports].[DMCMuniEntryPleas]',
            self.pcvh_fcvh_cases_box: '[reports].[DMCMuniEntryPrelimCommContViolHearings]',
            self.final_pretrial_cases_box: '[reports].[DMCMuniEntryFinalPreTrials]',
            self.trials_to_court_cases_box: '[reports].[DMCMuniEntryBenchTrials]',
        }

        for case_list in self.daily_case_lists:
            stored_proc = STORED_PROC_DICT.get(case_list)
            query_string = sql_query.daily_case_list_query(stored_proc)
            self.query = QSqlQuery(db_connection)
            self.query.prepare(query_string)
            self.query.exec()
            daily_case_list = []
            while self.query.next():
                case_number = self.query.value('CaseNumber')
                last_name = self.query.value('LastName').title()
                last_name = clean_last_name(last_name)
                case = f'{last_name} - {case_number}'
                daily_case_list.append(case)

            daily_case_list.insert(0, '')
            old_case_count = len(case_list) - 1 if len(case_list) > 1 else 0
            daily_case_list = sorted(daily_case_list)
            case_list.clear()
            case_list.addItems(daily_case_list)
            case_count = len(case_list) - 1
            logger.info(
                f'Table: {case_list.name} - Preload Cases: {old_case_count};'
                + f' Postload Cases {case_count}',
                )
        close_db_connection(db_connection)

    def reload_case_lists(self) -> None:
        """This method is connected to the reload cases button and calls load_case_lists."""
        logger.info('Reload cases button pressed.')
        self.load_case_lists()

    def show_hide_daily_case_lists(self) -> None:
        for case_list in self.daily_case_lists:
            case_list.setCurrentText('')
            case_list.setHidden(True)
            case_list.setEnabled(False)

    def assign_judge(self) -> None:
        assigned_judge, time_now = set_random_judge()
        self.assign_judge_label.setText(assigned_judge)
        self.last_judge_assigned_label.setText(
            f'The last judge assigned was {assigned_judge}.\n'
            + f' The assignment was made at {time_now}.',
            )

    def set_person_stack_widget(self) -> None:
        logger.action('Entry Tab Changed')
        judicial_officers = self.judicial_officers_Stack
        assignment_commissioners = self.assignment_commissioners_Stack
        admin_staff = self.admin_staff_Stack
        if self.tabWidget.currentWidget().objectName() == 'crim_traffic_Tab':
            self.stackedWidget.setCurrentWidget(judicial_officers)
        if self.tabWidget.currentWidget().objectName() == 'scheduling_Tab':
            self.stackedWidget.setCurrentWidget(assignment_commissioners)
        if self.tabWidget.currentWidget().objectName() == 'admin_Tab':
            self.stackedWidget.setCurrentWidget(admin_staff)
        if self.tabWidget.currentWidget().objectName() == 'civil_Tab':
            self.stackedWidget.setCurrentWidget(judicial_officers)
        current_stacked_widget = self.stackedWidget.currentWidget().objectName()
        current_tab_widget = self.tabWidget.currentWidget().objectName()
        logger.info(f'Current stackedWidget is {current_stacked_widget}')
        logger.info(f'Current tabWidget is {current_tab_widget}')

    def set_entries_tab(self) -> None:
        logger.action('Search Tab Changed')
        if self.search_tabWidget.currentWidget().objectName() == 'civil_case_search_tab':
            self.tabWidget.setCurrentWidget(self.civil_Tab)

    def query_case_info(self):
        """Queries a SQL Server database (AuthorityCourtDBO or AuthorityCivilDBO) and retreives case info."""

        if self.search_tabWidget.currentWidget().objectName() == 'case_search_tab':
            case_number = self.case_search_box.text()
            case_number = update_crimtraffic_case_number(case_number)
            self.case_search_box.setText(case_number)
            cms_case_data = sql_server.CriminalCaseSqlServer(case_number).load_case()
            self.set_crimtraffic_case_info_from_search(cms_case_data)

        elif self.search_tabWidget.currentWidget().objectName() == 'civil_case_search_tab':
            case_number = self.civil_case_search_box.text()
            case_number = update_civil_case_number(case_number)
            self.civil_case_search_box.setText(case_number)
            cms_case_data = civil.CivilCaseSqlServer(case_number).load_case()
            self.set_civil_case_info_from_search(cms_case_data)

    def set_crimtraffic_case_info_from_search(self, cms_case_data) -> None:
        """Sets the case search fields on the UI with data from the case that is retrieved."""
        self.case_number_label_field.setText(cms_case_data.case_number)
        def_first_name = cms_case_data.defendant.first_name
        def_last_name = cms_case_data.defendant.last_name
        self.case_name_label_field.setText(f'State of Ohio v. {def_first_name} {def_last_name}')
        charge_list_text = ', '.join(str(charge[0]) for charge in cms_case_data.charges_list)
        self.case_charges_label_field.setText(charge_list_text)

    def set_civil_case_info_from_search(self, cms_case_data):
        self.civil_case_number_field.setText(cms_case_data.case_number)
        self.civil_case_name_field.setText(
            f'{cms_case_data.primary_plaintiff.party_name} vs. {cms_case_data.primary_defendant.party_name}'
        )
        self.civil_case_type_field.setText(cms_case_data.case_type)

    def show_case_docket_case_list(self):
        """Value Error catch put in to handle if the empty slot of daily case list is selected."""
        try:
            last_name, case_number = self.daily_case_list.currentText().split(' - ')
        except ValueError as err:
            logger.warning(err)
            case_number = ''
        self.show_case_docket(case_number)

    def show_case_docket(self, case_number=None):
        if case_number is None:
            case_number = self.case_search_box.text()
            case_number = update_crimtraffic_case_number(case_number)
            self.case_search_box.setText(case_number)
        data_list = sql_server.CaseDocketSQLServer(case_number).get_docket()
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
        MainWindowViewModifier(self)

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


class MainWindowViewModifier(object):
    """Class that modifies the view file."""

    def __init__(self, mainwindow: object) -> None:
        self.mainwindow = mainwindow
        self.mainwindow.setupUi(self.mainwindow)
        self.create_daily_case_lists()
        self.mainwindow.setWindowIcon(QIcon(f'{ICON_PATH}gavel.ico'))
        self.mainwindow.setWindowTitle(f'MuniEntry - Version {VERSION_NUMBER}')
        self.mainwindow.judicial_officer_buttons_dict = self.connect_judicial_officers()
        self.mainwindow.dialog_buttons_dict = self.connect_dialog_buttons()
        self.mainwindow.daily_case_lists = [
            self.mainwindow.arraignments_cases_box,
            self.mainwindow.slated_cases_box,
            self.mainwindow.pleas_cases_box,
            self.mainwindow.pcvh_fcvh_cases_box,
            self.mainwindow.final_pretrial_cases_box,
            self.mainwindow.trials_to_court_cases_box,
        ]

    def connect_judicial_officers(self) -> dict:
        return {
            self.mainwindow.bunner_radioButton: JudicialOfficer('Amanda', 'Bunner', 'Magistrate'),
            self.mainwindow.pelanda_radioButton: JudicialOfficer('Kevin', 'Pelanda', 'Magistrate'),
            self.mainwindow.kudela_radioButton: JudicialOfficer('Justin', 'Kudela', 'Magistrate'),
            self.mainwindow.rohrer_radioButton: JudicialOfficer('Kyle', 'Rohrer', 'Judge'),
            self.mainwindow.hemmeter_radioButton: JudicialOfficer('Marianne', 'Hemmeter', 'Judge'),
            self.mainwindow.visiting_judge_radioButton:
                JudicialOfficer('None', 'Assigned', 'Judge'),
            self.mainwindow.dattilo_radioButton:
                JudicialOfficer('Pat', 'Dattilo', 'Assignment Commissioner'),
            self.mainwindow.patterson_radioButton:
                JudicialOfficer('Kathryn', 'Patterson', 'Assignment Commissioner'),
            self.mainwindow.none_radioButton:
                JudicialOfficer('None', 'Assigned', 'Assignment Commissioner'),
            self.mainwindow.assn_comm_dattilo_radioButton:
                JudicialOfficer('Pat', 'Dattilo', 'Assignment Commissioner'),
            self.mainwindow.assn_comm_patterson_radioButton:
                JudicialOfficer('Kathryn', 'Patterson', 'Assignment Commissioner'),
            self.mainwindow.court_admin_kudela_radioButton:
                JudicialOfficer('Justin', 'Kudela', 'Court Administrator'),
            self.mainwindow.jury_comm_patterson_radioButton:
                JudicialOfficer('Kathryn', 'Patterson', 'Jury Commissioner'),
            self.mainwindow.none_admin_radioButton:
                JudicialOfficer('None', 'Assigned', 'Admin Staff Person'),
            self.mainwindow.bunner_admin_radioButton:
                JudicialOfficer('A', 'B', 'Admin Staff Person'),
        }

    def connect_dialog_buttons(self):
        return {
            ###CrimTraffic###
            self.mainwindow.ArraignmentContinueButton:
                arraignment_continue_dialog.ArraignmentContinueDialog,
            self.mainwindow.FineOnlyPleaButton: fine_only_plea_dialog.FineOnlyPleaDialog,
            self.mainwindow.JailCCPleaButton: jail_cc_plea_dialog.JailCCPleaDialog,
            self.mainwindow.DiversionButton: diversion_dialog.DiversionPleaDialog,
            self.mainwindow.NotGuiltyBondButton: not_guilty_bond_dialog.NotGuiltyBondDialog,
            self.mainwindow.FailureToAppearButton: failure_to_appear_dialog.FailureToAppearDialog,
            self.mainwindow.ProbationViolationBondButton:
                probation_violation_bond_dialog.ProbationViolationBondDialog,
            self.mainwindow.BondHearingButton: bond_hearing_dialog.BondHearingDialog,
            self.mainwindow.PleaOnlyButton: plea_only_future_sentence_dialog.PleaOnlyDialog,
            self.mainwindow.NoPleaBondButton: no_plea_bond_dialog.NoPleaBondDialog,
            self.mainwindow.LeapAdmissionButton: leap_plea_dialog.LeapAdmissionPleaDialog,
            self.mainwindow.LeapAdmissionValidButton: leap_plea_valid_dialog.LeapPleaValidDialog,
            self.mainwindow.LeapSentencingButton: leap_sentencing_dialog.LeapSentencingDialog,
            self.mainwindow.TrialSentencingButton: trial_sentencing_dialog.TrialSentencingDialog,
            self.mainwindow.SentencingOnlyButton: sentencing_only_dialog.SentencingOnlyDialog,
            self.mainwindow.FreeformEntryButton: freeform_dialog.FreeformDialog,

            ###Civil###
            self.mainwindow.CivFreeformEntryButton: civ_freeform_dialog.CivFreeformDialog,

            ###Scheduling###
            self.mainwindow.hemmeter_schedulingEntryButton:
                sched_entry_dialogs.SchedulingEntryDialog,
            self.mainwindow.rohrer_schedulingEntryButton:
                sched_entry_dialogs.SchedulingEntryDialog,
            self.mainwindow.hemmeter_final_jury_hearingButton:
                final_jury_hearing_notice_dialog.FinalJuryNoticeHearingDialog,
            self.mainwindow.rohrer_final_jury_hearingButton:
                final_jury_hearing_notice_dialog.FinalJuryNoticeHearingDialog,
            self.mainwindow.hemmeter_general_hearingButton:
                general_hearing_notice_dialog.GeneralNoticeOfHearingDialog,
            self.mainwindow.rohrer_general_hearingButton:
                general_hearing_notice_dialog.GeneralNoticeOfHearingDialog,
            self.mainwindow.hemmeter_trial_court_hearingButton:
                trial_to_court_hearing_notice_dialog.TrialToCourtHearingDialog,
            self.mainwindow.rohrer_trial_court_hearingButton:
                trial_to_court_hearing_notice_dialog.TrialToCourtHearingDialog,

            ###Admin###
            self.mainwindow.limited_driving_privilegesButton:
                driving_privileges_dialog.DrivingPrivilegesDialog,
            self.mainwindow.juror_paymentButton: jury_payment_dialog.JuryPaymentDialog,
            self.mainwindow.fiscal_entriesButton: admin_fiscal_dialog.AdminFiscalDialog,

            ###Workflow###
            self.mainwindow.hemmeter_workflowButton: hemmeter.HemmeterWorkflowDialog,
            self.mainwindow.rohrer_workflowButton: rohrer.RohrerWorkflowDialog,
            self.mainwindow.bunner_workflowButton: bunner.BunnerWorkflowDialog,
            self.mainwindow.pretrial_workflowButton: probation.PretrialWorkflowDialog,
            self.mainwindow.community_control_workflowButton: probation.ComControlWorkflowDialog,

        }

    def create_daily_case_lists(self) -> None:
        self.mainwindow.arraignments_cases_box.setup_combo_box(
            'arraignments',
            self.mainwindow.arraignments_radioButton,
            self.mainwindow,
        )
        self.mainwindow.slated_cases_box.setup_combo_box(
            'slated',
            self.mainwindow.slated_radioButton,
            self.mainwindow,
        )
        self.mainwindow.final_pretrial_cases_box.setup_combo_box(
            'final_pretrials',
            self.mainwindow.final_pretrial_radioButton,
            self.mainwindow,
        )
        self.mainwindow.pleas_cases_box.setup_combo_box(
            'pleas',
            self.mainwindow.pleas_radioButton,
            self.mainwindow,
        )
        self.mainwindow.trials_to_court_cases_box.setup_combo_box(
            'trials_to_court',
            self.mainwindow.trials_to_court_radioButton,
            self.mainwindow,
        )
        self.mainwindow.pcvh_fcvh_cases_box.setup_combo_box(
            'pcvh_fcvh',
            self.mainwindow.pcvh_fcvh_radioButton,
            self.mainwindow,
        )


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
