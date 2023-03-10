"""Module for custom PushButtons used for dialogs."""
from loguru import logger
from PyQt6.QtWidgets import QPushButton

from munientry.checkers.dialog_preload_checkers import (
    AdminFiscalPreloadChecker,
    AdminPreloadChecker,
    CivilPreloadChecker,
    CrimTrafficPreloadChecker,
    SchedulingPreloadChecker,
)
from munientry.loaders.dialog_loader import CrimDialogButtonLoader, SchedDialogButtonLoader
from munientry.mainwindow.dialog_dictionary import BUTTON_DICT


class DialogButton(QPushButton):
    """Custom QPushButton used for loading dialogs."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.set_up_widget()

    def set_up_widget(self):
        self.released.connect(self.load_dialog)

    def load_dialog(self):
        button = self.sender()
        mainwindow = self.window()


class CrimDialogButton(DialogButton):

    def __init__(self, parent=None):
        super().__init__(parent)

    def load_dialog(self):
        button = self.sender()
        dialog = BUTTON_DICT.get(button.objectName())
        mainwindow = self.window()
        if CrimTrafficPreloadChecker(mainwindow).perform_checks():
            load_data = CrimDialogButtonLoader(mainwindow).get_case_data()
            judicial_officer, cms_case_data, case_table, workflow_status = load_data
            dialog(judicial_officer, cms_case_data, case_table, workflow_status).exec()


class SchedDialogButton(DialogButton):

    def __init__(self, parent=None):
        super().__init__(parent)

    def load_dialog(self):
        button = self.sender()
        dialog = BUTTON_DICT.get(button.objectName())
        mainwindow = self.window()
        if SchedulingPreloadChecker(mainwindow).perform_checks():
            load_data = SchedDialogButtonLoader(mainwindow).get_case_data()
            judicial_officer, cms_case_data, case_table= load_data
            dialog(judicial_officer, cms_case_data, case_table).exec()


class AdminDialogButton(DialogButton):
    pass


class WorkDialogButton(DialogButton):
    pass