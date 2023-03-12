"""Module for testing all Probation Tab dialog buttons on mainwindow open."""
import pytest

from tests.conftest import enter_data, mouse_click

parametrize_args = 'dialog_button, dialog_title'

probation_dialog_buttons = [
    ('terms_comm_control_btn', 'Terms of Community Control Case Information'),
]

@pytest.fixture
def probation_caselist_setup(main_window):
    def _setup_buttons():
        main_window.chief_prob_officer_radio_btn.click()
        main_window.pleas_radio_btn.click()
    return _setup_buttons


@pytest.fixture
def probation_casesearch_setup(main_window):
    def _setup_buttons():
        main_window.chief_prob_officer_radio_btn.click()
        main_window.cases_tab_widget.setCurrentWidget(main_window.crim_case_search_tab)
    return _setup_buttons


@pytest.mark.parametrize(parametrize_args, probation_dialog_buttons)
def tests_dialogs_open_nocase_from_caselist(main_window, probation_caselist_setup, dialog_button, dialog_title):
    """Tests all Probation dialog buttons open from the case list when no case is selected."""
    probation_caselist_setup()
    mouse_click(getattr(main_window, dialog_button))
    assert main_window.dialog.windowTitle() == dialog_title
    assert main_window.dialog.case_number_lineEdit.text() == ''


@pytest.mark.parametrize(parametrize_args, probation_dialog_buttons)
def test_dialogs_open_with_case_from_caselist(main_window, probation_caselist_setup, dialog_button, dialog_title):
    """Tests all Probation dialog buttons open from the case list when a case is selected."""
    probation_caselist_setup()
    enter_data(main_window.pleas_cases_box, 'Barkschat - 21TRC05611')
    mouse_click(getattr(main_window, dialog_button))
    assert main_window.dialog.windowTitle() == dialog_title
    assert main_window.dialog.case_number_lineEdit.text() == '21TRC05611'


@pytest.mark.parametrize(parametrize_args, probation_dialog_buttons)
def test_dialogs_open_nocase_from_casesearch(main_window, probation_casesearch_setup, dialog_button, dialog_title):
    """Tests all Probation dialog buttons open from the case search when no case is selected."""
    probation_casesearch_setup()
    mouse_click(getattr(main_window, dialog_button))
    assert main_window.dialog.windowTitle() == dialog_title
    assert main_window.dialog.case_number_lineEdit.text() == ''


@pytest.mark.parametrize(parametrize_args, probation_dialog_buttons)
def test_dialogs_open_with_case_from_casesearch(main_window, probation_casesearch_setup, dialog_button, dialog_title):
    """Tests all Probation dialog buttons open from the case search when a case is selected."""
    probation_casesearch_setup()
    enter_data(main_window.crim_case_search_box, '22TRD01955')
    mouse_click(main_window.crim_get_case_btn)
    mouse_click(getattr(main_window, dialog_button))
    assert main_window.dialog.windowTitle() == dialog_title
    assert main_window.dialog.case_number_lineEdit.text() == '22TRD01955'
    assert main_window.dialog.defendant_last_name_lineEdit.text() == 'Mahan'
#
