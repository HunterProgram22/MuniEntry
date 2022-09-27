"""Builder module for the LEAP Sentencing Dialog."""
import munientry.builders.base_dialogs
from loguru import logger

from munientry.builders.crimtraffic.add_conditions_dialog import AddConditionsDialog
from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.checkers.no_jail_sentencing_checkers import (
    LeapSentencingDialogInfoChecker,
)
from munientry.controllers import charges_grids as cg
from munientry.data.cms_case_loaders import CmsFraLoader
from munientry.models.case_information.sentencing_entries import (
    LeapSentencingEntryCaseInformation,
)
from munientry.updaters.grid_case_updaters import LeapSentencingDialogUpdater
from munientry.views.leap_sentencing_dialog_ui import Ui_LeapSentencingDialog


class LeapSentencingDialogViewModifier(crim.BaseDialogViewModifier):
    """View builder for LEAP Sentencing Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog.charges_gridLayout.__class__ = cg.FineOnlyChargeGrid


class LeapSentencingDialogSlotFunctions(crim.BaseDialogSlotFunctions):
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


class LeapSentencingDialogSignalConnector(munientry.builders.base_dialogs.BaseDialogSignalConnector):
    """Signal Connector for LEAP Sentencing Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()
        self.connect_plea_all_button_signals()
        self.connect_fra_signals()
        self.connect_court_cost_signals()
        self.connect_main_dialog_additional_condition_signals()
        self.dialog.credit_for_jail_checkBox.toggled.connect(
            self.dialog.functions.set_fines_credit_for_jail_field,
        )


class LeapSentencingDialog(crim.CriminalDialogBuilder, Ui_LeapSentencingDialog):
    """Dialog builder class for 'LEAP Sentencing' dialog."""

    build_dict = {
        'dialog_name': 'Leap Sentencing Dialog',
        'view': LeapSentencingDialogViewModifier,
        'slots': LeapSentencingDialogSlotFunctions,
        'signals': LeapSentencingDialogSignalConnector,
        'case_information_model': LeapSentencingEntryCaseInformation,
        'loader': CmsFraLoader,
        'updater': LeapSentencingDialogUpdater,
        'info_checker': LeapSentencingDialogInfoChecker,
    }

    def additional_setup(self):
        self.additional_conditions_list = [
            ('license_suspension_checkBox', self.entry_case_information.license_suspension),
            ('community_service_checkBox', self.entry_case_information.community_service),
            ('other_conditions_checkBox', self.entry_case_information.other_conditions),
        ]
        self.functions.set_fines_credit_for_jail_field()


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
