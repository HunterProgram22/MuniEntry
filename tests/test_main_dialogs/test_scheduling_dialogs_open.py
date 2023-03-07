"""Module for testing all Scheduling Tab dialog buttons on mainwindow open."""
import pytest

from tests.conftest import enter_data, mouse_click

TEST_LIST = 'dialog_button, dialog_title'


scheduling_dialog_buttons = [
    (
        'hemmeter_final_jury_hearingButton',
        'Final And Jury Notice Hearing Entry Case Information - Judge Marianne T. Hemmeter',
    ),
    (
        'rohrer_final_jury_hearingButton',
        'Final And Jury Notice Hearing Entry Case Information - Judge Kyle E. Rohrer',
    ),
    (
        'hemmeter_general_hearingButton',
        'General Notice Of Hearing Entry Case Information - Judge Marianne T. Hemmeter',
    ),
    (
        'rohrer_general_hearingButton',
        'General Notice Of Hearing Entry Case Information - Judge Kyle E. Rohrer',
    ),
    (
        'hemmeter_trial_court_hearingButton',
        'Trial To Court Notice Hearing Entry Case Information - Judge Marianne T. Hemmeter',
    ),
    (
        'rohrer_trial_court_hearingButton',
        'Trial To Court Notice Hearing Entry Case Information - Judge Kyle E. Rohrer',
    ),
    ('rohrer_schedulingEntryButton', 'Rohrer Scheduling Entry Case Information'),
    ('hemmeter_schedulingEntryButton', 'Hemmeter Scheduling Entry Case Information'),
]


@pytest.mark.parametrize(TEST_LIST, scheduling_dialog_buttons)
def test_dialogs_open_nocase_from_caselist(main_window, dialog_button, dialog_title):
    """Tests all Scheduling dialog buttons open from the case list when no case is selected."""
    mouse_click(main_window.assn_comm_2_radio_btn)
    mouse_click(main_window.arraignments_radioButton)
    mouse_click(getattr(main_window, dialog_button))
    assert main_window.dialog.windowTitle() == dialog_title
    assert main_window.dialog.case_number_lineEdit.text() == ''


@pytest.mark.parametrize(TEST_LIST, scheduling_dialog_buttons)
def test_dialogs_open_with_case_from_caselist(main_window, dialog_button, dialog_title):
    """Tests all Scheduling dialog buttons open from the case list when a case is selected."""
    mouse_click(main_window.assn_comm_1_radio_btn)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, 'Barkschat - 21TRC05611')
    mouse_click(getattr(main_window, dialog_button))
    assert main_window.dialog.windowTitle() == dialog_title
    assert main_window.dialog.case_number_lineEdit.text() == '21TRC05611'


@pytest.mark.parametrize(TEST_LIST, scheduling_dialog_buttons)
def test_dialogs_open_with_case_from_casesearch(main_window, dialog_button, dialog_title):
    """Tests all Scheduling dialog buttons open from the case search when no case is selected."""
    mouse_click(main_window.assn_comm_2_radio_btn)
    main_window.search_tabWidget.setCurrentWidget(main_window.case_search_tab)
    mouse_click(getattr(main_window, dialog_button))
    assert main_window.dialog.windowTitle() == dialog_title
    assert main_window.dialog.case_number_lineEdit.text() == ''


@pytest.mark.parametrize(TEST_LIST, scheduling_dialog_buttons)
def test_dialogs_open_nocase_from_casesearch(main_window, dialog_button, dialog_title):
    """Tests all Scheduling dialog buttons open from the case search when a case is selected."""
    mouse_click(main_window.assn_comm_2_radio_btn)
    main_window.search_tabWidget.setCurrentWidget(main_window.case_search_tab)
    enter_data(main_window.case_search_box, '22TRD01955')
    mouse_click(main_window.get_case_Button)
    mouse_click(getattr(main_window, dialog_button))
    assert main_window.dialog.windowTitle() == dialog_title
    assert main_window.dialog.case_number_lineEdit.text() == '22TRD01955'
    assert main_window.dialog.defendant_last_name_lineEdit.text() == 'Mahan'
