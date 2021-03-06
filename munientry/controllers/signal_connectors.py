"""Module that contains SignalConnector classes. SignalConnector classes are called
when a dialog is built and connect all of the interface objects (i.e. buttons,
checkboxes, etc.) to the dialog."""
from loguru import logger
from munientry.controllers.slot_functions import BaseDialogSlotFunctions, BondHearingDialogSlotFunctions


class BaseDialogSignalConnector:
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

    def connect_statute_and_offense_boxes(self, dialog):
        dialog.statute_choice_box.currentTextChanged.connect(
            dialog.functions.set_offense
        )
        dialog.offense_choice_box.currentTextChanged.connect(
            dialog.functions.set_statute
        )


class AddChargeDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_statute_and_offense_boxes(dialog)
        dialog.clear_fields_Button.released.connect(dialog.functions.clear_add_charge_fields)
        dialog.add_charge_Button.released.connect(dialog.functions.add_charge_process)
        dialog.freeform_entry_checkBox.toggled.connect(dialog.functions.set_freeform_entry)


class AmendChargeDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_statute_and_offense_boxes(dialog)
        dialog.clear_fields_Button.released.connect(dialog.functions.clear_amend_charge_fields)
        dialog.amend_charge_Button.released.connect(dialog.functions.amend_offense_process)
        dialog.freeform_entry_checkBox.toggled.connect(dialog.functions.set_freeform_entry)


class FineOnlyDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals(dialog)
        self.connect_plea_all_button_signals(dialog)
        self.connect_fra_signals(dialog)
        self.connect_court_cost_signals(dialog)
        self.connect_main_dialog_additional_condition_signals(dialog)
        dialog.credit_for_jail_checkBox.toggled.connect(dialog.functions.set_fines_credit_for_jail_field)


class LeapSentencingDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals(dialog)
        self.connect_plea_all_button_signals(dialog)
        self.connect_fra_signals(dialog)
        self.connect_court_cost_signals(dialog)
        self.connect_main_dialog_additional_condition_signals(dialog)
        dialog.credit_for_jail_checkBox.toggled.connect(dialog.functions.set_fines_credit_for_jail_field)


class LeapAdmissionPleaDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        """The plea all buttons are connected directly because the base dialog method also connects
        findings and a Leap Admission Plea does not have findings."""
        super().__init__(dialog)
        self.connect_main_dialog_common_signals(dialog)
        dialog.add_charge_Button.released.connect(dialog.functions.start_add_charge_dialog)
        dialog.guilty_all_Button.pressed.connect(dialog.charges_gridLayout.set_all_pleas)
        dialog.no_contest_all_Button.pressed.connect(dialog.charges_gridLayout.set_all_pleas)
        dialog.time_to_complete_box.currentTextChanged.connect(dialog.functions.set_leap_sentencing_date)


class LeapAdmissionPleaValidDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        """The plea all buttons are connected directly because the base dialog method also connects
        findings and a Leap Admission Plea does not have findings."""
        super().__init__(dialog)
        self.connect_main_dialog_common_signals(dialog)
        dialog.add_charge_Button.released.connect(dialog.functions.start_add_charge_dialog)
        dialog.guilty_all_Button.pressed.connect(dialog.charges_gridLayout.set_all_pleas)


class PleaOnlyDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals(dialog)
        self.connect_plea_all_button_signals(dialog)


class JailCCDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals(dialog)
        self.connect_plea_all_button_signals(dialog)
        self.connect_fra_signals(dialog)
        self.connect_court_cost_signals(dialog)
        self.connect_main_dialog_additional_condition_signals(dialog)
        dialog.jail_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.add_companion_cases_checkBox.toggled.connect(dialog.functions.show_companion_case_fields)
        dialog.community_control_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.impoundment_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.victim_notification_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.add_jail_report_Button.pressed.connect(dialog.functions.start_add_jail_report_dialog)


class SentencingOnlyDialogSignalConnector(JailCCDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)


class TrialSentencingDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals(dialog)
        dialog.add_charge_Button.released.connect(dialog.functions.start_add_charge_dialog)
        dialog.guilty_all_Button.pressed.connect(dialog.charges_gridLayout.set_all_trial_findings)
        dialog.not_guilty_all_Button.pressed.connect(dialog.charges_gridLayout.set_all_trial_findings)
        self.connect_fra_signals(dialog)
        self.connect_court_cost_signals(dialog)
        self.connect_main_dialog_additional_condition_signals(dialog)
        dialog.jail_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.add_companion_cases_checkBox.toggled.connect(dialog.functions.show_companion_case_fields)
        dialog.community_control_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.impoundment_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.victim_notification_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.add_jail_report_Button.pressed.connect(dialog.functions.start_add_jail_report_dialog)


class DiversionDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals(dialog)
        self.connect_plea_all_button_signals(dialog)
        self.connect_fra_signals(dialog)
        dialog.diversion_jail_imposed_checkBox.toggled.connect(dialog.functions.show_jail_report_date_box)
        dialog.pay_restitution_checkBox.toggled.connect(dialog.functions.show_restitution_boxes)
        dialog.other_conditions_checkBox.toggled.connect(dialog.functions.show_other_conditions_box)


class NotGuiltyBondDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals(dialog)
        self.connect_not_guilty_all_button(dialog)
        dialog.bond_type_box.currentTextChanged.connect(dialog.functions.show_hide_bond_conditions)
        dialog.add_charge_Button.released.connect(dialog.functions.start_add_charge_dialog)
        dialog.add_special_conditions_Button.pressed.connect(dialog.functions.start_add_special_bond_conditions_dialog)
        dialog.admin_license_suspension_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.domestic_violence_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.no_contact_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.custodial_supervision_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.other_conditions_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.vehicle_seizure_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.monitoring_checkBox.toggled.connect(dialog.functions.show_hide_checkbox_connected_fields)
        dialog.specialized_docket_checkBox.toggled.connect(dialog.functions.show_hide_checkbox_connected_fields)


class NoPleaBondDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals(dialog)
        dialog.add_special_conditions_Button.pressed.connect(dialog.functions.start_add_special_bond_conditions_dialog)
        dialog.admin_license_suspension_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.domestic_violence_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.no_contact_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.custodial_supervision_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.other_conditions_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.vehicle_seizure_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.monitoring_checkBox.toggled.connect(dialog.functions.show_hide_checkbox_connected_fields)
        dialog.specialized_docket_checkBox.toggled.connect(dialog.functions.show_hide_checkbox_connected_fields)


class BondHearingDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals(dialog)
        dialog.bond_modification_decision_box.currentTextChanged.connect(dialog.functions.show_bond_boxes)
        dialog.add_special_conditions_Button.pressed.connect(dialog.functions.start_add_special_bond_conditions_dialog)
        dialog.admin_license_suspension_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.domestic_violence_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.no_contact_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.custodial_supervision_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.other_conditions_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.vehicle_seizure_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.monitoring_checkBox.toggled.connect(dialog.functions.show_hide_checkbox_connected_fields)
        dialog.specialized_docket_checkBox.toggled.connect(dialog.functions.show_hide_checkbox_connected_fields)


class ProbationViolationBondDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals(dialog)
        dialog.bond_type_box.currentTextChanged.connect(dialog.functions.hide_bond_conditions)
        dialog.bond_type_box.currentTextChanged.connect(dialog.functions.set_if_no_bond)


class FreeformDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals(dialog)


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


class AddSpecialBondConditionsDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_condition_dialog_main_signals(dialog)


if __name__ == "__main__":
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
