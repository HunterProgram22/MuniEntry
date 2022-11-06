"""Module for testing Add Community Control Dialog user interface.

Module Level Parameters - fixtures setup and imported automatically from the conftest file.
    jcp_dialog
    comm_control_dialog_com_control_conditions = community control dialog with the community
    control frame enabled
"""
import pytest

from tests.conftest import mouse_click

all_community_control_checkbox_conditions = [
    'daily_reporting_checkBox',
    'community_control_not_within_500_feet_checkBox',
    'community_control_no_contact_checkBox',
    'house_arrest_checkBox',
    'gps_exclusion_checkBox',
    'alcohol_monitoring_checkBox',
    'interlock_vehicles_checkBox',
    'community_control_community_service_checkBox',
    'antitheft_checkBox',
    'anger_management_checkBox',
    'alcohol_evaluation_checkBox',
    'domestic_violence_program_checkBox',
    'driver_intervention_program_checkBox',
    'mental_health_evaluation_checkBox',
    'pay_restitution_checkBox',
    'other_community_control_checkBox',
    'specialized_docket_checkBox',
]


@pytest.mark.parametrize('checkbox', all_community_control_checkbox_conditions)
def test_all_checkbox_conditions(com_control_dialog_com_control_conditions, checkbox):
    """Tests to see if checking the checkbox actually results in checkbox being checked."""
    mouse_click(getattr(com_control_dialog_com_control_conditions, checkbox))
    assert getattr(com_control_dialog_com_control_conditions, checkbox).isChecked()


all_conditions_checkbox_test_list = [
    ('community_control_checkBox', 'community_control_frame'),
    ('community_service_checkBox', 'community_service_frame'),
    ('license_suspension_checkBox', 'license_suspension_frame'),
    ('victim_notification_checkBox', 'victim_notification_frame'),
    ('impoundment_checkBox', 'impoundment_frame'),
    ('other_conditions_checkBox', 'other_conditions_frame'),
]


@pytest.mark.parametrize('checkbox, frame', all_conditions_checkbox_test_list)
def test_conditions_frames_work_when_checked(jcp_dialog, checkbox, frame):
    """Tests if a condition frame is enabled on the Community Control Dialog.

    The test checks the condition box on the main dialog (Jail CC Plea is used) and then opens
    the secondary Community Control Dialog to see if the appropriate frame is shown.
    """
    mouse_click(getattr(jcp_dialog, checkbox))
    mouse_click(jcp_dialog.add_conditions_Button)
    assert getattr(jcp_dialog.popup_dialog, frame).isEnabled() is True
