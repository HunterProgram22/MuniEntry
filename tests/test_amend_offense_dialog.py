import pytest
from conftest import mouse_click, enter_data
from controllers.conditions_dialogs import AddConditionsDialog
from controllers.base_dialogs import AmendOffenseDialog
from PyQt5 import QtWidgets

def start_amend_offense_dialog(njp_dialog, qtbot):
    button_index = 0  # Set to 0 for first charge in list for texting
    amend_dialog = AmendOffenseDialog(njp_dialog, njp_dialog.entry_case_information, button_index)
    qtbot.addWidget(amend_dialog)
    return amend_dialog


"""TESTING"""
def test_amend_offense_title(njp_dialog, qtbot):
    mouse_click(njp_dialog.charges_gridLayout.itemAtPosition(8, 2).widget())
    amend_dialog = start_amend_offense_dialog(njp_dialog, qtbot)
    assert amend_dialog.windowTitle() == "Amend Charge"
    print(QtWidgets.QApplication.activeModalWidget())


def test_case_information_dialog(njp_dialog, qtbot):
    mouse_click(njp_dialog.charges_gridLayout.itemAtPosition(8, 2).widget())
    amend_dialog = start_amend_offense_dialog(njp_dialog, qtbot)
    assert amend_dialog.case_number_label.text() == "21TRD09200"
    assert amend_dialog.defendant_name_label.text() == "State of Ohio v. BRANDON ROWEDDA"


def test_amend_offense_granted(njp_dialog, qtbot):
    mouse_click(njp_dialog.charges_gridLayout.itemAtPosition(8, 2).widget())
    amend_dialog = start_amend_offense_dialog(njp_dialog, qtbot)
    amend_dialog.motion_decision_box.setCurrentText("Granted")
    assert amend_dialog.motion_decision_box.currentText() == "Granted"
    mouse_click(amend_dialog.amend_offense_Button)
    mouse_click(njp_dialog.guilty_all_Button)
    mouse_click(njp_dialog.create_entry_Button)


def test_amend_offense_denied(njp_dialog, qtbot):
    mouse_click(njp_dialog.charges_gridLayout.itemAtPosition(8, 2).widget())
    amend_dialog = start_amend_offense_dialog(njp_dialog, qtbot)
    amend_dialog.motion_decision_box.setCurrentText("Denied")
    assert amend_dialog.motion_decision_box.currentText() == "Denied"
    mouse_click(amend_dialog.amend_offense_Button)
    mouse_click(njp_dialog.no_contest_all_Button)
    mouse_click(njp_dialog.create_entry_Button)
