import pytest
from tests.conftest import mouse_click, enter_data, check_barkschat

@pytest.fixture
def jcp_dialog(qtbot, main_window):
    mouse_click(main_window.judge_2_radio_btn)
    mouse_click(main_window.pleas_radio_btn)
    enter_data(main_window.pleas_cases_box, 'Barkschat - 21TRC05611')
    mouse_click(main_window.JailCCPleaButton)
    mouse_click(main_window.dialog.guilty_all_Button)
    enter_data(main_window.dialog.fra_in_court_box, 'Yes')
    enter_data(main_window.dialog.charges_gridLayout.itemAtPosition(9, 2).widget(), '40')
    mouse_click(main_window.dialog.jail_checkBox)
    yield main_window.dialog


def test_create_jail_cc_plea_entry(jcp_dialog, mock_entry):
    mouse_click(jcp_dialog.create_entry_Button)
    for charge in jcp_dialog.entry_case_information.charges_list:
        assert charge.plea == 'Guilty'


jail_scenarios = [
    # ('Yes', '5', 'Sentence'), # Commented out - requires manual interaction has always worked
    ('No', '5', 'Sentence'),
    # ('Yes', '5', 'Costs and Fines'), #  Same as above
    ('No', '5', 'Costs and Fines'),
]


@pytest.mark.parametrize('in_jail, jail_credit, jail_apply', jail_scenarios)
def test_jail_time_credit_box_transfers_to_model(jcp_dialog, mock_entry, in_jail, jail_credit, jail_apply):
    enter_data(jcp_dialog.in_jail_box, in_jail)
    enter_data(jcp_dialog.jail_time_credit_box, jail_credit)
    enter_data(jcp_dialog.jail_time_credit_apply_box, jail_apply)
    mouse_click(jcp_dialog.create_entry_Button)
    assert jcp_dialog.entry_case_information.jail_terms.days_in_jail == 5


def test_total_jail_time_imposed(jcp_dialog, mock_entry):
    enter_data(jcp_dialog.charges_gridLayout.itemAtPosition(9, 4).widget(), '20')
    mouse_click(jcp_dialog.create_entry_Button)
    assert jcp_dialog.entry_case_information.jail_terms.total_jail_days_imposed == 60


def test_total_jail_time_suspended(jcp_dialog, mock_entry):
    enter_data(jcp_dialog.charges_gridLayout.itemAtPosition(10, 4).widget(), '20')
    mouse_click(jcp_dialog.create_entry_Button)
    assert jcp_dialog.entry_case_information.jail_terms.total_jail_days_imposed == 40
    assert jcp_dialog.entry_case_information.jail_terms.total_jail_days_suspended == 20


def test_companion_case_info_transfers_to_model(qtbot, jcp_dialog, mock_entry):
    mouse_click(jcp_dialog.add_companion_cases_checkBox)
    enter_data(jcp_dialog.companion_cases_box, '12TEST3456')
    mouse_click(jcp_dialog.create_entry_Button)
    assert jcp_dialog.entry_case_information.jail_terms.companion_cases_exist == True
    assert jcp_dialog.entry_case_information.jail_terms.companion_cases_numbers == '12TEST3456'
