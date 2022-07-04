"""The condtions dialogs module contains secondary dialogs that are opened from a main dialog."""
from loguru import logger
from PyQt5.QtWidgets import QDialog

from munientry.builders.base_dialogs import BaseDialog
from munientry.controllers.signal_connectors import (
    AddCommunityControlDialogSignalConnector,
    AddConditionsDialogSignalConnector,
    AddJailOnlyDialogSignalConnector,
    AddSpecialBondConditionsDialogSignalConnector,
)
from munientry.controllers.slot_functions import (
    AddCommunityControlDialogSlotFunctions,
    AddConditionsDialogSlotFunctions,
    AddJailOnlyDialogSlotFunctions,
    AddSpecialBondConditionsDialogSlotFunctions,
)
from munientry.controllers.view_modifiers import (
    AddCommunityControlDialogViewModifier,
    AddConditionsDialogViewModifier,
    AddJailOnlyDialogViewModifier,
    AddSpecialBondConditionsDialogViewModifier,
)
from munientry.views.add_community_control_dialog_ui import Ui_AddCommunityControlDialog
from munientry.views.add_conditions_dialog_ui import Ui_AddConditionsDialog
from munientry.views.add_jail_only_dialog_ui import Ui_AddJailOnly
from munientry.views.add_special_bond_conditions_dialog_ui import (
    Ui_AddSpecialBondConditionsDialog,
)

DIALOG = 'DIALOG'


def enable_condition_frames(conditions_dialog: QDialog, main_dialog: QDialog) -> None:
    """The function is called to hide frames on load of dialog.

    Hides conditions that have not been selected in the main dialog. This is necessary
    because the base view of a dialog contains all possible frames.
    """
    for frame_item in conditions_dialog.conditions_frames:
        (frame_checkbox, frame) = frame_item
        if getattr(main_dialog, frame_checkbox).isChecked():
            getattr(conditions_dialog, frame).setEnabled(True)
        else:
            frame = getattr(conditions_dialog, frame)
            frame.setParent(None)
            frame.deleteLater()


class AddConditionsDialog(BaseDialog, Ui_AddConditionsDialog):
    """The secondary conditions dialog for non-community control conditions.

    Dialogs that use: FineOnlyPleaDialog, LeapSentencingDialog.
    """

    conditions_frames = [
        ('other_conditions_checkBox', 'other_conditions_frame'),
        ('license_suspension_checkBox', 'license_suspension_frame'),
        ('community_service_checkBox', 'community_service_frame'),
    ]

    def __init__(self, main_dialog: QDialog, parent: QDialog = None) -> None:
        logger.log(DIALOG, 'AddConditionsDialog Opened')
        self.charges_list = main_dialog.entry_case_information.charges_list
        self.main_dialog = main_dialog
        super().__init__(parent)
        enable_condition_frames(self, main_dialog)

    def modify_view(self) -> AddConditionsDialogViewModifier:
        return AddConditionsDialogViewModifier(self)

    def connect_signals_to_slots(self) -> None:
        self.functions = AddConditionsDialogSlotFunctions(self)
        self.functions.update_community_service_due_date()
        AddConditionsDialogSignalConnector(self)


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
        logger.log(DIALOG, 'AddJailOnlyDialog Opened')
        self.charges_list = main_dialog.entry_case_information.charges_list
        self.main_dialog = main_dialog
        super().__init__(parent)

    def modify_view(self) -> AddJailOnlyDialogViewModifier:
        return AddJailOnlyDialogViewModifier(self)

    def connect_signals_to_slots(self) -> None:
        self.functions = AddJailOnlyDialogSlotFunctions(self)
        AddJailOnlyDialogSignalConnector(self)

    def start_jail_only_dialog(self) -> None:
        self.update_entry_case_information()
        AddJailOnlyDialog(self).exec()


class AddCommunityControlDialog(BaseDialog, Ui_AddCommunityControlDialog):
    """The secondary conditions sentencing dialogs with community control.

    Dialogs that use: JailCCPleaDialog, SentencingOnlyDialog, TrialSentencingDialog.

    The conditions_checkbox_dict is called by the BaseDialogSlotFunctions
    to hide boxes on load that are optional.
    """

    conditions_frames = [
        ('other_conditions_checkBox', 'other_conditions_frame'),
        ('license_suspension_checkBox', 'license_suspension_frame'),
        ('community_service_checkBox', 'community_service_frame'),
        ('community_control_checkBox', 'community_control_frame'),
        ('impoundment_checkBox', 'impoundment_frame'),
        ('victim_notification_checkBox', 'victim_notification_frame'),
    ]

    condition_checkbox_dict = {
        'gps_exclusion_checkBox': [
            'gps_exclusion_radius_box',
            'gps_exclusion_location_box',
        ],
        'community_control_not_within_500_feet_checkBox': [
            'community_control_not_within_500_feet_person_box',
        ],
        'community_control_no_contact_checkBox': ['community_control_no_contact_with_box'],
        'house_arrest_checkBox': ['house_arrest_time_box'],
        'community_control_community_service_checkBox': [
            'community_control_community_service_hours_box',
        ],
        'other_community_control_checkBox': ['other_community_control_conditions_box'],
        'alcohol_monitoring_checkBox': ['alcohol_monitoring_time_box'],
        'pay_restitution_checkBox': ['pay_restitution_to_box', 'pay_restitution_amount_box'],
        'companion_cases_checkBox': [
            'companion_cases_box',
            'jail_term_type_box',
            'consecutive_jail_days_label',
        ],
        'specialized_docket_checkBox': ['specialized_docket_box'],
    }

    def __init__(self, main_dialog: QDialog, parent: QDialog = None) -> None:
        logger.log(DIALOG, 'AddCommunityControlDialog Opened')
        self.charges_list = main_dialog.entry_case_information.charges_list
        self.main_dialog = main_dialog
        super().__init__(parent)
        enable_condition_frames(self, main_dialog)

    def modify_view(self) -> AddCommunityControlDialogViewModifier:
        return AddCommunityControlDialogViewModifier(self)

    def connect_signals_to_slots(self) -> None:
        self.functions = AddCommunityControlDialogSlotFunctions(self)
        AddCommunityControlDialogSignalConnector(self)


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
        logger.log(DIALOG, 'AddSpecialBondConditionsDialog Opened')
        self.charges_list = main_dialog.entry_case_information.charges_list
        self.main_dialog = main_dialog
        super().__init__(parent)
        enable_condition_frames(self, main_dialog)

    def modify_view(self) -> AddSpecialBondConditionsDialogViewModifier:
        return AddSpecialBondConditionsDialogViewModifier(self)

    def connect_signals_to_slots(self) -> None:
        self.functions = AddSpecialBondConditionsDialogSlotFunctions(self)
        AddSpecialBondConditionsDialogSignalConnector(self)


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
