"""Test module for Community Control Dialog functionality.

Module Level Parameters - fixtures setup and imported automatically from the conftest file.
    main_window
    comm_control_dialog
"""
import pytest
from PyQt6.QtCore import QTimer

from tests.conftest import mouse_click, CLOSE_TIMER


def test_dialog_opens(com_control_dialog):
    assert com_control_dialog.windowTitle() == 'Community Control Terms'


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


@pytest.mark.skip('Requires manual interaction - comment out to run if needed')
@pytest.mark.parametrize('checkbox', all_community_control_checkbox_conditions)
def test_conditions_hold_if_dialog_closed_opened(qtbot, main_window, checkbox):
    mouse_click(main_window.hemmeter_radioButton)
    mouse_click(main_window.final_pretrial_radioButton)
    mouse_click(main_window.JailCCPleaButton)
    mouse_click(main_window.dialog.community_control_checkBox)
    mouse_click(main_window.dialog.add_conditions_Button)

    def close_popup_dialog():
        qtbot.addWidget(main_window.dialog.popup_dialog)
        mouse_click(main_window.dialog.popup_dialog.add_conditions_Button)

    mouse_click(getattr(main_window.dialog.popup_dialog, checkbox))
    QTimer.singleShot(CLOSE_TIMER, close_popup_dialog)
    mouse_click(main_window.dialog.popup_dialog.add_conditions_Button)
    mouse_click(main_window.dialog.add_conditions_Button)
    assert getattr(main_window.dialog.popup_dialog, checkbox).isChecked()
