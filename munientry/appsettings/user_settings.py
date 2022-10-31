"""Module for user settings for the application."""
from loguru import logger

from munientry.settings import SOCKET_NAME


def load_user_settings(mainwindow):
    if SOCKET_NAME in ['Justin_Home_PC', 'Justin_Work_Laptop_PC']:
        return AdminUserSettings(mainwindow)
    return GeneralUserSettings(mainwindow)


class AdminUserSettings(object):
    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        logger.info('Setting Admin User Settings')
        self.mainwindow.tabWidget.setTabVisible(3, True)
        self.mainwindow.search_tabWidget.setTabVisible(2, True)


class GeneralUserSettings(object):
    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        logger.info('Setting General User Settings')
        self.mainwindow.tabWidget.setTabVisible(3, False)
        self.mainwindow.search_tabWidget.setTabVisible(2, False)
        self.mainwindow.workflows_person_tab.setTabVisible(1, False)
        self.mainwindow.workflows_person_tab.setTabVisible(2, False)
        self.mainwindow.workflows_person_tab.setTabVisible(3, False)
