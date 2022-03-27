import pytest
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore, QtWidgets
from pytestqt.plugin import QtBot
from conftest import mouse_click, enter_data


def test_dialog_opens(qtbot, dialog):
    assert dialog.windowTitle() == "Failure To Appear Case Information"


all_fta_conditions_test_list = [
    "arrest_warrant_checkBox",
    "bond_forfeited_checkBox",
    "set_no_trial_checkBox",
    "operator_license_checkBox",
    "non_resident_license_checkBox",
    "supplemental_summons_checkBox",
    "proof_of_service_checkBox",
    "registration_block_checkBox",
]

@pytest.mark.parametrize("checkBox", all_fta_conditions_test_list)
def test_all_checkbox_conditions(qtbot, dialog, checkBox):
    mouse_click(getattr(dialog, checkBox))
    assert getattr(dialog, checkBox).isChecked()


all_fta_checkbox_conditions_model_test_list = [
    ("arrest_warrant_checkBox", "arrest_warrant"),
    ("bond_forfeited_checkBox", "bond_forfeited"),
    ("set_no_trial_checkBox", "set_no_trial"),
    ("operator_license_checkBox", "forfeit_license"),
    ("non_resident_license_checkBox", "non_resident_license"),
    ("supplemental_summons_checkBox", "supplemental_summons"),
    ("proof_of_service_checkBox", "proof_of_service"),
    ("registration_block_checkBox", "registration_block"),
    ("set_bond_checkBox", "set_bond"),
]

@pytest.mark.parametrize("checkBox, model", all_fta_checkbox_conditions_model_test_list)
def test_model_updated_if_conditions_checked(qtbot, dialog, checkBox, model):
    mouse_click(dialog.defense_counsel_waived_checkBox)
    mouse_click(getattr(dialog, checkBox))
    mouse_click(dialog.create_entry_Button)
    assert getattr(dialog.entry_case_information.fta_conditions, model) == True


def test_arrest_warrant_radius_box_update_model(qtbot, dialog):
    mouse_click(dialog.defense_counsel_waived_checkBox)
    enter_data(dialog.arrest_warrant_radius_box, "2")
    mouse_click(dialog.create_entry_Button)
    assert dialog.entry_case_information.fta_conditions.arrest_warrant_radius == "2 (Statewide)"


def test_set_bond_update_model(qtbot, dialog):
    mouse_click(dialog.defense_counsel_waived_checkBox)
    enter_data(dialog.bond_type_box, "Cash or Surety Bond")
    enter_data(dialog.bond_amount_box, "$5,000")
    mouse_click(dialog.create_entry_Button)
    assert dialog.entry_case_information.fta_conditions.bond_type == "Cash or Surety Bond"
    assert dialog.entry_case_information.fta_conditions.bond_amount == "$5,000"
