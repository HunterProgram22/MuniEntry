import pytest
from PyQt5.QtCore import QTimer
from tests.conftest import mouse_click


def test_dialog_opens(com_control_dialog):
    assert com_control_dialog.windowTitle() == "Community Control Terms"


all_community_control_checkbox_conditions_test_list = [
    "daily_reporting_checkBox",
    "community_control_not_within_500_feet_checkBox",
    "community_control_no_contact_checkBox",
    "house_arrest_checkBox",
    "gps_exclusion_checkBox",
    "alcohol_monitoring_checkBox",
    "interlock_vehicles_checkBox",
    "community_control_community_service_checkBox",
    "antitheft_checkBox",
    "anger_management_checkBox",
    "alcohol_evaluation_checkBox",
    "domestic_violence_program_checkBox",
    "driver_intervention_program_checkBox",
    "mental_health_evaluation_checkBox",
    "pay_restitution_checkBox",
    "other_community_control_checkBox",
    "specialized_docket_checkBox",
]

@pytest.mark.parametrize("checkBox", all_community_control_checkbox_conditions_test_list)
def test_all_checkbox_conditions(qtbot, com_control_dialog_com_control_conditions, checkBox):
    mouse_click(getattr(com_control_dialog_com_control_conditions, checkBox))
    assert getattr(com_control_dialog_com_control_conditions, checkBox).isChecked()


@pytest.mark.skip
@pytest.mark.parametrize("checkBox", all_community_control_checkbox_conditions_test_list)
def test_if_conditions_hold_if_checked_dialog_closed_then_reopened(qtbot, main_window, checkBox):
    """These tests are being skipped because they require manual interaction TODO: fix"""
    mouse_click(main_window.hemmeter_radioButton)
    mouse_click(main_window.final_pretrial_radioButton)
    mouse_click(main_window.JailCCPleaButton)
    mouse_click(main_window.dialog.community_control_checkBox)
    mouse_click(main_window.dialog.add_conditions_Button)

    def close_popup_dialog():
        mouse_click(main_window.dialog.popup_dialog.add_conditions_Button)

    qtbot.addWidget(main_window.dialog.popup_dialog)
    mouse_click(getattr(main_window.dialog.popup_dialog, checkBox))
    QTimer.singleShot(100, close_popup_dialog)
    mouse_click(main_window.dialog.popup_dialog.add_conditions_Button)
    mouse_click(main_window.dialog.add_conditions_Button)
    qtbot.addWidget(main_window.dialog.popup_dialog)
    assert getattr(main_window.dialog.popup_dialog, checkBox).isChecked()


all_conditions_checkbox_test_list = [
    ("community_control_checkBox", "community_control_frame"),
    ("community_service_checkBox", "community_service_frame"),
    ("license_suspension_checkBox", "license_suspension_frame"),
    ("victim_notification_checkBox", "victim_notification_frame"),
    ("impoundment_checkBox", "impoundment_frame"),
    ("other_conditions_checkBox", "other_conditions_frame"),
]

@pytest.mark.parametrize("checkBox, frame", all_conditions_checkbox_test_list)
def test_conditions_frames_work_when_condition_checked(qtbot, jcp_dialog, checkBox, frame):
    mouse_click(getattr(jcp_dialog, checkBox))
    mouse_click(jcp_dialog.add_conditions_Button)
    assert getattr(jcp_dialog.popup_dialog, frame).isEnabled() == True
