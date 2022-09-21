from datetime import date, timedelta

import pytest
from tests.conftest import mouse_click, enter_data, check_barkschat

from munientry.controllers.helper_functions import set_future_date

TODAY = date.today()

@pytest.fixture
def mock_entry(leap_dialog, monkeypatch):
    def mock_create_entry():
        return "Entry Created"
    monkeypatch.setattr(leap_dialog.functions, 'create_entry', mock_create_entry)


@pytest.fixture
def leap_dialog(qtbot, main_window):
    mouse_click(main_window.bunner_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, "Barkschat - 21TRC05611")
    mouse_click(main_window.LeapAdmissionButton)
    mouse_click(main_window.dialog.guilty_all_Button)
    return main_window.dialog


@pytest.fixture
def leap_valid_dialog(qtbot, main_window):
    mouse_click(main_window.bunner_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, "Barkschat - 21TRC05611")
    mouse_click(main_window.LeapAdmissionValidButton)
    mouse_click(main_window.dialog.guilty_all_Button)
    return main_window.dialog


def test_leap_dialog_opens(leap_dialog):
    assert leap_dialog.windowTitle() == "LEAP Admission Plea Case Information"

def test_leap_valid_dialog_opens(leap_valid_dialog):
    assert leap_valid_dialog.windowTitle() == "LEAP Plea - Already Valid Case Information"

# leap_dialogs_test_list = [
#     'leap_dialog',
#     'leap_valid_dialog',
# ]
#
# @pytest.mark.parametrize('dialog', leap_dialogs_test_list)
# def test_check_waived_counsel_disables_def_counsel_box(qtbot, dialog):
#     assert dialog.defense_counsel_name_box.isEnabled()
#     assert dialog.defense_counsel_type_box.isEnabled()
#     mouse_click(dialog.defense_counsel_waived_checkBox)
#     assert dialog.defense_counsel_name_box.isEnabled() == False
#     assert dialog.defense_counsel_type_box.isEnabled() == False
