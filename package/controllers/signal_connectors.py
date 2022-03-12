"""Module that contains SignalConnector classes. SignalConnector classes are called
when a dialog is built and connect all of the interface objects (i.e. buttons,
checkboxes, etc.) to the dialog."""
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog
from db.databases import create_statute_list, create_offense_list
from loguru import logger
from package.controllers.slot_functions import BaseDialogSlotFunctions, \
    AmendChargeDialogSlotFunctions, AddChargeDialogSlotFunctions, charges_database
from package.controllers.view_modifiers import AddChargeDialogViewModifier, AmendChargeDialogViewModifier
from package.models.case_information import AmendOffenseDetails
from package.views.add_charge_dialog_ui import Ui_AddChargeDialog
from package.views.amend_charge_dialog_ui import Ui_AmendChargeDialog


class BaseDialogSignalConnector(object):
    def __init__(self, dialog):
        dialog.cancel_Button.released.connect(dialog.functions.close_event)

    def connect_main_dialog_common_signals(self, dialog):
        dialog.clear_fields_case_Button.released.connect(dialog.functions.clear_case_information_fields)
        dialog.create_entry_Button.released.connect(dialog.functions.create_entry_process)
        dialog.close_dialog_Button.released.connect(dialog.functions.close_dialog)
        dialog.add_charge_Button.released.connect(dialog.functions.start_add_charge_dialog)
        dialog.defense_counsel_waived_checkBox.toggled.connect(dialog.set_defense_counsel)

    def connect_fra_signals(self, dialog):
        dialog.fra_in_file_box.currentTextChanged.connect(dialog.set_fra_in_file)
        dialog.fra_in_court_box.currentTextChanged.connect(dialog.set_fra_in_court)

    def connect_plea_all_button_signals(self, dialog):
        dialog.guilty_all_Button.pressed.connect(dialog.set_plea_and_findings_process)
        dialog.no_contest_all_Button.pressed.connect(dialog.set_plea_and_findings_process)

    def connect_court_cost_signals(self, dialog):
        dialog.ability_to_pay_box.currentTextChanged.connect(dialog.set_pay_date)
        dialog.costs_and_fines_Button.clicked.connect(dialog.show_costs_and_fines)

    def connect_main_dialog_additional_condition_signals(self, dialog):
        dialog.license_suspension_checkBox.toggled.connect(dialog.conditions_checkbox_toggle)
        dialog.community_service_checkBox.toggled.connect(dialog.conditions_checkbox_toggle)
        dialog.other_conditions_checkBox.toggled.connect(dialog.conditions_checkbox_toggle)
        dialog.add_conditions_Button.pressed.connect(dialog.start_add_conditions_dialog)

    def connect_condition_dialog_main_signals(self, dialog):
        dialog.add_conditions_Button.pressed.connect(dialog.add_conditions)
        dialog.add_conditions_Button.released.connect(dialog.close_window)

    def connect_jail_frame_signals(self, dialog):
        dialog.report_type_box.currentTextChanged.connect(dialog.set_report_date)
        dialog.jail_sentence_execution_type_box.currentTextChanged.connect(dialog.show_report_days_notes_box)
        dialog.companion_cases_checkBox.toggled.connect(dialog.set_field_enabled)

    def connect_community_service_days_update(self, dialog):
        dialog.community_service_days_to_complete_box.currentIndexChanged.connect(
            dialog.update_community_service_due_date
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


class AmendChargeDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_statute_and_offense_boxes(dialog)
        dialog.clear_fields_Button.released.connect(dialog.functions.clear_amend_charge_fields)
        dialog.amend_charge_Button.released.connect(dialog.functions.amend_offense)


class FineOnlyDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals(dialog)
        self.connect_plea_all_button_signals(dialog)
        self.connect_fra_signals(dialog)
        self.connect_court_cost_signals(dialog)
        self.connect_main_dialog_additional_condition_signals(dialog)
        dialog.credit_for_jail_checkBox.toggled.connect(dialog.set_fines_credit_for_jail_field)


class JailCCDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals(dialog)
        self.connect_plea_all_button_signals(dialog)
        self.connect_fra_signals(dialog)
        self.connect_court_cost_signals(dialog)
        self.connect_main_dialog_additional_condition_signals(dialog)
        dialog.jail_checkBox.toggled.connect(dialog.conditions_checkbox_toggle)
        dialog.community_control_checkBox.toggled.connect(dialog.conditions_checkbox_toggle)
        dialog.impoundment_checkBox.toggled.connect(dialog.conditions_checkbox_toggle)
        dialog.victim_notification_checkBox.toggled.connect(dialog.conditions_checkbox_toggle)


class DiversionDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals(dialog)
        self.connect_plea_all_button_signals(dialog)
        self.connect_fra_signals(dialog)
        dialog.diversion_jail_imposed_checkBox.toggled.connect(dialog.show_jail_report_date_box)
        dialog.other_conditions_checkBox.toggled.connect(dialog.show_other_conditions_box)


class NotGuiltyBondDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals(dialog)
        dialog.not_guilty_all_Button.pressed.connect(dialog.set_plea_and_findings_process)
        dialog.add_special_conditions_Button.pressed.connect(dialog.start_add_special_bond_conditions_dialog)
        dialog.admin_license_suspension_checkBox.toggled.connect(dialog.conditions_checkbox_toggle)
        dialog.domestic_violence_checkBox.toggled.connect(dialog.conditions_checkbox_toggle)
        dialog.no_contact_checkBox.toggled.connect(dialog.conditions_checkbox_toggle)
        dialog.custodial_supervision_checkBox.toggled.connect(dialog.conditions_checkbox_toggle)
        dialog.other_conditions_checkBox.toggled.connect(dialog.conditions_checkbox_toggle)
        dialog.vehicle_seizure_checkBox.toggled.connect(dialog.conditions_checkbox_toggle)
        dialog.monitoring_checkBox.toggled.connect(dialog.set_field_enabled)
        dialog.specialized_docket_checkBox.toggled.connect(dialog.set_field_enabled)


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
        dialog.gps_exclusion_checkBox.toggled.connect(dialog.set_field_enabled)
        dialog.community_control_not_within_500_feet_checkBox.toggled.connect(dialog.set_field_enabled)
        dialog.community_control_no_contact_checkBox.toggled.connect(dialog.set_field_enabled)
        dialog.house_arrest_checkBox.toggled.connect(dialog.set_field_enabled)
        dialog.community_control_community_service_checkBox.toggled.connect(dialog.set_field_enabled)
        dialog.other_community_control_checkBox.toggled.connect(dialog.set_field_enabled)
        dialog.alcohol_monitoring_checkBox.toggled.connect(dialog.set_field_enabled)
        dialog.pay_restitution_checkBox.toggled.connect(dialog.set_field_enabled)


class AddSpecialBondConditionsDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_condition_dialog_main_signals(dialog)


class BaseChargeDialog(QDialog):
    @logger.catch
    def __init__(self, main_dialog, button_index=None, parent=None):
        super().__init__(parent)
        self.button_index = button_index
        self.main_dialog = main_dialog
        charges_database.open()
        self.modify_view()
        self.create_dialog_slot_functions()
        self.connect_signals_to_slots()
        self.set_statute_and_offense_choice_boxes()

    def set_statute_and_offense_choice_boxes(self):
        self.statute_choice_box.addItems(create_statute_list())
        self.offense_choice_box.addItems(create_offense_list())
        self.statute_choice_box.setCurrentText("")
        self.offense_choice_box.setCurrentText("")


class AddChargeDialog(BaseChargeDialog, Ui_AddChargeDialog):
    def __init__(self, main_dialog, parent=None):
        super().__init__(main_dialog, parent)

    def modify_view(self):
        return AddChargeDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = AddChargeDialogSlotFunctions(self)

    def connect_signals_to_slots(self):
        return AddChargeDialogSignalConnector(self)



class AmendChargeDialog(BaseChargeDialog, Ui_AmendChargeDialog):
    def __init__(self, main_dialog, parent=None):
        super().__init__(main_dialog, parent)
        self.amend_offense_details = AmendOffenseDetails()
        self.charge = self.sender().charge
        self.current_offense_name = self.sender().charge.offense
        self.original_charge_label.setText(self.current_offense_name)

    def modify_view(self):
        return AmendChargeDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = AmendChargeDialogSlotFunctions(self)

    @logger.catch
    def connect_signals_to_slots(self):
        return AmendChargeDialogSignalConnector(self)
