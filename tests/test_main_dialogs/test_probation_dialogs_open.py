"""Module for testing all Probation Tab dialog buttons on mainwindow open."""
import pytest

from tests.conftest import enter_data, mouse_click

TEST_LIST = 'dialog_button, dialog_title'


probation_dialog_buttons = [
    ('terms_comm_control_btn', 'Terms of Community Control Case Information'),
]


@pytest.mark.parametrize(TEST_LIST, probation_dialog_buttons)
def tests_dialogs_open_nocase_from_caselist(main_window, dialog_button, dialog_title):
    """Tests all Probation dialog buttons open from the case list when no case is selected."""
    mouse_click(main_window.chief_prob_officer_radio_btn)
    mouse_click(main_window.pleas_radio_btn)
    mouse_click(getattr(main_window, dialog_button))
    assert main_window.dialog.windowTitle() == dialog_title
    assert main_window.dialog.case_number_lineEdit.text() == ''


@pytest.mark.parametrize(TEST_LIST, probation_dialog_buttons)
def test_dialogs_open_with_case_from_caselist(main_window, dialog_button, dialog_title):
    """Tests all Probation dialog buttons open from the case list when a case is selected."""
    mouse_click(main_window.chief_prob_officer_radio_btn)
    mouse_click(main_window.pleas_radio_btn)
    enter_data(main_window.pleas_cases_box, 'Barkschat - 21TRC05611')
    mouse_click(getattr(main_window, dialog_button))
    assert main_window.dialog.windowTitle() == dialog_title
    assert main_window.dialog.case_number_lineEdit.text() == '21TRC05611'


@pytest.mark.parametrize(TEST_LIST, probation_dialog_buttons)
def test_dialogs_open_nocase_from_casesearch(main_window, dialog_button, dialog_title):
    """Tests all Probation dialog buttons open from the case search when no case is selected."""
    mouse_click(main_window.chief_prob_officer_radio_btn)
    main_window.cases_tab_widget.setCurrentWidget(main_window.crim_case_search_tab)
    mouse_click(getattr(main_window, dialog_button))
    assert main_window.dialog.windowTitle() == dialog_title
    assert main_window.dialog.case_number_lineEdit.text() == ''


@pytest.mark.parametrize(TEST_LIST, probation_dialog_buttons)
def test_dialogs_open_with_case_from_casesearch(main_window, dialog_button, dialog_title):
    """Tests all Probation dialog buttons open from the case search when a case is selected."""
    mouse_click(main_window.chief_prob_officer_radio_btn)
    main_window.cases_tab_widget.setCurrentWidget(main_window.crim_case_search_tab)
    enter_data(main_window.crim_case_search_box, '22TRD01955')
    mouse_click(main_window.crim_get_case_btn)
    mouse_click(getattr(main_window, dialog_button))
    assert main_window.dialog.windowTitle() == dialog_title
    assert main_window.dialog.case_number_lineEdit.text() == '22TRD01955'
    assert main_window.dialog.defendant_last_name_lineEdit.text() == 'Mahan'
#
