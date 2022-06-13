import pytest
from tests.conftest import mouse_click, enter_data, check_barkschat


@pytest.fixture
def mock_entry(sentencing_only_dialog, monkeypatch):
    def mock_create_entry():
        return "Entry Created"
    monkeypatch.setattr(sentencing_only_dialog.functions, 'create_entry', mock_create_entry)


@pytest.fixture()
def sentencing_only_dialog(qtbot, main_window):
    "Jail CC Plea Dialog = sentencing_only_dialog."
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, "Barkschat - 21TRC05611")
    mouse_click(main_window.JailCCPleaButton)
    mouse_click(main_window.dialog.guilty_all_Button)
    enter_data(main_window.dialog.fra_in_court_box, "Yes")
    return main_window.dialog


def test_dialog_opens(sentencing_only_dialog):
    assert sentencing_only_dialog.windowTitle() == "Jail Community Control Plea Case Information"


def test_create_jail_cc_plea_entry(qtbot, sentencing_only_dialog, mock_entry):
    mock_entry
    mouse_click(sentencing_only_dialog.create_entry_Button)
    for charge in sentencing_only_dialog.entry_case_information.charges_list:
        assert charge.plea == "Guilty"


def test_model_update_multiple_charges(qtbot, sentencing_only_dialog, mock_entry):
    mock_entry
    mouse_click(sentencing_only_dialog.create_entry_Button)
    charges = sentencing_only_dialog.entry_case_information.charges_list
    check_barkschat(charges, "Guilty")


def test_offense_of_violence_box_checkable(qtbot, sentencing_only_dialog):
    mouse_click(sentencing_only_dialog.offense_of_violence_checkBox)
    assert sentencing_only_dialog.offense_of_violence_checkBox.isChecked()
    mouse_click(sentencing_only_dialog.offense_of_violence_checkBox)
    assert sentencing_only_dialog.offense_of_violence_checkBox.isChecked() == False


def test_offense_of_violence_box_checked_updates_model(qtbot, sentencing_only_dialog, mock_entry):
    mock_entry
    mouse_click(sentencing_only_dialog.offense_of_violence_checkBox)
    mouse_click(sentencing_only_dialog.create_entry_Button)
    assert sentencing_only_dialog.entry_case_information.offense_of_violence == True


court_costs_test_list = [
    "Yes",
    "Waived",
    "Imposed in companion case",
    "No",
]

@pytest.mark.parametrize("costs_option", court_costs_test_list)
def test_court_costs_selected_updates_model(qtbot, sentencing_only_dialog, mock_entry, costs_option):
    mock_entry
    enter_data(sentencing_only_dialog.court_costs_box, costs_option)
    mouse_click(sentencing_only_dialog.create_entry_Button)
    assert sentencing_only_dialog.entry_case_information.court_costs.ordered == costs_option
