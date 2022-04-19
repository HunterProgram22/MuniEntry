from datetime import date, timedelta

import pytest
from tests.conftest import mouse_click, enter_data, check_barkschat

from package.controllers.helper_functions import set_future_date

TODAY = date.today()

@pytest.fixture
def mock_entry(fop_dialog, monkeypatch):
    def mock_create_entry():
        return "Entry Created"
    monkeypatch.setattr(fop_dialog.functions, 'create_entry', mock_create_entry)


@pytest.fixture
def fop_dialog(qtbot, main_window):
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, "Barkschat - 21TRC05611")
    mouse_click(main_window.FineOnlyPleaButton)
    mouse_click(main_window.dialog.no_contest_all_Button)
    enter_data(main_window.dialog.fra_in_court_box, "Yes")
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


def test_create_fine_only_plea_entry(qtbot, fop_dialog, mock_entry):
    mock_entry
    mouse_click(fop_dialog.create_entry_Button)
    for charge in fop_dialog.entry_case_information.charges_list:
        assert charge.plea == "No Contest"


def test_model_update_multiple_charges(qtbot, fop_dialog, mock_entry):
    mock_entry
    mouse_click(fop_dialog.create_entry_Button)
    charges = fop_dialog.entry_case_information.charges_list
    check_barkschat(charges, "No Contest")


court_costs_test_list = [
    "Yes",
    "Waived",
    "Imposed in companion case",
    "No",
]

@pytest.mark.parametrize("costs_option", court_costs_test_list)
def test_court_costs_selected_updates_model(qtbot, fop_dialog, mock_entry, costs_option):
    mock_entry
    enter_data(fop_dialog.court_costs_box, costs_option)
    mouse_click(fop_dialog.create_entry_Button)
    assert fop_dialog.entry_case_information.court_costs.ordered == costs_option
