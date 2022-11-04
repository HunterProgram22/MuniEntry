"""Module for user settings for the application."""
from loguru import logger

from munientry.settings import SOCKET_NAME


def load_user_settings(mainwindow) -> 'UserSettings':
    """Returns the user settings based on the computer that is loading the application."""
    user_settings = USER_SETTINGS.get(SOCKET_NAME, GeneralUserSettings)
    return user_settings(mainwindow)


class UserSettings(object):
    """Base UserSettings class."""

    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        self.load_settings()
        logger.info(f'Settings set to: {self.settings_name}')


class AdminUserSettings(UserSettings):
    """Admin User settings - provide full access to all application options and features."""

    settings_name = 'Admin User'

    def load_settings(self):
        self.mainwindow.tabWidget.setTabVisible(3, True)
        self.mainwindow.search_tabWidget.setTabVisible(2, True)


class GeneralUserSettings(UserSettings):
    """General User settings - default settings for access to all production features."""

    settings_name = 'General User'

    def load_settings(self):
        self.mainwindow.tabWidget.setTabVisible(3, False)
        self.mainwindow.search_tabWidget.setTabVisible(2, False)
        self.mainwindow.workflows_person_tab.setTabVisible(1, False)
        self.mainwindow.workflows_person_tab.setTabVisible(2, False)
        self.mainwindow.workflows_person_tab.setTabVisible(3, False)


USER_SETTINGS = {
    'Justin_Home_PC': AdminUserSettings,
    'Justin_Work_Laptop': AdminUserSettings,
}
