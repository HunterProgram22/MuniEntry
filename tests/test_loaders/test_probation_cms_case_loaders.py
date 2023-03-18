"""Module for testing the ProbationCmsLoader."""
import pytest

from tests.conftest import (
    BLANK,
    DIALOG_BUTTON,
    PROBATION_ALL_DIALOG_BUTTONS,
    CaseToTest,
    enter_data,
    mouse_click,
)

TEST_CASE = CaseToTest('Barkschat - 21TRC05611', 'Kelly')


def probation_dialog_nocase_setup(main_window, dialog_button):
    """Setup for loading probation dialog with no case."""
    mouse_click(main_window.chief_prob_officer_radio_btn)
    mouse_click(main_window.pleas_radio_btn)
    mouse_click(getattr(main_window, dialog_button))


def probation_dialog_withcase_setup(main_window, dialog_button):
    """Setup for loading probation dialog with a test case."""
    mouse_click(main_window.chief_prob_officer_radio_btn)
    mouse_click(main_window.pleas_radio_btn)
    enter_data(main_window.pleas_cases_box, TEST_CASE.case_list_id)
    mouse_click(getattr(main_window, dialog_button))


@pytest.mark.parametrize(DIALOG_BUTTON, PROBATION_ALL_DIALOG_BUTTONS)
def test_probationcmsloader_nocase_case_number(main_window, dialog_button):
    """Tests that ProbationCmsLoader with no case loads empty case number field."""
    probation_dialog_nocase_setup(main_window, dialog_button)
    assert main_window.dialog.case_number_lineEdit.text() == BLANK


@pytest.mark.parametrize(DIALOG_BUTTON, PROBATION_ALL_DIALOG_BUTTONS)
def test_probationcmsloader_nocase_defendant_name(main_window, dialog_button):
    """Tests that ProbationCmsLoader with no case loads empty defendant name fields."""
    probation_dialog_nocase_setup(main_window, dialog_button)
    assert main_window.dialog.defendant_first_name_lineEdit.text() == BLANK
    assert main_window.dialog.defendant_last_name_lineEdit.text() == BLANK


@pytest.mark.parametrize(DIALOG_BUTTON, PROBATION_ALL_DIALOG_BUTTONS)
def test_probationcmsloader_withcase_case_number(main_window, dialog_button):
    """Tests that ProbationCmsLoader with test case loads case number field."""
    probation_dialog_withcase_setup(main_window, dialog_button)
    assert main_window.dialog.case_number_lineEdit.text() == TEST_CASE.case_number


@pytest.mark.parametrize(DIALOG_BUTTON, PROBATION_ALL_DIALOG_BUTTONS)
def test_probationcmsloader_withcase_def_name(main_window, dialog_button):
    """Tests that ProbationCmsLoader with test case loads defendant name fields."""
    probation_dialog_withcase_setup(main_window, dialog_button)
    assert main_window.dialog.defendant_first_name_lineEdit.text() == TEST_CASE.first_name
    assert main_window.dialog.defendant_last_name_lineEdit.text() == TEST_CASE.last_name
