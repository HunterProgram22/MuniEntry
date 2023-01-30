"""Module connecting all functions for the mainwindow mainmenu."""
from functools import partial

from munientry.mainmenu.batch_menu import run_batch_fta_process
from munientry.mainmenu.logs_menu import open_current_log
from munientry.mainmenu.reports.authoritycourt_reports import run_event_type_report
from munientry.mainmenu.reports.munientry_reports import run_courtroom_report
from munientry.mainmenu.open_menu import open_entries_folder
from munientry.mainmenu.settings_menu import open_workflow_settings


class MainMenu(object):
    """Class for setting up the mainmenu for the Main Window."""

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
        self.mainwindow.actionCourtroom_A.triggered.connect(
            partial(run_courtroom_report, self.mainwindow, 1)
        )
        self.mainwindow.actionCourtroom_B.triggered.connect(
            partial(run_courtroom_report, self.mainwindow, 2)
        )
        self.mainwindow.actionCourtroom_C.triggered.connect(
            partial(run_courtroom_report, self.mainwindow, 3)
        )

    def connect_logs_menu_functions(self) -> None:
        self.mainwindow.actionOpen_Current_Log.triggered.connect(open_current_log)

    def connect_settings_menu_functions(self) -> None:
        self.mainwindow.actionWorkflow.triggered.connect(
            partial(open_workflow_settings, self.mainwindow)
        )
