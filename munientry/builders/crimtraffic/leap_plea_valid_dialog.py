"""Builder module for Leap Plea - Already Valid Dialog."""
from loguru import logger

from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.builders.crimtraffic.leap_plea_dialog import (
    LeapAdmissionPleaDialogSlotFunctions,
    LeapAdmissionPleaDialogViewModifier,
)
from munientry.checkers.plea_only_checkers import LeapAdmissionPleaDialogInfoChecker
from munientry.data.cms_case_loaders import CmsChargeLoader
from munientry.models.case_information.plea_entries import (
    LeapAdmissionEntryCaseInformation,
)
from munientry.updaters.grid_case_updaters import LeapAdmissionPleaDialogUpdater
from munientry.views.leap_plea_valid_dialog_ui import Ui_LeapPleaValidDialog


class LeapAdmissionPleaValidDialogSignalConnector(crim.CrimTrafficSignalConnector):
    """Signal Connector for Leap Plea - Already Valid Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()
        self.dialog.add_charge_Button.released.connect(
            self.dialog.functions.start_add_charge_dialog,
        )
        self.dialog.guilty_all_Button.pressed.connect(
            self.dialog.charges_gridLayout.set_all_pleas,
        )


class LeapPleaValidDialog(crim.CrimTrafficDialogBuilder, Ui_LeapPleaValidDialog):
    """Dialog builder class for 'LEAP Admission Plea - Already Valid' dialog."""

    build_dict = {
        'dialog_name': 'Leap Admission Plea Already Valid Dialog',
        'view': LeapAdmissionPleaDialogViewModifier,
        'slots': LeapAdmissionPleaDialogSlotFunctions,
        'signals': LeapAdmissionPleaValidDialogSignalConnector,
        'case_information_model': LeapAdmissionEntryCaseInformation,
        'loader': CmsChargeLoader,
        'updater': LeapAdmissionPleaDialogUpdater,
        'info_checker': LeapAdmissionPleaDialogInfoChecker,
    }


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
