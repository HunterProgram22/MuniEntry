import pytest
from PyQt5.QtCore import QTimer
from tests.conftest import mouse_click


@pytest.fixture
def com_control_dialog(qtbot, main_window):
    """Add Community Control is comcontrol_dialog. Uses the Jail Dialog
    as the main dialog because that is required."""
    mouse_click(main_window.hemmeter_radioButton)
    mouse_click(main_window.final_pretrial_radioButton)
    mouse_click(main_window.JailCCPleaButton)

    def close_popup_dialog():
        qtbot.addWidget(main_window.dialog.popup_dialog)
        mouse_click(main_window.dialog.popup_dialog.add_conditions_Button)

    QTimer.singleShot(50, close_popup_dialog)
    mouse_click(main_window.dialog.add_conditions_Button)
    return main_window.dialog.popup_dialog


@pytest.fixture
def com_control_dialog_com_control_conditions(qtbot, main_window):
    """Add Community Control is comcontrol_dialog. Uses the Jail Dialog
    as the main dialog because that is required."""
    mouse_click(main_window.hemmeter_radioButton)
    mouse_click(main_window.final_pretrial_radioButton)
    mouse_click(main_window.JailCCPleaButton)
    mouse_click(main_window.dialog.community_control_checkBox)

    def close_popup_dialog():
        qtbot.addWidget(main_window.dialog.popup_dialog)
        mouse_click(main_window.dialog.popup_dialog.add_conditions_Button)

    QTimer.singleShot(50, close_popup_dialog)
    mouse_click(main_window.dialog.add_conditions_Button)
    return main_window.dialog.popup_dialog


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


@pytest.mark.manual
@pytest.mark.parametrize("checkBox", all_community_control_checkbox_conditions_test_list)
def test_if_conditions_hold_if_checked_dialog_closed_then_reopened(qtbot, main_window, checkBox):
    mouse_click(main_window.hemmeter_radioButton)
    mouse_click(main_window.final_pretrial_radioButton)
    mouse_click(main_window.JailCCPleaButton)
    mouse_click(main_window.dialog.community_control_checkBox)
    mouse_click(main_window.dialog.add_conditions_Button)

    def close_popup_dialog():
        qtbot.addWidget(main_window.dialog.popup_dialog)
        mouse_click(main_window.dialog.popup_dialog.cancel_Button)


    qtbot.addWidget(main_window.dialog.popup_dialog)
    mouse_click(getattr(main_window.dialog.popup_dialog, checkBox))
    mouse_click(main_window.dialog.popup_dialog.add_conditions_Button)
    QTimer.singleShot(100, close_popup_dialog)
    mouse_click(main_window.dialog.add_conditions_Button)
    assert getattr(main_window.dialog.popup_dialog, checkBox).isChecked()