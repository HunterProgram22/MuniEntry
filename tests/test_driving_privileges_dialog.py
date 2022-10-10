"""Test module for Driving Privileges Dialog UI Functionality.

Module Level Parameters - fixtures setup and imported automatically from the conftest file.
    driving_priv_dialog
"""
from tests.conftest import mouse_click


def test_dialog_opens(driving_priv_dialog):
    """Tests to see if the dialog opens when Diversion Plea is selected from Main Window."""
    assert driving_priv_dialog.windowTitle() == 'Driving Privileges Entry Case Information'


def test_other_conditions_checkbox(driving_priv_dialog):
    """Test if checking other conditions checkbox shows other conditions field."""
    mouse_click(driving_priv_dialog.other_conditions_checkBox)
    assert driving_priv_dialog.other_conditions_lineEdit.isEnabled() is True
