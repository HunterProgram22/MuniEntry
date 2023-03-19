"""Test module for creating probation entries."""
import pytest

from tests.conftest import enter_data, mouse_click, MUNI10_SAVE_PATH
from munientry.entrycreators.entry_creator import ProbationEntryCreator

probation_tab_entries = [
    ('terms_comm_control_btn', 'terms_test'),
    ('notice_comm_control_violation_btn', 'notice_test'),
]


@pytest.mark.parametrize('dialog_button, test_name', probation_tab_entries)
def test_all_entry_buttons_with_case(monkeypatch, main_window, dialog_button, test_name):
    data = ProbationEntryCreator
    monkeypatch.setattr(data, 'save_path', MUNI10_SAVE_PATH)
    mouse_click(main_window.chief_prob_officer_radio_btn)
    main_window.cases_tab_widget.setCurrentWidget(main_window.crim_case_search_tab)
    enter_data(main_window.crim_case_search_box, '22TRD01944')
    mouse_click(main_window.crim_case_search_tab)
    mouse_click((getattr(main_window, dialog_button)))
    enter_data(main_window.dialog.case_number_lineEdit, test_name)

    # Create and Open Word Document - Passes even if no entry is opened b/c it checks data
    mouse_click(main_window.dialog.create_entry_Button)
    assert main_window.dialog.entry_case_information.case_number == f'22TRD01944{test_name}'
    assert main_window.dialog.entry_case_information.defendant.last_name == 'Conkey'
