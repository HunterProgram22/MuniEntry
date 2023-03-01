"""Test module for creating scheduling entries.

Module Level Parameters - fixtures setup and imported automatically from the conftest file.
    main_window
"""
import pytest

from tests.conftest import enter_data, mouse_click, MUNI10_SAVE_PATH
from munientry.entrycreators.entry_creator import SchedulingEntryCreator

scheduling_tab_entries = [
    ('hemmeter_final_jury_hearingButton', 'hemmeter_final_test', 'final_pretrial_dateEdit'),
    ('rohrer_final_jury_hearingButton', 'rohrer_final_test', 'final_pretrial_dateEdit'),
    ('hemmeter_general_hearingButton', 'hemmeter_general_test', 'hearing_dateEdit'),
    ('rohrer_general_hearingButton', 'rohrer_general_test', 'hearing_dateEdit'),
    ('hemmeter_trial_court_hearingButton', 'hemmeter_ttc_test', 'trial_dateEdit'),
    ('rohrer_trial_court_hearingButton', 'rohrer_ttc_test', 'trial_dateEdit'),
    ('rohrer_schedulingEntryButton', 'rohrer_sched_entry_test', 'trial_dateEdit'),
    ('hemmeter_schedulingEntryButton', 'hemmeter_sched_entry_test', 'trial_dateEdit'),
]


@pytest.mark.parametrize('dialog_button, test_name, date_field', scheduling_tab_entries)
def test_all_entry_buttons_with_case(monkeypatch, main_window, dialog_button, test_name, date_field):
    """Tests the creation of all scheduling entries."""
    data = SchedulingEntryCreator
    monkeypatch.setattr(data, 'save_path', MUNI10_SAVE_PATH)
    mouse_click(main_window.dattilo_radioButton)
    main_window.search_tabWidget.setCurrentWidget(main_window.case_search_tab)
    enter_data(main_window.case_search_box, '21TRC05611')
    mouse_click(main_window.get_case_Button)
    mouse_click(getattr(main_window, dialog_button))
    enter_data(main_window.dialog.case_number_lineEdit, test_name)
    enter_data(getattr(main_window.dialog, date_field), '01/01/2050')  # Set to pass a check

    # Create and Open Word Document - Passes even if no entry is opened b/c it checks data
    mouse_click(main_window.dialog.create_entry_Button)
    assert main_window.dialog.entry_case_information.case_number == f'21TRC05611{test_name}'
