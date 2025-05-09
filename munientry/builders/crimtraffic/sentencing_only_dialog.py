"""Builder module for the Jail CC Plea Dialog."""
from loguru import logger

from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.builders.secondary.add_community_control_dialog import (
    AddCommunityControlDialog,
)
from munientry.builders.secondary.add_jail_only_dialog import AddJailOnlyDialog
from munientry.checkers.crim_checks import JailTimeChecks
from munientry.loaders.cms_case_loaders import CmsFraLoader
from munientry.models.case_information.sentencing_entries import (
    SentencingOnlyEntryCaseInformation,
)
from munientry.settings.pyqt_constants import MAX_JAIL_TIME_VALIDATOR
from munientry.updaters.grid_case_updaters import SentencingOnlyDialogUpdater
from munientry.views.sentencing_only_dialog_ui import Ui_SentencingOnlyDialog


class SentencingOnlyDialogViewModifier(crim.CrimTrafficViewModifier):
    """View builder for Sentencing Only Dialog."""


class SentencingOnlyDialogSlotFunctions(crim.CrimTrafficSlotFunctions, crim.FineCostsMixin):
    """Additional functions for Sentencing Only Dialog."""

    def show_companion_case_fields(self):
        if self.dialog.add_companion_cases_checkBox.isChecked():
            self.dialog.companion_cases_box.setHidden(False)
            self.dialog.companion_cases_sentence_box.setHidden(False)
            self.dialog.companion_cases_sentence_label.setHidden(False)
        else:
            self.dialog.companion_cases_box.setHidden(True)
            self.dialog.companion_cases_sentence_box.setHidden(True)
            self.dialog.companion_cases_sentence_label.setHidden(True)

    def start_add_jail_report_dialog(self):
        self.dialog.update_entry_case_information()
        self.dialog.popup_dialog = AddJailOnlyDialog(self.dialog)
        self.dialog.popup_dialog.exec()

    def start_add_conditions_dialog(self):
        self.dialog.update_entry_case_information()
        self.dialog.popup_dialog = AddCommunityControlDialog(self.dialog)
        self.dialog.popup_dialog.exec()


class SentencingOnlyDialogSignalConnector(crim.CrimTrafficSignalConnector):
    """Signal Connector for Sentencing Only Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()
        self.connect_plea_all_button_signals()
        self.connect_fra_signals()
        self.connect_court_cost_signals()
        self.connect_main_dialog_add_condition_signals()
        self.connect_dialog_specific_signals()

    def connect_dialog_specific_signals(self):
        self.dialog.jail_checkBox.toggled.connect(self.dialog.functions.conditions_checkbox_toggle)
        self.dialog.add_companion_cases_checkBox.toggled.connect(
            self.dialog.functions.show_companion_case_fields,
        )
        self.dialog.community_control_checkBox.toggled.connect(
            self.dialog.functions.conditions_checkbox_toggle,
        )
        self.dialog.impoundment_checkBox.toggled.connect(
            self.dialog.functions.conditions_checkbox_toggle,
        )
        self.dialog.victim_notification_checkBox.toggled.connect(
            self.dialog.functions.conditions_checkbox_toggle,
        )
        self.dialog.add_jail_report_Button.pressed.connect(
            self.dialog.functions.start_add_jail_report_dialog,
        )


class SentencingOnlyCheckList(JailTimeChecks):
    """Check list for Sentencing Only Checks, same as JailCCPlea, but plea check is different."""

    check_list = [
        'check_defense_counsel',
        'check_plea_date',
        'check_if_no_finding_entered',
        'check_insurance',
        'check_additional_conditions_ordered',
        'check_if_jail_suspended_more_than_imposed',
        'check_if_days_in_jail_blank_but_in_jail',
        'check_if_in_jail_blank_but_has_jail_days',
        'check_if_apply_jail_credit_blank_but_in_jail',
        'check_if_jail_reporting_required',
        'check_if_jail_equals_suspended_and_imposed',
        'check_if_jail_credit_more_than_imposed',
        'check_if_in_jail_and_reporting_set',
    ]
    conditions_list = [
        ('license_suspension', 'license_type', 'License Suspension'),
        ('community_service', 'hours_of_service', 'Community Service'),
        ('other_conditions', 'terms', 'Other Conditions'),
        ('community_control', 'term_of_control', 'Community Control'),
        ('impoundment', 'vehicle_make_model', 'Immobilize/Impound'),
    ]


class SentencingOnlyDialog(crim.CrimTrafficDialogBuilder, Ui_SentencingOnlyDialog):
    """Dialog builder class for 'Sentencing Only - Already Plead' dialog."""

    _case_information_model = SentencingOnlyEntryCaseInformation
    _case_loader = CmsFraLoader
    _info_checker = SentencingOnlyCheckList
    _model_updater = SentencingOnlyDialogUpdater
    _signal_connector = SentencingOnlyDialogSignalConnector
    _slots = SentencingOnlyDialogSlotFunctions
    _view_modifier = SentencingOnlyDialogViewModifier
    dialog_name = 'Sentencing Judgment Entry'

    def additional_setup(self):
        validator = MAX_JAIL_TIME_VALIDATOR
        self.jail_time_credit_box.setValidator(validator)
        self.additional_conditions_list = [
            ('community_control_checkBox', self.entry_case_information.community_control),
            ('license_suspension_checkBox', self.entry_case_information.license_suspension),
            ('community_service_checkBox', self.entry_case_information.community_service),
            ('other_conditions_checkBox', self.entry_case_information.other_conditions),
            ('jail_checkBox', self.entry_case_information.jail_terms),
            ('impoundment_checkBox', self.entry_case_information.impoundment),
            ('victim_notification_checkBox', self.entry_case_information.victim_notification),
        ]
        self.functions.set_fines_costs_pay_date()  # Sets the fines and costs pay fields
