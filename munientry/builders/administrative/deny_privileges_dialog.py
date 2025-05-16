"""Contains classes for building the Deny Privileges Dialog."""
from loguru import logger
from PyQt6.QtCore import QDate

from munientry.builders.administrative import base_admin_builders as admin
from munientry.checkers.base_checks import BaseChecks
from munientry.entrycreators.entry_creator import DrivingPrivilegesEntryCreator
from munientry.loaders.cms_case_loaders import CmsDrivingInfoLoader
from munientry.models.privileges_models import DenyPrivilegesInformation
from munientry.models.party_types import JudicialOfficer
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
            self.dialog.out_of_state_license_check_box,
            self.dialog.no_pay_plan_check_box,
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

    def create_entry_process(self) -> None:
        DrivingPrivilegesEntryCreator(self.dialog).create_entry_process()


class DenyPrivilegesCaseInformationUpdater(CaseInformationUpdater):
    """Updates case information for Deny Privileges Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_case_number_and_date()
        self.set_privileges_info()

    def set_case_number_and_date(self):
        self.model.judicial_officer = self.set_judicial_officer()
        self.model.case_number = self.dialog.case_number_lineEdit.text()
        self.model.plea_trial_date = self.dialog.plea_trial_date.date().toString('MMMM dd, yyyy')

    def set_judicial_officer(self):
        """This method sets the judicial officer for the case information model.

        It overrides the selected officer for denial of driving privileges because they are prepared
        by an assignment commissioner for the signature of a judge and judges are not available
        options for staff on the Administrative entries tab. This is not ideal.
        """
        judicial_officer = self.dialog.judicial_officer
        if judicial_officer.last_name == 'Spiers':
            return JudicialOfficer('Mark', 'Fowler', 'Judge')
        elif judicial_officer.last_name == 'Dattilo':
            return JudicialOfficer('Kyle', 'Rohrer', 'Judge')
        else:
            return judicial_officer

    def set_privileges_info(self):
        self.model.deny_privileges = self.dialog.deny_privileges_radio_btn.isChecked()
        self.model.permit_test_or_renew = self.dialog.permit_test_radio_btn.isChecked()
        self.model.permit_renew_expired = self.dialog.permit_renew_radio_btn.isChecked()
        self.model.hard_time = self.dialog.hard_time_check_box.isChecked()
        self.model.no_insurance = self.dialog.no_insurance_check_box.isChecked()
        self.model.petition_incomplete = self.dialog.petition_incomplete_check_box.isChecked()
        self.model.no_jurisdiction = self.dialog.no_jurisdiction_check_box.isChecked()
        self.model.no_employer_info = self.dialog.no_employer_info_check_box.isChecked()
        self.model.prohibited_activities = self.dialog.prohibited_activities_check_box.isChecked()
        self.model.out_of_state_license = self.dialog.out_of_state_license_check_box.isChecked()
        self.model.license_expiration_date = self.dialog.license_exp_date_field.get_date_as_string()
        self.model.permanent_id = self.dialog.permanent_id_check_box.isChecked()
        self.model.no_pay_plan = self.dialog.no_pay_plan_check_box.isChecked()


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

    _case_information_model = DenyPrivilegesInformation
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
