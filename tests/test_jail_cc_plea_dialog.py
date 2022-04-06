import pytest
from PyQt5.QtCore import QTimer
from conftest import mouse_click, enter_data


@pytest.fixture
def jcp_dialog(qtbot, main_window):
    """Jail CC Plea Dialog is jcp_dialog"""
    mouse_click(main_window.hemmeter_radioButton)
    mouse_click(main_window.arraignments_radioButton)
    mouse_click(main_window.JailCCPleaButton)
    return main_window.dialog


def test_dialog_opens(jcp_dialog):
    assert jcp_dialog.windowTitle() == "Jail Community Control Plea Case Information"


@pytest.fixture()
def jcp_multiple_charges(qtbot, main_window):
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, "Barkschat - 21TRC05611")

    def handle_dialog():
        qtbot.addWidget(main_window.dialog)
        mouse_click(main_window.dialog.close_dialog_Button)

    QTimer.singleShot(100, handle_dialog)
    mouse_click(main_window.JailCCPleaButton)
    mouse_click(main_window.dialog.guilty_all_Button)
    enter_data(main_window.dialog.fra_in_court_box, "Yes")
    return main_window.dialog


def test_create_jail_cc_plea_entry(qtbot, jcp_multiple_charges):
    enter_data(jcp_multiple_charges.case_number_lineEdit, "1")
    mouse_click(jcp_multiple_charges.create_entry_Button)
    for charge in jcp_multiple_charges.entry_case_information.charges_list:
        assert charge.plea == "Guilty"


def test_model_update_multiple_charges(qtbot, jcp_multiple_charges):
    enter_data(jcp_multiple_charges.case_number_lineEdit, "2")
    mouse_click(jcp_multiple_charges.create_entry_Button)
    charges = jcp_multiple_charges.entry_case_information.charges_list
    assert charges[0].offense == "OVI Alcohol / Drugs 3rd"
    assert charges[0].statute == "4511.19A1A***"
    assert charges[0].degree == "UCM"
    assert charges[0].plea == "Guilty"
    assert charges[1].offense == "OVI Refusal 3rd/10yr Prior 20yr"
    assert charges[1].statute == "4511.19A2***"
    assert charges[1].degree == "UCM"
    assert charges[1].plea == "Guilty"
    assert charges[2].offense == "Driving In Marked Lanes"
    assert charges[2].statute == "4511.33"
    assert charges[2].degree == "MM"
    assert charges[2].plea == "Guilty"


def test_offense_of_violence_box_checkable(qtbot, jcp_dialog):
    mouse_click(jcp_dialog.offense_of_violence_checkBox)
    assert jcp_dialog.offense_of_violence_checkBox.isChecked()
    mouse_click(jcp_dialog.offense_of_violence_checkBox)
    assert jcp_dialog.offense_of_violence_checkBox.isChecked() == False


def test_offense_of_violence_box_checked_updates_model(qtbot, jcp_multiple_charges):
    mouse_click(jcp_multiple_charges.offense_of_violence_checkBox)
    mouse_click(jcp_multiple_charges.create_entry_Button)
    assert jcp_multiple_charges.entry_case_information.offense_of_violence == True