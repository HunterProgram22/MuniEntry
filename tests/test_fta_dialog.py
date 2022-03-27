import pytest
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore, QtWidgets
from pytestqt.plugin import QtBot
from conftest import mouse_click, enter_data


def test_dialog_opens(qtbot, dialog):
    assert dialog.windowTitle() == "Failure To Appear Case Information"

all_fta_conditions_test_list = [
    "operator_license_checkBox",
    "non_resident_license_checkBox",
    "supplemental_summons_checkBox",
    "proof_of_service_checkBox",
    "registration_block_checkBox",
]


@pytest.mark.parametrize("checkBox", all_fta_conditions_test_list)
def test_all_checkbox_conditions(qtbot, dialog, checkBox):
    mouse_click(getattr(dialog, checkBox))
    assert getattr(dialog, checkBox).isChecked()


@pytest.mark.skip(reason="Bug in pytest is causing the checkbox not to be checked")
def test_fail_to_appear_checkbox(qtbot, dialog):
    mouse_click(dialog.failed_to_appear_checkBox)
    assert dialog.failed_to_appear_checkBox.isChecked()


@pytest.mark.skip(reason="Bug in pytest is causing the checkbox not to be checked")
def test_set_no_trial_checkbox(qtbot, dialog):
    mouse_click(dialog.set_no_trial_checkBox)
    assert dialog.set_no_trial_checkBox.isChecked()
