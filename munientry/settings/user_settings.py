"""Module for user settings for the application."""
from types import MappingProxyType

from loguru import logger

from munientry.settings.app_settings import HOST_NAME, CaseTabs, EntryTabs, MainTabs, WorkflowTabs
from munientry.settings.config_settings import load_config



class UserSettings(object):
    """Base UserSettings class."""

    settings_name: str
    hidden_tabs: dict[str, list] = {}

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
        """Loops through dictionary of tabs with lists of subtabs to set not visible."""
        for key, tabs in self.hidden_tabs.items():
            for tab_index in tabs:
                tab = getattr(self, key)
                is_visible = False
                tab.setTabVisible(tab_index, is_visible)

    def set_current_view(self):
        """Called in some subclasses to set the default view for the user."""


class AdminUserSettings(UserSettings):
    """Admin User settings - provide full access to all application options and features."""

    settings_name = 'Admin User'


class CommissionerUserSettings(UserSettings):
    """Commissioner User settings - opens application on scheduling tab."""

    settings_name = 'Commisssioner User'
    hidden_tabs = {
        'main_tab': [MainTabs.workflows.value],
    }

    def set_current_view(self):
        self.entries_tab.setCurrentIndex(EntryTabs.scheduling.value)
        self.court_staff.set_person_stack_widget()


class CourtroomUserSettings(UserSettings):
    """Courtroom User settings - shows only CrimTraffic Entries tab for entries."""

    settings_name = 'Courtroom User'
    hidden_tabs = {
        'main_tab': [MainTabs.workflows.value],
        'entries_tab': [
            EntryTabs.scheduling.value,
            EntryTabs.administrative.value,
            EntryTabs.probation.value,
        ],
    }


class GeneralUserSettings(UserSettings):
    """General User settings - default settings for access to all production features."""

    settings_name = 'General User'
    hidden_tabs = {
        'workflow_persons_tab': [
            WorkflowTabs.admin_judge.value,
            WorkflowTabs.judge_two.value,
            WorkflowTabs.magistrate_one.value,
        ],
    }


class ProbationUserSettings(UserSettings):
    """Probation User settings - for Probation users with access to Probation workflows only."""

    settings_name = 'Probation User'
    hidden_tabs = {
        'cases_tab': [
            CaseTabs.civil_search.value,
        ],
        'entries_tab': [
            EntryTabs.scheduling.value,
            EntryTabs.administrative.value,
            EntryTabs.crim_traffic.value,
            EntryTabs.civil.value,
        ],
        'workflow_persons_tab': [
            WorkflowTabs.admin_judge.value,
            WorkflowTabs.judge_two.value,
            WorkflowTabs.magistrate_one.value,
        ],
    }

    def set_current_view(self):
        self.court_staff.set_person_stack_widget()


USER_SETTINGS = MappingProxyType({
    'AdminUserSettings': AdminUserSettings,
    'CommissionerUserSettings': CommissionerUserSettings,
    'CourtroomUserSettings': CourtroomUserSettings,
    'GeneralUserSettings': GeneralUserSettings,
    'ProbationUserSettings': ProbationUserSettings,
})


def load_user_settings(mainwindow) -> 'UserSettings':
    """Returns the user settings based on the computer that is loading the application."""
    config = load_config()
    user_settings_config = config['user_settings']
    computer_config = config['sockets']
    user_computer = computer_config.get(HOST_NAME, 'None')
    user_settings_key = user_settings_config.get(user_computer, 'GeneralUserSettings')
    user_settings = USER_SETTINGS.get(user_settings_key, GeneralUserSettings)
    return user_settings(mainwindow)
