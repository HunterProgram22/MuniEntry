"""Contains classes for building the Admin Fiscal Dialog."""
from loguru import logger

from munientry.builders import base_builders as base
from munientry.builders.administrative import base_admin_builders as admin
from munientry.checkers.base_checks import BaseChecker
from munientry.entrycreators.entry_creator import AdminFiscalEntryCreator
from munientry.models.admin_fiscal_models import AdminFiscalEntryInformation
from munientry.models.template_types import TEMPLATE_DICT
from munientry.appsettings.pyqt_constants import TODAY
from munientry.updaters.base_updaters import BaseDialogUpdater
from munientry.views.admin_fiscal_dialog_ui import Ui_AdminFiscalDialog


class AdminFiscalViewModifier(admin.AdminViewModifier):
    """View class that creates and modifies the view for the Admin Fiscal Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_view_dates()

    def set_view_dates(self):
        self.dialog.plea_trial_date.setDate(TODAY)


class AdminFiscalSignalConnector(admin.AdminSignalConnector):
    """Connects signals to slots for Admin Fiscal Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()


class AdminFiscalSlotFunctions(admin.AdminSlotFunctions):
    """Slot functions used only by Admin Fiscal Dialog."""

    def create_entry_process(self) -> None:
        AdminFiscalEntryCreator(self.dialog).create_entry_process()

    def clear_case_information_fields(self):
        self.dialog.account_number_box.clear()
        self.dialog.subaccount_number_box.clear()


class AdminFiscalCaseInformationUpdater(BaseDialogUpdater):
    """Updates case information for Admin Fiscal Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.model.plea_trial_date = self.dialog.plea_trial_date.date().toString('MMMM dd, yyyy')
        self.set_account_numbers()
        self.set_subaccount_numbers()
        self.set_payment_information()

    def set_account_numbers(self):
        self.model.judicial_officer = self.dialog.judicial_officer
        account_number_box_string = self.dialog.account_number_box.currentText()
        acount_name, account_number = account_number_box_string.split(' - ')
        self.model.account_name = acount_name
        self.model.account_number = account_number

    def set_subaccount_numbers(self):
        subaccount_number_box_string = self.dialog.subaccount_number_box.currentText()
        subaccount_name, subaccount_number = subaccount_number_box_string.split(' - ')
        self.model.subaccount_name = subaccount_name
        self.model.subaccount_number = subaccount_number

    def set_payment_information(self):
        self.model.disbursement_reason = self.dialog.disbursement_reason_lineEdit.text()
        self.model.disbursement_amount = self.dialog.disbursement_amount_lineEdit.text()
        self.model.disbursement_vendor = self.dialog.disbursement_vendor_lineEdit.text()
        self.model.invoice_number = self.dialog.invoice_number_lineEdit.text()


class AdminFiscalInfoChecker(BaseChecker):
    """Class with checks for the Admin Fiscal Dialog."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.dialog_check_list = []
        self.check_status = self.perform_check_list()


class AdminFiscalDialog(base.BaseDialogBuilder, Ui_AdminFiscalDialog):
    """Builder for the Admin Fiscal Dialog.

    The judicial_officer for this entry is the selected Administrative Staff Person.
    """

    _case_information_model = AdminFiscalEntryInformation
    _case_loader = None
    _info_checker = AdminFiscalInfoChecker
    _model_updater = AdminFiscalCaseInformationUpdater
    _signal_connector = AdminFiscalSignalConnector
    _slots = AdminFiscalSlotFunctions
    _view_modifier = AdminFiscalViewModifier
    dialog_name = 'Admin Fiscal Entry'

    def __init__(self, judicial_officer=None, parent=None):
        super().__init__(parent)
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.judicial_officer = judicial_officer
        self.load_entry_case_information_model()
        self.additional_setup()

    def additional_setup(self):
        self.setWindowTitle(f'{self.dialog_name} Information')


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
