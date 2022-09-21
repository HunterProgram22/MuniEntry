"""Module containing classes to build Plea Only Dialogs."""
from loguru import logger

from munientry.builders.base_dialogs import CriminalDialogBuilder
from munientry.checkers.plea_only_checkers import (
    LeapAdmissionPleaDialogInfoChecker,
)
from munientry.controllers.signal_connectors import (
    LeapAdmissionPleaDialogSignalConnector,
    LeapAdmissionPleaValidDialogSignalConnector,
)
from munientry.controllers.slot_functions import (
    LeapAdmissionPleaDialogSlotFunctions,
)
from munientry.controllers.view_modifiers import (
    LeapAdmissionPleaDialogViewModifier,
)
from munientry.data.cms_case_loaders import CmsChargeLoader
from munientry.models.case_information.plea_entries import (
    LeapAdmissionEntryCaseInformation,
)
from munientry.updaters.grid_case_updaters import (
    LeapAdmissionPleaDialogUpdater,
)
from munientry.views.leap_admission_plea_dialog_ui import Ui_LeapAdmissionPleaDialog
from munientry.views.leap_plea_valid_dialog_ui import Ui_LeapPleaValidDialog


class LeapAdmissionPleaDialog(CriminalDialogBuilder, Ui_LeapAdmissionPleaDialog):
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

    def __init__(
        self,
        judicial_officer: object,
        cms_case: str = None,
        case_table: str = None,
        parent: object = None,
    ) -> None:
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.functions.set_leap_sentencing_date('120 days')
        self.entry_case_information.judicial_officer = self.judicial_officer


class LeapPleaValidDialog(CriminalDialogBuilder, Ui_LeapPleaValidDialog):
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

    def __init__(
        self,
        judicial_officer: object,
        cms_case: str = None,
        case_table: str = None,
        parent: object = None,
    ) -> None:
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.entry_case_information.judicial_officer = self.judicial_officer


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
