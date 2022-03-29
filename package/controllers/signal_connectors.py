"""Module that contains SignalConnector classes. SignalConnector classes are called
when a dialog is built and connect all of the interface objects (i.e. buttons,
checkboxes, etc.) to the dialog."""
from package.controllers.slot_functions import BaseDialogSlotFunctions


class BaseDialogSignalConnector:
    def __init__(self, dialog):
        dialog.cancel_Button.released.connect(dialog.functions.close_event)

    def connect_main_dialog_common_signals(self, dialog):
        dialog.clear_fields_case_Button.released.connect(dialog.functions.clear_case_information_fields)
        dialog.create_entry_Button.released.connect(dialog.functions.create_entry_process)
        dialog.close_dialog_Button.released.connect(dialog.functions.close_dialog)
        dialog.defense_counsel_waived_checkBox.toggled.connect(dialog.functions.set_defense_counsel)

    def connect_fra_signals(self, dialog):
        dialog.fra_in_file_box.currentTextChanged.connect(dialog.functions.set_fra_in_file)
        dialog.fra_in_court_box.currentTextChanged.connect(dialog.functions.set_fra_in_court)

    def connect_plea_all_button_signals(self, dialog):
        dialog.add_charge_Button.released.connect(dialog.functions.start_add_charge_dialog)
        dialog.guilty_all_Button.pressed.connect(dialog.functions.set_plea_and_findings_process)
        dialog.no_contest_all_Button.pressed.connect(dialog.functions.set_plea_and_findings_process)

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
        dialog.companion_cases_checkBox.toggled.connect(dialog.functions.set_field_enabled)

    def connect_community_service_days_update(self, dialog):
        dialog.community_service_days_to_complete_box.currentIndexChanged.connect(
            dialog.functions.update_community_service_due_date
        )

    def connect_statute_and_offense_boxes(self, dialog):
        dialog.statute_choice_box.currentTextChanged.connect(
            lambda key, dialog=dialog: BaseDialogSlotFunctions.set_statute_and_offense(key, dialog))
        dialog.offense_choice_box.currentTextChanged.connect(
            lambda key, dialog=dialog: BaseDialogSlotFunctions.set_statute_and_offense(key, dialog))


class AddChargeDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_statute_and_offense_boxes(dialog)
        dialog.clear_fields_Button.released.connect(dialog.functions.clear_add_charge_fields)
        dialog.add_charge_Button.released.connect(dialog.functions.add_charge_process)
        # dialog.freeform_entry_checkBox.toggled.connect(dialog.functions.set_freeform_entry)


class AmendChargeDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_statute_and_offense_boxes(dialog)
        dialog.clear_fields_Button.released.connect(dialog.functions.clear_amend_charge_fields)
        dialog.amend_charge_Button.released.connect(dialog.functions.amend_offense_process)


class FineOnlyDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals(dialog)
        self.connect_plea_all_button_signals(dialog)
        self.connect_fra_signals(dialog)
        self.connect_court_cost_signals(dialog)
        self.connect_main_dialog_additional_condition_signals(dialog)
        dialog.credit_for_jail_checkBox.toggled.connect(dialog.functions.set_fines_credit_for_jail_field)


class JailCCDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals(dialog)
        self.connect_plea_all_button_signals(dialog)
        self.connect_fra_signals(dialog)
        self.connect_court_cost_signals(dialog)
        self.connect_main_dialog_additional_condition_signals(dialog)
        dialog.jail_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.community_control_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.impoundment_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.victim_notification_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)


class DiversionDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals(dialog)
        self.connect_plea_all_button_signals(dialog)
        self.connect_fra_signals(dialog)
        dialog.diversion_jail_imposed_checkBox.toggled.connect(dialog.functions.show_jail_report_date_box)
        dialog.other_conditions_checkBox.toggled.connect(dialog.functions.show_other_conditions_box)


class NotGuiltyBondDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals(dialog)
        dialog.not_guilty_all_Button.pressed.connect(dialog.functions.set_plea_and_findings_process)
        dialog.add_special_conditions_Button.pressed.connect(dialog.functions.start_add_special_bond_conditions_dialog)
        dialog.admin_license_suspension_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.domestic_violence_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.no_contact_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.custodial_supervision_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.other_conditions_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.vehicle_seizure_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.monitoring_checkBox.toggled.connect(dialog.functions.set_field_enabled)
        dialog.specialized_docket_checkBox.toggled.connect(dialog.functions.set_field_enabled)


class ProbationViolationBondDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals(dialog)
        dialog.bond_type_box.currentTextChanged.connect(dialog.functions.hide_bond_conditions)
        dialog.bond_type_box.currentTextChanged.connect(dialog.functions.set_if_no_bond)


class FailureToAppearDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals(dialog)
        dialog.arrest_warrant_checkBox.toggled.connect(dialog.functions.hide_warrant_radius)
        dialog.set_bond_checkBox.toggled.connect(dialog.functions.hide_bond_boxes)
        dialog.bond_type_box.currentTextChanged.connect(dialog.functions.set_bond_amount_box)


class AddConditionsDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_condition_dialog_main_signals(dialog)
        self.connect_community_service_days_update(dialog)


class AddJailOnlyDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_condition_dialog_main_signals(dialog)
        self.connect_jail_frame_signals(dialog)


class AddCommunityControlDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_condition_dialog_main_signals(dialog)
        self.connect_community_service_days_update(dialog)
        self.connect_jail_frame_signals(dialog)
        self.connect_community_control_dialog_specific_signals(dialog)

    def connect_community_control_dialog_specific_signals(self, dialog):
        dialog.gps_exclusion_checkBox.toggled.connect(dialog.functions.set_field_enabled)
        dialog.community_control_not_within_500_feet_checkBox.toggled.connect(dialog.functions.set_field_enabled)
        dialog.community_control_no_contact_checkBox.toggled.connect(dialog.functions.set_field_enabled)
        dialog.house_arrest_checkBox.toggled.connect(dialog.functions.set_field_enabled)
        dialog.community_control_community_service_checkBox.toggled.connect(dialog.functions.set_field_enabled)
        dialog.other_community_control_checkBox.toggled.connect(dialog.functions.set_field_enabled)
        dialog.alcohol_monitoring_checkBox.toggled.connect(dialog.functions.set_field_enabled)
        dialog.pay_restitution_checkBox.toggled.connect(dialog.functions.set_field_enabled)


class AddSpecialBondConditionsDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_condition_dialog_main_signals(dialog)
