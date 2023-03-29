"""Builder module for the Leap Plea Dialog."""
from loguru import logger
from PyQt6.QtCore import QDate

from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.checkers.crim_checks import ChargeGridChecks
from munientry.helper_functions import set_future_date
from munientry.loaders.cms_case_loaders import CmsChargeLoader
from munientry.models.case_information.plea_entries import (
    LeapAdmissionEntryCaseInformation,
)
from munientry.updaters.grid_case_updaters import LeapAdmissionPleaDialogUpdater
from munientry.views.leap_admission_plea_dialog_ui import Ui_LeapAdmissionPleaDialog


class LeapAdmissionPleaDialogViewModifier(crim.CrimTrafficViewModifier):
    """View builder for Leap Plea and Leap Plea - Already Valid Dialogs."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_appearance_reason()


class LeapAdmissionPleaDialogSlotFunctions(crim.CrimTrafficSlotFunctions):
    """Additional functions for Leap Plea Dialogs."""

    def set_leap_sentencing_date(self, days_to_add_string):
        """Sets the sentencing date to the Monday after the number of days added."""
        today = QDate.currentDate()
        if days_to_add_string == 'forthwith':
            self.dialog.sentencing_date.setDate(today)
        else:
            days_to_add = self.get_days_to_add(days_to_add_string)
            total_days_to_add = set_future_date(days_to_add, 'Monday')
            self.dialog.sentencing_date.setDate(
                today.addDays(total_days_to_add),
            )

    def get_days_to_add(self, days_to_add_string):
        leap_sentence_date_dict = {
            '120 days': 120,
            '30 days': 30,
        }
        return leap_sentence_date_dict.get(days_to_add_string)


class LeapAdmissionPleaDialogSignalConnector(crim.CrimTrafficSignalConnector):
    """Signal Connector for Leap Plea Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()
        self.dialog.add_charge_Button.released.connect(
            self.dialog.functions.start_add_charge_dialog,
        )
        self.dialog.guilty_all_Button.pressed.connect(
            self.dialog.charges_gridLayout.set_all_pleas,
        )
        self.dialog.no_contest_all_Button.pressed.connect(
            self.dialog.charges_gridLayout.set_all_pleas,
        )
        self.dialog.time_to_complete_box.currentTextChanged.connect(
            self.dialog.functions.set_leap_sentencing_date,
        )


class LeapAdmissionPleaCheckList(ChargeGridChecks):
    """Check list for LEAP Admission Plea Dialog."""

    check_list = [
        'check_defense_counsel',
        'check_if_no_plea_entered',
    ]


class LeapAdmissionPleaDialog(crim.CrimTrafficDialogBuilder, Ui_LeapAdmissionPleaDialog):
    """Dialog builder class for 'LEAP Admission Plea' dialog."""

    _case_information_model = LeapAdmissionEntryCaseInformation
    _case_loader = CmsChargeLoader
    _info_checker = LeapAdmissionPleaCheckList
    _model_updater = LeapAdmissionPleaDialogUpdater
    _signal_connector = LeapAdmissionPleaDialogSignalConnector
    _slots = LeapAdmissionPleaDialogSlotFunctions
    _view_modifier = LeapAdmissionPleaDialogViewModifier
    dialog_name = 'Leap Admission Plea Entry'

    def additional_setup(self):
        self.functions.set_leap_sentencing_date('120 days')
