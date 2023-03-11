"""Module for custom PushButtons used for dialogs."""

from loguru import logger
from PyQt6.QtWidgets import QPushButton

from munientry.loaders.driving_caseload_functions import get_cms_driving_case_data
from munientry.loaders.criminal_caseload_functions import (
    get_crim_cms_case_data,
    set_case_table,
)
from munientry.loaders.civil_caseload_functions import get_civil_cms_case_data
from munientry.mainwindow.dialog_dictionary import DIALOG_BUTTON_DICT
from munientry.mainwindow.dialog_preload_checkers import (
    AdminFiscalPreloadChecker,
    AdminPreloadChecker,
    CivilPreloadChecker,
    CrimTrafficPreloadChecker,
    SchedulingPreloadChecker,
)



class DialogButton(QPushButton):
    """Custom QPushButton used for loading dialogs."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.set_up_widget()

    def set_up_widget(self):
        self.released.connect(self.load_dialog)

    def _create_dialog_instance(self, mainwindow, *args, **kwargs):
        dialog = DIALOG_BUTTON_DICT.get(self.sender().objectName())
        judicial_officer = mainwindow.judicial_officer
        cms_case_data = kwargs.pop('cms_case_data', None)
        case_table = kwargs.pop('case_table', None)
        workflow_status = kwargs.pop('workflow_status', None)
        mainwindow.dialog = dialog(
            judicial_officer, cms_case_data, case_table, workflow_status, *args, **kwargs,
        )
        logger.info(f'CMS Case Data: {cms_case_data}')
        mainwindow.dialog.exec()


class CrimDialogButton(DialogButton):
    """Custom Dialog button for all CrimTraffic dialogs."""

    def load_dialog(self):
        mainwindow = self.window()
        if CrimTrafficPreloadChecker(mainwindow).perform_checks():
            self._create_dialog_instance(
                mainwindow,
                cms_case_data=get_crim_cms_case_data(mainwindow),
                case_table=set_case_table(mainwindow),
                workflow_status=mainwindow.digital_workflow.workflow_status,
            )


class SchedDialogButton(DialogButton):
    """Custom Dialog button for all Scheduling dialogs."""

    def load_dialog(self):
        mainwindow = self.window()
        if SchedulingPreloadChecker(mainwindow).perform_checks():
            self._create_dialog_instance(
                mainwindow,
                cms_case_data=get_crim_cms_case_data(mainwindow),
                case_table=set_case_table(mainwindow),
            )


class CivilDialogButton(DialogButton):
    """Custom Dialog button for all Civil dialogs."""

    def load_dialog(self):
        mainwindow = self.window()
        if CivilPreloadChecker(mainwindow).perform_checks():
            self._create_dialog_instance(
                mainwindow,
                cms_case_data=get_civil_cms_case_data(mainwindow),
            )


class AdminDrivingDialogButton(DialogButton):
    """Custom Dialog button for Limited Driving Privileges dialog only."""

    def load_dialog(self):
        mainwindow = self.window()
        if AdminPreloadChecker(mainwindow).perform_checks():
            self._create_dialog_instance(
                mainwindow,
                cms_case_data=get_cms_driving_case_data(mainwindow),
            )


class AdminJuryDialogButton(DialogButton):
    """Custom Dialog button for Jury Payment Entry only."""

    def load_dialog(self):
        mainwindow = self.window()
        if AdminPreloadChecker(mainwindow).perform_checks():
            self._create_dialog_instance(
                mainwindow,
                cms_case_data=get_crim_cms_case_data(mainwindow),
                case_table=set_case_table(mainwindow),
            )


class AdminFiscalDialogButton(DialogButton):
    """Custom Dialog button for Fiscal Journal Entries only."""

    def load_dialog(self):
        mainwindow = self.window()
        if AdminFiscalPreloadChecker(mainwindow).perform_checks():
            self._create_dialog_instance(
                mainwindow,
            )


class WorkDialogButton(DialogButton):
    """Custom Dialog button for Workflow dialog buttons."""

    def load_dialog(self):
        button = self.sender()
        mainwindow = self.window()
        dialog = DIALOG_BUTTON_DICT.get(button.objectName())
        mainwindow.dialog = dialog()
        mainwindow.dialog.exec()
