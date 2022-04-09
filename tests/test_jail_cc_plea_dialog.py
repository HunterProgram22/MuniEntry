import pytest
from tests.conftest import mouse_click, enter_data, check_barkschat


@pytest.fixture
def mock_entry(jcp_dialog, monkeypatch):
    def mock_create_entry():
        return "Entry Created"
    monkeypatch.setattr(jcp_dialog.functions, 'create_entry', mock_create_entry)


@pytest.fixture()
def jcp_dialog(qtbot, main_window):
    "Jail CC Plea Dialog = jcp_dialog."
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, "Barkschat - 21TRC05611")
    mouse_click(main_window.JailCCPleaButton)
    mouse_click(main_window.dialog.guilty_all_Button)
    enter_data(main_window.dialog.fra_in_court_box, "Yes")
    return main_window.dialog


def test_dialog_opens(jcp_dialog):
    assert jcp_dialog.windowTitle() == "Jail Community Control Plea Case Information"


def test_create_jail_cc_plea_entry(qtbot, jcp_dialog, mock_entry):
    mock_entry
    enter_data(jcp_dialog.case_number_lineEdit, "1")
    mouse_click(jcp_dialog.create_entry_Button)
    for charge in jcp_dialog.entry_case_information.charges_list:
        assert charge.plea == "Guilty"


def test_model_update_multiple_charges(qtbot, jcp_dialog, mock_entry):
    mock_entry
    enter_data(jcp_dialog.case_number_lineEdit, "2")
    mouse_click(jcp_dialog.create_entry_Button)
    charges = jcp_dialog.entry_case_information.charges_list
    check_barkschat(charges, "Guilty")


def test_offense_of_violence_box_checkable(qtbot, jcp_dialog):
    mouse_click(jcp_dialog.offense_of_violence_checkBox)
    assert jcp_dialog.offense_of_violence_checkBox.isChecked()
    mouse_click(jcp_dialog.offense_of_violence_checkBox)
    assert jcp_dialog.offense_of_violence_checkBox.isChecked() == False


def test_offense_of_violence_box_checked_updates_model(qtbot, jcp_dialog, mock_entry):
    mock_entry
    mouse_click(jcp_dialog.offense_of_violence_checkBox)
    mouse_click(jcp_dialog.create_entry_Button)
    assert jcp_dialog.entry_case_information.offense_of_violence == True


court_costs_test_list = [
    "Yes",
    "Waived",
    "Imposed in companion case",
    "No",
]

@pytest.mark.parametrize("costs_option", court_costs_test_list)
def test_court_costs_selected_updates_model(qtbot, jcp_dialog, mock_entry, costs_option):
    mock_entry
    enter_data(jcp_dialog.court_costs_box, costs_option)
    mouse_click(jcp_dialog.create_entry_Button)
    assert jcp_dialog.entry_case_information.court_costs.ordered == costs_option


