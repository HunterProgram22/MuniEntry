"""Contains classes for building the Admin Fiscal Dialog."""
from loguru import logger
from PyQt5.QtCore import QDate

from munientry.builders import base_builders as base
from munientry.builders.administrative import base_admin_builders as admin
from munientry.checkers.base_checks import BaseChecker
from munientry.models.admin_fiscal_models import AdminFiscalEntryInformation
from munientry.settings import FISCAL_SAVE_PATH
from munientry.views.admin_fiscal_dialog_ui import Ui_AdminFiscalDialog
from munientry.updaters.base_updaters import BaseDialogUpdater
from munientry.widgets.message_boxes import BLANK, FAIL, PASS, RequiredBox
from munientry.models.template_types import TEMPLATE_DICT

TODAY = QDate.currentDate()


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
        self.connect_other_dialog_signals()

    def connect_other_dialog_signals(self):
        pass


class AdminFiscalSlotFunctions(admin.AdminSlotFunctions):
    """Slot functions used only by Admin Fiscal Dialog."""

    save_path = FISCAL_SAVE_PATH

    def __init__(self, dialog):
        super().__init__(dialog)

    def clear_case_information_fields(self):
        self.dialog.account_number_box.clear()
        self.dialog.subaccount_number_box.clear()

    def set_document_name(self) -> str:
        """Overrides BaseDialogSlotFunctions set_document_name.

        Sets the document name based on driver name instead of case number.
        """
        account_number = self.dialog.entry_case_information.account_number
        vendor_name = self.dialog.entry_case_information.disbursement_vendor
        invoice = self.dialog.entry_case_information.invoice_number
        return f'{account_number}_{vendor_name}_{invoice}.docx'


class AdminFiscalCaseInformationUpdater(BaseDialogUpdater):
    """Updates case information for Admin Fiscal Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_account_numbers_and_date()
        self.set_payment_information()

    def set_account_numbers_and_date(self):
        self.model.judicial_officer = self.dialog.judicial_officer
        account_number_box_string = self.dialog.account_number_box.currentText()
        self.model.account_name, self.model.account_number = account_number_box_string.split(' - ')
        subaccount_number_box_string = self.dialog.subaccount_number_box.currentText()
        self.model.subaccount_name, self.model.subaccount_number = subaccount_number_box_string.split(' - ')
        self.model.plea_trial_date = self.dialog.plea_trial_date.date().toString('MMMM dd, yyyy')

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

    build_dict = {
        'dialog_name': 'Admin Fiscal Entry',
        'view': AdminFiscalViewModifier,
        'slots': AdminFiscalSlotFunctions,
        'signals': AdminFiscalSignalConnector,
        'case_information_model': AdminFiscalEntryInformation,
        'loader': None,
        'updater': AdminFiscalCaseInformationUpdater,
        'info_checker': AdminFiscalInfoChecker,
    }
    def __init__(self, judicial_officer=None, parent=None):
        super().__init__(parent)
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.judicial_officer = judicial_officer
        self.load_entry_case_information_model()
        self.additional_setup()

    def additional_setup(self):
        self.setWindowTitle(f'{self.dialog_name} Information')


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
