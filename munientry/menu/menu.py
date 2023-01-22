"""Module connecting all functions for the mainwindow menu."""
from functools import partial

from munientry.menu.batch.batch import run_batch_fta_process
from munientry.menu.logs.logs import open_current_log
from munientry.menu.reports.reports import run_event_type_report
from munientry.menu.open.open import open_entries_folder
from munientry.menu.settings.settings import open_workflow_settings


class MainWindowMenu(object):
    """Class for setting up the menu for the Main Window."""

    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        self.connect_open_menu_functions()
        self.connect_batch_menu_functions()
        self.connect_reports_menu_functions()
        self.connect_logs_menu_functions()
        self.connect_settings_menu_functions()

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

    def connect_batch_menu_functions(self) -> None:
        self.mainwindow.actionRun_batch_FTA_Entries.triggered.connect(run_batch_fta_process)

    def connect_reports_menu_functions(self) -> None:
        self.connect_authority_court_reports()
        self.connect_munientry_reports()

    def connect_authority_court_reports(self):
        self.mainwindow.actionArraignments.triggered.connect(
            partial(run_event_type_report, self.mainwindow, 'Arraignments')
        )
        self.mainwindow.actionFinal_Pretrials.triggered.connect(
            partial(run_event_type_report, self.mainwindow, 'Final Pretrials')
        )
        self.mainwindow.actionTrials_To_Court.triggered.connect(
            partial(run_event_type_report, self.mainwindow, 'Trials To Court')
        )
        self.mainwindow.actionPleas.triggered.connect(
            partial(run_event_type_report, self.mainwindow, 'Pleas')
        )
        self.mainwindow.actionJury_Trials.triggered.connect(
            partial(run_event_type_report, self.mainwindow, 'Jury Trials')
        )

    def connect_munientry_reports(self):
        pass

    def connect_logs_menu_functions(self) -> None:
        self.mainwindow.actionOpen_Current_Log.triggered.connect(open_current_log)

    def connect_settings_menu_functions(self) -> None:
        self.mainwindow.actionWorkflow.triggered.connect(
            partial(open_workflow_settings, self.mainwindow)
        )
