"""Module builder for Add Conditions Secondary Dialog."""
from loguru import logger

from munientry.builders.secondary import base_secondary_builders as second
from munientry.views.add_conditions_dialog_ui import Ui_AddConditionsDialog


class AddConditionsDialogViewModifier(second.SecondaryViewModifier):
    """View Builder for Additional Conditions Secondary Dialog."""

    condition_classes = [
        ('other_conditions_checkBox', 'other_conditions'),
        ('license_suspension_checkBox', 'license_suspension'),
        ('community_service_checkBox', 'community_service'),
    ]

    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_conditions_case_information_banner()
        self.load_existing_data_to_dialog()


class AddConditionsDialogSlotFunctions(second.SecondarySlotFunctions):
    """Additional functions for Additional Conditions Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.main_dialog = dialog.main_dialog

    def add_conditions(self):
        if self.main_dialog.community_service_checkBox.isChecked():
            self.dialog.transfer_view_data_to_model(
                self.main_dialog.entry_case_information.community_service,
            )
        if self.main_dialog.license_suspension_checkBox.isChecked():
            self.dialog.transfer_view_data_to_model(
                self.main_dialog.entry_case_information.license_suspension,
            )
        if self.main_dialog.other_conditions_checkBox.isChecked():
            self.dialog.transfer_view_data_to_model(
                self.main_dialog.entry_case_information.other_conditions,
            )


class AddConditionsDialogSignalConnector(second.SecondarySignalConnector):
    """Signal Connector for Additional Conditions Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_condition_dialog_main_signals()
        self.connect_community_service_days_update()


class AddConditionsDialog(second.SecondaryDialogBuilder, Ui_AddConditionsDialog):
    """The secondary conditions dialog builder for non-community control conditions.

    Dialogs that use: FineOnlyPleaDialog, LeapSentencingDialog.
    """

    _signal_connector = AddConditionsDialogSignalConnector
    _slots = AddConditionsDialogSlotFunctions
    _view_modifier = AddConditionsDialogViewModifier
    dialog_name = 'Add Conditions Dialog'

    conditions_frames = [
        ('other_conditions_checkBox', 'other_conditions_frame'),
        ('license_suspension_checkBox', 'license_suspension_frame'),
        ('community_service_checkBox', 'community_service_frame'),
    ]

    def __init__(self, main_dialog, parent=None) -> None:
        super().__init__(main_dialog, parent)
        self.additional_setup()
        second.enable_condition_frames(self, main_dialog)

    def additional_setup(self):
        self.functions.update_community_service_due_date()


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
