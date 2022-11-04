"""Contains classes for building the Juror Payment Dialog."""
from loguru import logger

from munientry.builders.administrative import base_admin_builders as admin
from munientry.checkers.base_checks import BaseChecker
from munientry.models.jury_models import JuryPaymentInformation
from munientry.loaders.cms_case_loaders import CmsNoChargeLoader
from munientry.updaters.jury_updaters import JuryPaymentCaseInformationUpdater
from munientry.views.juror_payment_dialog_ui import Ui_JurorPaymentDialog
from munientry.appsettings.pyqt_constants import TODAY


class JuryPaymentViewModifier(admin.AdminViewModifier):
    """View class that creates and modifies the view for the Jury Payment Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_view_dates()

    def set_view_dates(self):
        self.dialog.entry_date.setDate(TODAY)
        self.dialog.trial_date.setDate(TODAY.addDays(-1))


class JuryPaymentSlotFunctions(admin.AdminSlotFunctions):
    """Additional functions for the Jury Payment Dialog"""

    def calculate_juror_pay(self):
        logger.debug('Pay those jurors!')


class JuryPaymentSignalConnector(admin.AdminSignalConnector):
    """Connects signals to slots for Jury Payment Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()
        self.connect_other_dialog_signals()

    def connect_other_dialog_signals(self):
        self.dialog.calculate_payment_Button.released.connect(self.dialog.functions.calculate_juror_pay)


class JuryPaymentInfoChecker(BaseChecker):
    """Class with checks for the Admin Fiscal Dialog."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.dialog_check_list = []
        self.check_status = self.perform_check_list()


class JuryPaymentDialog(admin.AdminDialogBuilder, Ui_JurorPaymentDialog):
    """Builder for the Jury Payment Dialog.

    The judicial_officer for this entry should be the Jury Commissioner.
    """

    build_dict = {
        'dialog_name': 'Jury Payment Entry',
        'view': JuryPaymentViewModifier,
        'slots': JuryPaymentSlotFunctions,
        'signals': JuryPaymentSignalConnector,
        'case_information_model': JuryPaymentInformation,
        'loader': CmsNoChargeLoader,
        'updater': JuryPaymentCaseInformationUpdater,
        'info_checker': JuryPaymentInfoChecker,
    }

    # def __init__(self, judicial_officer=None, parent=None):
    #     super().__init__(parent)
    #     self.template = TEMPLATE_DICT.get(self.dialog_name)
    #     self.judicial_officer = judicial_officer
    #     self.load_entry_case_information_model()
