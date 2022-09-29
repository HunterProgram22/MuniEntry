"""Module builder for Add Conditions Secondary Dialog."""
from __future__ import annotations

from typing import Any

import munientry.builders.base_builders
from loguru import logger

from munientry.builders.secondary import base_secondary_builders as second
from munientry.builders import base_builders as base
from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.settings import WIDGET_TYPE_ACCESS_DICT
from munientry.views.add_conditions_dialog_ui import Ui_AddConditionsDialog


class AddConditionsDialogViewModifier(crim.CrimTrafficViewModifier):
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


class AddConditionsDialogSlotFunctions(crim.CrimTrafficSlotFunctions):
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


class AddConditionsDialogSignalConnector(crim.CrimTrafficSignalConnector):
    """Signal Connector for Additional Conditions Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_condition_dialog_main_signals()
        self.connect_community_service_days_update()


class AddConditionsDialog(second.SecondaryDialogBuilder, Ui_AddConditionsDialog):
    """The secondary conditions dialog builder for non-community control conditions.

    Dialogs that use: FineOnlyPleaDialog, LeapSentencingDialog.
    """

    build_dict = {
        'dialog_name': 'Additional Conditions Dialog',
        'view': AddConditionsDialogViewModifier,
        'slots': AddConditionsDialogSlotFunctions,
        'signals': AddConditionsDialogSignalConnector,
    }

    conditions_frames = [
        ('other_conditions_checkBox', 'other_conditions_frame'),
        ('license_suspension_checkBox', 'license_suspension_frame'),
        ('community_service_checkBox', 'community_service_frame'),
    ]

    def __init__(self, main_dialog, parent=None) -> None:
        self.charges_list = main_dialog.entry_case_information.charges_list
        self.main_dialog = main_dialog
        super().__init__(parent)
        self.additional_setup()
        logger.dialog(f'{self.dialog_name} Opened')
        crim.enable_condition_frames(self, main_dialog)

    def additional_setup(self):
        self.functions.update_community_service_due_date()

    def transfer_view_data_to_model(self, model_class: type[Any]) -> None:
        """Takes data in the view fields and transfers to appropriate model class attribute.

        Method loops through all items in terms list which are maps of a model attribute to
        a view field. The appropriate transfer method is obtained from the WIDGET_TYPE_ACCESS_DICT

        Args:
            model_class: A dataclass object that has a terms_list attribute mapping
                view fields to model attributes.
        """
        for (model_attribute, view_field) in model_class.terms_list:
            widget_type = getattr(self, view_field).__class__.__name__
            view = getattr(self, view_field)
            view_field_data = getattr(view, WIDGET_TYPE_ACCESS_DICT.get(widget_type, 'None'))()
            class_name = model_class.__class__.__name__
            setattr(model_class, model_attribute, view_field_data)
            logger.info(f'{class_name} {model_attribute} set to: {view_field_data}.')


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
