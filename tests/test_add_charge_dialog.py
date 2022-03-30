import pytest
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from conftest import mouse_click, enter_data


@pytest.fixture
def add_charge_dialog(qtbot, main_window):
    """Add Charge Dialog is add_charge_dialog"""
    mouse_click(main_window.hemmeter_radioButton)
    mouse_click(main_window.arraignments_radioButton)
    mouse_click(main_window.JailCCPleaButton)

    def close_popup_dialog():
        qtbot.addWidget(main_window.dialog.popup_dialog)
        mouse_click(main_window.dialog.popup_dialog.add_charge_Button)

    QTimer.singleShot(100, close_popup_dialog)
    mouse_click(main_window.dialog.add_charge_Button)
    return main_window.dialog.popup_dialog


all_add_charge_dialogs_test_list = [
    "FineOnlyPleaButton",
    "JailCCPleaButton",
    "NotGuiltyBondButton",
    "DiversionButton",
]

@pytest.mark.parametrize("test_input", all_add_charge_dialogs_test_list)
def test_add_charge_works_all_dialogs(qtbot, main_window, test_input):
    """Tests to make sure the Add Charge button opens the Add Charge Dialog for any
    Main Entry Dialog that has an Add Charge button."""
    mouse_click(main_window.hemmeter_radioButton)
    mouse_click(main_window.arraignments_radioButton)
    dialog_button = getattr(main_window, test_input)
    mouse_click(dialog_button)

    def close_popup_dialog():
        qtbot.addWidget(main_window.dialog.popup_dialog)
        mouse_click(main_window.dialog.popup_dialog.add_charge_Button)

    QTimer.singleShot(100, close_popup_dialog)
    mouse_click(main_window.dialog.add_charge_Button)
    assert main_window.dialog.popup_dialog.windowTitle() == "Add Charge"


def test_add_charge_dialog_opens(add_charge_dialog):
    assert add_charge_dialog.windowTitle() == "Add Charge"


def test_add_charge_dialog_loads_empty(add_charge_dialog):
    assert add_charge_dialog.statute_choice_box.currentText() == ""
    assert add_charge_dialog.offense_choice_box.currentText() == ""
    assert add_charge_dialog.degree_choice_box.currentText() == ""


def test_if_checking_freeform_clears_fields(add_charge_dialog):
    enter_data(add_charge_dialog.offense_choice_box, "A")
    mouse_click(add_charge_dialog.freeform_entry_checkBox)
    assert add_charge_dialog.statute_choice_box.currentText() == ""
    assert add_charge_dialog.offense_choice_box.currentText() == ""
    assert add_charge_dialog.degree_choice_box.currentText() == ""


def test_if_clear_field_button_clears(add_charge_dialog):
    enter_data(add_charge_dialog.offense_choice_box, "A")
    mouse_click(add_charge_dialog.clear_fields_Button)
    assert add_charge_dialog.statute_choice_box.currentText() == ""
    assert add_charge_dialog.offense_choice_box.currentText() == ""
    assert add_charge_dialog.degree_choice_box.currentText() == ""


def test_if_checking_freeform_makes_editable(add_charge_dialog):
    mouse_click(add_charge_dialog.freeform_entry_checkBox)
    assert add_charge_dialog.statute_choice_box.isEditable()
    assert add_charge_dialog.offense_choice_box.isEditable()


def test_if_checking_freeform_twice_makes_uneditable(add_charge_dialog):
    mouse_click(add_charge_dialog.freeform_entry_checkBox)
    mouse_click(add_charge_dialog.freeform_entry_checkBox)
    assert add_charge_dialog.statute_choice_box.isEditable() == False
    assert add_charge_dialog.offense_choice_box.isEditable() == False

