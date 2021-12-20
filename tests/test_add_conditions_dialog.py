import pytest
from conftest import mouse_click, enter_data
from controllers.conditions_dialogs import AddConditionsDialog, AmendOffenseDialog
from datetime import date, timedelta


TODAY = date.today()

def start_add_conditions_dialog(njp_dialog, qtbot):
    mouse_click(njp_dialog.add_conditions_Button)
    add_conditions = AddConditionsDialog(njp_dialog)
    qtbot.addWidget(add_conditions)
    return add_conditions


def test_add_conditions(njp_dialog, qtbot):
    add_conditions = start_add_conditions_dialog(njp_dialog, qtbot)
    assert add_conditions.windowTitle() == "Additional Conditions"


def test_license_suspension_conditions_checked(njp_dialog, qtbot):
    mouse_click(njp_dialog.license_suspension_checkBox)
    add_conditions = start_add_conditions_dialog(njp_dialog, qtbot)
    assert add_conditions.license_suspension_frame.isEnabled() == True


def test_license_suspension_conditions_unchecked(njp_dialog, qtbot):
    add_conditions = start_add_conditions_dialog(njp_dialog, qtbot)
    assert add_conditions.license_suspension_frame.isEnabled() == False


def test_community_service_conditions_checked(njp_dialog, qtbot):
    mouse_click(njp_dialog.community_service_checkBox)
    add_conditions = start_add_conditions_dialog(njp_dialog, qtbot)
    assert add_conditions.community_service_frame.isEnabled() == True


def test_community_service_conditions_unchecked(njp_dialog, qtbot):
    add_conditions = start_add_conditions_dialog(njp_dialog, qtbot)
    assert add_conditions.community_service_frame.isEnabled() == False


def test_other_conditions_checked(njp_dialog, qtbot):
    mouse_click(njp_dialog.other_conditions_checkBox)
    add_conditions = start_add_conditions_dialog(njp_dialog, qtbot)
    assert add_conditions.other_conditions_frame.isEnabled() == True


def test_other_conditions_unchecked(njp_dialog, qtbot):
    add_conditions = start_add_conditions_dialog(njp_dialog, qtbot)
    assert add_conditions.other_conditions_frame.isEnabled() == False
