"""Test module for Community Control Dialog functionality.

Module Level Parameters - fixtures setup and imported automatically from the conftest file.
    main_window
    comm_control_dialog
"""
import pytest
from PyQt6.QtCore import QTimer

from tests.conftest import CLOSE_TIMER, enter_data, mouse_click

dialogs_with_community_control = [
    'JailCCPleaButton',
    'TrialSentencingButton',
    'SentencingOnlyButton',
]


@pytest.mark.parametrize('dialog_button', dialogs_with_community_control)
def test_community_control_opens_all_dialogs(main_window, dialog_button):
    """Tests that the Community Control Dialog opens for all main Dialogs for which it is used."""
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, 'Barkschat - 21TRC05611')
    mouse_click(getattr(main_window, dialog_button))

    def close_popup_dialog():
        mouse_click(main_window.dialog.popup_dialog.add_conditions_Button)

    QTimer.singleShot(CLOSE_TIMER, close_popup_dialog)
    mouse_click(main_window.dialog.add_conditions_Button)
    assert main_window.dialog.popup_dialog.windowTitle() == 'Community Control Terms'


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
    """Tests that when a condition is checked in Community Control the condition is retained.

    This selects a condition in the Community Control Dialog, then closes the dialog by adding
    the condition then reopens it to check if the condition is still checked.

    The test is set to skip because it requires manual interaction, but if changes are made that
    affect community control it should be run.
    """
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
