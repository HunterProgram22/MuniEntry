"""Module builder for Add Community Control Secondary Dialog."""
from loguru import logger

from munientry.builders.secondary import base_secondary_builders as second
from munientry.views.add_community_control_dialog_ui import Ui_AddCommunityControlDialog


class AddCommunityControlDialogViewModifier(second.SecondaryViewModifier):
    """View builder for Add Community Control Secondary Dialog."""

    condition_classes = [
        ('other_conditions_checkBox', 'other_conditions'),
        ('license_suspension_checkBox', 'license_suspension'),
        ('community_service_checkBox', 'community_service'),
        ('community_control_checkBox', 'community_control'),
        ('impoundment_checkBox', 'impoundment'),
        ('victim_notification_checkBox', 'victim_notification'),
    ]

    condition_checkbox_list = [
        ('gps_exclusion_checkBox', 'gps_exclusion_radius_box'),
        ('gps_exclusion_checkBox', 'gps_exclusion_location_box'),
        (
            'community_control_not_within_500_feet_checkBox',
            'community_control_not_within_500_feet_person_box',
        ),
        ('community_control_no_contact_checkBox', 'community_control_no_contact_with_box'),
        ('house_arrest_checkBox', 'house_arrest_time_box'),
        (
            'community_control_community_service_checkBox',
            'community_control_community_service_hours_box',
        ),
        ('other_community_control_checkBox', 'other_community_control_conditions_box'),
        ('alcohol_monitoring_checkBox', 'alcohol_monitoring_time_box'),
        ('pay_restitution_checkBox', 'pay_restitution_amount_box'),
        ('pay_restitution_checkBox', 'pay_restitution_to_box'),
        ('specialized_docket_checkBox', 'specialized_docket_box'),
    ]

    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_conditions_case_information_banner()
        self.load_existing_data_to_dialog()
        self.hide_boxes()


class AddCommunityControlDialogSlotFunctions(second.SecondarySlotFunctions):
    """Additional functions for Add Community Control Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.main_dialog = dialog.main_dialog

    def add_conditions(self):
        if self.main_dialog.community_service_checkBox.isChecked():
            self.dialog.transfer_view_data_to_model(
                self.main_dialog.entry_case_information.community_service,
            )
        if self.main_dialog.other_conditions_checkBox.isChecked():
            self.dialog.transfer_view_data_to_model(
                self.main_dialog.entry_case_information.other_conditions,
            )
        if self.main_dialog.community_control_checkBox.isChecked():
            self.dialog.transfer_view_data_to_model(
                self.main_dialog.entry_case_information.community_control,
            )
        if self.main_dialog.license_suspension_checkBox.isChecked():
            self.dialog.transfer_view_data_to_model(
                self.main_dialog.entry_case_information.license_suspension,
            )
        if self.main_dialog.impoundment_checkBox.isChecked():
            self.dialog.transfer_view_data_to_model(
                self.main_dialog.entry_case_information.impoundment,
            )
        if self.main_dialog.victim_notification_checkBox.isChecked():
            self.dialog.transfer_view_data_to_model(
                self.main_dialog.entry_case_information.victim_notification,
            )


class AddCommunityControlDialogSignalConnector(second.SecondarySignalConnector):
    """Signal Connector for Add Community Control Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_condition_dialog_main_signals()
        self.connect_community_service_days_update()
        self.connect_community_control_signals()

    def connect_community_control_signals(self):
        self.dialog.gps_exclusion_checkBox.toggled.connect(
            self.dialog.functions.show_hide_checkbox_connected_fields,
        )
        self.dialog.community_control_not_within_500_feet_checkBox.toggled.connect(
            self.dialog.functions.show_hide_checkbox_connected_fields,
        )
        self.dialog.community_control_no_contact_checkBox.toggled.connect(
            self.dialog.functions.show_hide_checkbox_connected_fields,
        )
        self.dialog.house_arrest_checkBox.toggled.connect(
            self.dialog.functions.show_hide_checkbox_connected_fields,
        )
        self.dialog.community_control_community_service_checkBox.toggled.connect(
            self.dialog.functions.show_hide_checkbox_connected_fields,
        )
        self.dialog.other_community_control_checkBox.toggled.connect(
            self.dialog.functions.show_hide_checkbox_connected_fields,
        )
        self.dialog.alcohol_monitoring_checkBox.toggled.connect(
            self.dialog.functions.show_hide_checkbox_connected_fields,
        )
        self.dialog.pay_restitution_checkBox.toggled.connect(
            self.dialog.functions.show_hide_checkbox_connected_fields,
        )
        self.dialog.specialized_docket_checkBox.toggled.connect(
            self.dialog.functions.show_hide_checkbox_connected_fields,
        )


class AddCommunityControlDialog(second.SecondaryDialogBuilder, Ui_AddCommunityControlDialog):
    """The secondary conditions sentencing dialogs with community control.

    Dialogs that use: JailCCPleaDialog, SentencingOnlyDialog, TrialSentencingDialog.

    The conditions_checkbox_dict is called by the BaseDialogSlotFunctions
    to hide boxes on load that are optional.
    """

    build_dict = {
        'dialog_name': 'Add Community Control Dialog',
        'view': AddCommunityControlDialogViewModifier,
        'slots': AddCommunityControlDialogSlotFunctions,
        'signals': AddCommunityControlDialogSignalConnector,
    }

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

    def __init__(self, main_dialog, parent=None) -> None:
        super().__init__(main_dialog, parent)
        second.enable_condition_frames(self, main_dialog)


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
