"""Contains classes for building the Deny Privileges Dialog."""
from loguru import logger
from PyQt6.QtCore import QDate

from munientry.builders.administrative import base_admin_builders as admin
from munientry.checkers.base_checks import BaseChecks
from munientry.loaders.cms_case_loaders import CmsDrivingInfoLoader
from munientry.models.privileges_models import DrivingPrivilegesInformation
from munientry.updaters.general_updaters import CaseInformationUpdater
from munientry.views.deny_privileges_dialog_ui import Ui_DenyPrivilegesDialog


class DenyPrivilegesViewModifier(admin.AdminViewModifier):
    """View class that creates and modifies the view for the Deny Privileges Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_view_dates()

    def set_view_dates(self):
        self.dialog.plea_trial_date.setDate(QDate.currentDate())


class DenyPrivilegesSignalConnector(admin.AdminSignalConnector):
    """Connects signals to slots for Deny Privileges Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()
        self.connect_other_dialog_signals()

    def connect_other_dialog_signals(self):
        self.dialog.deny_privileges_radio_btn.toggled.connect(
            self.dialog.functions.show_hide_deny_reasons_checkboxes,
        )
        self.dialog.permit_test_radio_btn.toggled.connect(
            self.dialog.functions.show_hide_test_reasons_fields,
        )


class DenyPrivilegesSlotFunctions(admin.AdminSlotFunctions):
    """Slot functions used only by Deny Privileges Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.deny_reasons_checkboxes = [
            self.dialog.hard_time_check_box,
            self.dialog.no_insurance_check_box,
            self.dialog.no_jurisdiction_check_box,
            self.dialog.petition_incomplete_check_box,
            self.dialog.prohibited_activities_check_box,
            self.dialog.no_employer_info_check_box,
        ]
        self.test_reasons_fields = [
            self.dialog.license_exp_date_label,
            self.dialog.license_exp_date_field,
            self.dialog.permanent_id_check_box,
        ]

    def show_hide_test_reasons_fields(self):
        if self.dialog.permit_test_radio_btn.isChecked():
            self.show_fields(self.test_reasons_fields)
        else:
            self.hide_fields(self.test_reasons_fields)

    def show_hide_deny_reasons_checkboxes(self):
        if self.dialog.deny_privileges_radio_btn.isChecked():
            self.show_fields(self.deny_reasons_checkboxes)
        else:
            self.hide_fields(self.deny_reasons_checkboxes)

    def show_fields(self, field_list):
        for element in field_list:
            element.show()

    def hide_fields(self, field_list):
        for element in field_list:
            element.hide()


class DenyPrivilegesCaseInformationUpdater(CaseInformationUpdater):
    """Updates case information for Deny Privileges Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)


class DenyPrivilegesDialogInfoChecks(BaseChecks):
    """Class with checks for the Deny Privileges Dialog."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.dialog_check_list = [
        ]
        self.check_status = self.perform_check_list()


class DenyPrivilegesDialog(admin.AdminDialogBuilder, Ui_DenyPrivilegesDialog):
    """Builder for the Deny Privileges Dialog.

    The judicial_officer for this entry is the selected Assignment Commissioner.
    """

    _case_information_model = DrivingPrivilegesInformation
    _case_loader = CmsDrivingInfoLoader
    _info_checker = DenyPrivilegesDialogInfoChecks
    _model_updater = DenyPrivilegesCaseInformationUpdater
    _signal_connector = DenyPrivilegesSignalConnector
    _slots = DenyPrivilegesSlotFunctions
    _view_modifier = DenyPrivilegesViewModifier
    dialog_name = 'Deny Privileges Entry'

    def additional_setup(self):
        self.setWindowTitle(f'{self.dialog_name} Case Information')
        self.functions.show_hide_deny_reasons_checkboxes()
        self.functions.show_hide_test_reasons_fields()