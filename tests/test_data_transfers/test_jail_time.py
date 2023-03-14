import pytest
from tests.conftest import mouse_click, enter_data, check_barkschat


def test_create_jail_cc_plea_entry(jcp_dialog_jail, mock_entry):
    mouse_click(jcp_dialog_jail.create_entry_Button)
    for charge in jcp_dialog_jail.entry_case_information.charges_list:
        assert charge.plea == 'Guilty'


jail_scenarios = [
    # ('Yes', '5', 'Sentence'), # Commented out - requires manual interaction has always worked
    ('No', '5', 'Sentence'),
    # ('Yes', '5', 'Costs and Fines'), #  Same as above
    ('No', '5', 'Costs and Fines'),
]


@pytest.mark.parametrize('in_jail, jail_credit, jail_apply', jail_scenarios)
def test_jail_time_credit_box_transfers_to_model(jcp_dialog_jail, mock_entry, in_jail, jail_credit, jail_apply):
    enter_data(jcp_dialog_jail.in_jail_box, in_jail)
    enter_data(jcp_dialog_jail.jail_time_credit_box, jail_credit)
    enter_data(jcp_dialog_jail.jail_time_credit_apply_box, jail_apply)
    mouse_click(jcp_dialog_jail.create_entry_Button)
    assert jcp_dialog_jail.entry_case_information.jail_terms.days_in_jail == 5


def test_total_jail_time_imposed(jcp_dialog_jail, mock_entry):
    enter_data(jcp_dialog_jail.charges_gridLayout.itemAtPosition(9, 4).widget(), '20')
    mouse_click(jcp_dialog_jail.create_entry_Button)
    assert jcp_dialog_jail.entry_case_information.jail_terms.total_jail_days_imposed == 60


def test_total_jail_time_suspended(jcp_dialog_jail, mock_entry):
    enter_data(jcp_dialog_jail.charges_gridLayout.itemAtPosition(10, 4).widget(), '20')
    mouse_click(jcp_dialog_jail.create_entry_Button)
    assert jcp_dialog_jail.entry_case_information.jail_terms.total_jail_days_imposed == 40
    assert jcp_dialog_jail.entry_case_information.jail_terms.total_jail_days_suspended == 20


def test_companion_case_info_transfers_to_model(jcp_dialog_jail, mock_entry):
    mouse_click(jcp_dialog_jail.add_companion_cases_checkBox)
    enter_data(jcp_dialog_jail.companion_cases_box, '12TEST3456')
    mouse_click(jcp_dialog_jail.create_entry_Button)
    assert jcp_dialog_jail.entry_case_information.jail_terms.companion_cases_exist == True
    assert jcp_dialog_jail.entry_case_information.jail_terms.companion_cases_numbers == '12TEST3456'
