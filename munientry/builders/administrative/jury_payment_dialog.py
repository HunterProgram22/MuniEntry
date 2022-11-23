"""Contains classes for building the Juror Payment Dialog."""
from loguru import logger

from num2words import num2words

from munientry.builders.administrative import base_admin_builders as admin
from munientry.checkers.base_checks import BaseChecker
from munientry.creators.entry_creator import JuryPaymentEntryCreator
from munientry.models.jury_models import JuryPaymentInformation
from munientry.loaders.cms_case_loaders import CmsLoader
from munientry.updaters.base_updaters import BaseDialogUpdater
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

    def create_entry_process(self) -> None:
        JuryPaymentEntryCreator(self.dialog).create_entry_process()

    def calculate_juror_pay(self):
        jurors_reported = int(self.dialog.jurors_reported_lineEdit.text())
        jurors_seated = int(self.dialog.jurors_seated_box.currentText())
        jurors_not_seated_pay = self.calculate_jurors_not_seated_pay(jurors_reported, jurors_seated)
        jurors_seated_pay = self.calculate_jurors_seated_pay(jurors_seated)
        self.dialog.jurors_not_seated_pay_lineEdit.setText(str(jurors_not_seated_pay))
        self.dialog.jurors_seated_pay_lineEdit.setText(str(jurors_seated_pay))
        self.dialog.jurors_total_pay_lineEdit.setText(str(jurors_seated_pay + jurors_not_seated_pay))

    def calculate_jurors_not_seated_pay(self, jurors_reported, jurors_seated):
        jurors_not_seated = jurors_reported - jurors_seated
        return (25*jurors_not_seated)

    def calculate_jurors_seated_pay(self, jurors_seated):
        if self.dialog.trial_length_box.currentText() == 'Two Days':
            return (40*2*jurors_seated)
        return (40*jurors_seated)

    def set_seated_jurors(self):
        if self.dialog.trial_length_box.currentText() == 'No Trial - Jury Not Seated':
            self.dialog.jurors_seated_box.setCurrentText('0')
        else:
            self.dialog.jurors_seated_box.setCurrentText('9')


class JuryPaymentSignalConnector(admin.AdminSignalConnector):
    """Connects signals to slots for Jury Payment Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()
        self.connect_other_dialog_signals()

    def connect_other_dialog_signals(self):
        self.dialog.calculate_payment_Button.released.connect(self.dialog.functions.calculate_juror_pay)
        self.dialog.trial_length_box.currentTextChanged.connect(self.dialog.functions.set_seated_jurors)


class JuryPaymentInfoChecker(BaseChecker):
    """Class with checks for the Jury Payment Dialog."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.dialog_check_list = []
        self.check_status = self.perform_check_list()


class JuryPaymentCaseInformationUpdater(BaseDialogUpdater):
    """Base class for Jury Payment Updater."""

    def __init__(self, dialog: 'QDialog') -> None:
        super().__init__(dialog)
        self.model.judicial_officer = self.dialog.judicial_officer
        self.update_model_with_case_information_frame_data()
        self.update_juror_information()
        self.set_juror_pay_information()

    def update_model_with_case_information_frame_data(self) -> None:
        self.set_case_number_and_date()
        self.set_party_information()

    def set_case_number_and_date(self) -> None:
        self.model.case_number = self.dialog.case_number_lineEdit.text()
        self.model.trial_date = self.dialog.trial_date.date().toString('MMMM dd, yyyy')
        self.model.entry_date = self.dialog.entry_date.date().toString('MMMM dd, yyyy')

    def set_party_information(self) -> None:
        self.model.defendant.first_name = self.dialog.defendant_first_name_lineEdit.text()
        self.model.defendant.last_name = self.dialog.defendant_last_name_lineEdit.text()

    def update_juror_information(self):
        self.model.trial_length = self.dialog.trial_length_box.currentText()
        self.model.jurors_reported = self.dialog.jurors_reported_lineEdit.text()
        self.model.jurors_reported_word = num2words(int(self.model.jurors_reported))
        self.model.jurors_seated = self.dialog.jurors_seated_box.currentText()
        self.model.jurors_seated_word = num2words(int(self.model.jurors_seated))
        self.model.jurors_not_seated = int(self.model.jurors_reported) - int(self.model.jurors_seated)
        self.model.jurors_not_seated_word = num2words(int(self.model.jurors_not_seated))

    def set_juror_pay_information(self):
        self.model.jurors_pay_not_seated = self.dialog.jurors_not_seated_pay_lineEdit.text()
        self.model.jurors_pay_not_seated_word = num2words(int(self.model.jurors_pay_not_seated))
        self.model.jurors_pay_seated = self.dialog.jurors_seated_pay_lineEdit.text()
        self.model.jurors_pay_seated_word = num2words(int(self.model.jurors_pay_seated))
        self.model.jury_panel_total_pay = self.dialog.jurors_total_pay_lineEdit.text()
        self.model.jury_panel_total_pay_word = num2words(int(self.model.jury_panel_total_pay))


class JuryPaymentDialog(admin.AdminDialogBuilder, Ui_JurorPaymentDialog):
    """Builder for the Jury Payment Dialog."""

    _case_information_model = JuryPaymentInformation
    _case_loader = CmsLoader
    _info_checker = JuryPaymentInfoChecker
    _model_updater = JuryPaymentCaseInformationUpdater
    _signal_connector = JuryPaymentSignalConnector
    _slots = JuryPaymentSlotFunctions
    _view_modifier = JuryPaymentViewModifier
    dialog_name = 'Jury Payment Entry'
