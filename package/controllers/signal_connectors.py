"""Module that contains SignalConnector classes. SignalConnector classes are called
when a dialog is built and connect all of the interface objects (i.e. buttons,
checkboxes, etc.) to the dialog."""
from PyQt5 import QtCore
from package.controllers.base_dialogs import CriminalSlotFunctions


class BaseDialogSignalConnector(object):
    def __init__(self, dialog):
        dialog.cancel_Button.pressed.connect(dialog.close_event)
        dialog.clear_fields_case_Button.pressed.connect(
            lambda dialog=dialog: CriminalSlotFunctions.clear_case_information_fields(dialog))
        dialog.create_entry_Button.clicked.connect(
            lambda _bool, dialog=dialog: CriminalSlotFunctions.create_entry_process(_bool, dialog))
        dialog.close_dialog_Button.pressed.connect(
            lambda dialog=dialog: CriminalSlotFunctions.close_dialog(dialog))
        dialog.add_charge_Button.clicked.connect(dialog.start_add_charge_dialog)
        dialog.defense_counsel_waived_checkBox.toggled.connect(dialog.set_defense_counsel)

    def connect_fra_signals(self, dialog):
        dialog.fra_in_file_box.currentTextChanged.connect(dialog.set_fra_in_file)
        dialog.fra_in_court_box.currentTextChanged.connect(dialog.set_fra_in_court)

    def connect_plea_all_button_signals(self, dialog):
        dialog.guilty_all_Button.pressed.connect(dialog.set_plea_and_findings_process)
        dialog.no_contest_all_Button.pressed.connect(dialog.set_plea_and_findings_process)


class FineOnlyDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_fra_signals(dialog)
        self.connect_plea_all_button_signals(dialog)
        dialog.credit_for_jail_checkBox.toggled.connect(dialog.set_fines_credit_for_jail_field)


class JailCCDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_fra_signals(dialog)
        self.connect_plea_all_button_signals(dialog)
        dialog.jail_checkBox.toggled.connect(dialog.conditions_checkbox_toggle)
        dialog.community_control_checkBox.toggled.connect(dialog.conditions_checkbox_toggle)
        dialog.impoundment_checkBox.toggled.connect(dialog.conditions_checkbox_toggle)
        dialog.victim_notification_checkBox.toggled.connect(dialog.conditions_checkbox_toggle)


class DiversionDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_fra_signals(dialog)
        self.connect_plea_all_button_signals(dialog)
        dialog.diversion_jail_imposed_checkBox.toggled.connect(dialog.show_jail_report_date_box)
        dialog.other_conditions_checkBox.toggled.connect(dialog.show_other_conditions_box)


class NotGuiltyBondDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
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