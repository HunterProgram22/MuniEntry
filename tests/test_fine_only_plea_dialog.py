from datetime import date, timedelta

import pytest
from PyQt5.QtCore import QTimer
from conftest import mouse_click, enter_data

from package.controllers.helper_functions import set_future_date

TODAY = date.today()


@pytest.fixture
def fop_dialog(qtbot, main_window):
    """Fine Only Plea Dialog is fop_dialog"""
    mouse_click(main_window.hemmeter_radioButton)
    mouse_click(main_window.arraignments_radioButton)
    mouse_click(main_window.FineOnlyPleaButton)
    return main_window.dialog


def test_dialog_opens(fop_dialog):
    assert fop_dialog.windowTitle() == "Fine Only Plea Case Information"


###TEST VIEW###
all_fop_checkbox_conditions_test_list = [
    "license_suspension_checkBox",
    "community_service_checkBox",
    "other_conditions_checkBox",
]


@pytest.mark.parametrize("checkBox", all_fop_checkbox_conditions_test_list)
def test_all_checkbox_conditions(qtbot, fop_dialog, checkBox):
    mouse_click(getattr(fop_dialog, checkBox))
    assert getattr(fop_dialog, checkBox).isChecked()


def test_check_waived_counsel_disables_def_counsel_box(fop_dialog):
    assert fop_dialog.defense_counsel_name_box.isEnabled()
    assert fop_dialog.defense_counsel_type_box.isEnabled()
    mouse_click(fop_dialog.defense_counsel_waived_checkBox)
    assert fop_dialog.defense_counsel_name_box.isEnabled() == False
    assert fop_dialog.defense_counsel_type_box.isEnabled() == False


def test_court_costs_due_date(fop_dialog):
    fop_dialog.ability_to_pay_box.setCurrentText("forthwith")
    assert fop_dialog.balance_due_date.date() == TODAY
    fop_dialog.ability_to_pay_box.setCurrentText("within 30 days")
    thirty = set_future_date(30, "Tuesday")
    assert fop_dialog.balance_due_date.date() == TODAY + timedelta(days=thirty)
    fop_dialog.ability_to_pay_box.setCurrentText("within 60 days")
    sixty = set_future_date(60, "Tuesday")
    assert fop_dialog.balance_due_date.date() == TODAY + timedelta(days=sixty)
    fop_dialog.ability_to_pay_box.setCurrentText("within 90 days")
    ninety = set_future_date(90, "Tuesday")
    assert fop_dialog.balance_due_date.date() == TODAY + timedelta(days=ninety)


def test_credit_for_jail_shows_box_if_checked(fop_dialog):
    assert fop_dialog.jail_time_credit_box.isHidden()
    mouse_click(fop_dialog.credit_for_jail_checkBox)
    assert fop_dialog.jail_time_credit_box.isHidden() == False



@pytest.fixture()
def fop_multiple_charges(qtbot, main_window):
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, "Barkschat - 21TRC05611")

    def handle_dialog():
        qtbot.addWidget(main_window.dialog)
        mouse_click(main_window.dialog.close_dialog_Button)

    QTimer.singleShot(100, handle_dialog)
    mouse_click(main_window.FineOnlyPleaButton)
    mouse_click(main_window.dialog.no_contest_all_Button)
    enter_data(main_window.dialog.fra_in_court_box, "Yes")
    return main_window.dialog


def test_create_not_guilty_bond_entry(qtbot, fop_multiple_charges):
    enter_data(fop_multiple_charges.case_number_lineEdit, "1")
    mouse_click(fop_multiple_charges.create_entry_Button)
    for charge in fop_multiple_charges.entry_case_information.charges_list:
        assert charge.plea == "No Contest"


def test_model_update_multiple_charges(qtbot, fop_multiple_charges):
    enter_data(fop_multiple_charges.case_number_lineEdit, "2")
    mouse_click(fop_multiple_charges.create_entry_Button)
    charges = fop_multiple_charges.entry_case_information.charges_list
    assert charges[0].offense == "OVI Alcohol / Drugs 3rd"
    assert charges[0].statute == "4511.19A1A***"
    assert charges[0].degree == "UCM"
    assert charges[0].plea == "No Contest"
    assert charges[1].offense == "OVI Refusal 3rd/10yr Prior 20yr"
    assert charges[1].statute == "4511.19A2***"
    assert charges[1].degree == "UCM"
    assert charges[1].plea == "No Contest"
    assert charges[2].offense == "Driving In Marked Lanes"
    assert charges[2].statute == "4511.33"
    assert charges[2].degree == "MM"
    assert charges[2].plea == "No Contest"
