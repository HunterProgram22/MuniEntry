"""Module containing classes to build Plea and Sentencing Dialogs."""
from PyQt5.QtGui import QIntValidator

from package.controllers.cms_case_loaders import CmsFraLoader
from package.controllers.signal_connectors import (
    DiversionDialogSignalConnector,
    FineOnlyDialogSignalConnector,
    JailCCDialogSignalConnector,
)
from package.controllers.slot_functions import (
    DiversionDialogSlotFunctions,
    FineOnlyDialogSlotFunctions,
    JailCCDialogSlotFunctions,
)
from package.controllers.view_modifiers import (
    DiversionDialogViewModifier,
    FineOnlyDialogViewModifier,
    JailCCDialogViewModifier,
)
from package.dialog_builders.base_dialogs import CriminalBaseDialog
from package.information_checkers.jail_charge_grid_checkers import (
    JailCCPleaDialogInfoChecker,
)
from package.information_checkers.no_jail_sentencing_checkers import (
    DiversionDialogInfoChecker,
    FineOnlyDialogInfoChecker,
)
from package.models.case_information.sentencing_entries import (
    DiversionEntryCaseInformation,
    FineOnlyEntryCaseInformation,
    JailCCEntryCaseInformation,
)
from package.models.template_types import TEMPLATE_DICT
from package.updaters.grid_case_updaters import (
    DiversionDialogUpdater,
    FineOnlyDialogUpdater,
    JailCCDialogUpdater,
)
from package.views.diversion_plea_dialog_ui import Ui_DiversionPleaDialog
from package.views.fine_only_plea_dialog_ui import Ui_FineOnlyPleaDialog
from package.views.jail_cc_plea_dialog_ui import Ui_JailCCPleaDialog


class DiversionPleaDialog(CriminalBaseDialog, Ui_DiversionPleaDialog):
    """Dialog builder class for 'Diversion' dialog."""

    def __init__(
        self,
        judicial_officer: object,
        cms_case: str = None,
        case_table: str = None,
        parent: object = None,
    ) -> None:
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.dialog_name = 'Diversion Plea Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.functions.show_restitution_boxes()

    def modify_view(self) -> None:
        DiversionDialogViewModifier(self)

    def create_dialog_slot_functions(self) -> None:
        self.functions = DiversionDialogSlotFunctions(self)
        self.functions.show_jail_report_date_box()
        self.functions.show_other_conditions_box()

    def connect_signals_to_slots(self) -> None:
        DiversionDialogSignalConnector(self)

    def load_entry_case_information_model(self) -> None:
        self.entry_case_information = DiversionEntryCaseInformation()
        self.entry_case_information.judicial_officer = self.judicial_officer
        self.entry_case_information.diversion.ordered = True

    def load_cms_data_to_view(self) -> None:
        CmsFraLoader(self)

    def update_entry_case_information(self) -> None:
        DiversionDialogUpdater(self)

    def perform_info_checks(self) -> None:
        self.dialog_checks = DiversionDialogInfoChecker(self)


class JailCCPleaDialog(CriminalBaseDialog, Ui_JailCCPleaDialog):
    """Dialog builder class for 'Jail and/or Community Control' dialog."""

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
        self.dialog_name = 'Jail CC Plea Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        if self.case_table == 'slated':
            self.in_jail_box.setCurrentText('Yes')

    def modify_view(self) -> None:
        JailCCDialogViewModifier(self)

    def create_dialog_slot_functions(self) -> None:
        self.functions = JailCCDialogSlotFunctions(self)
        self.functions.show_companion_case_fields()

    def connect_signals_to_slots(self) -> None:
        JailCCDialogSignalConnector(self)

    def load_entry_case_information_model(self) -> None:
        self.entry_case_information = JailCCEntryCaseInformation()
        self.entry_case_information.judicial_officer = self.judicial_officer

    def load_cms_data_to_view(self) -> None:
        CmsFraLoader(self)

    def update_entry_case_information(self) -> None:
        JailCCDialogUpdater(self)

    def perform_info_checks(self) -> None:
        self.dialog_checks = JailCCPleaDialogInfoChecker(self)


class FineOnlyPleaDialog(CriminalBaseDialog, Ui_FineOnlyPleaDialog):
    """Dialog builder class for 'Fine Only' dialog."""

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
        self.dialog_name = 'Fine Only Plea Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)

    def modify_view(self) -> None:
        FineOnlyDialogViewModifier(self)

    def create_dialog_slot_functions(self) -> None:
        self.functions = FineOnlyDialogSlotFunctions(self)
        self.functions.set_fines_credit_for_jail_field()

    def connect_signals_to_slots(self) -> None:
        FineOnlyDialogSignalConnector(self)

    def load_entry_case_information_model(self) -> None:
        self.entry_case_information = FineOnlyEntryCaseInformation()
        self.entry_case_information.judicial_officer = self.judicial_officer

    def load_cms_data_to_view(self) -> None:
        CmsFraLoader(self)

    def update_entry_case_information(self) -> None:
        FineOnlyDialogUpdater(self)

    def perform_info_checks(self) -> None:
        self.dialog_checks = FineOnlyDialogInfoChecker(self)
