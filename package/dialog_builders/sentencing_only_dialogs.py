from PyQt5.QtGui import QIntValidator
from package.controllers.cms_case_loaders import CmsFraLoader
from package.controllers.signal_connectors import TrialSentencingDialogSignalConnector, \
    LeapSentencingDialogSignalConnector, SentencingOnlyDialogSignalConnector
from package.controllers.slot_functions import TrialSentencingDialogSlotFunctions, \
    LeapSentencingDialogSlotFunctions, SentencingOnlyDialogSlotFunctions
from package.controllers.view_modifiers import TrialSentencingDialogViewModifier, \
    LeapSentencingDialogViewModifier, SentencingOnlyDialogViewModifier
from package.dialog_builders.base_dialogs import CriminalBaseDialog
from package.information_checkers.jail_charge_grid_checkers import TrialSentencingDialogInfoChecker, \
    SentencingOnlyDialogInfoChecker
from package.information_checkers.no_jail_sentencing_checkers import LeapSentencingDialogInfoChecker
from package.models.case_information.sentencing_entries import TrialSentencingEntryCaseInformation, \
    LeapSentencingEntryCaseInformation, SentencingOnlyEntryCaseInformation
from package.models.template_types import TEMPLATE_DICT
from package.updaters.grid_case_updaters import TrialSentencingDialogUpdater, \
    LeapSentencingDialogUpdater, SentencingOnlyDialogUpdater
from package.views.leap_sentencing_dialog_ui import Ui_LeapSentencingDialog
from package.views.sentencing_only_dialog_ui import Ui_SentencingOnlyDialog
from package.views.trial_sentencing_dialog_ui import Ui_TrialSentencingDialog


class TrialSentencingDialog(CriminalBaseDialog, Ui_TrialSentencingDialog):
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
        self.dialog_name = 'Trial Sentencing Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)

    def modify_view(self) -> None:
        TrialSentencingDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = TrialSentencingDialogSlotFunctions(self)
        self.functions.show_companion_case_fields()

    def connect_signals_to_slots(self):
        return TrialSentencingDialogSignalConnector(self)

    def load_entry_case_information_model(self):
        self.entry_case_information = TrialSentencingEntryCaseInformation()
        self.entry_case_information.judicial_officer = self.judicial_officer

    def load_cms_data_to_view(self) -> None:
        CmsFraLoader(self)

    def update_entry_case_information(self):
        return TrialSentencingDialogUpdater(self)

    def perform_info_checks(self):
        self.dialog_checks = TrialSentencingDialogInfoChecker(self)


class LeapSentencingDialog(CriminalBaseDialog, Ui_LeapSentencingDialog):
    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
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

    def create_dialog_slot_functions(self):
        self.functions = LeapSentencingDialogSlotFunctions(self)
        self.functions.set_fines_credit_for_jail_field()

    def connect_signals_to_slots(self):
        return LeapSentencingDialogSignalConnector(self)

    def load_entry_case_information_model(self):
        self.entry_case_information = LeapSentencingEntryCaseInformation()
        self.entry_case_information.judicial_officer = self.judicial_officer

    def load_cms_data_to_view(self) -> None:
        CmsFraLoader(self)

    def update_entry_case_information(self):
        return LeapSentencingDialogUpdater(self)

    def perform_info_checks(self):
        self.dialog_checks = LeapSentencingDialogInfoChecker(self)


class SentencingOnlyDialog(CriminalBaseDialog, Ui_SentencingOnlyDialog):
    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
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

    def create_dialog_slot_functions(self):
        self.functions = SentencingOnlyDialogSlotFunctions(self)

    def connect_signals_to_slots(self):
        return SentencingOnlyDialogSignalConnector(self)

    def load_entry_case_information_model(self):
        self.entry_case_information = SentencingOnlyEntryCaseInformation()
        self.entry_case_information.judicial_officer = self.judicial_officer

    def load_cms_data_to_view(self) -> None:
        CmsFraLoader(self)

    def update_entry_case_information(self):
        return SentencingOnlyDialogUpdater(self)

    def perform_info_checks(self):
        self.dialog_checks = SentencingOnlyDialogInfoChecker(self)