"""Test module for creating admin entries.

Module Level Parameters - fixtures setup and imported automatically from the conftest file.
    main_window
    add_charge_dialog
"""
import pytest
from PyQt5.QtCore import QTimer

from tests.conftest import CLOSE_TIMER, enter_data, mouse_click

all_add_charge_dialogs_test_list = [
    'FineOnlyPleaButton',
    'JailCCPleaButton',
    'NotGuiltyBondButton',
    'DiversionButton',
    'PleaOnlyButton',
    'LeapSentencingButton',
    'LeapAdmissionButton',
    'LeapAdmissionValidButton',
    'TrialSentencingButton',
    'SentencingOnlyButton',
]


def close_popup_dialog(qtbot, main_window):
    qtbot.addWidget(main_window.dialog.popup_dialog)
    mouse_click(main_window.dialog.popup_dialog.add_charge_Button)


@pytest.mark.parametrize('test_input', all_add_charge_dialogs_test_list)
def test_add_charge_works_all_dialogs(qtbot, main_window, test_input):
    """Tests the Add Charge button opens the Add Charge Dialog and adds a charge.

    Test is run for all Main Entry Dialogs that have an Add Charge button.

    The column count on open is 3 and when add charge is pressed it should add 2 columns.
    """
    mouse_click(main_window.hemmeter_radioButton)
    mouse_click(main_window.arraignments_radioButton)
    dialog_button = getattr(main_window, test_input)
    mouse_click(dialog_button)


    QTimer.singleShot(CLOSE_TIMER, close_popup_dialog)
    mouse_click(main_window.dialog.add_charge_Button)
    assert main_window.dialog.popup_dialog.windowTitle() == 'Add Charge'
    assert main_window.dialog.charges_gridLayout.columnCount() == 3
    mouse_click(main_window.dialog.popup_dialog.add_charge_Button)
    assert main_window.dialog.charges_gridLayout.columnCount() == 5


def test_add_charge_dialog_opens(add_charge_dialog):
    assert add_charge_dialog.windowTitle() == 'Add Charge'


def test_add_charge_dialog_loads_empty(add_charge_dialog):
    assert add_charge_dialog.statute_choice_box.currentText() == ''
    assert add_charge_dialog.offense_choice_box.currentText() == ''
    assert add_charge_dialog.degree_choice_box.currentText() == ''


def test_if_checking_freeform_clears_fields(add_charge_dialog):
    enter_data(add_charge_dialog.offense_choice_box, 'A')
    mouse_click(add_charge_dialog.freeform_entry_checkBox)
    assert add_charge_dialog.statute_choice_box.currentText() == ''
    assert add_charge_dialog.offense_choice_box.currentText() == ''
    assert add_charge_dialog.degree_choice_box.currentText() == ''


def test_if_clear_field_button_clears(add_charge_dialog):
    enter_data(add_charge_dialog.offense_choice_box, 'A')
    mouse_click(add_charge_dialog.clear_fields_Button)
    assert add_charge_dialog.statute_choice_box.currentText() == ''
    assert add_charge_dialog.offense_choice_box.currentText() == ''
    assert add_charge_dialog.degree_choice_box.currentText() == ''


def test_if_checking_freeform_makes_editable(add_charge_dialog):
    mouse_click(add_charge_dialog.freeform_entry_checkBox)
    assert add_charge_dialog.statute_choice_box.isEditable()
    assert add_charge_dialog.offense_choice_box.isEditable()


def test_if_unchecking_freeform_makes_uneditable(add_charge_dialog):
    mouse_click(add_charge_dialog.freeform_entry_checkBox)
    mouse_click(add_charge_dialog.freeform_entry_checkBox)
    assert add_charge_dialog.statute_choice_box.isEditable() is False
    assert add_charge_dialog.offense_choice_box.isEditable() is False
