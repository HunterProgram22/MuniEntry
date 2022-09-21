"""Builder module for the Leap Plea and Leap Plea - Already Valid Dialogs."""
from PyQt5.QtCore import QDate
from loguru import logger

from munientry.builders.base_dialogs import CriminalDialogBuilder
from munientry.checkers.plea_only_checkers import LeapAdmissionPleaDialogInfoChecker
from munientry.controllers import charges_grids as cg
from munientry.controllers.helper_functions import set_future_date
from munientry.controllers.signal_connectors import BaseDialogSignalConnector
from munientry.controllers.slot_functions import BaseDialogSlotFunctions
from munientry.controllers.view_modifiers import BaseDialogViewModifier
from munientry.data.cms_case_loaders import CmsChargeLoader
from munientry.models.case_information.plea_entries import LeapAdmissionEntryCaseInformation
from munientry.updaters.grid_case_updaters import LeapAdmissionPleaDialogUpdater
from munientry.views.leap_admission_plea_dialog_ui import Ui_LeapAdmissionPleaDialog
from munientry.views.leap_plea_valid_dialog_ui import Ui_LeapPleaValidDialog


class LeapAdmissionPleaDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog.charges_gridLayout.__class__ = cg.LeapAdmissionPleaGrid
        self.set_appearance_reason()


class LeapAdmissionPleaDialogSlotFunctions(BaseDialogSlotFunctions):
    def __init__(self, dialog):
        self.dialog = dialog

    def set_leap_sentencing_date(self, days_to_add_string):
        """Sets the sentencing date to the Monday after the number of days added."""
        if days_to_add_string == "forthwith":
            self.dialog.sentencing_date.setDate(QDate.currentDate())
        else:
            days_to_add = self.get_days_to_add(days_to_add_string)
            total_days_to_add = set_future_date(days_to_add, "Monday")
            self.dialog.sentencing_date.setDate(
                QDate.currentDate().addDays(total_days_to_add)
            )

    def get_days_to_add(self, days_to_add_string):
        leap_sentence_date_dict = {
            '120 days': 120,
            '30 days': 30,
        }
        return leap_sentence_date_dict.get(days_to_add_string)


class LeapAdmissionPleaDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        """The plea all buttons are connected directly because the base dialog method also connects
        findings and a Leap Admission Plea does not have findings."""
        super().__init__(dialog)
        self.connect_main_dialog_common_signals(dialog)
        dialog.add_charge_Button.released.connect(dialog.functions.start_add_charge_dialog)
        dialog.guilty_all_Button.pressed.connect(dialog.charges_gridLayout.set_all_pleas)
        dialog.no_contest_all_Button.pressed.connect(dialog.charges_gridLayout.set_all_pleas)
        dialog.time_to_complete_box.currentTextChanged.connect(dialog.functions.set_leap_sentencing_date)


class LeapAdmissionPleaValidDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        """The plea all buttons are connected directly because the base dialog method also connects
        findings and a Leap Admission Plea does not have findings."""
        super().__init__(dialog)
        self.connect_main_dialog_common_signals(dialog)
        dialog.add_charge_Button.released.connect(dialog.functions.start_add_charge_dialog)
        dialog.guilty_all_Button.pressed.connect(dialog.charges_gridLayout.set_all_pleas)

        
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

