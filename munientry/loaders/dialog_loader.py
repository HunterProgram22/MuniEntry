"""Module containing classes and functions for loading dialogs from the Main Window."""
from __future__ import annotations

from typing import Optional

from loguru import logger
from PyQt6.QtWidgets import QMessageBox

from munientry.data import sql_server_getters as sql_server
from munientry.models.cms_models import CmsCaseInformation
from munientry.models.privileges_models import DrivingPrivilegesInformation
from munientry.widgets.message_boxes import WarningBox


def search_daily_case_list(daily_case_list, last_name: str) -> tuple:
    """Loops through all cases in daily case list to find matching last names.

    :daily_case_list: A DailyCaseListComboBox object.
    """
    case_match_count = 0
    matched_cases_list = []
    for case in daily_case_list.all_items():
        if case == '':
            continue
        checked_last_name, checked_case_number = case.split(' - ')
        if checked_last_name == last_name:
            case_match_count += 1
            matched_cases_list.append(checked_case_number)
    return case_match_count, matched_cases_list


def ask_if_cases_combined(last_name: str, matched_cases_list: list) -> object:
    """Asks user if they want to combine matched cases or just load single selected case."""
    case_numbers = '\n'.join(matched_cases_list)
    case_count = len(matched_cases_list)
    message = (
        f'There are {case_count} cases with the last name {last_name}.\n\nThe matching '
        + f'cases are:\n{case_numbers}\n\nDo you want to combine them into a single entry?'
    )
    return WarningBox(message, 'Companion Cases').exec()


def check_for_companion_cases(daily_case_list) -> CmsCaseInformation:
    """Checks for matching last names to find potential companion cases to load.

    :daily_case_list: A DailyCaseListComboBox object.
    """
    last_name, case_number = daily_case_list.currentText().split(' - ')
    case_match_count, matched_cases_list = search_daily_case_list(daily_case_list, last_name)
    if case_match_count > 1:
        response = ask_if_cases_combined(last_name, matched_cases_list)
        if response == QMessageBox.StandardButton.Yes:
            return load_multiple_cases(matched_cases_list)
    return load_single_case(case_number)


def set_case_to_load(daily_case_list) -> CmsCaseInformation:
    """Returns CmsCaseInformation object model for loading to the template.

    :daily_case_list: The DailyCaseListComboBox that is currently selected on the Main Window.
    """
    if daily_case_list.currentText() == '':
        return load_no_case()
    return check_for_companion_cases(daily_case_list)


def load_no_case() -> CmsCaseInformation:
    """Loads the CmsCaseInformation model with no data.

    Avoids unnecessary call to the database when there is no data to load.
    """
    return CmsCaseInformation()


def load_no_case_driving() -> DrivingPrivilegesInformation:
    """Loads the DrivingPrivilegesInformation model with no data.

    Avoids unnecessary call to the database when there is no data to load.
    """
    return DrivingPrivilegesInformation()


def load_single_case(case_number: str) -> CmsCaseInformation:
    """Loads a single case into the CmsCaseInformation model."""
    return sql_server.CriminalCaseSQLServer(case_number).load_case()


def load_single_driving_info_case(case_number: str) -> CmsCaseInformation:
    """Loads a single with Driving Info query into the CmsCaseInformation model."""
    return sql_server.DrivingInfoSQLServer(case_number).load_case()


def load_multiple_cases(matched_case_numbers: list) -> CmsCaseInformation:
    """Loads multiple cases into the CmsCaseInformation model."""
    return sql_server.MultipleCriminalCaseSQLServer(matched_case_numbers).load_case()


class DialogLoader(object):
    """Base Loader class for loading a Dialog, actual Dialog is loaded by subclass."""

    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        self.dialog = self.load_dialog()

    def load_dialog(self):
        self.button_dict = self.mainwindow.dialog_buttons_dict

    def _set_case_table(self):
        if self.mainwindow.search_tabWidget.currentWidget().objectName() == 'case_list_tab':
            return self.mainwindow.daily_case_list.name
        return None

    def _get_cms_case_data(self):
        if self.mainwindow.search_tabWidget.currentWidget().objectName() == 'case_list_tab':
            return set_case_to_load(self.mainwindow.daily_case_list)
        case_number = self.mainwindow.case_search_box.text()
        return load_single_case(case_number)

    def _get_case_number(self) -> Optional[str]:
        if self.mainwindow.search_tabWidget.currentWidget().objectName() == 'case_list_tab':
            try:
                _last_name, case_number = self.mainwindow.daily_case_list.currentText().split(' - ')
            except ValueError as err:
                logger.warning(err)
                return None
            return case_number
        return self.mainwindow.case_search_box.text()


class CrimTrafficDialogLoader(DialogLoader):
    """Loader class for CrimTraffic Dialogs."""

    def load_dialog(self):
        super().load_dialog()
        return self._load_crimtraffic_dialog_process()

    def _load_crimtraffic_dialog_process(self):
        case_table = self._set_case_table()
        judicial_officer = self.mainwindow.judicial_officer
        cms_case_data = self._get_cms_case_data()
        logger.info(f'CMS Case Data: {cms_case_data}')
        return self.button_dict.get(self.mainwindow.sender())(
            judicial_officer,
            cms_case=cms_case_data,
            case_table=case_table,
            workflow_status=self.mainwindow.digital_workflow.workflow_status,
        )


class AdminJuryDialogLoader(DialogLoader):
    """Loader class for Jury Payment Dialog."""

    def load_dialog(self):
        super().load_dialog()
        return self._load_admin_jury_pay_dialog_process()

    def _load_admin_jury_pay_dialog_process(self):
        case_table = self._set_case_table()
        judicial_officer = self.mainwindow.judicial_officer
        cms_case_data = self._get_cms_case_data()
        logger.info(f'CMS Case Data: {cms_case_data}')
        return self.button_dict.get(self.mainwindow.sender())(
            judicial_officer,
            cms_case=cms_case_data,
            case_table=case_table,
        )


class AdminDrivingDialogLoader(DialogLoader):
    """Loader class for Driving Privileges Dialog."""

    def load_dialog(self):
        super().load_dialog()
        return self._load_admin_driving_dialog_process()

    def _load_admin_driving_dialog_process(self):
        """Used for driving privileges entry because case search query is unique."""
        case_table = None
        judicial_officer = self.mainwindow.judicial_officer
        case_number = self._get_case_number()
        if case_number is None:
            cms_case_data = load_no_case_driving()
        else:
            cms_case_data = load_single_driving_info_case(case_number)
        logger.info(f'CMS Case Data: {cms_case_data}')
        return self.button_dict.get(self.mainwindow.sender())(
            judicial_officer,
            cms_case=cms_case_data,
            case_table=case_table,
        )


class AdminFiscalDialogLoader(DialogLoader):
    """Loader class for Admin Fiscal Entries Dialog."""

    def load_dialog(self):
        super().load_dialog()
        return self._load_admin_fiscal_dialog_process()

    def _load_admin_fiscal_dialog_process(self):
        judicial_officer = self.mainwindow.judicial_officer
        return self.button_dict.get(self.mainwindow.sender())(judicial_officer)


class DigitalWorkflowDialogLoader(DialogLoader):
    """Loader class for Judge and Magistrate Digital Workflow Dialogs."""

    def load_dialog(self):
        super().load_dialog()
        return self._load_digital_workflow_dialog_process()

    def _load_digital_workflow_dialog_process(self):
        return self.button_dict.get(self.mainwindow.sender())()


class ProbationWorkflowDialogLoader(DialogLoader):
    """Loader class for Probation Digital Workflow Dialogs."""

    def load_dialog(self):
        """This method is the same as load digital workflow dialog for now.

        May need changes later or can refactor into single method.
        """
        super().load_dialog()
        return self._load_digital_workflow_dialog_process()

    def _load_digital_workflow_dialog_process(self):
        return self.button_dict.get(self.mainwindow.sender())()


class SchedulingDialogLoader(DialogLoader):
    """Loader class for Scheduling Dialogs."""

    def load_dialog(self):
        super().load_dialog()
        return self._load_scheduling_dialog_process()

    def _load_scheduling_dialog_process(self):
        case_table = self._set_case_table()
        judicial_officer = self.mainwindow.judicial_officer
        cms_case_data = self._get_cms_case_data()
        logger.info(f'CMS Case Data: {cms_case_data}')
        return self.button_dict.get(self.mainwindow.sender())(
            judicial_officer,
            cms_case=cms_case_data,
            case_table=case_table,
        )
