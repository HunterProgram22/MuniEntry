"""Module for testing Add Conditions Dialog user interface.

Module Level Parameters - fixtures setup and imported automatically from the conftest file.
    fop_dialog
    conditions_dialog = conditions dialog with all frames enabled
"""
import pytest

from tests.conftest import mouse_click

all_conditions_checkbox_list = [
    'als_terminated_checkBox',
    'remedial_driving_class_checkBox',
    'license_susp_interlock_checkBox',
]


@pytest.mark.parametrize('checkbox', all_conditions_checkbox_list)
def test_all_checkbox_conditions(conditions_dialog, checkbox):
    """Tests to see if checking the checkbox actually results in checkbox being checked."""
    mouse_click(getattr(conditions_dialog, checkbox))
    assert getattr(conditions_dialog, checkbox).isChecked()


all_conditions_checkbox_test_list = [
    ('license_suspension_checkBox', 'license_suspension_frame'),
    ('community_service_checkBox', 'community_service_frame'),
    ('other_conditions_checkBox', 'other_conditions_frame'),
]


@pytest.mark.parametrize('checkbox, frame', all_conditions_checkbox_test_list)
def test_conditions_hold_when_checked(fop_dialog, checkbox, frame):
    """Tests if a condition frame is enabled on the Community Control Dialog.

    The test checks the condition box on the main dialog (Jail CC Plea is used) and then opens
    the secondary Community Control Dialog to see if the appropriate frame is shown.
    """
    mouse_click(getattr(fop_dialog, checkbox))
    mouse_click(fop_dialog.add_conditions_Button)
    assert getattr(fop_dialog.popup_dialog, frame).isEnabled() is True
