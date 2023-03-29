"""Builder module for the Plea Only - Future Sentencing Dialog."""
from loguru import logger
from PyQt6.QtCore import QDate

from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.checkers.base_checks import ChargeGridInfoChecker, InsuranceInfoChecker
from munientry.helper_functions import set_future_date
from munientry.loaders.cms_case_loaders import CmsFraLoader
from munientry.models.case_information.sentencing_entries import (
    DiversionEntryCaseInformation,
)
from munientry.updaters.grid_case_updaters import DiversionDialogUpdater
from munientry.views.diversion_plea_dialog_ui import Ui_DiversionPleaDialog
from munientry.widgets.message_boxes import PASS, RequiredBox, FAIL

DIVERSION_ADD_DAYS = 97


class DiversionDialogViewModifier(crim.CrimTrafficViewModifier):
    """View builder for Diversion Dialog."""

    def __init__(self, dialog):
        """Diversion uses the JailCharges Grid because all aspects of the grid are the same."""
        super().__init__(dialog)
        self.set_appearance_reason()
        self.set_diversion_fine_pay_date_box()
        self.set_diversion_jail_report_date_box()

    def set_diversion_fine_pay_date_box(self):
        """Diversion pay date is set to the first Tuesday after 97 days.

        90 days to comply, plus 7 days to process paperwork (per Judge Hemmeter).
        """
        today = QDate.currentDate()
        diversion_pay_days_to_add = set_future_date(DIVERSION_ADD_DAYS, 'Tuesday')
        self.dialog.diversion_fine_pay_date_box.setDate(
            today.addDays(diversion_pay_days_to_add),
        )

    def set_diversion_jail_report_date_box(self):
        """Diversion jail report date is set to the first Friday after 97 days.

        90 days to comply, plus 7 days to process paperwork (per Judge Hemmeter).
        """
        today = QDate.currentDate()
        jail_report_days_to_add = set_future_date(DIVERSION_ADD_DAYS, 'Friday')
        self.dialog.diversion_jail_report_date_box.setDate(
            today.addDays(jail_report_days_to_add),
        )


class DiversionDialogSlotFunctions(crim.CrimTrafficSlotFunctions):
    """Additional functions for Diversion Dialog."""

    def show_other_conditions_box(self):
        if self.dialog.other_conditions_checkBox.isChecked():
            self.dialog.other_conditions_textEdit.setHidden(False)
            self.dialog.other_conditions_textEdit.setFocus()
        else:
            self.dialog.other_conditions_textEdit.setHidden(True)

    def show_jail_report_date_box(self):
        if self.dialog.diversion_jail_imposed_checkBox.isChecked():
            self.dialog.diversion_jail_report_date_box.setHidden(False)
            self.dialog.diversion_jail_report_date_box.setEnabled(False)
            self.dialog.diversion_jail_report_date_label.setHidden(False)
            self.dialog.jail_report_date_note_label.setHidden(False)
        else:
            self.dialog.diversion_jail_report_date_box.setHidden(True)
            self.dialog.diversion_jail_report_date_box.setEnabled(True)
            self.dialog.diversion_jail_report_date_label.setHidden(True)
            self.dialog.jail_report_date_note_label.setHidden(True)

    def show_restitution_boxes(self):
        if self.dialog.pay_restitution_checkBox.isChecked():
            self.dialog.pay_restitution_to_box.setHidden(False)
            self.dialog.pay_restitution_amount_box.setHidden(False)
            self.dialog.pay_restitution_to_label.setHidden(False)
            self.dialog.pay_restitution_amount_label.setHidden(False)
        else:
            self.dialog.pay_restitution_to_box.setHidden(True)
            self.dialog.pay_restitution_amount_box.setHidden(True)
            self.dialog.pay_restitution_to_label.setHidden(True)
            self.dialog.pay_restitution_amount_label.setHidden(True)


class DiversionDialogSignalConnector(crim.CrimTrafficSignalConnector):
    """Signal Connector for Diversion Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()
        self.connect_plea_all_button_signals()
        self.connect_fra_signals()
        self.dialog.diversion_jail_imposed_checkBox.toggled.connect(
            self.dialog.functions.show_jail_report_date_box,
        )
        self.dialog.pay_restitution_checkBox.toggled.connect(
            self.dialog.functions.show_restitution_boxes,
        )
        self.dialog.other_conditions_checkBox.toggled.connect(
            self.dialog.functions.show_other_conditions_box,
        )


class DiversionPleaDialog(crim.CrimTrafficDialogBuilder, Ui_DiversionPleaDialog):
    """Dialog builder class for 'Diversion' dialog."""

    _case_information_model = DiversionEntryCaseInformation
    _case_loader = CmsFraLoader
    _info_checker = DiversionDialogInfoChecker
    _model_updater = DiversionDialogUpdater
    _signal_connector = DiversionDialogSignalConnector
    _slots = DiversionDialogSlotFunctions
    _view_modifier = DiversionDialogViewModifier
    dialog_name = 'Diversion Judgment Entry'

    def additional_setup(self):
        self.functions.show_restitution_boxes()
        self.functions.show_jail_report_date_box()
        self.functions.show_other_conditions_box()
        self.entry_case_information.diversion.ordered = True


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')


class DiversionDialogInfoChecker(ChargeGridInfoChecker, InsuranceInfoChecker):
    """Class with checks for Diversion Dialog."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.check_list = [
            'check_defense_counsel',
            'check_if_no_plea_entered',
            'check_if_no_finding_entered',
            'check_if_diversion_program_selected',
            'check_insurance',
        ]
        self.check_status = self.perform_check_list()

    def check_if_diversion_program_selected(self) -> str:
        diversion_program_list = [
            'marijuana_diversion',
            'theft_diversion',
            'other_diversion',
        ]
        for program in diversion_program_list:
            if getattr(self.dialog.entry_case_information.diversion, program) is True:
                return PASS
        message = 'No Diversion Program was selected.\n\nPlease choose a Diversion Program.'
        RequiredBox(message, 'Diversion Program Required').exec()
        return FAIL
