"""Test module for Diversion Dialog UI Functionality.

Module Level Parameters - fixtures setup and imported automatically from the conftest file.
    diversion_dialog
"""
from tests.conftest import mouse_click


def test_dialog_opens(diversion_dialog):
    """Tests to see if the dialog opens when Diversion Plea is selected from Main Window."""
    assert diversion_dialog.windowTitle() == 'Diversion Plea Case Information'


def test_jail_time_imposed_checkbox(diversion_dialog):
    """Tests to see if checking Jail Time Imposed checkbox shows Jail Report Date field."""
    mouse_click(diversion_dialog.diversion_jail_imposed_checkBox)
    assert diversion_dialog.diversion_jail_report_date_box.isHidden() is False
    assert diversion_dialog.diversion_jail_report_date_box.isEnabled() is True
