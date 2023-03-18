"""Test module for creating probation entries."""
import pytest

from tests.conftest import enter_data, mouse_click, MUNI10_SAVE_PATH
from munientry.entrycreators.entry_creator import ProbationEntryCreator


@pytest.fixture
def setup_entry_dialog(monkeypatch, main_window):
    """The preliminary setup for creating an entry."""
    data = ProbationEntryCreator
    monkeypatch.setattr(data, 'save_path', MUNI10_SAVE_PATH)
    mouse_click(main_window.chief_prob_officer_radio_btn)
    main_window.cases_tab_widget.setCurrentWidget(main_window.crim_case_search_tab)
    enter_data(main_window.crim_case_search_box, '22TRD01944')
    mouse_click(main_window.crim_case_search_tab)


def test_terms_of_comm_control_entry(setup_entry_dialog, main_window):
    mouse_click(main_window.terms_comm_control_btn)
    mouse_click(main_window.dialog.create_entry_Button)
    assert main_window.dialog.entry_case_information.defendant.last_name == 'Conkey'
