"""Module for testing Add Special Bond Conditions Dialog user interface.

Module Level Parameters - fixtures setup and imported automatically from the conftest file.
    ngb_dialog
    conditions_dialog = conditions dialog with all frames enabled
"""
import pytest

from tests.conftest import mouse_click

all_conditions_checkbox_list = [
    'tow_to_residence_checkBox',
    'motion_to_return_vehicle_checkBox',
    'domestic_violence_vacate_checkBox',
    'domestic_violence_surrender_weapons_checkBox',
]


@pytest.mark.parametrize('checkbox', all_conditions_checkbox_list)
def test_all_checkbox_conditions(special_conditions_dialog, checkbox):
    """Tests to see if checking the checkbox actually results in checkbox being checked."""
    mouse_click(getattr(special_conditions_dialog, checkbox))
    assert getattr(special_conditions_dialog, checkbox).isChecked()


all_special_bond_conditions_frames = [
    ('domestic_violence_checkBox', 'domestic_violence_frame'),
    ('admin_license_suspension_checkBox', 'admin_license_suspension_frame'),
    ('custodial_supervision_checkBox', 'custodial_supervision_frame'),
    ('vehicle_seizure_checkBox', 'vehicle_seizure_frame'),
    ('no_contact_checkBox', 'no_contact_frame'),
    ('other_conditions_checkBox', 'other_conditions_frame'),
]


@pytest.mark.parametrize('checkbox, frame', all_special_bond_conditions_frames)
def test_conditions_frames_work_when_checked(ngb_dialog, checkbox, frame):
    """Tests if a condition frame is enabled on the Special Bond Conditions Dialog.

    The test checks the condition box on the main dialog (Not Guilty Plea and Bond is used) and
    then opens the secondary Special Bond Conditions Dialog to see if appropriate frame is shown.
    """
    mouse_click(getattr(ngb_dialog, checkbox))
    mouse_click(ngb_dialog.add_special_conditions_Button)
    assert getattr(ngb_dialog.popup_dialog, frame).isEnabled()
