"""Module containing classes to build Sentencing Only Dialogs."""
from loguru import logger
from PyQt5.QtGui import QIntValidator

from package.controllers.cms_case_loaders import CmsFraLoader
from package.controllers.signal_connectors import (
    LeapSentencingDialogSignalConnector,
    SentencingOnlyDialogSignalConnector,
    TrialSentencingDialogSignalConnector,
)
from package.controllers.slot_functions import (
    LeapSentencingDialogSlotFunctions,
    SentencingOnlyDialogSlotFunctions,
    TrialSentencingDialogSlotFunctions,
)
from package.controllers.view_modifiers import (
    LeapSentencingDialogViewModifier,
    SentencingOnlyDialogViewModifier,
    TrialSentencingDialogViewModifier,
)
from package.dialog_builders.base_dialogs import CriminalBaseDialog
from package.information_checkers.jail_charge_grid_checkers import (
    SentencingOnlyDialogInfoChecker,
    TrialSentencingDialogInfoChecker,
)
from package.information_checkers.no_jail_sentencing_checkers import (
    LeapSentencingDialogInfoChecker,
)
from package.models.case_information.sentencing_entries import (
    LeapSentencingEntryCaseInformation,
    SentencingOnlyEntryCaseInformation,
    TrialSentencingEntryCaseInformation,
)
from package.models.template_types import TEMPLATE_DICT
from package.updaters.grid_case_updaters import (
    LeapSentencingDialogUpdater,
    SentencingOnlyDialogUpdater,
    TrialSentencingDialogUpdater,
)
from package.views.leap_sentencing_dialog_ui import Ui_LeapSentencingDialog
from package.views.sentencing_only_dialog_ui import Ui_SentencingOnlyDialog
from package.views.trial_sentencing_dialog_ui import Ui_TrialSentencingDialog


class TrialSentencingDialog(CriminalBaseDialog, Ui_TrialSentencingDialog):
    """Dialog builder class for 'Jury Trial / Trial to Court Sentencing' dialog."""

    def __init__(
        self,
        judicial_officer: object,
        cms_case: str = None,
        case_table: str = None,
        parent: object = None,
    ) -> None:
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.validator = QIntValidator(0, 1000, self)
        self.jail_time_credit_box.setValidator(self.validator)
        self.additional_conditions_list = [
            ('community_control_checkBox', self.entry_case_information.community_control),
            ('license_suspension_checkBox', self.entry_case_information.license_suspension),
            ('community_service_checkBox', self.entry_case_information.community_service),
            ('other_conditions_checkBox', self.entry_case_information.other_conditions),
            ('jail_checkBox', self.entry_case_information.jail_terms),
            ('impoundment_checkBox', self.entry_case_information.impoundment),
            ('victim_notification_checkBox', self.entry_case_information.victim_notification),
        ]
        self.dialog_name = 'Trial Sentencing Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)

    def modify_view(self) -> None:
        TrialSentencingDialogViewModifier(self)

    def create_dialog_slot_functions(self) -> None:
        self.functions = TrialSentencingDialogSlotFunctions(self)
        self.functions.show_companion_case_fields()

    def connect_signals_to_slots(self) -> None:
        TrialSentencingDialogSignalConnector(self)

    def load_entry_case_information_model(self) -> None:
        self.entry_case_information = TrialSentencingEntryCaseInformation()
        self.entry_case_information.judicial_officer = self.judicial_officer

    def load_cms_data_to_view(self) -> None:
        CmsFraLoader(self)

    def update_entry_case_information(self) -> None:
        TrialSentencingDialogUpdater(self)

    def perform_info_checks(self) -> None:
        self.dialog_checks = TrialSentencingDialogInfoChecker(self)


class LeapSentencingDialog(CriminalBaseDialog, Ui_LeapSentencingDialog):
    """Dialog builder class for 'LEAP Sentencing' dialog."""

    def __init__(
        self,
        judicial_officer: object,
        cms_case: str = None,
        case_table: str = None,
        parent: object = None,
    ) -> None:
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.additional_conditions_list = [
            ('license_suspension_checkBox', self.entry_case_information.license_suspension),
            ('community_service_checkBox', self.entry_case_information.community_service),
            ('other_conditions_checkBox', self.entry_case_information.other_conditions),
        ]
        self.dialog_name = 'Leap Sentencing Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)

    def modify_view(self) -> None:
        LeapSentencingDialogViewModifier(self)

    def create_dialog_slot_functions(self) -> None:
        self.functions = LeapSentencingDialogSlotFunctions(self)
        self.functions.set_fines_credit_for_jail_field()

    def connect_signals_to_slots(self) -> None:
        LeapSentencingDialogSignalConnector(self)

    def load_entry_case_information_model(self) -> None:
        self.entry_case_information = LeapSentencingEntryCaseInformation()
        self.entry_case_information.judicial_officer = self.judicial_officer

    def load_cms_data_to_view(self) -> None:
        CmsFraLoader(self)

    def update_entry_case_information(self) -> None:
        LeapSentencingDialogUpdater(self)

    def perform_info_checks(self) -> None:
        self.dialog_checks = LeapSentencingDialogInfoChecker(self)


class SentencingOnlyDialog(CriminalBaseDialog, Ui_SentencingOnlyDialog):
    """Dialog builder class for 'Sentencing Only - Already Plead' dialog."""

    def __init__(
        self,
        judicial_officer: object,
        cms_case: str = None,
        case_table: str = None,
        parent: object = None,
    ) -> None:
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.additional_conditions_list = [
            ('community_control_checkBox', self.entry_case_information.community_control),
            ('license_suspension_checkBox', self.entry_case_information.license_suspension),
            ('community_service_checkBox', self.entry_case_information.community_service),
            ('other_conditions_checkBox', self.entry_case_information.other_conditions),
            ('jail_checkBox', self.entry_case_information.jail_terms),
            ('impoundment_checkBox', self.entry_case_information.impoundment),
            ('victim_notification_checkBox', self.entry_case_information.victim_notification),
        ]
        self.dialog_name = 'Sentencing Only Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)

    def modify_view(self) -> None:
        SentencingOnlyDialogViewModifier(self)

    def create_dialog_slot_functions(self) -> None:
        self.functions = SentencingOnlyDialogSlotFunctions(self)

    def connect_signals_to_slots(self) -> None:
        SentencingOnlyDialogSignalConnector(self)

    def load_entry_case_information_model(self) -> None:
        self.entry_case_information = SentencingOnlyEntryCaseInformation()
        self.entry_case_information.judicial_officer = self.judicial_officer

    def load_cms_data_to_view(self) -> None:
        CmsFraLoader(self)

    def update_entry_case_information(self) -> None:
        SentencingOnlyDialogUpdater(self)

    def perform_info_checks(self) -> None:
        self.dialog_checks = SentencingOnlyDialogInfoChecker(self)


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
