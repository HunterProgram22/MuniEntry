"""Builder module for the Plea Only - Future Sentencing Dialog."""
from loguru import logger
from PyQt6.QtCore import QDate

from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.checkers.crim_checks import InsuranceChecks, ChargeGridChecks
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
        self.set_diversion_fine_pay_date()
        self.set_diversion_jail_report_date()

    def set_diversion_fine_pay_date(self):
        """Diversion pay date is set to the first Tuesday after 97 days.

        90 days to comply, plus 7 days to process paperwork (per Judge Hemmeter).
        """
        today = QDate.currentDate()
        diversion_pay_days_to_add = set_future_date(DIVERSION_ADD_DAYS, 'Tuesday')
        self.dialog.diversion_fine_pay_date.setDate(
            today.addDays(diversion_pay_days_to_add),
        )

    def set_diversion_jail_report_date(self):
        """Diversion jail report date is set to the first Friday after 97 days.

        90 days to comply, plus 7 days to process paperwork (per Judge Hemmeter).
        """
        today = QDate.currentDate()
        jail_report_days_to_add = set_future_date(DIVERSION_ADD_DAYS, 'Friday')
        self.dialog.diversion_jail_report_date.setDate(
            today.addDays(jail_report_days_to_add),
        )


class DiversionDialogSlotFunctions(crim.CrimTrafficSlotFunctions):
    """Additional functions for Diversion Dialog."""

    def show_other_conditions_box(self):
        if self.dialog.other_conditions_check_box.isChecked():
            self.dialog.other_conditions_text.setHidden(False)
            self.dialog.other_conditions_text.setFocus()
        else:
            self.dialog.other_conditions_text.setHidden(True)

    def show_jail_report_date(self):
        if self.dialog.diversion_jail_imposed_check_box.isChecked():
            self.dialog.diversion_jail_report_date.setHidden(False)
            self.dialog.diversion_jail_report_date.setEnabled(False)
            self.dialog.diversion_jail_report_date_label.setHidden(False)
            self.dialog.jail_report_date_note_label.setHidden(False)
        else:
            self.dialog.diversion_jail_report_date.setHidden(True)
            self.dialog.diversion_jail_report_date.setEnabled(True)
            self.dialog.diversion_jail_report_date_label.setHidden(True)
            self.dialog.jail_report_date_note_label.setHidden(True)

    def show_restitution_boxes(self):
        if self.dialog.pay_restitution_check_box.isChecked():
            self.dialog.pay_restitution_to_line.setHidden(False)
            self.dialog.pay_restitution_amount_line.setHidden(False)
            self.dialog.pay_restitution_to_label.setHidden(False)
            self.dialog.pay_restitution_amount_label.setHidden(False)
        else:
            self.dialog.pay_restitution_to_line.setHidden(True)
            self.dialog.pay_restitution_amount_line.setHidden(True)
            self.dialog.pay_restitution_to_label.setHidden(True)
            self.dialog.pay_restitution_amount_label.setHidden(True)


class DiversionDialogSignalConnector(crim.CrimTrafficSignalConnector):
    """Signal Connector for Diversion Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()
        self.connect_plea_all_button_signals()
        self.connect_fra_signals()
        self.dialog.diversion_jail_imposed_check_box.toggled.connect(
            self.dialog.functions.show_jail_report_date,
        )
        self.dialog.pay_restitution_check_box.toggled.connect(
            self.dialog.functions.show_restitution_boxes,
        )
        self.dialog.other_conditions_check_box.toggled.connect(
            self.dialog.functions.show_other_conditions_box,
        )


class DiversionCheckList(ChargeGridChecks, InsuranceChecks):
    """Check list for Diversion Dialog."""

    check_list = [
        'check_defense_counsel',
        'check_if_no_plea_entered',
        'check_if_no_finding_entered',
        'check_if_diversion_program_selected',
        'check_insurance',
    ]


class DiversionPleaDialog(crim.CrimTrafficDialogBuilder, Ui_DiversionPleaDialog):
    """Dialog builder class for 'Diversion' dialog."""

    _case_information_model = DiversionEntryCaseInformation
    _case_loader = CmsFraLoader
    _info_checker = DiversionCheckList
    _model_updater = DiversionDialogUpdater
    _signal_connector = DiversionDialogSignalConnector
    _slots = DiversionDialogSlotFunctions
    _view_modifier = DiversionDialogViewModifier
    dialog_name = 'Diversion Judgment Entry'

    def additional_setup(self):
        self.functions.show_restitution_boxes()
        self.functions.show_jail_report_date()
        self.functions.show_other_conditions_box()
        self.entry_case_information.diversion.ordered = True
