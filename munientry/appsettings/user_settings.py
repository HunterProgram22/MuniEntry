"""Module for user settings for the application."""
from enum import Enum

from loguru import logger
from munientry.appsettings.settings import config, HOST_NAME


class MainTabs(Enum):
    ENTRIES = 0
    WORKFLOWS = 1


class WorkflowTabs(Enum):
    PROBATION = 0
    ADMIN_JUDGE = 1
    JUDGE_TWO = 2
    MAGISTRATE_ONE = 3


class EntryTabs(Enum):
    CRIM_TRAFFIC = 0
    SCHEDULING = 1
    ADMINISTRATIVE = 2
    CIVIL = 3
    PROBATION = 4


class CasesTabs(Enum):
    CRIM_CASELISTS = 0
    CRIM_SEARCH = 1
    CIVIL_SEARCH = 2


class UserSettings(object):
    """Base UserSettings class."""

    settings_name = None

    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        self.main_tab = mainwindow.main_TabWidget
        self.entries_tab = mainwindow.entries_tab_widget
        self.cases_tab = mainwindow.cases_tab_widget
        self.court_staff = mainwindow.court_staff
        self.workflow_persons_tab = mainwindow.workflows_person_tab
        self.load_settings()
        logger.info(f'Settings set to: {self.settings_name}')
        self.set_current_view()

    def load_settings(self):
        for key, value in self.hidden_tabs.items():
            for item in value:
                tab = getattr(self, key)
                tab.setTabVisible(item, False)

    def set_current_view(self):
        pass


class AdminUserSettings(UserSettings):
    """Admin User settings - provide full access to all application options and features."""

    settings_name = 'Admin User'


class CommissionerUserSettings(UserSettings):
    """Commissioner User settings - opens application on scheduling tab."""

    settings_name = 'Commisssioner User'
    hidden_tabs = {
        'main_tab': [MainTabs.WORKFLOWS.value],
    }

    def set_current_view(self):
        self.entries_tab.setCurrentIndex(EntryTabs.SCHEDULING.value)
        self.court_staff.set_person_stack_widget()


class CourtroomUserSettings(UserSettings):
    """Courtroom User settings - shows only CrimTraffic Entries tab for entries."""

    settings_name = 'Courtroom User'
    hidden_tabs = {
        'main_tab': [MainTabs.WORKFLOWS.value],
        'entries_tab': [
            EntryTabs.SCHEDULING.value,
            EntryTabs.ADMINISTRATIVE.value,
            EntryTabs.PROBATION.value
        ]
    }


class GeneralUserSettings(UserSettings):
    """General User settings - default settings for access to all production features."""

    settings_name = 'General User'
    hidden_tabs = {
        'workflow_persons_tab': [
            WorkflowTabs.ADMIN_JUDGE.value,
            WorkflowTabs.JUDGE_TWO.value,
            WorkflowTabs.MAGISTRATE_ONE.value,
        ],
    }


class ProbationUserSettings(UserSettings):
    """Probation User settings - for Probation users with access to Probation workflows only."""

    settings_name = 'Probation User'
    hidden_tabs = {
        'cases_tab': [
            CasesTabs.CIVIL_SEARCH.value,
        ],
        'entries_tab': [
            EntryTabs.SCHEDULING.value,
            EntryTabs.ADMINISTRATIVE.value,
            EntryTabs.CRIM_TRAFFIC.value,
            EntryTabs.CIVIL.value,
        ],
        'workflow_persons_tab': [
            WorkflowTabs.ADMIN_JUDGE.value,
            WorkflowTabs.JUDGE_TWO.value,
            WorkflowTabs.MAGISTRATE_ONE.value,
        ],
    }

    def set_current_view(self):
        self.court_staff.set_person_stack_widget()


def load_user_settings(mainwindow) -> 'UserSettings':
    """Returns the user settings based on the computer that is loading the application."""
    user_settings_config = config['user_settings']
    user_settings_key = user_settings_config.get(HOST_NAME, 'GeneralUserSettings')
    user_settings = USER_SETTINGS.get(user_settings_key, GeneralUserSettings)
    return user_settings(mainwindow)


USER_SETTINGS = {
    'AdminUserSettings': AdminUserSettings,
    'CommissionerUserSettings': CommissionerUserSettings,
    'CourtroomUserSettings': CourtroomUserSettings,
    'GeneralUserSettings': GeneralUserSettings,
    'ProbationUserSettings': ProbationUserSettings,
}
