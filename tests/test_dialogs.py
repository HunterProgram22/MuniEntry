import pytest
from conftest import mouse_click


dialog_list = [
    (pytest.lazy_fixture("njp_dialog"), "No Jail Plea Case Information"),
    (pytest.lazy_fixture("ngb_dialog"), "Not Guilty Bond Case Information")
]

dialog_entry_list = [
    (pytest.lazy_fixture("njp_dialog"))
]


@pytest.mark.parametrize("test_input, expected", dialog_list)
def test_dialog_window_title(test_input, expected):
    assert test_input.windowTitle() == expected


@pytest.mark.parametrize("test_input", dialog_entry_list)
def test_dialog_guilty_create_entry(test_input):
    mouse_click(test_input.guilty_all_Button)
    mouse_click(test_input.create_entry_Button)
    assert test_input.entry_case_information.case_number == '21TRD09200'


@pytest.mark.parametrize("test_input", dialog_entry_list)
def test_dialog_no_contest_create_entry(test_input):
    mouse_click(test_input.no_contest_all_Button)
    mouse_click(test_input.create_entry_Button)
    assert test_input.entry_case_information.case_number == '21TRD09200'
