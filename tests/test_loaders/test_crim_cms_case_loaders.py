"""Module for testing the cms_case_loaders.py classes."""
import pytest

from tests.conftest import (
    BLANK,
    CRIMTRAFFIC_ALL_DIALOG_BUTTONS,
    CRIMTRAFFIC_CHARGE_DIALOG_BUTTONS,
    CRIMTRAFFIC_FRA_DIALOG_BUTTONS,
    DIALOG_BUTTON,
    CaseToTest,
    enter_data,
    mouse_click,
)

TEST_CASE = CaseToTest('Barkschat - 21TRC05611', 'Kelly')


def crim_dialog_nocase_setup(main_window, dialog_button):
    """Setup for loading crim/traffic dialog with no case."""
    mouse_click(main_window.judge_2_radio_btn)
    mouse_click(main_window.pleas_radio_btn)
    mouse_click(getattr(main_window, dialog_button))


def crim_dialog_withcase_setup(main_window, dialog_button):
    """Setup for loading crim/traffic dialog with a test case."""
    mouse_click(main_window.judge_2_radio_btn)
    mouse_click(main_window.pleas_radio_btn)
    enter_data(main_window.pleas_cases_box, TEST_CASE.case_list_id)
    mouse_click(getattr(main_window, dialog_button))


@pytest.mark.parametrize(DIALOG_BUTTON, CRIMTRAFFIC_ALL_DIALOG_BUTTONS)
def test_crimcmsloader_nocase_case_number(main_window, dialog_button):
    """Tests that base CmsLoader with no case loads empty case number field."""
    crim_dialog_nocase_setup(main_window, dialog_button)
    assert main_window.dialog.case_number_lineEdit.text() == BLANK


@pytest.mark.parametrize(DIALOG_BUTTON, CRIMTRAFFIC_ALL_DIALOG_BUTTONS)
def test_crimcmsloader_nocase_defendant_name(main_window, dialog_button):
    """Tests that base CmsLoader with no case loads empty defendant name fields."""
    crim_dialog_nocase_setup(main_window, dialog_button)
    assert main_window.dialog.defendant_first_name_lineEdit.text() == BLANK
    assert main_window.dialog.defendant_last_name_lineEdit.text() == BLANK


@pytest.mark.parametrize(DIALOG_BUTTON, CRIMTRAFFIC_ALL_DIALOG_BUTTONS)
def test_crimcmsloader_withcase_case_number(main_window, dialog_button):
    """Tests that base CmsLoader with case selected loads case number field."""
    crim_dialog_withcase_setup(main_window, dialog_button)
    assert main_window.dialog.case_number_lineEdit.text() == TEST_CASE.case_number


@pytest.mark.parametrize(DIALOG_BUTTON, CRIMTRAFFIC_ALL_DIALOG_BUTTONS)
def test_crimcmsloader_withcase_defendant_name(main_window, dialog_button):
    """Tests that base CmsLoader with case loads defendant name fields."""
    crim_dialog_withcase_setup(main_window, dialog_button)
    assert main_window.dialog.defendant_first_name_lineEdit.text() == TEST_CASE.first_name
    assert main_window.dialog.defendant_last_name_lineEdit.text() == TEST_CASE.last_name


@pytest.mark.parametrize(DIALOG_BUTTON, CRIMTRAFFIC_CHARGE_DIALOG_BUTTONS)
def test_crimcmschargeloader(main_window, dialog_button):
    """Tests that CrimTraffic dialogs with charge grids loads charges."""
    crim_dialog_withcase_setup(main_window, dialog_button)
    charge_grid = main_window.dialog.charges_gridLayout
    assert charge_grid.itemAtPosition(0, 2).widget().text() == 'OVI Alcohol / Drugs 3rd'
    assert charge_grid.itemAtPosition(0, 4).widget().text() == 'OVI Refusal 3rd/10yr Prior 20yr'
    assert charge_grid.itemAtPosition(0, 6).widget().text() == 'Driving in Marked Lanes'


@pytest.mark.parametrize(DIALOG_BUTTON, CRIMTRAFFIC_FRA_DIALOG_BUTTONS)
def test_crimcmsfraloader_nocase(main_window, dialog_button):
    """Tests CrimTraffic dialogs with FRA loads 'N/A' for FRA information when no case."""
    crim_dialog_nocase_setup(main_window, dialog_button)
    assert main_window.dialog.fra_in_file_box.currentText() == 'N/A'
    assert main_window.dialog.fra_in_court_box.currentText() == 'N/A'


@pytest.mark.parametrize(DIALOG_BUTTON, CRIMTRAFFIC_FRA_DIALOG_BUTTONS)
def test_crimcmsfraloader_withcase_nofra(main_window, dialog_button):
    """Tests CrimTraffic dialogs with FRA loads correct FRA information with case."""
    crim_dialog_withcase_setup(main_window, dialog_button)
    assert main_window.dialog.fra_in_file_box.currentText() == 'No'
    assert main_window.dialog.fra_in_court_box.currentText() == 'N/A'


@pytest.mark.parametrize(DIALOG_BUTTON, CRIMTRAFFIC_FRA_DIALOG_BUTTONS)
def test_crimcmsfraloader_withcase_yesfra(main_window, dialog_button):
    """Tests CrimTraffic dialogs with FRA loads correct FRA information with case."""
    mouse_click(main_window.judge_2_radio_btn)
    mouse_click(main_window.arraignments_radio_btn)
    enter_data(main_window.arraignments_cases_box, 'Creamer - 22TRD01698')
    mouse_click(getattr(main_window, dialog_button))
    assert main_window.dialog.fra_in_file_box.currentText() == 'Yes'
    assert main_window.dialog.fra_in_court_box.currentText() == 'No'
