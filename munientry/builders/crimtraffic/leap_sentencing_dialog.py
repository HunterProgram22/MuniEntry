"""Builder module for the LEAP Sentencing Dialog."""
from loguru import logger

from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.builders.secondary.add_conditions_dialog import AddConditionsDialog
from munientry.checkers.crim_checks import InsuranceChecks, ChargeGridChecks
from munientry.loaders.cms_case_loaders import CmsFraLoader
from munientry.models.case_information.sentencing_entries import (
    LeapSentencingEntryCaseInformation,
)
from munientry.updaters.grid_case_updaters import LeapSentencingDialogUpdater
from munientry.views.leap_sentencing_dialog_ui import Ui_LeapSentencingDialog


class LeapSentencingDialogViewModifier(crim.CrimTrafficViewModifier):
    """View builder for LEAP Sentencing Dialog."""


class LeapSentencingDialogSlotFunctions(crim.CrimTrafficSlotFunctions, crim.FineCostsMixin):
    """Additional functions for LEAP Sentencing Dialog."""

    def set_fines_credit_for_jail_field(self):
        if self.dialog.credit_for_jail_checkBox.isChecked():
            self.dialog.jail_time_credit_box.setEnabled(True)
            self.dialog.jail_time_credit_box.setHidden(False)
            self.dialog.jail_time_credit_box.setFocus()
        else:
            self.dialog.jail_time_credit_box.setEnabled(False)
            self.dialog.jail_time_credit_box.setHidden(True)

    def start_add_conditions_dialog(self):
        self.dialog.update_entry_case_information()
        self.dialog.popup_dialog = AddConditionsDialog(self.dialog)
        self.dialog.popup_dialog.exec()


class LeapSentencingDialogSignalConnector(crim.CrimTrafficSignalConnector):
    """Signal Connector for LEAP Sentencing Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()
        self.connect_plea_all_button_signals()
        self.connect_fra_signals()
        self.connect_court_cost_signals()
        self.connect_main_dialog_add_condition_signals()
        self.dialog.credit_for_jail_checkBox.toggled.connect(
            self.dialog.functions.set_fines_credit_for_jail_field,
        )


class LeapSentencingCheckList(ChargeGridChecks, InsuranceChecks):
    """Check list for LEAP Sentencing Dialog."""

    check_list = [
        'check_defense_counsel',
        'check_leap_plea_date',
        'check_if_no_plea_entered',
        'check_if_no_finding_entered',
        'check_insurance',
        'check_additional_conditions_ordered',
    ]
    conditions_list = [
        ('license_suspension', 'license_type', 'License Suspension'),
        ('community_service', 'hours_of_service', 'Community Service'),
        ('other_conditions', 'terms', 'Other Conditions'),
    ]


class LeapSentencingDialog(crim.CrimTrafficDialogBuilder, Ui_LeapSentencingDialog):
    """Dialog builder class for 'LEAP Sentencing' dialog."""

    _case_information_model = LeapSentencingEntryCaseInformation
    _case_loader = CmsFraLoader
    _info_checker = LeapSentencingCheckList
    _model_updater = LeapSentencingDialogUpdater
    _signal_connector = LeapSentencingDialogSignalConnector
    _slots = LeapSentencingDialogSlotFunctions
    _view_modifier = LeapSentencingDialogViewModifier
    dialog_name = 'Leap Sentencing Judgment Entry'

    def additional_setup(self):
        self.additional_conditions_list = [
            ('license_suspension_checkBox', self.entry_case_information.license_suspension),
            ('community_service_checkBox', self.entry_case_information.community_service),
            ('other_conditions_checkBox', self.entry_case_information.other_conditions),
        ]
        self.functions.set_fines_credit_for_jail_field()
        self.functions.set_fines_costs_pay_date()  # Sets the fines and costs pay fields
