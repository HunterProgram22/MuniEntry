"""Module for testing the cms_case_loaders.py classes."""
import pytest

from tests.conftest import (
    CRIMTRAFFIC_ALL_DIALOG_BUTTONS,
    CRIMTRAFFIC_CHARGE_DIALOG_BUTTONS,
    CRIMTRAFFIC_FRA_DIALOG_BUTTONS,
    SCHEDULING_ALL_DIALOG_BUTTONS,
    enter_data,
    mouse_click,
)

DIALOG_BUTTON = 'dialog_button'


def dialog_nocase_setup(main_window, dialog_button):
    """Setup for loading dialog with no case."""
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.pleas_radioButton)
    mouse_click(getattr(main_window, dialog_button))


def scheduling_dialog_nocase_setup(main_window, dialog_button):
    """Setup for loading scheduling dialog with no case."""
    mouse_click(main_window.dattilo_radioButton)
    mouse_click(main_window.pleas_radioButton)
    mouse_click(getattr(main_window, dialog_button))


def dialog_withcase_setup(main_window, dialog_button):
    """Setup for loading dialog with a test case."""
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, 'Barkschat - 21TRC05611')
    mouse_click(getattr(main_window, dialog_button))


def scheduling_dialog_withcase_setup(main_window, dialog_button):
    """Setup for loading scheduling dialog with a test case."""
    mouse_click(main_window.dattilo_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, 'Barkschat - 21TRC05611')
    mouse_click(getattr(main_window, dialog_button))


@pytest.mark.parametrize(DIALOG_BUTTON, CRIMTRAFFIC_ALL_DIALOG_BUTTONS)
def test_cmsloader_nocase_case_number(main_window, dialog_button):
    """Tests that base CmsLoader with no case loads empty case number field."""
    dialog_nocase_setup(main_window, dialog_button)
    assert main_window.dialog.case_number_lineEdit.text() == ''


@pytest.mark.parametrize(DIALOG_BUTTON, SCHEDULING_ALL_DIALOG_BUTTONS)
def test_schedulingcmsloader_nocase_case_number(main_window, dialog_button):
    """Tests that SchedulingCmsLoader with no case loads empty case number field."""
    scheduling_dialog_nocase_setup(main_window, dialog_button)
    assert main_window.dialog.case_number_lineEdit.text() == ''


@pytest.mark.parametrize(DIALOG_BUTTON, CRIMTRAFFIC_ALL_DIALOG_BUTTONS)
def test_cmsloader_nocase_defendant_name(main_window, dialog_button):
    """Tests that base CmsLoader with no case loads empty defendant name fields."""
    dialog_nocase_setup(main_window, dialog_button)
    assert main_window.dialog.defendant_first_name_lineEdit.text() == ''
    assert main_window.dialog.defendant_last_name_lineEdit.text() == ''


@pytest.mark.parametrize(DIALOG_BUTTON, SCHEDULING_ALL_DIALOG_BUTTONS)
def test_schedulingcmsloader_nocase_defendant_name(main_window, dialog_button):
    """Tests that SchedulingCmsLoader with no case loads empty defendant name fields."""
    scheduling_dialog_nocase_setup(main_window, dialog_button)
    assert main_window.dialog.defendant_first_name_lineEdit.text() == ''
    assert main_window.dialog.defendant_last_name_lineEdit.text() == ''


@pytest.mark.parametrize(DIALOG_BUTTON, CRIMTRAFFIC_ALL_DIALOG_BUTTONS)
def test_cmsloader_withcase_case_number(main_window, dialog_button):
    """Tests that base CmsLoader with case selected loads case number field."""
    dialog_withcase_setup(main_window, dialog_button)
    assert main_window.dialog.case_number_lineEdit.text() == '21TRC05611'


@pytest.mark.parametrize(DIALOG_BUTTON, SCHEDULING_ALL_DIALOG_BUTTONS)
def test_schedulingcmsloader_withcase_case_number(main_window, dialog_button):
    """Tests that SchedulingCmsLoader with test case loads case number field."""
    scheduling_dialog_withcase_setup(main_window, dialog_button)
    assert main_window.dialog.case_number_lineEdit.text() == '21TRC05611'


@pytest.mark.parametrize(DIALOG_BUTTON, CRIMTRAFFIC_ALL_DIALOG_BUTTONS)
def test_cmsloader_withcase_defendant_name(main_window, dialog_button):
    """Tests that base CmsLoader with case loads defendant name fields."""
    dialog_withcase_setup(main_window, dialog_button)
    assert main_window.dialog.defendant_first_name_lineEdit.text() == 'Kelly'
    assert main_window.dialog.defendant_last_name_lineEdit.text() == 'Barkschat'


@pytest.mark.parametrize(DIALOG_BUTTON, SCHEDULING_ALL_DIALOG_BUTTONS)
def test_schedulingcmsloader_withcase_defendant_name(main_window, dialog_button):
    """Tests that SchedulingCmsLoader with test case loads defendant name fields."""
    scheduling_dialog_withcase_setup(main_window, dialog_button)
    assert main_window.dialog.defendant_first_name_lineEdit.text() == 'Kelly'
    assert main_window.dialog.defendant_last_name_lineEdit.text() == 'Barkschat'


@pytest.mark.parametrize(DIALOG_BUTTON, CRIMTRAFFIC_CHARGE_DIALOG_BUTTONS)
def test_cmschargeloader(main_window, dialog_button):
    """Tests that CrimTraffic dialogs with charge grids loads charges."""
    dialog_withcase_setup(main_window, dialog_button)
    charge_grid = main_window.dialog.charges_gridLayout
    assert charge_grid.itemAtPosition(0, 2).widget().text() == 'OVI Alcohol / Drugs 3rd'
    assert charge_grid.itemAtPosition(0, 4).widget().text() == 'OVI Refusal 3rd/10yr Prior 20yr'
    assert charge_grid.itemAtPosition(0, 6).widget().text() == 'Driving in Marked Lanes'


@pytest.mark.parametrize(DIALOG_BUTTON, CRIMTRAFFIC_FRA_DIALOG_BUTTONS)
def test_cmsfraloader_nocase(main_window, dialog_button):
    """Tests CrimTraffic dialogs with FRA loads 'N/A' for FRA information when no case."""
    dialog_nocase_setup(main_window, dialog_button)
    assert main_window.dialog.fra_in_file_box.currentText() == 'N/A'
    assert main_window.dialog.fra_in_court_box.currentText() == 'N/A'


@pytest.mark.parametrize(DIALOG_BUTTON, CRIMTRAFFIC_FRA_DIALOG_BUTTONS)
def test_cmsfraloader_withcase_nofra(main_window, dialog_button):
    """Tests CrimTraffic dialogs with FRA loads correct FRA information with case."""
    dialog_withcase_setup(main_window, dialog_button)
    assert main_window.dialog.fra_in_file_box.currentText() == 'No'
    assert main_window.dialog.fra_in_court_box.currentText() == 'N/A'


@pytest.mark.parametrize(DIALOG_BUTTON, CRIMTRAFFIC_FRA_DIALOG_BUTTONS)
def test_cmsfraloader_withcase_yesfra(main_window, dialog_button):
    """Tests CrimTraffic dialogs with FRA loads correct FRA information with case."""
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.arraignments_radioButton)
    enter_data(main_window.arraignments_cases_box, 'Creamer - 22TRD01698')
    mouse_click(getattr(main_window, dialog_button))
    assert main_window.dialog.fra_in_file_box.currentText() == 'Yes'
    assert main_window.dialog.fra_in_court_box.currentText() == 'No'


def test_cmsdrivinginfoloader_nocase(main_window):
    """Tests CmsDrivingInfoLoader loads empty with no case."""
    mouse_click(main_window.assn_comm_patterson_radioButton)
    mouse_click(main_window.arraignments_radioButton)
    mouse_click(getattr(main_window, 'limited_driving_privilegesButton'))
    assert main_window.dialog.case_number_lineEdit.text() == ''
    assert main_window.dialog.defendant_first_name_lineEdit.text() == ''
    assert main_window.dialog.defendant_last_name_lineEdit.text() == ''


def test_cmsdrivinginfoloader_withcase(main_window):
    """Tests CmsDrivingInfoLoader loads with test case."""
    mouse_click(main_window.assn_comm_patterson_radioButton)
    mouse_click(main_window.arraignments_radioButton)
    enter_data(main_window.arraignments_cases_box, 'Conkey - 22TRD01944')
    mouse_click(getattr(main_window, 'limited_driving_privilegesButton'))
    assert main_window.dialog.case_number_lineEdit.text() == '22TRD01944'
    assert main_window.dialog.defendant_first_name_lineEdit.text() == 'Scott'
    assert main_window.dialog.defendant_last_name_lineEdit.text() == 'Conkey'
