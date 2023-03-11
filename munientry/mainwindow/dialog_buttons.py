"""Module for custom PushButtons used for dialogs."""
from typing import Optional

from loguru import logger
from PyQt6.QtWidgets import QPushButton

from munientry.loaders.driving_caseload_functions import (
    load_no_case_driving,
    load_single_driving_info_case,
)
from munientry.mainwindow.dialog_preload_checkers import (
    AdminFiscalPreloadChecker,
    AdminPreloadChecker,
    CivilPreloadChecker,
    CrimTrafficPreloadChecker,
    SchedulingPreloadChecker,
)
from munientry.mainwindow.dialog_dictionary import BUTTON_DICT
from munientry.loaders.general_caseload_functions import (
    load_case_information,
    load_single_case,
    load_single_civil_case,
)


class DialogButton(QPushButton):
    """Custom QPushButton used for loading dialogs."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.set_up_widget()

    def set_up_widget(self):
        self.released.connect(self.load_dialog)

    def _set_case_table(self, mainwindow):
        if mainwindow.cases_tab_widget.currentWidget().objectName() == 'case_list_tab':
            return mainwindow.daily_case_list.name
        return None

    def _get_cms_case_data(self, mainwindow):
        if mainwindow.cases_tab_widget.currentWidget().objectName() == 'case_list_tab':
            return load_case_information(mainwindow.daily_case_list)
        case_number = mainwindow.crim_case_search_box.text()
        return load_single_case(case_number)

    def _get_case_number(self, mainwindow) -> Optional[str]:
        if mainwindow.cases_tab_widget.currentWidget().objectName() == 'case_list_tab':
            try:
                _last_name, case_number = mainwindow.daily_case_list.currentText().split(' - ')
            except ValueError as err:
                logger.warning(err)
                return None
            return case_number
        return mainwindow.crim_case_search_box.text()

    def _create_dialog_instance(self, mainwindow, *args, **kwargs):
        button = self.sender()
        dialog = BUTTON_DICT.get(button.objectName())
        judicial_officer = mainwindow.judicial_officer
        cms_case_data = kwargs.pop('cms_case_data', None)
        case_table = kwargs.pop('case_table', None)
        workflow_status = kwargs.pop('workflow_status', None)
        mainwindow.dialog = dialog(judicial_officer, cms_case_data, case_table, workflow_status, *args, **kwargs)
        logger.info(f'CMS Case Data: {cms_case_data}')
        mainwindow.dialog.exec()


class CrimDialogButton(DialogButton):

    def load_dialog(self):
        mainwindow = self.window()
        if CrimTrafficPreloadChecker(mainwindow).perform_checks():
            self._create_dialog_instance(
                mainwindow,
                cms_case_data = self._get_cms_case_data(mainwindow),
                case_table = self._set_case_table(mainwindow),
                workflow_status = mainwindow.digital_workflow.workflow_status,
            )


class SchedDialogButton(DialogButton):

    def load_dialog(self):
        mainwindow = self.window()
        if SchedulingPreloadChecker(mainwindow).perform_checks():
            self._create_dialog_instance(
                mainwindow,
                cms_case_data = self._get_cms_case_data(mainwindow),
                case_table = self._set_case_table(mainwindow),
            )


class CivilDialogButton(DialogButton):

    def load_dialog(self):
        mainwindow = self.window()
        if CivilPreloadChecker(mainwindow).perform_checks():
            self._create_dialog_instance(
                mainwindow,
                cms_case_data = self._get_cms_case_data(mainwindow),
            )

    def _get_cms_case_data(self, mainwindow):
        case_number = mainwindow.civil_case_search_box.text()
        return load_single_civil_case(case_number)


class AdminDrivingDialogButton(DialogButton):

    def load_dialog(self):
        mainwindow = self.window()
        if AdminPreloadChecker(mainwindow).perform_checks():
            self._create_dialog_instance(
                mainwindow,
                cms_case_data = self._get_cms_driving_case_data(mainwindow),
            )

    def _get_cms_driving_case_data(self, mainwindow):
        case_number = self._get_case_number(mainwindow)
        if case_number is None:
            return load_no_case_driving()
        return load_single_driving_info_case(case_number)


class AdminJuryDialogButton(DialogButton):

    def load_dialog(self):
        mainwindow = self.window()
        if AdminPreloadChecker(mainwindow).perform_checks():
            self._create_dialog_instance(
                mainwindow,
                cms_case_data=self._get_cms_case_data(mainwindow),
                case_table=self._set_case_table(mainwindow),
            )


class AdminFiscalDialogButton(DialogButton):

    def load_dialog(self):
        mainwindow = self.window()
        if AdminFiscalPreloadChecker(mainwindow).perform_checks():
            self._create_dialog_instance(
                mainwindow,
            )


class WorkDialogButton(DialogButton):

    def load_dialog(self):
        button = self.sender()
        mainwindow = self.window()
        dialog = BUTTON_DICT.get(button.objectName())
        mainwindow.dialog = dialog()
        mainwindow.dialog.exec()
