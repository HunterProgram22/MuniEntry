"""Builder module for the Leap Plea Dialog."""
from loguru import logger
from PyQt5.QtCore import QDate

from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.checkers.plea_only_checkers import LeapAdmissionPleaDialogInfoChecker
from munientry.controllers import charges_grids as cg
from munientry.controllers.helper_functions import set_future_date
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
        self.dialog.charges_gridLayout.__class__ = cg.LeapAdmissionPleaGrid
        self.set_appearance_reason()


class LeapAdmissionPleaDialogSlotFunctions(crim.CrimTrafficSlotFunctions):
    """Additional functions for Leap Plea Dialogs."""

    def set_leap_sentencing_date(self, days_to_add_string):
        """Sets the sentencing date to the Monday after the number of days added."""
        if days_to_add_string == 'forthwith':
            self.dialog.sentencing_date.setDate(QDate.currentDate())
        else:
            days_to_add = self.get_days_to_add(days_to_add_string)
            total_days_to_add = set_future_date(days_to_add, 'Monday')
            self.dialog.sentencing_date.setDate(
                QDate.currentDate().addDays(total_days_to_add),
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


class LeapAdmissionPleaDialog(crim.CrimTrafficDialogBuilder, Ui_LeapAdmissionPleaDialog):
    """Dialog builder class for 'LEAP Admission Plea' dialog."""

    build_dict = {
        'dialog_name': 'Leap Admission Plea Dialog',
        'view': LeapAdmissionPleaDialogViewModifier,
        'slots': LeapAdmissionPleaDialogSlotFunctions,
        'signals': LeapAdmissionPleaDialogSignalConnector,
        'case_information_model': LeapAdmissionEntryCaseInformation,
        'loader': CmsChargeLoader,
        'updater': LeapAdmissionPleaDialogUpdater,
        'info_checker': LeapAdmissionPleaDialogInfoChecker,
    }

    def additional_setup(self):
        self.functions.set_leap_sentencing_date('120 days')


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
