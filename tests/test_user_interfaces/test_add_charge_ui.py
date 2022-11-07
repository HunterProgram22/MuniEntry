"""Module for testing Add Charge Dialog user interface."""
from tests.conftest import enter_data, mouse_click


def test_add_charge_dialog_loads_empty(add_charge_dialog):
    """Tests that when Add Charge Dialog opens all data fields are empty."""
    assert add_charge_dialog.statute_choice_box.currentText() == ''
    assert add_charge_dialog.offense_choice_box.currentText() == ''
    assert add_charge_dialog.degree_choice_box.currentText() == ''


def test_if_checking_freeform_clears_fields(add_charge_dialog):
    """Tests that checking freeform enabled checkbox clears all data fields."""
    enter_data(add_charge_dialog.offense_choice_box, 'A')
    mouse_click(add_charge_dialog.freeform_entry_checkBox)
    assert add_charge_dialog.statute_choice_box.currentText() == ''
    assert add_charge_dialog.offense_choice_box.currentText() == ''
    assert add_charge_dialog.degree_choice_box.currentText() == ''


def test_if_clear_field_button_clears(add_charge_dialog):
    """Tests that pressing clear fields buttons clears all data fields."""
    enter_data(add_charge_dialog.offense_choice_box, 'A')
    mouse_click(add_charge_dialog.clear_fields_Button)
    assert add_charge_dialog.statute_choice_box.currentText() == ''
    assert add_charge_dialog.offense_choice_box.currentText() == ''
    assert add_charge_dialog.degree_choice_box.currentText() == ''


def test_if_checking_freeform_makes_editable(add_charge_dialog):
    """Tests that checking freeform enabled sets statute and offense boxes to editable.

    Degree choice box is not editable because only specific degrees permitted.
    """
    mouse_click(add_charge_dialog.freeform_entry_checkBox)
    assert add_charge_dialog.statute_choice_box.isEditable()
    assert add_charge_dialog.offense_choice_box.isEditable()


def test_if_unchecking_freeform_makes_uneditable(add_charge_dialog):
    """Tests that unchecking freeform enabled sets statute and offense boxes to uneditable."""
    mouse_click(add_charge_dialog.freeform_entry_checkBox)
    mouse_click(add_charge_dialog.freeform_entry_checkBox)
    assert add_charge_dialog.statute_choice_box.isEditable() is False
    assert add_charge_dialog.offense_choice_box.isEditable() is False
