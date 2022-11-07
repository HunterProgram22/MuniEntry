"""Builder module for the Fine Only Plea Dialog."""
from loguru import logger

from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.builders.secondary.add_conditions_dialog import AddConditionsDialog
from munientry.checkers.no_jail_sentencing_checkers import FineOnlyDialogInfoChecker
from munientry.loaders.cms_case_loaders import CmsFraLoader
from munientry.models.case_information.sentencing_entries import (
    FineOnlyEntryCaseInformation,
)
from munientry.updaters.grid_case_updaters import FineOnlyDialogUpdater
from munientry.views.fine_only_plea_dialog_ui import Ui_FineOnlyPleaDialog


class FineOnlyDialogViewModifier(crim.CrimTrafficViewModifier):
    """View builder for Fine Only Plea Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_appearance_reason()


class FineOnlyDialogSlotFunctions(crim.CrimTrafficSlotFunctions, crim.FineCostsMixin):
    """Additional functions for Fine Only Plea Dialog."""

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


class FineOnlyDialogSignalConnector(crim.CrimTrafficSignalConnector):
    """Signal Connector for Fine Only Plea Dialog."""

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


class FineOnlyPleaDialog(crim.CrimTrafficDialogBuilder, Ui_FineOnlyPleaDialog):
    """Dialog builder class for 'Fine Only' dialog."""

    build_dict = {
        'dialog_name': 'Fine Only Plea Dialog',
        'view': FineOnlyDialogViewModifier,
        'slots': FineOnlyDialogSlotFunctions,
        'signals': FineOnlyDialogSignalConnector,
        'case_information_model': FineOnlyEntryCaseInformation,
        'loader': CmsFraLoader,
        'updater': FineOnlyDialogUpdater,
        'info_checker': FineOnlyDialogInfoChecker,
    }

    def additional_setup(self):
        self.additional_conditions_list = [
            ('license_suspension_checkBox', self.entry_case_information.license_suspension),
            ('community_service_checkBox', self.entry_case_information.community_service),
            ('other_conditions_checkBox', self.entry_case_information.other_conditions),
        ]
        self.functions.set_fines_credit_for_jail_field()  # Hides credit_for_jail field on load


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
