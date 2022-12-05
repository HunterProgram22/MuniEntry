"""Module containing all functions for the mainwindow menu."""
import os
from functools import partial

from loguru import logger
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QGroupBox, QVBoxLayout, QRadioButton

from munientry.mainwindow.batch_entries import run_batch_fta_arraignments
from munientry.logging_module import USER_LOG_NAME
from munientry.menu.menu_folder_actions import open_entries_folder, run_courtroom_report, run_event_type_report
from munientry.appsettings.paths import LOG_PATH, BATCH_SAVE_PATH, ICON_PATH
from munientry.widgets import message_boxes


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
            partial(run_event_type_report, self.mainwindow, 'Arraignments')
        )
        self.mainwindow.actionFinal_Pretrials.triggered.connect(
            partial(run_event_type_report, self.mainwindow, 'Final Pretrials')
        )
        self.mainwindow.actionCourtroom_A_Events.triggered.connect(
            partial(run_courtroom_report, self.mainwindow, 1)
        )
        self.mainwindow.actionCourtroom_B_Events.triggered.connect(
            partial(run_courtroom_report, self.mainwindow, 2)
        )
        self.mainwindow.actionCourtroom_C_Events.triggered.connect(
            partial(run_courtroom_report, self.mainwindow, 3)
        )

    def open_workflow_settings(self, _signal=None) -> None:
        self.settings_menu = SettingDialog(self.mainwindow)
        self.settings_menu.exec()
