import pytest
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from conftest import mouse_click, enter_data


@pytest.fixture
def ngb_dialog(qtbot, main_window):
    """Not Guilty Bond Dialog is ngb_dialog"""
    mouse_click(main_window.hemmeter_radioButton)
    mouse_click(main_window.arraignments_radioButton)
    mouse_click(main_window.NotGuiltyBondButton)
    return main_window.dialog


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
    assert getattr(ngb_dialog, "monitoring_type_box").currentText() == "GPS Only"


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
def test_model_updated_if_conditions_checked(qtbot, ngb_dialog, checkBox, model):
    """This is a test for the checkbox conditions of the model BondConditions."""
    mouse_click(ngb_dialog.defense_counsel_waived_checkBox)
    mouse_click(getattr(ngb_dialog, checkBox))

    def close_message():
        try:
            qtbot.addWidget(ngb_dialog.message_box)
            mouse_click(ngb_dialog.message_box.button(QtWidgets.QMessageBox.Ok))
        except AttributeError:
            pass

    QTimer.singleShot(100, close_message)
    mouse_click(ngb_dialog.create_entry_Button)
    assert getattr(ngb_dialog.entry_case_information.bond_conditions, model) == True


def test_special_conditions_model_update():
    pass


def test_create_not_guilty_bond_entry(qtbot, main_window):
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, "Barkschat - 21TRC05611")

    def handle_dialog():
        qtbot.addWidget(main_window.dialog)
        mouse_click(main_window.dialog.close_dialog_Button)

    QTimer.singleShot(150, handle_dialog)
    mouse_click(main_window.NotGuiltyBondButton)
    mouse_click(main_window.dialog.not_guilty_all_Button)
    mouse_click(main_window.dialog.create_entry_Button)
    for charge in main_window.dialog.entry_case_information.charges_list:
        assert charge.plea == "Not Guilty"



