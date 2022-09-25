"""Module that contains SignalConnector classes. SignalConnector classes are called
when a dialog is built and connect all of the interface objects (i.e. buttons,
checkboxes, etc.) to the dialog."""
from loguru import logger


class BaseDialogSignalConnectorOld:
    def __init__(self, dialog):
        dialog.cancel_Button.released.connect(dialog.functions.close_window)

    def connect_main_dialog_common_signals(self, dialog):
        dialog.clear_fields_case_Button.released.connect(dialog.functions.clear_case_information_fields)
        dialog.create_entry_Button.released.connect(dialog.functions.create_entry_process)
        dialog.close_dialog_Button.released.connect(dialog.functions.close_window)
        dialog.defense_counsel_waived_checkBox.toggled.connect(dialog.functions.set_defense_counsel)

    def connect_fra_signals(self, dialog):
        dialog.fra_in_file_box.currentTextChanged.connect(dialog.functions.set_fra_in_file)
        dialog.fra_in_court_box.currentTextChanged.connect(dialog.functions.set_fra_in_court)

    def connect_plea_all_button_signals(self, dialog):
        dialog.add_charge_Button.released.connect(dialog.functions.start_add_charge_dialog)
        dialog.guilty_all_Button.pressed.connect(dialog.charges_gridLayout.set_all_pleas)
        dialog.guilty_all_Button.pressed.connect(dialog.charges_gridLayout.set_all_findings)
        dialog.no_contest_all_Button.pressed.connect(dialog.charges_gridLayout.set_all_pleas)
        dialog.no_contest_all_Button.pressed.connect(dialog.charges_gridLayout.set_all_findings)

    def connect_not_guilty_all_button(self, dialog):
        dialog.not_guilty_all_Button.pressed.connect(dialog.charges_gridLayout.set_all_pleas)

    def connect_court_cost_signals(self, dialog):
        dialog.ability_to_pay_box.currentTextChanged.connect(dialog.functions.set_fines_costs_pay_date)
        dialog.costs_and_fines_Button.released.connect(dialog.functions.show_costs_and_fines)

    def connect_main_dialog_additional_condition_signals(self, dialog):
        dialog.license_suspension_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.community_service_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.other_conditions_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.add_conditions_Button.pressed.connect(dialog.functions.start_add_conditions_dialog)

    def connect_condition_dialog_main_signals(self, dialog):
        dialog.add_conditions_Button.pressed.connect(dialog.functions.add_conditions)
        dialog.add_conditions_Button.released.connect(dialog.functions.close_window)

    def connect_jail_frame_signals(self, dialog):
        dialog.report_type_box.currentTextChanged.connect(dialog.functions.set_report_date)
        dialog.jail_sentence_execution_type_box.currentTextChanged.connect(dialog.functions.show_report_days_notes_box)

    def connect_community_service_days_update(self, dialog):
        dialog.community_service_days_to_complete_box.currentIndexChanged.connect(
            dialog.functions.update_community_service_due_date
        )


class AddJailOnlyDialogSignalConnector(BaseDialogSignalConnectorOld):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_condition_dialog_main_signals(dialog)
        self.connect_jail_frame_signals(dialog)


class AddCommunityControlDialogSignalConnector(BaseDialogSignalConnectorOld):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_condition_dialog_main_signals(dialog)
        self.connect_community_service_days_update(dialog)
        self.connect_community_control_dialog_specific_signals(dialog)

    def connect_community_control_dialog_specific_signals(self, dialog):
        dialog.gps_exclusion_checkBox.toggled.connect(dialog.functions.show_hide_checkbox_connected_fields)
        dialog.community_control_not_within_500_feet_checkBox.toggled.connect(dialog.functions.show_hide_checkbox_connected_fields)
        dialog.community_control_no_contact_checkBox.toggled.connect(dialog.functions.show_hide_checkbox_connected_fields)
        dialog.house_arrest_checkBox.toggled.connect(dialog.functions.show_hide_checkbox_connected_fields)
        dialog.community_control_community_service_checkBox.toggled.connect(dialog.functions.show_hide_checkbox_connected_fields)
        dialog.other_community_control_checkBox.toggled.connect(dialog.functions.show_hide_checkbox_connected_fields)
        dialog.alcohol_monitoring_checkBox.toggled.connect(dialog.functions.show_hide_checkbox_connected_fields)
        dialog.pay_restitution_checkBox.toggled.connect(dialog.functions.show_hide_checkbox_connected_fields)
        dialog.specialized_docket_checkBox.toggled.connect(dialog.functions.show_hide_checkbox_connected_fields)


class AddSpecialBondConditionsDialogSignalConnector(BaseDialogSignalConnectorOld):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_condition_dialog_main_signals(dialog)


if __name__ == "__main__":
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
