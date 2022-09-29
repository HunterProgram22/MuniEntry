"""Module builder for Add Jail Dialog."""
from __future__ import annotations

from typing import Any

from loguru import logger

from munientry.builders.secondary import base_secondary_builders as second
from munientry.builders import base_builders as base
from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.settings import WIDGET_TYPE_ACCESS_DICT
from munientry.views.add_jail_only_dialog_ui import Ui_AddJailOnly


class AddJailOnlyDialogViewModifier(crim.CrimTrafficViewModifier):
    """View builder for Add Jail Dialog."""

    condition_classes = [
        ('jail_checkBox', 'jail_terms'),
    ]

    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_conditions_case_information_banner()
        self.load_existing_data_to_dialog()


class AddJailOnlyDialogSlotFunctions(crim.CrimTrafficSlotFunctions):
    """Additional functions for Add Jail Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.main_dialog = dialog.main_dialog

    def add_conditions(self):
        if self.main_dialog.jail_checkBox.isChecked():
            self.dialog.transfer_view_data_to_model(
                self.main_dialog.entry_case_information.jail_terms,
            )

    def set_report_date_boxes(self):
        if self.dialog.report_type_box.currentText() == 'future date':
            self.dialog.report_date_box.setEnabled(True)
            self.dialog.report_date_box.setHidden(False)
            self.dialog.report_time_box.setEnabled(True)
            self.dialog.report_time_box.setHidden(False)
            self.dialog.report_date_label.setHidden(False)
            self.dialog.report_time_label.setHidden(False)
        else:
            self.dialog.report_date_box.setDisabled(True)
            self.dialog.report_date_box.setHidden(True)
            self.dialog.report_time_box.setDisabled(True)
            self.dialog.report_time_box.setHidden(True)
            self.dialog.report_date_label.setHidden(True)
            self.dialog.report_time_label.setHidden(True)

    def show_report_days_notes_box(self):
        if self.dialog.jail_sentence_execution_type_box.currentText() == 'consecutive days':
            self.dialog.jail_report_days_notes_box.setDisabled(True)
            self.dialog.jail_report_days_notes_box.setHidden(True)
        else:
            self.dialog.jail_report_days_notes_box.setDisabled(False)
            self.dialog.jail_report_days_notes_box.setHidden(False)


class AddJailOnlyDialogSignalConnector(crim.CrimTrafficSignalConnector):
    """Signal Connector for Add Jail Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_condition_dialog_main_signals()
        self.connect_jail_frame_signals()

    def connect_jail_frame_signals(self):
        self.dialog.report_type_box.currentTextChanged.connect(
            self.dialog.functions.set_report_date_boxes,
        )
        self.dialog.jail_sentence_execution_type_box.currentTextChanged.connect(
            self.dialog.functions.show_report_days_notes_box,
        )


class AddJailOnlyDialog(second.SecondaryDialogBuilder, Ui_AddJailOnly):
    """Secondary dialog for setting jail reporting information.

    Dialogs that use: JailCCPleaDialog, SentencingOnlyDialog, TrialSentencingDialog.

    The conditions_checkbox_dict is called by the BaseDialogSlotFunctions
    show_hide_checkbox_connected_fields to hide boxes on load that are optional.
    """

    build_dict = {
        'dialog_name': 'Add Jail Only Dialog',
        'view': AddJailOnlyDialogViewModifier,
        'slots': AddJailOnlyDialogSlotFunctions,
        'signals': AddJailOnlyDialogSignalConnector,
    }

    condition_checkbox_dict = {
        'companion_cases_checkBox': [
            'companion_cases_box',
            'jail_term_type_box',
            'consecutive_jail_days_label',
        ],
    }

    def __init__(self, main_dialog, parent=None) -> None:
        self.charges_list = main_dialog.entry_case_information.charges_list
        self.main_dialog = main_dialog
        super().__init__(parent)
        self.additional_setup()
        logger.dialog(f'{self.dialog_name} Opened')

    def additional_setup(self):
        self.functions.set_report_date_boxes()
        self.functions.show_report_days_notes_box()

    def start_jail_only_dialog(self) -> None:
        """TODO: Check if this is ever called - delete if not."""
        logger.debug('Add JAIL dialog called')
        self.update_entry_case_information()
        AddJailOnlyDialog(self).exec()

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
