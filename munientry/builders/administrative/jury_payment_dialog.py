"""Contains classes for building the Juror Payment Dialog."""
from loguru import logger

from munientry.builders.administrative import base_admin_builders as admin
from munientry.models.jury_models import JuryPaymentInformation
from munientry.loaders.cms_case_loaders import CmsNoChargeLoader
from munientry.views.juror_payment_dialog_ui import Ui_JurorPaymentDialog
from munientry.appsettings.pyqt_constants import TODAY


class JuryPaymentViewModifier(admin.AdminViewModifier):
    """View class that creates and modifies the view for the Jury Payment Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_view_dates()

    def set_view_dates(self):
        self.dialog.plea_trial_date.setDate(TODAY)


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


class JuryPaymentDialog(admin.AdminDialogBuilder, Ui_JurorPaymentDialog):
    """Builder for the Jury Payment Dialog.

    The judicial_officer for this entry is should be the Jury Commissioner.
    """

    build_dict = {
        'dialog_name': 'Jury Payment Entry',
        'view': JuryPaymentViewModifier,
        'slots': JuryPaymentSlotFunctions,
        'signals': JuryPaymentSignalConnector,
        'case_information_model': JuryPaymentInformation,
        'loader': CmsNoChargeLoader,
    }
