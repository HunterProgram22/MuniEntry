"""Module for testing all CrimTraffic Tab dialog buttons on mainwindow open."""
import pytest

from tests.conftest import enter_data, mouse_click

TEST_LIST = 'dialog_button, dialog_title'


crimtraffic_dialog_buttons = [
    ('FineOnlyPleaButton', 'Fine Only Plea Case Information'),
    ('JailCCPleaButton', 'Jail Community Control Plea Case Information'),
    ('DiversionButton', 'Diversion Plea Case Information'),

    ('NotGuiltyBondButton', 'Not Guilty Bond Case Information'),
    ('PleaOnlyButton', 'Plea Future Sentencing Case Information'),

    ('NoPleaBondButton', 'No Plea Bond Case Information'),
    ('BondHearingButton', 'Bond Hearing Case Information'),
    ('ProbationViolationBondButton', 'Community Control Violation Bond Case Information'),

    ('LeapAdmissionButton', 'LEAP Admission Plea Case Information'),
    ('LeapAdmissionValidButton', 'LEAP Plea - Already Valid Case Information'),
    ('LeapSentencingButton', 'LEAP Sentencing Case Information'),

    ('TrialSentencingButton', 'Trial Sentencing Case Information'),
    ('SentencingOnlyButton', 'Sentencing Only Case Information'),

    ('FailureToAppearButton', 'Failure To Appear Case Information'),
    ('FreeformEntryButton', 'Freeform Entry Case Information'),
]


@pytest.mark.parametrize(TEST_LIST, crimtraffic_dialog_buttons)
def test_dialogs_open_nocase_from_caselist(main_window, dialog_button, dialog_title):
    """Tests all CrimTraffic dialog buttons open from the case list when no case is selected."""
    mouse_click(main_window.hemmeter_radioButton)
    mouse_click(main_window.arraignments_radioButton)
    mouse_click(getattr(main_window, dialog_button))
    assert main_window.dialog.windowTitle() == dialog_title
    assert main_window.dialog.case_number_lineEdit.text() == ''


@pytest.mark.parametrize(TEST_LIST, crimtraffic_dialog_buttons)
def test_dialogs_open_with_case_from_caselist(main_window, dialog_button, dialog_title):
    """Tests all CrimTraffic dialog buttons open from the case list when a case is selected."""
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, 'Barkschat - 21TRC05611')
    mouse_click(getattr(main_window, dialog_button))
    assert main_window.dialog.windowTitle() == dialog_title
    assert main_window.dialog.case_number_lineEdit.text() == '21TRC05611'


@pytest.mark.parametrize(TEST_LIST, crimtraffic_dialog_buttons)
def test_dialogs_open_nocase_from_casesearch(main_window, dialog_button, dialog_title):
    """Tests all CrimTraffic dialog buttons open from the case search when no case is selected."""
    mouse_click(main_window.bunner_radioButton)
    main_window.search_tabWidget.setCurrentWidget(main_window.case_search_tab)
    mouse_click(getattr(main_window, dialog_button))
    assert main_window.dialog.windowTitle() == dialog_title
    assert main_window.dialog.case_number_lineEdit.text() == ''


@pytest.mark.parametrize(TEST_LIST, crimtraffic_dialog_buttons)
def test_dialogs_open_with_case_from_casesearch(main_window, dialog_button, dialog_title):
    """Tests all CrimTraffic dialog buttons open from the case search when a case is selected."""
    mouse_click(main_window.hemmeter_radioButton)
    main_window.search_tabWidget.setCurrentWidget(main_window.case_search_tab)
    enter_data(main_window.case_search_box, '22TRD01955')
    mouse_click(main_window.get_case_Button)
    mouse_click(getattr(main_window, dialog_button))
    assert main_window.dialog.windowTitle() == dialog_title
    assert main_window.dialog.case_number_lineEdit.text() == '22TRD01955'
    assert main_window.dialog.defendant_last_name_lineEdit.text() == 'Mahan'
