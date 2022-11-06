"""Module for testing Amend Charge Dialog user interface."""
from tests.conftest import enter_data, mouse_click


def test_amend_charge_dialog_loads_empty(amend_charge_dialog):
    """Tests that when Add Charge Dialog opens all data fields are empty."""
    assert amend_charge_dialog.statute_choice_box.currentText() == ''
    assert amend_charge_dialog.offense_choice_box.currentText() == ''
    assert amend_charge_dialog.degree_choice_box.currentText() == ''


def test_if_checking_freeform_clears_fields(amend_charge_dialog):
    """Tests that checking freeform enabled checkbox clears all data fields."""
    enter_data(amend_charge_dialog.offense_choice_box, 'A')
    mouse_click(amend_charge_dialog.freeform_entry_checkBox)
    assert amend_charge_dialog.statute_choice_box.currentText() == ''
    assert amend_charge_dialog.offense_choice_box.currentText() == ''
    assert amend_charge_dialog.degree_choice_box.currentText() == ''


def test_if_clear_field_button_clears(amend_charge_dialog):
    """Tests that pressing clear fields buttons clears all data fields."""
    enter_data(amend_charge_dialog.offense_choice_box, 'A')
    mouse_click(amend_charge_dialog.clear_fields_Button)
    assert amend_charge_dialog.statute_choice_box.currentText() == ''
    assert amend_charge_dialog.offense_choice_box.currentText() == ''
    assert amend_charge_dialog.degree_choice_box.currentText() == ''


def test_if_checking_freeform_makes_editable(amend_charge_dialog):
    """Tests that checking freeform enabled sets statute and offense boxes to editable.

    Degree choice box is not editable because only specific degrees permitted.
    """
    mouse_click(amend_charge_dialog.freeform_entry_checkBox)
    assert amend_charge_dialog.statute_choice_box.isEditable() is True
    assert amend_charge_dialog.offense_choice_box.isEditable() is True


def test_if_unchecking_freeform_uneditable(amend_charge_dialog):
    """Tests that unchecking freeform enabled sets statute and offense boxes to uneditable."""
    mouse_click(amend_charge_dialog.freeform_entry_checkBox)
    mouse_click(amend_charge_dialog.freeform_entry_checkBox)
    assert amend_charge_dialog.statute_choice_box.isEditable() is False
    assert amend_charge_dialog.offense_choice_box.isEditable() is False
