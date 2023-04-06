"""Test module for Diversion Dialog UI Functionality.

Module Level Parameters - fixtures setup and imported automatically from the conftest file.
    diversion_dialog
"""
import pytest
from tests.conftest import mouse_click


def test_dialog_opens(diversion_dialog):
    """Tests to see if the dialog opens when Diversion Plea is selected from Main Window."""
    assert diversion_dialog.windowTitle() == 'Diversion Plea Case Information'


def test_jail_time_imposed_checkbox(diversion_dialog):
    """Tests to see if checking Jail Time Imposed checkbox shows Jail Report Date field."""
    mouse_click(diversion_dialog.diversion_jail_imposed_check_box)
    assert diversion_dialog.diversion_jail_report_date.isEnabled() is True


# @pytest.mark.skip('This test is failing sometimes - cannot determine why - UI works.')
def test_restitution_imposed_checkbox(diversion_dialog):
    """Tests to see if checking Restitution Imposed checkbox shows Restitution fields."""
    mouse_click(diversion_dialog.pay_restitution_check_box)
    assert diversion_dialog.pay_restitution_to_line.isHidden() is False


def test_other_conditions_checkbox(diversion_dialog):
    """Tests to see if other conditions field shows when other checkbox is checked."""
    mouse_click(diversion_dialog.other_conditions_check_box)
    assert diversion_dialog.other_conditions_check_box.isChecked() is True
    assert diversion_dialog.other_conditions_text.isHidden() is False
