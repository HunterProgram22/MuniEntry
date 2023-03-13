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


class UserSettings(object):
    """Base UserSettings class."""

    settings_name = None

    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        self.main_tab = mainwindow.main_TabWidget
        self.workflow_persons_tab = mainwindow.workflows_person_tab
        self.load_settings()
        logger.info(f'Settings set to: {self.settings_name}')

    def load_settings(self):
        for key, value in self.hidden_tabs.items():
            for item in value:
                tab = getattr(self, key)
                tab.setTabVisible(item, False)


class AdminUserSettings(UserSettings):
    """Admin User settings - provide full access to all application options and features."""

    settings_name = 'Admin User'


class CommissionerUserSettings(UserSettings):
    """Commissioner User settings - opens application on scheduling tab."""

    settings_name = 'Commisssioner User'
    hidden_tabs = {
        'main_tab': [MainTabs.WORKFLOWS.value],
        'workflow_persons_tab': [WorkflowTabs.ADMIN_JUDGE.value, WorkflowTabs.JUDGE_TWO.value, WorkflowTabs.MAGISTRATE_ONE.value],
    }


class CourtroomUserSettings(UserSettings):
    """Courtroom User settings - shows only CrimTraffic Entries tab for entries."""

    settings_name = 'Courtroom User'

    def load_settings(self):
        self.mainwindow.main_TabWidget.setTabVisible(1, False)
        self.mainwindow.tabWidget.setTabVisible(1, False)
        self.mainwindow.tabWidget.setTabVisible(2, False)
        self.mainwindow.workflows_person_tab.setTabVisible(1, False)
        self.mainwindow.workflows_person_tab.setTabVisible(2, False)
        self.mainwindow.workflows_person_tab.setTabVisible(3, False)


class GeneralUserSettings(UserSettings):
    """General User settings - default settings for access to all production features."""

    settings_name = 'General User'

    def load_settings(self):
        self.mainwindow.workflows_person_tab.setTabVisible(1, False)
        self.mainwindow.workflows_person_tab.setTabVisible(2, False)
        self.mainwindow.workflows_person_tab.setTabVisible(3, False)


class ProbationUserSettings(UserSettings):
    """Probation User settings - for Probation users with access to Probation workflows only."""

    settings_name = 'Probation User'
    hidden_tabs = {
        'main_tab': [MainTabs.WORKFLOWS.value],
        'workflow_persons_tab': [WorkflowTabs.ADMIN_JUDGE.value, WorkflowTabs.JUDGE_TWO.value, WorkflowTabs.MAGISTRATE_ONE.value],
    }

    def load_settings(self):
        self.mainwindow.entries_tab_widget.setTabVisible(0, False)
        self.mainwindow.entries_tab_widget.setTabVisible(1, False)
        self.mainwindow.entries_tab_widget.setTabVisible(2, False)
        self.mainwindow.entries_tab_widget.setTabVisible(3, False)
        self.mainwindow.court_staff.set_person_stack_widget()
        self.mainwindow.cases_tab_widget.setTabVisible(2, False)
        self.mainwindow.workflows_person_tab.setTabVisible(1, False)
        self.mainwindow.workflows_person_tab.setTabVisible(2, False)
        self.mainwindow.workflows_person_tab.setTabVisible(3, False)


def load_user_settings(mainwindow) -> 'UserSettings':
    """Returns the user settings based on the computer that is loading the application."""
    user_settings_config = config['user_settings']
    user_settings_key = user_settings_config.get(HOST_NAME, 'GeneralUserSettings')
    user_settings = USER_SETTINGS.get(user_settings_key, GeneralUserSettings)
    return user_settings(mainwindow)


USER_SETTINGS = {
    'AdminUserSettings': CommissionerUserSettings,
    'CommissionerUserSettings': CommissionerUserSettings,
    'CourtroomUserSettings': CourtroomUserSettings,
    'GeneralUserSettings': GeneralUserSettings,
    'ProbationUserSettings': ProbationUserSettings,
}
