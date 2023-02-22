"""Test module for creating crimtraffic entries."""
from tests.conftest import enter_data, mouse_click, MUNI10_SAVE_PATH
from munientry.entrycreators.entry_creator import CivilEntryCreator



def entry_dialog(monkeypatch, main_window):
    """The preliminary setup for creating an entry."""
    data = CivilEntryCreator
    monkeypatch.setattr(data, 'save_path', MUNI10_SAVE_PATH)
    mouse_click(main_window.bunner_radioButton)
    main_window.search_tabWidget.setCurrentWidget(main_window.civil_case_search_tab)
    enter_data(main_window.civil_case_search_box, '22CVF00002')
    mouse_click(main_window.civil_get_case_Button)


def test_civil_freeform_entry(monkeypatch, main_window):
    entry_dialog(monkeypatch, main_window)
    mouse_click(main_window.CivFreeformEntryButton)
    mouse_click(main_window.dialog.create_entry_Button)
    assert main_window.dialog.entry_case_information.defendant.party_name == 'Jill Belt'
