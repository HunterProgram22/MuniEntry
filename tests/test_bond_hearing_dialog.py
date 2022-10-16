import pytest
from PyQt6 import QtWidgets
from PyQt6.QtCore import QTimer
from tests.conftest import mouse_click, enter_data, check_barkschat


@pytest.fixture()
def bhd_dialog(qtbot, main_window):
    """Not Guilty Bond Dialog is ngb_dialog"""
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, "Barkschat - 21TRC05611")
    mouse_click(main_window.BondHearingButton)
    return main_window.dialog


@pytest.fixture
def mock_entry(bhd_dialog, monkeypatch):
    def mock_create_entry():
        return "Entry Created"
    monkeypatch.setattr(bhd_dialog.functions, 'create_entry', mock_create_entry)


def test_dialog_opens(bhd_dialog):
    assert bhd_dialog.windowTitle() == "Bond Hearing Case Information"


###TEST VIEW###
all_bhd_bond_checkbox_conditions_test_list = [
    "no_alcohol_drugs_checkBox",
    "alcohol_drugs_assessment_checkBox",
    "mental_health_assessment_checkBox",
    "comply_protection_order_checkBox",
    "monitoring_checkBox",
    "specialized_docket_checkBox",
    "alcohol_test_kiosk_checkBox",
    "domestic_violence_checkBox",
    "admin_license_suspension_checkBox",
    "custodial_supervision_checkBox",
    "vehicle_seizure_checkBox",
    "no_contact_checkBox",
    "other_conditions_checkBox",
]


@pytest.mark.parametrize("checkBox", all_bhd_bond_checkbox_conditions_test_list)
def test_all_checkbox_conditions(qtbot, bhd_dialog, checkBox):
    mouse_click(getattr(bhd_dialog, checkBox))
    assert getattr(bhd_dialog, checkBox).isChecked()


def test_monitoring_condition(qtbot, bhd_dialog):
    mouse_click(getattr(bhd_dialog, "monitoring_checkBox"))
    enter_data(getattr(bhd_dialog, "monitoring_type_box"), "G")
    assert getattr(bhd_dialog, "monitoring_type_box").isHidden() == False
    assert getattr(bhd_dialog, "monitoring_type_box").currentText() == "GPS"


def test_specialized_docket_condition(qtbot, bhd_dialog):
    mouse_click(getattr(bhd_dialog, "specialized_docket_checkBox"))
    enter_data(getattr(bhd_dialog, "specialized_docket_type_box"), "M")
    assert getattr(bhd_dialog, "specialized_docket_type_box").isHidden() == False
    assert getattr(bhd_dialog, "specialized_docket_type_box").currentText() == "Mission (Veteran's) Court"


###TEST MODEL###
main_bhd_bond_conditions_model_test_list = [
    ("no_alcohol_drugs_checkBox", "no_alcohol_drugs"),
    ("alcohol_drugs_assessment_checkBox", "alcohol_drugs_assessment"),
    ("mental_health_assessment_checkBox", "mental_health_assessment"),
    ("comply_protection_order_checkBox", "comply_protection_order"),
    ("monitoring_checkBox", "monitoring"),
    ("specialized_docket_checkBox", "specialized_docket"),
    ("alcohol_test_kiosk_checkBox", "alcohol_test_kiosk"),
]

@pytest.mark.parametrize("checkBox, model", main_bhd_bond_conditions_model_test_list)
def test_model_updated_if_conditions_checked(qtbot, bhd_dialog, checkBox, model, mock_entry):
    """This is a test for the checkbox conditions of the model BondConditions."""
    mock_entry
    mouse_click(bhd_dialog.defense_counsel_waived_checkBox)
    mouse_click(getattr(bhd_dialog, checkBox))
    bhd_dialog.bond_modification_decision_box.setCurrentText("request to modify bond is granted")
    mouse_click(bhd_dialog.create_entry_Button)
    assert getattr(bhd_dialog.entry_case_information.bond_conditions, model) == True


def test_special_conditions_model_update():
    pass


def test_create_bond_hearing_entry(qtbot, bhd_dialog, mock_entry):
    mock_entry
    bhd_dialog.bond_modification_decision_box.setCurrentText("request to modify bond is granted")
    mouse_click(bhd_dialog.create_entry_Button)
    assert bhd_dialog.entry_case_information.bond_conditions.bond_type == "Recognizance (OR) Bond"


main_bhd_bond_decisions_model_test_list = [
    ("request to modify bond is granted", "bond modification hearing"),
    ("request to modify bond is denied", "bond modification hearing"),
    ("request to revoke bond is granted", "bond revocation hearing"),
    ("request to revoke bond is denied", "bond revocation hearing"),
]

@pytest.mark.parametrize("bond_decision, appearance_reason", main_bhd_bond_decisions_model_test_list)
def test_model_updated_for_bond_decision(qtbot, bhd_dialog, bond_decision, appearance_reason, mock_entry):
    mock_entry
    enter_data(bhd_dialog.appearance_reason_box, appearance_reason)
    bhd_dialog.bond_modification_decision_box.setCurrentText(bond_decision)
    mouse_click(bhd_dialog.create_entry_Button)
    assert bhd_dialog.entry_case_information.bond_conditions.bond_modification_decision == bond_decision
