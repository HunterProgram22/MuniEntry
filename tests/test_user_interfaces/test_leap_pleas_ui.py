from datetime import date, timedelta

import pytest
from tests.conftest import mouse_click, enter_data

from munientry.helper_functions import set_future_date

TODAY = date.today()


@pytest.fixture
def leap_dialog(qtbot, main_window):
    mouse_click(main_window.mag_1_radio_btn)
    mouse_click(main_window.pleas_radio_btn)
    enter_data(main_window.pleas_cases_box, "Barkschat - 21TRC05611")
    mouse_click(main_window.LeapAdmissionButton)
    mouse_click(main_window.dialog.guilty_all_Button)
    return main_window.dialog


@pytest.fixture
def leap_valid_dialog(qtbot, main_window):
    mouse_click(main_window.mag_1_radio_btn)
    mouse_click(main_window.pleas_radio_btn)
    enter_data(main_window.pleas_cases_box, "Barkschat - 21TRC05611")
    mouse_click(main_window.LeapAdmissionValidButton)
    mouse_click(main_window.dialog.guilty_all_Button)
    return main_window.dialog


def test_leap_dialog_opens(leap_dialog):
    assert leap_dialog.windowTitle() == "LEAP Admission Plea Case Information"


def test_leap_valid_dialog_opens(leap_valid_dialog):
    assert leap_valid_dialog.windowTitle() == "LEAP Plea - Already Valid Case Information"


def test_check_waived_counsel_disables_def_counsel_box(leap_dialog):
    assert leap_dialog.defense_counsel_name_box.isEnabled()
    assert leap_dialog.defense_counsel_type_box.isEnabled()
    mouse_click(leap_dialog.defense_counsel_waived_checkBox)
    assert leap_dialog.defense_counsel_name_box.isEnabled() == False
    assert leap_dialog.defense_counsel_type_box.isEnabled() == False


def test_check_waived_counsel_disables_def_counsel_box_leap_valid(leap_valid_dialog):
    assert leap_valid_dialog.defense_counsel_name_box.isEnabled()
    assert leap_valid_dialog.defense_counsel_type_box.isEnabled()
    mouse_click(leap_valid_dialog.defense_counsel_waived_checkBox)
    assert leap_valid_dialog.defense_counsel_name_box.isEnabled() == False
    assert leap_valid_dialog.defense_counsel_type_box.isEnabled() == False


def test_sentencing_date(leap_dialog):
    date = set_future_date(120, "Monday")
    assert leap_dialog.sentencing_date.date() == TODAY + timedelta(days=date)
