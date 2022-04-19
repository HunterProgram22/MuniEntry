import pytest
from tests.conftest import mouse_click, enter_data, check_barkschat

@pytest.fixture
def mock_entry(jcp_dialog, monkeypatch):
    def mock_create_entry():
        return "Entry Created"
    monkeypatch.setattr(jcp_dialog.functions, 'create_entry', mock_create_entry)


@pytest.fixture()
def jcp_dialog_case(qtbot, main_window):
    "Jail CC Plea Dialog = jcp_dialog."
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, "Barkschat - 21TRC05611")
    mouse_click(main_window.JailCCPleaButton)
    return main_window.dialog


@pytest.fixture()
def jcp_dialog_no_case(qtbot, main_window):
    "Jail CC Plea Dialog = jcp_dialog."
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.pleas_radioButton)
    mouse_click(main_window.JailCCPleaButton)
    return main_window.dialog


def test_cms_no_charge_loader(qtbot, jcp_dialog_no_case):
    assert jcp_dialog_no_case.windowTitle() == "Jail Community Control Plea Case Information"
    assert jcp_dialog_no_case.case_number_lineEdit.text() == ""


def test_cms_charge_loader(qtbot, jcp_dialog_case):
    assert jcp_dialog_case.windowTitle() == "Jail Community Control Plea Case Information"
    assert jcp_dialog_case.case_number_lineEdit.text() == "21TRC05611"
    assert jcp_dialog_case.charges_gridLayout.itemAtPosition(0, 2).widget().text() == "OVI Alcohol / Drugs 3rd"
