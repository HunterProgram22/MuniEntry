"""Contains classes for building the Time to Pay Dialog."""
from loguru import logger
from PyQt6.QtCore import QDate

from munientry.builders.administrative import base_admin_builders as admin
from munientry.checkers.base_checks import BaseChecks
# from munientry.entrycreators.entry_creator import JuryPaymentEntryCreator
from munientry.loaders.cms_case_loaders import CrimCmsLoader
from munientry.models.jury_models import JuryPaymentInformation
from munientry.updaters.base_updaters import BaseDialogUpdater
from munientry.views.time_to_pay_dialog_ui import Ui_TimeToPayDialog


class TimeToPayViewModifier(admin.AdminViewModifier):
    """View class that creates and modifies the view for the Time to Pay Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_view_dates()

    def set_view_dates(self):
        today = QDate.currentDate()
        self.dialog.entry_date.setDate(today)


class TimeToPaySlotFunctions(admin.AdminSlotFunctions):
    """Additional functions for the Time to Pay Dialog"""

    def create_entry_process(self) -> None:
        TimeToPayEntryCreator(self.dialog).create_entry_process()


class TimeToPaySignalConnector(admin.AdminSignalConnector):
    """Connects signals to slots for Time to Pay Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()


class TimeToPayInfoChecks(BaseChecks):
    """Class with checks for the Time to Pay Dialog."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.dialog_check_list = []
        self.check_status = self.perform_check_list()


class TimeToPayCaseInformationUpdater(BaseDialogUpdater):
    """Base class for Time to Pay Updater."""

    def __init__(self, dialog: 'QDialog') -> None:
        super().__init__(dialog)
        self.model.judicial_officer = self.dialog.judicial_officer
        self.update_model_with_case_information_frame_data()

    def update_model_with_case_information_frame_data(self) -> None:
        self.set_case_number_and_date()
        self.set_party_information()

    def set_case_number_and_date(self) -> None:
        self.model.case_number = self.dialog.case_number_lineEdit.text()
        self.model.entry_date = self.dialog.entry_date.date().toString('MMMM dd, yyyy')

    def set_party_information(self) -> None:
        self.model.defendant.first_name = self.dialog.defendant_first_name_lineEdit.text()
        self.model.defendant.last_name = self.dialog.defendant_last_name_lineEdit.text()


class TimeToPayDialog(admin.AdminDialogBuilder, Ui_TimeToPayDialog):
    """Builder for the Time to Pay Dialog."""

    _case_information_model = JuryPaymentInformation
    _case_loader = CrimCmsLoader
    _info_checker = TimeToPayInfoChecks
    _model_updater = TimeToPayCaseInformationUpdater
    _signal_connector = TimeToPaySignalConnector
    _slots = TimeToPaySlotFunctions
    _view_modifier = TimeToPayViewModifier
    dialog_name = 'Time To Pay Entry'
