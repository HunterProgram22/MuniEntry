"""Contains classes for building the Juror Payment Dialog."""
from loguru import logger

from munientry.builders.administrative import base_admin_builders as admin
from munientry.views.juror_payment_dialog_ui import Ui_JurorPaymentDialog


class JuryPaymentViewModifier(admin.AdminViewModifier):
    """View class that creates and modifies the view for the Jury Payment Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_view_dates()

    def set_view_dates(self):
        self.dialog.plea_trial_date.setDate(TODAY)


class JuryPaymentSignalConnector(admin.AdminSignalConnector):
    """Connects signals to slots for Jury Payment Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()


class JuryPaymentSlotFunctions(admin.AdminSignalConnector):
    """Additional functions for the Jury Payment Dialog"""


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
    }
