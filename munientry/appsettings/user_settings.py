"""Module for user settings for the application."""
from loguru import logger


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
        pass


class CommissionerUserSettings(UserSettings):
    """Commissioner User settings - opens application on scheduling tab."""

    settings_name = 'Commisssioner User'

    def load_settings(self):
        self.mainwindow.workflows_person_tab.setTabVisible(1, False)
        self.mainwindow.workflows_person_tab.setTabVisible(2, False)
        self.mainwindow.workflows_person_tab.setTabVisible(3, False)
        self.mainwindow.tabWidget.setCurrentIndex(1)


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

    def load_settings(self):
        self.mainwindow.main_TabWidget.setTabVisible(0, False)
        self.mainwindow.workflows_person_tab.setTabVisible(1, False)
        self.mainwindow.workflows_person_tab.setTabVisible(2, False)
        self.mainwindow.workflows_person_tab.setTabVisible(3, False)


