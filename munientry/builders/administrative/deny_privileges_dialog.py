"""Contains classes for building the Driving Privileges Dialog."""
from loguru import logger
from PyQt6.QtCore import QDate

from munientry.builders.administrative import base_admin_builders as admin
from munientry.checkers.base_checks import BaseChecks
from munientry.loaders.cms_case_loaders import CmsDrivingInfoLoader
from munientry.models.privileges_models import DrivingPrivilegesInformation
from munientry.updaters.general_updaters import CaseInformationUpdater
from munientry.views.deny_privileges_dialog_ui import Ui_DenyPrivilegesDialog


class DenyPrivilegesViewModifier(admin.AdminViewModifier):
    """View class that creates and modifies the view for the Driving Privileges Dialog."""

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


class DenyPrivilegesSlotFunctions(admin.AdminSlotFunctions):
    """Slot functions used only by Deny Privileges Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)


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