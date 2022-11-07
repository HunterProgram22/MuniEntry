"""Test module for creating scheduling entries.

Module Level Parameters - fixtures setup and imported automatically from the conftest file.
    main_window
"""
import pytest

from tests.conftest import enter_data, mouse_click

scheduling_tab_entries = [
    ('hemmeter_final_jury_hearingButton', 'hemmeter_final_test'),
    ('rohrer_final_jury_hearingButton', 'rohrer_final_test'),
    ('hemmeter_general_hearingButton', 'hemmeter_general_test'),
    ('rohrer_general_hearingButton', 'rohrer_general_test'),
    ('hemmeter_trial_court_hearingButton', 'hemmeter_ttc_test'),
    ('rohrer_trial_court_hearingButton', 'rohrer_ttc_test'),
    ('rohrer_schedulingEntryButton', 'rohrer_sched_entry_test'),
    ('hemmeter_schedulingEntryButton', 'hemmeter_sched_entry_test'),
]


@pytest.mark.parametrize('dialog_button, test_name', scheduling_tab_entries)
def test_all_entry_buttons_with_case(main_window, dialog_button, test_name):
    """Tests the creation of all scheduling entries, no data modified before creation."""
    mouse_click(main_window.dattilo_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, 'Barkschat - 21TRC05611')
    mouse_click(getattr(main_window, dialog_button))
    enter_data(main_window.dialog.case_number_lineEdit, test_name)

    # Create and Open Word Document - Passes even if no entry is opened b/c it checks data
    mouse_click(main_window.dialog.create_entry_Button)
    assert main_window.dialog.entry_case_information.case_number == f'21TRC05611{test_name}'