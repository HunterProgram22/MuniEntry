"""Module for testing all Admin Tab dialogs buttons on mainwindow open."""
import pytest

from tests.conftest import enter_data, mouse_click

TEST_LIST = 'test_input, dialog_title'


admin_dialog_buttons = [
    ('limited_driving_privilegesButton', 'Driving Privileges Entry Case Information'),
    ('juror_paymentButton', 'Juror Payment'),
]


@pytest.mark.parametrize(TEST_LIST, admin_dialog_buttons)
def tests_dialogs_open_nocase_from_caselist(main_window, test_input, dialog_title):
    """Tests all Admin dialog buttons open from the case list when no case is selected."""
    mouse_click(main_window.assn_comm_patterson_radioButton)
    mouse_click(main_window.arraignments_radioButton)
    mouse_click(getattr(main_window, test_input))
    assert main_window.dialog.windowTitle() == dialog_title
    assert main_window.dialog.case_number_lineEdit.text() == ''


@pytest.mark.parametrize(TEST_LIST, admin_dialog_buttons)
def test_dialogs_open_with_case_from_caselist(main_window, test_input, dialog_title):
    """Tests all Admin dialog buttons open from the case list when a case is selected."""
    mouse_click(main_window.assn_comm_dattilo_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, 'Barkschat - 21TRC05611')
    mouse_click(getattr(main_window, test_input))
    assert main_window.dialog.windowTitle() == dialog_title
    assert main_window.dialog.case_number_lineEdit.text() == '21TRC05611'


@pytest.mark.parametrize(TEST_LIST, admin_dialog_buttons)
def test_dialogs_open_nocase_from_casesearch(main_window, test_input, dialog_title):
    """Tests all Admin dialog buttons open from the case search when no case is selected."""
    mouse_click(main_window.assn_comm_patterson_radioButton)
    main_window.search_tabWidget.setCurrentWidget(main_window.case_search_tab)
    mouse_click(getattr(main_window, test_input))
    assert main_window.dialog.windowTitle() == dialog_title
    assert main_window.dialog.case_number_lineEdit.text() == ''


@pytest.mark.parametrize(TEST_LIST, admin_dialog_buttons)
def test_dialogs_open_with_case_from_casesearch(main_window, test_input, dialog_title):
    """Tests all Admin dialog buttons open from the case search when a case is selected."""
    mouse_click(main_window.assn_comm_patterson_radioButton)
    main_window.search_tabWidget.setCurrentWidget(main_window.case_search_tab)
    enter_data(main_window.case_search_box, '22TRD01955')
    mouse_click(main_window.get_case_Button)
    mouse_click(getattr(main_window, test_input))
    assert main_window.dialog.windowTitle() == dialog_title
    assert main_window.dialog.case_number_lineEdit.text() == '22TRD01955'
    assert main_window.dialog.defendant_last_name_lineEdit.text() == 'Mahan'


admin_noncase_dialog_buttons = [
    ('fiscal_entriesButton', 'Admin Fiscal Entry Information'),
]


@pytest.mark.parametrize(TEST_LIST, admin_noncase_dialog_buttons)
def test_all_admin_entry_noncase_dialogs(main_window, test_input, dialog_title):
    """Tests all Admin Nocase Dialogs open."""
    mouse_click(main_window.court_admin_kudela_radioButton)
    mouse_click(getattr(main_window, test_input))
    assert main_window.dialog.windowTitle() == dialog_title
    assert main_window.dialog.account_number_box.currentText() == (
        'Indigent Alcohol Monitoring - 24115000'
    )
