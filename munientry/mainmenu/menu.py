"""Module connecting all functions for the mainwindow mainmenu."""
from functools import partial

from munientry.mainmenu.batch_menu import create_single_fta_entry, run_batch_fta_process
from munientry.mainmenu.logs_menu import open_current_log
from munientry.mainmenu.open_menu import open_entries_folder
from munientry.mainmenu.reports import authoritycourt_reports, munientry_reports
from munientry.mainmenu.settings_menu import open_workflow_settings

ENTRIES_FOLDERS = (
    'driving_privileges',
    'crimtraffic_entries',
    'scheduling_entries',
    'jury_pay_entries',
    'batch_entries',
)
AUTHORITY_CRIMTRAFFIC_EVENT_TYPES = (
    'Arraignments',
    'Final Pretrials',
    'Trials To Court',
    'Pleas',
    'Jury Trials',
)
MUNIENTRY_DB_COURTROOMS = (1, 2, 3)  # 1 = Courtroom A, 2 = Courtroom B, 3 = Courtroom C


class MainMenu(object):
    """Class for setting up the main menu for the Main Window."""

    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        self.connect_functions()

    def connect_functions(self):
        self._connect_open_menu_functions()
        self._connect_batch_menu_functions()
        self._connect_reports_menu_functions()
        self._connect_logs_menu_functions()
        self._connect_settings_menu_functions()

    def _connect_open_menu_functions(self):
        folders = ENTRIES_FOLDERS
        actions = [
            self.mainwindow.actionDriving_Privileges_Folder,
            self.mainwindow.actionCrimTraffic_Folder,
            self.mainwindow.actionScheduling_Entries_Folder,
            self.mainwindow.actionJury_Pay_Entries_Folder,
            self.mainwindow.actionOpen_batch_FTA_Entries_Folder,
        ]
        for folder, action in zip(folders, actions):
            action.triggered.connect(partial(open_entries_folder, folder))

    def _connect_batch_menu_functions(self):
        self.mainwindow.actionRun_batch_FTA_Entries.triggered.connect(
            partial(
                run_batch_fta_process,
                self.mainwindow,
            )
        )
        self.mainwindow.actionCreate_single_FTA_Entry.triggered.connect(
            partial(
                create_single_fta_entry,
                self.mainwindow,
            )
        )

    def _connect_reports_menu_functions(self):
        self._connect_authority_court_reports()
        self._connect_munientry_reports()

    def _connect_authority_court_reports(self):
        event_types = AUTHORITY_CRIMTRAFFIC_EVENT_TYPES
        actions = [
            self.mainwindow.actionArraignments,
            self.mainwindow.actionFinal_Pretrials,
            self.mainwindow.actionTrials_To_Court,
            self.mainwindow.actionPleas,
            self.mainwindow.actionJury_Trials,
        ]
        for event_type, action in zip(event_types, actions):
            action.triggered.connect(
                partial(
                    authoritycourt_reports.run_event_type_report,
                    self.mainwindow,
                    event_type,
                ),
            )

    def _connect_munientry_reports(self):
        courtrooms = MUNIENTRY_DB_COURTROOMS
        actions = [
            self.mainwindow.actionCourtroom_A,
            self.mainwindow.actionCourtroom_B,
            self.mainwindow.actionCourtroom_C,
        ]
        for courtroom, action in zip(courtrooms, actions):
            action.triggered.connect(
                partial(
                    munientry_reports.run_courtroom_report,
                    self.mainwindow,
                    courtroom,
                ),
            )

    def _connect_logs_menu_functions(self) -> None:
        self.mainwindow.actionOpen_Current_Log.triggered.connect(open_current_log)

    def _connect_settings_menu_functions(self) -> None:
        self.mainwindow.actionWorkflow.triggered.connect(
            partial(open_workflow_settings, self.mainwindow),
        )
