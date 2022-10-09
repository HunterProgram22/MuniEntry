"""Contains classes for building the Admin Fiscal Dialog."""
from loguru import logger
from PyQt5.QtCore import QDate

from munientry.builders import base_builders as base
from munientry.builders.administrative import base_admin_builders as admin
from munientry.checkers.base_checks import BaseChecker
from munientry.models.admin_fiscal_models import AdminFiscalEntryInformation
from munientry.settings import DRIVE_SAVE_PATH
from munientry.views.admin_fiscal_dialog_ui import Ui_AdminFiscalDialog
from munientry.updaters.general_updaters import CaseInformationUpdater
from munientry.widgets.message_boxes import BLANK, FAIL, PASS, RequiredBox

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

    def __init__(self, dialog):
        super().__init__(dialog)

    def create_entry(self, save_path: str=None) -> None:
        """Overrides BaseDialogSlotFunctions create_entry.

        Sets a specific save path used to save Admin Fiscal.
        """
        save_path = DRIVE_SAVE_PATH
        super().create_entry(save_path)

    def set_document_name(self) -> str:
        """Overrides BaseDialogSlotFunctions set_document_name.

        Sets the document name based on driver name instead of case number.
        """
        template_name = self.dialog.template.template_name
        return f'TEST_{template_name}.docx'


class AdminFiscalCaseInformationUpdater(CaseInformationUpdater):
    """Updates case information for Admin Fiscal Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_case_number_and_date()

    def set_case_number_and_date(self):
        self.model.judicial_officer = self.dialog.judicial_officer
        self.model.case_number = self.dialog.case_number_lineEdit.text()
        self.model.plea_trial_date = self.dialog.plea_trial_date.date().toString('MMMM dd, yyyy')


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
        self.load_cms_data_to_view()
        self.additional_setup()

    def additional_setup(self):
        self.setWindowTitle(f'{self.dialog_name} Information')


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
