import pytest
from conftest import mouse_click


dialog_list = [
    (pytest.lazy_fixture("njp_dialog"), "No Jail Plea Case Information"),
    (pytest.lazy_fixture("ngb_dialog"), "Not Guilty Bond Case Information")
]

dialog_entry_list = [
    (pytest.lazy_fixture("njp_dialog")),
    (pytest.lazy_fixture("ngb_dialog"))
]


@pytest.mark.parametrize("test_input, expected", dialog_list)
def test_dialog_window_title(test_input, expected):
    assert test_input.windowTitle() == expected

#
# @pytest.mark.parametrize("test_input", dialog_entry_list)
# def test_dialog_guilty_create_entry(test_input):
#     mouse_click(test_input.guilty_all_Button)
#     mouse_click(test_input.create_entry_Button)
#     assert test_input.entry_case_information.case_number == '21TRD09200'
#
#
# @pytest.mark.parametrize("test_input", dialog_entry_list)
# def test_dialog_no_contest_create_entry(test_input):
#     mouse_click(test_input.no_contest_all_Button)
#     mouse_click(test_input.create_entry_Button)
#     assert test_input.entry_case_information.case_number == '21TRD09200'


@pytest.mark.parametrize("test_input", dialog_entry_list)
def test_offense_to_statute(test_input):
    test_input.offense_choice_box.setCurrentText("Driving Under Suspension")
    assert test_input.statute_choice_box.currentText() == "4510.11"
    assert test_input.degree_choice_box.currentText() == "M1"
    test_input.offense_choice_box.setCurrentText("Speeding > 25 mph")
    assert test_input.statute_choice_box.currentText() == "4511.21(B)(2)"
    assert test_input.degree_choice_box.currentText() == "Minor Misdemeanor"