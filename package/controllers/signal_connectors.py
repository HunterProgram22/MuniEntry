"""Module that contains SignalConnector classes. SignalConnector classes are called
when a dialog is built and connect all of the interface objects (i.e. buttons,
checkboxes, etc.) to the dialog."""
from PyQt5 import QtCore


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


class DiversionDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        dialog.diversion_jail_imposed_checkBox.toggled.connect(dialog.show_jail_report_date_box)
        dialog.other_conditions_checkBox.toggled.connect(dialog.show_other_conditions_box)
        dialog.guilty_all_Button.pressed.connect(dialog.set_plea_and_findings_process)
        dialog.fra_in_file_box.currentTextChanged.connect(dialog.set_fra_in_file)
        dialog.fra_in_court_box.currentTextChanged.connect(dialog.set_fra_in_court)
        dialog.no_contest_all_Button.pressed.connect(dialog.set_plea_and_findings_process)