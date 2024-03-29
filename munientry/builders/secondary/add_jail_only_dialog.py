"""Module builder for Add Jail Dialog."""
from loguru import logger

from munientry.builders.secondary import base_secondary_builders as second
from munientry.views.add_jail_only_dialog_ui import Ui_AddJailOnly


class AddJailOnlyDialogViewModifier(second.SecondaryViewModifier):
    """View builder for Add Jail Dialog."""

    condition_classes = [
        ('jail_checkBox', 'jail_terms'),
    ]

    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_conditions_case_information_banner()
        self.load_existing_data_to_dialog()


class AddJailOnlyDialogSlotFunctions(second.SecondarySlotFunctions):
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
            self.show_report_date_boxes()
        else:
            self.hide_report_date_boxes()

    def show_report_date_boxes(self):
        self.dialog.report_date_box.setEnabled(True)
        self.dialog.report_date_box.setHidden(False)
        self.dialog.report_time_box.setEnabled(True)
        self.dialog.report_time_box.setHidden(False)
        self.dialog.report_date_label.setHidden(False)
        self.dialog.report_time_label.setHidden(False)

    def hide_report_date_boxes(self):
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


class AddJailOnlyDialogSignalConnector(second.SecondarySignalConnector):
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

    _signal_connector = AddJailOnlyDialogSignalConnector
    _slots = AddJailOnlyDialogSlotFunctions
    _view_modifier = AddJailOnlyDialogViewModifier
    dialog_name = 'Add Jail Only Dialog'

    condition_checkbox_dict = {
        'companion_cases_checkBox': [
            'companion_cases_box',
            'jail_term_type_box',
            'consecutive_jail_days_label',
        ],
    }

    def __init__(self, main_dialog, parent=None) -> None:
        super().__init__(main_dialog, parent)
        self.additional_setup()

    def additional_setup(self):
        self.functions.set_report_date_boxes()
        self.functions.show_report_days_notes_box()


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
