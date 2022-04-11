import pytest
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from tests.conftest import mouse_click, enter_data, check_barkschat


@pytest.fixture()
def ngb_dialog(qtbot, main_window):
    """Not Guilty Bond Dialog is ngb_dialog"""
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, "Barkschat - 21TRC05611")
    mouse_click(main_window.NotGuiltyBondButton)
    mouse_click(main_window.dialog.not_guilty_all_Button)
    return main_window.dialog


@pytest.fixture
def mock_entry(ngb_dialog, monkeypatch):
    def mock_create_entry():
        return "Entry Created"
    monkeypatch.setattr(ngb_dialog.functions, 'create_entry', mock_create_entry)


def test_dialog_opens(ngb_dialog):
    assert ngb_dialog.windowTitle() == "Not Guilty Bond Case Information"


###TEST VIEW###
all_ngb_bond_checkbox_conditions_test_list = [
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


@pytest.mark.parametrize("checkBox", all_ngb_bond_checkbox_conditions_test_list)
def test_all_checkbox_conditions(qtbot, ngb_dialog, checkBox):
    mouse_click(getattr(ngb_dialog, checkBox))
    assert getattr(ngb_dialog, checkBox).isChecked()


def test_monitoring_condition(qtbot, ngb_dialog):
    mouse_click(getattr(ngb_dialog, "monitoring_checkBox"))
    enter_data(getattr(ngb_dialog, "monitoring_type_box"), "G")
    assert getattr(ngb_dialog, "monitoring_type_box").isHidden() == False
    assert getattr(ngb_dialog, "monitoring_type_box").currentText() == "GPS"


def test_specialized_docket_condition(qtbot, ngb_dialog):
    mouse_click(getattr(ngb_dialog, "specialized_docket_checkBox"))
    enter_data(getattr(ngb_dialog, "specialized_docket_type_box"), "M")
    assert getattr(ngb_dialog, "specialized_docket_type_box").isHidden() == False
    assert getattr(ngb_dialog, "specialized_docket_type_box").currentText() == "Mission (Veteran's) Court"


###TEST MODEL###
main_ngb_bond_conditions_model_test_list = [
    ("no_alcohol_drugs_checkBox", "no_alcohol_drugs"),
    ("alcohol_drugs_assessment_checkBox", "alcohol_drugs_assessment"),
    ("mental_health_assessment_checkBox", "mental_health_assessment"),
    ("comply_protection_order_checkBox", "comply_protection_order"),
    ("monitoring_checkBox", "monitoring"),
    ("specialized_docket_checkBox", "specialized_docket"),
    ("alcohol_test_kiosk_checkBox", "alcohol_test_kiosk"),
]

@pytest.mark.parametrize("checkBox, model", main_ngb_bond_conditions_model_test_list)
def test_model_updated_if_conditions_checked(qtbot, ngb_dialog, checkBox, model, mock_entry):
    """This is a test for the checkbox conditions of the model BondConditions."""
    mock_entry
    mouse_click(ngb_dialog.defense_counsel_waived_checkBox)
    mouse_click(getattr(ngb_dialog, checkBox))
    mouse_click(ngb_dialog.create_entry_Button)
    assert getattr(ngb_dialog.entry_case_information.bond_conditions, model) == True


def test_special_conditions_model_update():
    pass


def test_create_not_guilty_bond_entry(qtbot, ngb_dialog, mock_entry):
    mock_entry
    mouse_click(ngb_dialog.create_entry_Button)
    for charge in ngb_dialog.entry_case_information.charges_list:
        assert charge.plea == "Not Guilty"


def test_model_update_multiple_charges(qtbot, ngb_dialog, mock_entry):
    mock_entry
    mouse_click(ngb_dialog.create_entry_Button)
    charges = ngb_dialog.entry_case_information.charges_list
    check_barkschat(charges, "Not Guilty")
