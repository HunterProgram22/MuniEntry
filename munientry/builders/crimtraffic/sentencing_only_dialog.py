"""Builder module for the Jail CC Plea Dialog."""
from loguru import logger

from munientry.builders.conditions_dialogs import (
    AddCommunityControlDialog,
    AddJailOnlyDialog,
)
from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.checkers.jail_charge_grid_checkers import SentencingOnlyDialogInfoChecker
from munientry.controllers import charges_grids as cg
from munientry.data.cms_case_loaders import CmsFraLoader
from munientry.models.case_information.sentencing_entries import (
    SentencingOnlyEntryCaseInformation,
)
from munientry.updaters.grid_case_updaters import SentencingOnlyDialogUpdater
from munientry.views.sentencing_only_dialog_ui import Ui_SentencingOnlyDialog


class SentencingOnlyDialogViewModifier(crim.BaseDialogViewModifier):
    """View builder for Sentencing Only Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog.charges_gridLayout.__class__ = cg.JailChargesGrid


class SentencingOnlyDialogSlotFunctions(crim.BaseDialogSlotFunctions):
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


class SentencingOnlyDialogSignalConnector(crim.BaseDialogSignalConnector_Refactor):
    """Signal Connector for Sentencing Only Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()
        self.connect_plea_all_button_signals()
        self.connect_fra_signals()
        self.connect_court_cost_signals()
        self.connect_main_dialog_additional_condition_signals()
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


class SentencingOnlyDialog(crim.CriminalDialogBuilder, Ui_SentencingOnlyDialog):
    """Dialog builder class for 'Sentencing Only - Already Plead' dialog."""

    build_dict = {
        'dialog_name': 'Sentencing Only Dialog',
        'view': SentencingOnlyDialogViewModifier,
        'slots': SentencingOnlyDialogSlotFunctions,
        'signals': SentencingOnlyDialogSignalConnector,
        'case_information_model': SentencingOnlyEntryCaseInformation,
        'loader': CmsFraLoader,
        'updater': SentencingOnlyDialogUpdater,
        'info_checker': SentencingOnlyDialogInfoChecker,
    }

    def additional_setup(self):
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


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
