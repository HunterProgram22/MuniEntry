"""Builder module for Trial Sentencing Dialog."""
from loguru import logger

from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.builders.secondary.add_community_control_dialog import (
    AddCommunityControlDialog,
)
from munientry.builders.secondary.add_jail_only_dialog import AddJailOnlyDialog
from munientry.checkers.jail_charge_grid_checkers import (
    TrialSentencingDialogInfoChecker,
)
from munientry.loaders.cms_case_loaders import CmsFraLoader
from munientry.models.case_information.sentencing_entries import (
    TrialSentencingEntryCaseInformation,
)
from munientry.appsettings.pyqt_constants import MAX_JAIL_TIME_VALIDATOR
from munientry.updaters.grid_case_updaters import TrialSentencingDialogUpdater
from munientry.views.trial_sentencing_dialog_ui import Ui_TrialSentencingDialog


class TrialSentencingDialogViewModifier(crim.CrimTrafficViewModifier):
    """View builder for Trial Sentencing Dialog.

    The view uses the JailChargesGrid but the template does not have a plea field and instead uses
    tried to (either 'court' or 'jury') instead of the plea field.
    """


class TrialSentencingDialogSlotFunctions(crim.CrimTrafficSlotFunctions, crim.FineCostsMixin):
    """Additional functions for Trial Sentencing Dialog."""

    def set_all_findings_process(self):
        self.dialog.charges_gridLayout.set_all_trial_findings()

    def set_court_costs(self):
        self.dialog.court_costs_box.setCurrentText('No Costs or Fines')
        self.dialog.ability_to_pay_box.setHidden(True)
        self.dialog.balance_due_date.setHidden(True)

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


class TrialSentencingDialogSignalConnector(crim.CrimTrafficSignalConnector):
    """Signal Connector for Trial Sentencing Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()
        self.connect_fra_signals()
        self.connect_court_cost_signals()
        self.connect_main_dialog_add_condition_signals()
        self.connect_dialog_specific_signals()
        self.dialog.add_charge_Button.released.connect(
            self.dialog.functions.start_add_charge_dialog,
        )

    def connect_dialog_specific_signals(self):
        self.dialog.guilty_all_Button.pressed.connect(
            self.dialog.charges_gridLayout.set_all_trial_findings,
        )
        self.dialog.not_guilty_all_Button.pressed.connect(
            self.dialog.charges_gridLayout.set_all_trial_findings,
        )
        self.dialog.not_guilty_all_Button.pressed.connect(
            self.dialog.functions.set_court_costs,
        )
        self.dialog.jail_checkBox.toggled.connect(
            self.dialog.functions.conditions_checkbox_toggle,
        )
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


class TrialSentencingDialog(crim.CrimTrafficDialogBuilder, Ui_TrialSentencingDialog):
    """Dialog builder class for 'Jury Trial / Trial to Court Sentencing' dialog."""

    _case_information_model = TrialSentencingEntryCaseInformation
    _case_loader = CmsFraLoader
    _info_checker = TrialSentencingDialogInfoChecker
    _model_updater = TrialSentencingDialogUpdater
    _signal_connector = TrialSentencingDialogSignalConnector
    _slots = TrialSentencingDialogSlotFunctions
    _view_modifier = TrialSentencingDialogViewModifier
    dialog_name = 'Trial Sentencing Dialog'

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
        self.functions.show_companion_case_fields()


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
