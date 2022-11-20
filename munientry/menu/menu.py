"""Module containing all functions for the mainwindow menu."""
import os
from functools import partial
from collections import namedtuple

from loguru import logger
from PyQt6.QtGui import QIcon
from PyQt6.QtSql import QSqlQuery
from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QInputDialog, QTableWidgetItem, QGroupBox, QVBoxLayout, QRadioButton

from munientry.data.connections import close_db_connection, open_db_connection
from munientry.data.excel_getters import clean_offense_name
from munientry.data.sql_server_queries import event_type_report_query
from munientry.data.sql_lite_queries import courtroom_event_report_query
from munientry.mainwindow.batch_entries import run_batch_fta_arraignments
from munientry.logging_module import USER_LOG_NAME
from munientry.menu.menu_folder_actions import open_entries_folder
# from munientry.menu.menu_folder_actions import open_batch_entries_folder, \
#     open_driving_privileges_folder, open_crimtraffic_entries_folder, open_scheduling_entries_folder, \
#     open_jury_pay_entries_folder
from munientry.paths import LOG_PATH, BATCH_SAVE_PATH, ICON_PATH
from munientry.widgets import message_boxes, table_widgets

EVENT_REPORT_HEADERS = ('Case Number', 'Defendant Name', 'Primary Charge')
COURTROOM_REPORT_HEADERS = ('Case Number', 'Event', 'Time')
COURTROOM_NAME = {
    1: 'A',
    2: 'B',
    3: 'C',
}
# Arraignment - 27, Arraignment - 28, Continuance Arraignment - 77, Reset Case Arraignment - 361
ARRAIGNMENT_EVENT_IDS = "('27', '28', '77', '361')"
FINAL_PRETRIAL_EVENT_IDS = "('157', '160', '161')"

EVENT_IDS = {
    'Arraignments': ARRAIGNMENT_EVENT_IDS,
    'Final Pretrials': FINAL_PRETRIAL_EVENT_IDS,
}


class SettingDialog(QDialog):
    def __init__(self, mainwindow, parent=None):
        super().__init__(parent)
        self.mainwindow = mainwindow
        self.setWindowIcon(QIcon(f'{ICON_PATH}gavel.ico'))
        self.setWindowTitle('Workflow Settings')
        button_group = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel

        group_box = QGroupBox('Workflow Setting')

        self.workflow_on_radioButton = QRadioButton('Workflow On')
        self.workflow_off_radioButton = QRadioButton('Workflow Off')

        self.workflow_on_radioButton.toggled.connect(self.set_workflow)
        self.workflow_off_radioButton.toggled.connect(self.set_workflow)
        if self.mainwindow.digital_workflow.workflow_status == 'ON':
            self.workflow_on_radioButton.setChecked(True)
        else:
            self.workflow_off_radioButton.setChecked(True)

        radio_layout = QVBoxLayout()
        radio_layout.addWidget(self.workflow_on_radioButton)
        radio_layout.addWidget(self.workflow_off_radioButton)

        group_box.setLayout(radio_layout)

        button_box = QDialogButtonBox(button_group)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(group_box)
        layout.addWidget(button_box)
        self.setLayout(layout)

    def set_workflow(self):
        if self.sender().isChecked():
            if self.sender().text() == 'Workflow On':
                self.mainwindow.digital_workflow.workflow_status = 'ON'
                logger.info(self.mainwindow.digital_workflow.workflow_status)
            else:
                self.mainwindow.digital_workflow.workflow_status = 'OFF'
                logger.info(self.mainwindow.digital_workflow.workflow_status)


def open_current_log(_signal=None) -> None:
    """Menu function that opens the user logs directly or with keyboard shortcut."""
    os.startfile(f'{LOG_PATH}{USER_LOG_NAME}')
    logger.info(f'Current system log opened.')


def run_batch_fta_process(_signal=None) -> None:
    """Creates batch entries for failure to appear and opens folder where entries are saved."""
    entries_created = run_batch_fta_arraignments()
    message = f'The batch process created {entries_created} entries.'
    message_boxes.InfoBox(message, 'Entries Created').exec()
    os.startfile(f'{BATCH_SAVE_PATH}')
    logger.info(f'{message}')


def create_event_report_window(
    data_list: list, report_name: str, report_date: str,
) -> table_widgets.ReportWindow:
    """Creates a window to load the event table and print buttons onto."""
    window = table_widgets.ReportWindow(
        len(data_list), 3, f'{report_name} Report for {report_date}',
    )
    window.table.setHorizontalHeaderLabels(list(EVENT_REPORT_HEADERS))
    Case = namedtuple('Case', 'case_number defendant_name primary_charge')
    for row, case in enumerate(data_list):
        case = Case(case[0], case[1], case[2])
        window.table.setItem(row, 0, QTableWidgetItem(case.case_number))
        window.table.setItem(row, 1, QTableWidgetItem(case.defendant_name))
        window.table.setItem(row, 2, QTableWidgetItem(case.primary_charge))
    return window


def create_courtroom_report_window(
        data_list: list, report_name: str, report_date: str,
) -> table_widgets.ReportWindow:
    """Creates a window to load the event table and print buttons onto."""
    window = table_widgets.ReportWindow(
        len(data_list), 3, f'{report_name} Report for {report_date}',
    )
    window.table.setHorizontalHeaderLabels(list(COURTROOM_REPORT_HEADERS))
    Case = namedtuple('Case', 'case_number event time')
    for row, case in enumerate(data_list):
        case = Case(case[0], case[1], case[2])
        window.table.setItem(row, 0, QTableWidgetItem(case.case_number))
        window.table.setItem(row, 1, QTableWidgetItem(case.event))
        window.table.setItem(row, 2, QTableWidgetItem(case.time))
    return window


class MainWindowMenu(object):
    """Class for setting up the menu for the Main Window."""

    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        self.connect_menu_functions()
        self.connect_open_menu_functions()
        self.connect_reports_menu_functions()

    def connect_menu_functions(self) -> None:
        self.mainwindow.actionOpen_Current_Log.triggered.connect(open_current_log)
        self.mainwindow.actionRun_batch_FTA_Entries.triggered.connect(run_batch_fta_process)
        self.mainwindow.actionWorkflow.triggered.connect(self.open_workflow_settings)

    def connect_open_menu_functions(self) -> None:
        self.mainwindow.actionDriving_Privileges_Folder.triggered.connect(
            partial(open_entries_folder, 'driving_privileges'),
        )
        self.mainwindow.actionCrimTraffic_Folder.triggered.connect(
            partial(open_entries_folder, 'crimtraffic_entries'),
        )
        self.mainwindow.actionScheduling_Entries_Folder.triggered.connect(
            partial(open_entries_folder, 'scheduling_entries'),
        )
        self.mainwindow.actionJury_Pay_Entries_Folder.triggered.connect(
            partial(open_entries_folder, 'jury_pay_entries'),
        )
        self.mainwindow.actionOpen_batch_FTA_Entries_Folder.triggered.connect(
            partial(open_entries_folder, 'batch_entries'),
        )

    def connect_reports_menu_functions(self) -> None:
        self.mainwindow.actionArraignments.triggered.connect(
            partial(self.run_event_type_report, 'Arraignments')
        )
        self.mainwindow.actionFinal_Pretrials.triggered.connect(
            partial(self.run_event_type_report, 'Final Pretrials')
        )

        self.mainwindow.actionCourtroom_A_Events.triggered.connect(
            partial(self.run_courtroom_report, 1)
        )
        self.mainwindow.actionCourtroom_B_Events.triggered.connect(
            partial(self.run_courtroom_report, 2)
        )
        self.mainwindow.actionCourtroom_C_Events.triggered.connect(
            partial(self.run_courtroom_report, 3)
        )

    def open_workflow_settings(self, _signal=None) -> None:
        self.settings_menu = SettingDialog(self.mainwindow)
        self.settings_menu.exec()

    def run_event_type_report(self, event) -> None:
        report_date = self.get_report_date(event)
        event_ids = EVENT_IDS.get(event)
        query_string = event_type_report_query(report_date, event_ids)
        logger.info(query_string)
        self.show_report_table(event, report_date, query_string)

    # def run_arraignments_report(self) -> None:
    #     report_date = self.get_report_date('Arraignments')
    #     query_string = event_type_report_query(report_date, ARRAIGNMENT_EVENT_IDS)
    #     logger.info(query_string)
    #     self.show_report_table('Arraignments', report_date, query_string)
    #
    # def run_final_pretrials_report(self) -> None:
    #     report_date = self.get_report_date('Final Pretrials')
    #     query_string = event_type_report_query(report_date, FINAL_PRETRIAL_EVENT_IDS)
    #     logger.info(query_string)
    #     self.show_report_table('Final Pretrials', report_date, query_string)

    def run_courtroom_report(self, courtroom: int) -> None:
        courtroom_name = COURTROOM_NAME.get(courtroom)
        report_date = self.get_report_date(f'Courtroom {courtroom_name} Event')
        query_string = courtroom_event_report_query(report_date, courtroom)
        logger.info(query_string)
        self.show_courtroom_events(f'Courtroom {courtroom_name} Events', report_date, query_string)

    def show_courtroom_events(self, report_name: str, report_date: str, query_string: str) -> None:
        db = open_db_connection('con_munientry_db')
        data_list = self.get_courtroom_report_data(db, query_string)
        self.report_window = create_courtroom_report_window(data_list, report_name, report_date)
        self.report_window.table.setSortingEnabled(True)
        self.report_window.show()
        close_db_connection(db)

    def get_report_date(self, report: str) -> str:
        event_date = QInputDialog.getText(
            self.mainwindow, f'{report} Date', f'Enter {report} Date in format YYYY-MM-DD:',
        )
        return event_date[0]

    def get_courtroom_report_data(self, db, query_string: str) -> list:
        self.query = QSqlQuery(db)
        self.query.prepare(query_string)
        self.query.exec()
        data_list = []
        while self.query.next():
            data_list.append(
                (
                    self.query.value('case_number'),
                    self.query.value('event_type_name'),
                    self.query.value('case_event_time'),
                ),
            )
        return data_list

    def get_report_data(self, db, query_string: str) -> list:
        self.query = QSqlQuery(db)
        self.query.prepare(query_string)
        self.query.exec()
        data_list = []
        while self.query.next():
            data_list.append(
                (
                    self.query.value('CaseNumber'),
                    self.query.value('DefFullName').title(),
                    clean_offense_name(self.query.value('Charge')),
                ),
            )
        return data_list

    def show_report_table(self, report_name: str, report_date: str, query_string: str) -> None:
        db = open_db_connection('con_authority_court')
        data_list = self.get_report_data(db, query_string)
        self.report_window = create_event_report_window(data_list, report_name, report_date)
        self.report_window.table.setSortingEnabled(True)
        self.report_window.show()
        close_db_connection(db)
