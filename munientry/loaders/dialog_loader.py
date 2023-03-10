"""Contains classes for loading dialogs from the Main Window."""
from typing import Optional

from loguru import logger

from munientry.loaders.driving_caseload_functions import (
    load_no_case_driving,
    load_single_driving_info_case,
)
from munientry.loaders.general_caseload_functions import (
    load_case_information,
    load_single_case,
    load_single_civil_case,
)


class DialogLoader(object):
    """Base Loader class for loading a Dialog, actual Dialog is loaded by subclass."""

    def __init__(self, mainwindow):
        self.mainwindow = mainwindow

    def _set_case_table(self):
        if self.mainwindow.cases_tab_widget.currentWidget().objectName() == 'case_list_tab':
            return self.mainwindow.daily_case_list.name
        return None

    def _get_cms_case_data(self):
        if self.mainwindow.cases_tab_widget.currentWidget().objectName() == 'case_list_tab':
            return load_case_information(self.mainwindow.daily_case_list)
        case_number = self.mainwindow.crim_case_search_box.text()
        return load_single_case(case_number)

    def _get_case_number(self) -> Optional[str]:
        if self.mainwindow.cases_tab_widget.currentWidget().objectName() == 'case_list_tab':
            try:
                _last_name, case_number = self.mainwindow.daily_case_list.currentText().split(' - ')
            except ValueError as err:
                logger.warning(err)
                return None
            return case_number
        return self.mainwindow.crim_case_search_box.text()


class CrimDialogButtonLoader(DialogLoader):

    def get_case_data(self):
        case_table = self._set_case_table()
        judicial_officer = self.mainwindow.judicial_officer
        cms_case_data = self._get_cms_case_data()
        workflow_status = self.mainwindow.digital_workflow.workflow_status
        logger.info(f'CMS Case Data: {cms_case_data}')
        return (judicial_officer, cms_case_data, case_table, workflow_status)


class SchedDialogButtonLoader(DialogLoader):

    def get_case_data(self):
        case_table = self._set_case_table()
        judicial_officer = self.mainwindow.judicial_officer
        cms_case_data = self._get_cms_case_data()
        logger.info(f'CMS Case Data: {cms_case_data}')
        return (judicial_officer, cms_case_data, case_table)




# class CrimTrafficDialogLoader(DialogLoader):
#     """Loader class for CrimTraffic Dialogs."""
#
#     def load_dialog(self):
#         super().load_dialog()
#         return self._load_crimtraffic_dialog_process()
#
#     def _load_crimtraffic_dialog_process(self):
#         case_table = self._set_case_table()
#         judicial_officer = self.mainwindow.judicial_officer
#         cms_case_data = self._get_cms_case_data()
#         logger.info(f'CMS Case Data: {cms_case_data}')
#         return self.button_dict.get(self.mainwindow.sender())(
#             judicial_officer,
#             cms_case=cms_case_data,
#             case_table=case_table,
#             workflow_status=self.mainwindow.digital_workflow.workflow_status,
#         )
#
#
# class AdminJuryDialogLoader(DialogLoader):
#     """Loader class for Jury Payment Dialog."""
#
#     def load_dialog(self):
#         super().load_dialog()
#         return self._load_admin_jury_pay_dialog_process()
#
#     def _load_admin_jury_pay_dialog_process(self):
#         case_table = self._set_case_table()
#         judicial_officer = self.mainwindow.judicial_officer
#         cms_case_data = self._get_cms_case_data()
#         logger.info(f'CMS Case Data: {cms_case_data}')
#         return self.button_dict.get(self.mainwindow.sender())(
#             judicial_officer,
#             cms_case=cms_case_data,
#             case_table=case_table,
#         )
#
#
# class AdminDrivingDialogLoader(DialogLoader):
#     """Loader class for Driving Privileges Dialog."""
#
#     def load_dialog(self):
#         super().load_dialog()
#         return self._load_admin_driving_dialog_process()
#
#     def _load_admin_driving_dialog_process(self):
#         """Used for driving privileges entry because case search query is unique."""
#         case_table = None
#         judicial_officer = self.mainwindow.judicial_officer
#         case_number = self._get_case_number()
#         if case_number is None:
#             cms_case_data = load_no_case_driving()
#         else:
#             cms_case_data = load_single_driving_info_case(case_number)
#         logger.info(f'CMS Case Data: {cms_case_data}')
#         return self.button_dict.get(self.mainwindow.sender())(
#             judicial_officer,
#             cms_case=cms_case_data,
#             case_table=case_table,
#         )
#
#
# class AdminFiscalDialogLoader(DialogLoader):
#     """Loader class for Admin Fiscal Entries Dialog."""
#
#     def load_dialog(self):
#         super().load_dialog()
#         return self._load_admin_fiscal_dialog_process()
#
#     def _load_admin_fiscal_dialog_process(self):
#         judicial_officer = self.mainwindow.judicial_officer
#         return self.button_dict.get(self.mainwindow.sender())(judicial_officer)
#
#
# class DigitalWorkflowDialogLoader(DialogLoader):
#     """Loader class for Judge and Magistrate Digital Workflow Dialogs."""
#
#     def load_dialog(self):
#         super().load_dialog()
#         return self._load_digital_workflow_dialog_process()
#
#     def _load_digital_workflow_dialog_process(self):
#         return self.button_dict.get(self.mainwindow.sender())()
#
#
# class ProbationWorkflowDialogLoader(DialogLoader):
#     """Loader class for Probation Digital Workflow Dialogs."""
#
#     def load_dialog(self):
#         """This method is the same as load digital workflow dialog for now.
#
#         May need changes later or can refactor into single method.
#         """
#         super().load_dialog()
#         return self._load_digital_workflow_dialog_process()
#
#     def _load_digital_workflow_dialog_process(self):
#         return self.button_dict.get(self.mainwindow.sender())()
#
#
# class SchedulingDialogLoader(DialogLoader):
#     """Loader class for Scheduling Dialogs."""
#
#     def load_dialog(self):
#         super().load_dialog()
#         return self._load_scheduling_dialog_process()
#
#     def _load_scheduling_dialog_process(self):
#         case_table = self._set_case_table()
#         judicial_officer = self.mainwindow.judicial_officer
#         cms_case_data = self._get_cms_case_data()
#         logger.info(f'CMS Case Data: {cms_case_data}')
#         return self.button_dict.get(self.mainwindow.sender())(
#             judicial_officer,
#             cms_case=cms_case_data,
#             case_table=case_table,
#         )
#
#
# class CivilDialogLoader(object):
#     def __init__(self, mainwindow):
#         self.mainwindow = mainwindow
#         self.dialog = self.load_dialog()
#
#     def load_dialog(self):
#         self.button_dict = self.mainwindow.dialog_buttons_dict
#         return self._load_civil_dialog_process()
#
#     def _get_cms_case_data(self):
#         case_number = self.mainwindow.civil_case_search_box.text()
#         return load_single_civil_case(case_number)
#
#     def _load_civil_dialog_process(self):
#         judicial_officer = self.mainwindow.judicial_officer
#         cms_case_data = self._get_cms_case_data()
#         return self.button_dict.get(self.mainwindow.sender())(
#             judicial_officer,
#             cms_case=cms_case_data,
#         )
