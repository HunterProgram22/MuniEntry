import pytest
from tests.old_tests.conftest import mouse_click, enter_data




all_dialogs_nocase_list = [
    (pytest.lazy_fixture("njp_dialog_nocase")),
    (pytest.lazy_fixture("ngb_dialog_nocase")),
    (pytest.lazy_fixture("jail_dialog_nocase")),
    (pytest.lazy_fixture("diversion_dialog_nocase")),
]

dialog_all_plea_entry_list = [
    (pytest.lazy_fixture("njp_dialog")),
    (pytest.lazy_fixture("ngb_dialog")),
    (pytest.lazy_fixture("jail_dialog")),
    (pytest.lazy_fixture("diversion_dialog")),
]

dialog_guilty_plea_entry_list = [
    (pytest.lazy_fixture("njp_dialog")),
    (pytest.lazy_fixture("jail_dialog")),
    (pytest.lazy_fixture("diversion_dialog")),
]

dialog_no_contest_plea_entry_list = [
    (pytest.lazy_fixture("njp_dialog")),
    (pytest.lazy_fixture("jail_dialog")),
    (pytest.lazy_fixture("diversion_dialog")),
]


@pytest.mark.parametrize("test_input, expected", dialog_all_title_list)
def test_dialog_window_title(test_input, expected):
    assert test_input.windowTitle() == expected


@pytest.mark.parametrize("test_input", dialog_guilty_plea_entry_list)
def test_dialog_guilty_create_entry(test_input):
    mouse_click(test_input.defense_counsel_waived_checkBox)
    mouse_click(test_input.guilty_all_Button)
    mouse_click(test_input.create_entry_Button)
    mouse_click(test_input.close_dialog_Button)
    assert test_input.entry_case_information.case_number == '21TRD09200'


@pytest.mark.parametrize("test_input", dialog_no_contest_plea_entry_list)
def test_dialog_no_contest_create_entry(test_input):
    mouse_click(test_input.defense_counsel_waived_checkBox)
    mouse_click(test_input.no_contest_all_Button)
    mouse_click(test_input.create_entry_Button)
    assert test_input.entry_case_information.case_number == '21TRD09200'

# TODO: Update to new add charge process
# @pytest.mark.parametrize("test_input", dialog_all_plea_entry_list)
# def test_offense_to_statute(test_input):
#     mouse_click(test_input.add_charge_Button)
#     # dialog = AddChargeDialog()
#     # qtbot.addWidget(dialog)
#     test_input.offense_choice_box.setCurrentText("Driving Under Suspension")
#     assert test_input.statute_choice_box.currentText() == "4510.11"
#     assert test_input.degree_choice_box.currentText() == "M1"
#     test_input.offense_choice_box.setCurrentText("Speeding > 25 mph")
#     assert test_input.statute_choice_box.currentText() == "4511.21(B)(2)"
#     assert test_input.degree_choice_box.currentText() == "Minor Misdemeanor"


@pytest.mark.parametrize("test_input", all_dialogs_nocase_list)
def test_case_information_dialog(test_input):
    enter_data(test_input.case_number_lineEdit, "21TRC1234")
    enter_data(test_input.defendant_first_name_lineEdit, "John")
    enter_data(test_input.defendant_last_name_lineEdit, "Smith")
    assert test_input.case_number_lineEdit.text() == "21TRC1234"
    assert test_input.defendant_first_name_lineEdit.text() == "John"
    assert test_input.defendant_last_name_lineEdit.text() == "Smith"
    test_input.update_entry_case_information()
    assert test_input.entry_case_information.case_number == "21TRC1234"
    assert test_input.entry_case_information.defendant.first_name == "John"
    assert test_input.entry_case_information.defendant.last_name == "Smith"