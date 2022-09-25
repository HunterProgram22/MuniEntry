"""The condtions dialogs module contains secondary dialogs that are opened from a main dialog."""
from loguru import logger
from PyQt5.QtWidgets import QDialog

from munientry.builders.base_dialogs import BaseDialog
from munientry.builders.crimtraffic.base_crimtraffic_builders import enable_condition_frames
from munientry.controllers.signal_connectors import (
    AddJailOnlyDialogSignalConnector,
    AddSpecialBondConditionsDialogSignalConnector,
)
from munientry.controllers.slot_functions import (
    AddJailOnlyDialogSlotFunctions,
    AddSpecialBondConditionsDialogSlotFunctions,
)
from munientry.controllers.view_modifiers import (
    AddJailOnlyDialogViewModifier,
    AddSpecialBondConditionsDialogViewModifier,
)
from munientry.views.add_jail_only_dialog_ui import Ui_AddJailOnly
from munientry.views.add_special_bond_conditions_dialog_ui import (
    Ui_AddSpecialBondConditionsDialog,
)


class AddJailOnlyDialog(BaseDialog, Ui_AddJailOnly):
    """Secondary dialog for setting jail reporting information.

    Dialogs that use: JailCCPleaDialog, SentencingOnlyDialog, TrialSentencingDialog.

    The conditions_checkbox_dict is called by the BaseDialogSlotFunctions
    show_hide_checkbox_connected_fields to hide boxes on load that are optional.
    """

    condition_checkbox_dict = {
        'companion_cases_checkBox': [
            'companion_cases_box',
            'jail_term_type_box',
            'consecutive_jail_days_label',
        ],
    }

    def __init__(self, main_dialog: QDialog, parent: QDialog = None) -> None:
        logger.dialog('AddJailOnlyDialog Opened')
        self.charges_list = main_dialog.entry_case_information.charges_list
        self.main_dialog = main_dialog
        super().__init__(parent)

    def _modify_view(self) -> AddJailOnlyDialogViewModifier:
        return AddJailOnlyDialogViewModifier(self)

    def _connect_signals_to_slots(self) -> None:
        self.functions = AddJailOnlyDialogSlotFunctions(self)
        AddJailOnlyDialogSignalConnector(self)

    def start_jail_only_dialog(self) -> None:
        self.update_entry_case_information()
        AddJailOnlyDialog(self).exec()


class AddSpecialBondConditionsDialog(BaseDialog, Ui_AddSpecialBondConditionsDialog):
    """The secondary dialog for adding special bond conditions.

    Dialogs that use: NotGuiltyBondDialog, BondHearingDialog, NoPleaBondDialog.
    """

    conditions_frames = [
        ('other_conditions_checkBox', 'other_conditions_frame'),
        ('admin_license_suspension_checkBox', 'admin_license_suspension_frame'),
        ('domestic_violence_checkBox', 'domestic_violence_frame'),
        ('vehicle_seizure_checkBox', 'vehicle_seizure_frame'),
        ('no_contact_checkBox', 'no_contact_frame'),
        ('custodial_supervision_checkBox', 'custodial_supervision_frame'),
    ]

    def __init__(self, main_dialog: QDialog, parent: QDialog = None) -> None:
        logger.dialog('AddSpecialBondConditionsDialog Opened')
        self.charges_list = main_dialog.entry_case_information.charges_list
        self.main_dialog = main_dialog
        super().__init__(parent)
        enable_condition_frames(self, main_dialog)

    def _modify_view(self) -> AddSpecialBondConditionsDialogViewModifier:
        return AddSpecialBondConditionsDialogViewModifier(self)

    def _connect_signals_to_slots(self) -> None:
        self.functions = AddSpecialBondConditionsDialogSlotFunctions(self)
        AddSpecialBondConditionsDialogSignalConnector(self)


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
