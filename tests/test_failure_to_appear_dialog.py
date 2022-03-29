import pytest
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from conftest import mouse_click, enter_data


@pytest.fixture
def fta_dialog(qtbot, main_window):
    """Failure To Appear Dialog is fta_dialog"""
    mouse_click(main_window.hemmeter_radioButton)
    mouse_click(main_window.arraignments_radioButton)

    def close_dialog():
        qtbot.addWidget(main_window.dialog)
        mouse_click(main_window.dialog.close_dialog_Button)

    QTimer.singleShot(100, close_dialog)
    mouse_click(main_window.FailureToAppearButton)
    return main_window.dialog


def test_dialog_opens(fta_dialog):
    assert fta_dialog.windowTitle() == "Failure To Appear Case Information"


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
def test_all_checkbox_conditions(qtbot, fta_dialog, checkBox):
    mouse_click(getattr(fta_dialog, checkBox))
    assert getattr(fta_dialog, checkBox).isChecked()


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
def test_model_updated_if_conditions_checked(qtbot, fta_dialog, checkBox, model):
    mouse_click(fta_dialog.defense_counsel_waived_checkBox)
    mouse_click(getattr(fta_dialog, checkBox))

    def close_message():
        try:
            qtbot.addWidget(fta_dialog.message_box)
            mouse_click(fta_dialog.message_box.button(QtWidgets.QMessageBox.Ok))
        except AttributeError:
            pass

    QTimer.singleShot(100, close_message)

    mouse_click(fta_dialog.create_entry_Button)
    assert getattr(fta_dialog.entry_case_information.fta_conditions, model) == True


def test_arrest_warrant_radius_box_update_model(qtbot, fta_dialog):
    mouse_click(fta_dialog.defense_counsel_waived_checkBox)
    enter_data(fta_dialog.arrest_warrant_radius_box, "2")

    def close_message():
        try:
            qtbot.addWidget(fta_dialog.message_box)
            mouse_click(fta_dialog.message_box.button(QtWidgets.QMessageBox.Ok))
        except AttributeError:
            pass

    QTimer.singleShot(100, close_message)

    mouse_click(fta_dialog.create_entry_Button)
    assert fta_dialog.entry_case_information.fta_conditions.arrest_warrant_radius == "2 (Statewide)"


def test_set_bond_update_model(qtbot, fta_dialog):
    mouse_click(fta_dialog.defense_counsel_waived_checkBox)
    enter_data(fta_dialog.bond_type_box, "Cash or Surety Bond")
    enter_data(fta_dialog.bond_amount_box, "$5,000")

    def close_message():
        try:
            qtbot.addWidget(fta_dialog.message_box)
            mouse_click(fta_dialog.message_box.button(QtWidgets.QMessageBox.Ok))
        except AttributeError:
            pass

    QTimer.singleShot(100, close_message)
    mouse_click(fta_dialog.create_entry_Button)
    assert fta_dialog.entry_case_information.fta_conditions.bond_type == "Cash or Surety Bond"
    assert fta_dialog.entry_case_information.fta_conditions.bond_amount == "$5,000"
