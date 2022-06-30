from PyQt5.QtGui import QIntValidator
from package.controllers.cms_case_loaders import CmsFraLoader
from package.controllers.signal_connectors import DiversionDialogSignalConnector, \
    JailCCDialogSignalConnector, FineOnlyDialogSignalConnector
from package.controllers.slot_functions import DiversionDialogSlotFunctions, \
    JailCCDialogSlotFunctions, FineOnlyDialogSlotFunctions
from package.controllers.view_modifiers import DiversionDialogViewModifier, \
    JailCCDialogViewModifier, FineOnlyDialogViewModifier
from package.dialog_builders.base_dialogs import CriminalBaseDialog
from package.information_checkers.jail_charge_grid_checkers import JailCCPleaDialogInfoChecker
from package.information_checkers.no_jail_sentencing_checkers import DiversionDialogInfoChecker, \
    FineOnlyDialogInfoChecker
from package.models.case_information.sentencing_entries import DiversionEntryCaseInformation, \
    JailCCEntryCaseInformation, FineOnlyEntryCaseInformation
from package.models.template_types import TEMPLATE_DICT
from package.updaters.grid_case_updaters import DiversionDialogUpdater, JailCCDialogUpdater, \
    FineOnlyDialogUpdater
from package.views.diversion_plea_dialog_ui import Ui_DiversionPleaDialog
from package.views.fine_only_plea_dialog_ui import Ui_FineOnlyPleaDialog
from package.views.jail_cc_plea_dialog_ui import Ui_JailCCPleaDialog


class DiversionPleaDialog(CriminalBaseDialog, Ui_DiversionPleaDialog):
    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.dialog_name = 'Diversion Plea Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.functions.show_restitution_boxes()

    def modify_view(self) -> None:
        DiversionDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = DiversionDialogSlotFunctions(self)
        self.functions.show_jail_report_date_box()
        self.functions.show_other_conditions_box()

    def connect_signals_to_slots(self):
        return DiversionDialogSignalConnector(self)

    def load_entry_case_information_model(self):
        self.entry_case_information = DiversionEntryCaseInformation()
        self.entry_case_information.judicial_officer = self.judicial_officer
        self.entry_case_information.diversion.ordered = True

    def load_cms_data_to_view(self) -> None:
        CmsFraLoader(self)

    def update_entry_case_information(self):
        return DiversionDialogUpdater(self)

    def perform_info_checks(self):
        self.dialog_checks = DiversionDialogInfoChecker(self)


class JailCCPleaDialog(CriminalBaseDialog, Ui_JailCCPleaDialog):
    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
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

    def create_dialog_slot_functions(self):
        self.functions = JailCCDialogSlotFunctions(self)
        self.functions.show_companion_case_fields()

    def connect_signals_to_slots(self):
        return JailCCDialogSignalConnector(self)

    def load_entry_case_information_model(self):
        self.entry_case_information = JailCCEntryCaseInformation()
        self.entry_case_information.judicial_officer = self.judicial_officer

    def load_cms_data_to_view(self) -> None:
        CmsFraLoader(self)

    def update_entry_case_information(self):
        return JailCCDialogUpdater(self)

    def perform_info_checks(self):
        self.dialog_checks = JailCCPleaDialogInfoChecker(self)


class FineOnlyPleaDialog(CriminalBaseDialog, Ui_FineOnlyPleaDialog):
    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
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

    def create_dialog_slot_functions(self):
        self.functions = FineOnlyDialogSlotFunctions(self)
        self.functions.set_fines_credit_for_jail_field()

    def connect_signals_to_slots(self):
        return FineOnlyDialogSignalConnector(self)

    def load_entry_case_information_model(self):
        self.entry_case_information = FineOnlyEntryCaseInformation()
        self.entry_case_information.judicial_officer = self.judicial_officer

    def load_cms_data_to_view(self) -> None:
        CmsFraLoader(self)

    def update_entry_case_information(self):
        return FineOnlyDialogUpdater(self)

    def perform_info_checks(self):
        self.dialog_checks = FineOnlyDialogInfoChecker(self)