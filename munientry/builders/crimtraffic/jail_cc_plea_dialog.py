"""Builder module for the Jail CC Plea Dialog."""
from loguru import logger
from PyQt5.QtGui import QIntValidator

from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.builders.secondary.add_community_control_dialog import (
    AddCommunityControlDialog,
)
from munientry.builders.secondary.add_jail_only_dialog import AddJailOnlyDialog
from munientry.checkers.jail_charge_grid_checkers import JailCCPleaDialogInfoChecker
from munientry.controllers import charges_grids as cg
from munientry.data.cms_case_loaders import CmsFraLoader
from munientry.models.case_information.sentencing_entries import (
    JailCCEntryCaseInformation,
)
from munientry.updaters.grid_case_updaters import JailCCDialogUpdater
from munientry.views.jail_cc_plea_dialog_ui import Ui_JailCCPleaDialog


class JailCCDialogViewModifier(crim.CrimTrafficViewModifier):
    """View builder for Jail CC Plea Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog.charges_gridLayout.__class__ = cg.JailChargesGrid
        self.set_appearance_reason()


class JailCCDialogSlotFunctions(crim.CrimTrafficSlotFunctions, crim.FineCostsMixin):
    """Additional functions for Jail CC Plea Dialog."""

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


class JailCCDialogSignalConnector(crim.CrimTrafficSignalConnector):
    """Signal Connector for Jail CC Plea Dialog."""

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


class JailCCPleaDialog(crim.CrimTrafficDialogBuilder, Ui_JailCCPleaDialog):
    """Dialog builder class for 'Jail and/or Community Control' dialog."""

    build_dict = {
        'dialog_name': 'Jail CC Plea Dialog',
        'view': JailCCDialogViewModifier,
        'slots': JailCCDialogSlotFunctions,
        'signals': JailCCDialogSignalConnector,
        'case_information_model': JailCCEntryCaseInformation,
        'loader': CmsFraLoader,
        'updater': JailCCDialogUpdater,
        'info_checker': JailCCPleaDialogInfoChecker,
    }

    def additional_setup(self):
        """TODO: same refactor for all additional conditions list should be made."""
        validator = QIntValidator(0, 1000, self)
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
        if self.case_table == 'slated':
            self.in_jail_box.setCurrentText('Yes')


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
