"""Module for testing the cms_case_loaders.py classes."""
import pytest

from tests.conftest import (
    CRIMTRAFFIC_ALL_DIALOG_BUTTONS,
    CRIMTRAFFIC_CHARGE_DIALOG_BUTTONS,
    enter_data,
    mouse_click,
)

DIALOG_BUTTON = 'dialog_button'


def dialog_nocase_setup(main_window, dialog_button):
    """Setup for loading dialog with no case."""
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.pleas_radioButton)
    mouse_click(getattr(main_window, dialog_button))


def dialog_withcase_setup(main_window, dialog_button):
    """Setup for loading dialog with a test case."""
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, 'Barkschat - 21TRC05611')
    mouse_click(getattr(main_window, dialog_button))


@pytest.mark.parametrize(DIALOG_BUTTON, CRIMTRAFFIC_ALL_DIALOG_BUTTONS)
def test_cmsloader_nocase_case_number(main_window, dialog_button):
    """Tests that base CmsLoader with no case loads empty case number field."""
    dialog_nocase_setup(main_window, dialog_button)
    assert main_window.dialog.case_number_lineEdit.text() == ''


@pytest.mark.parametrize(DIALOG_BUTTON, CRIMTRAFFIC_ALL_DIALOG_BUTTONS)
def test_cmsloader_nocase_defendant_name(main_window, dialog_button):
    """Tests that base CmsLoader with no case loads empty defendant name fields."""
    dialog_nocase_setup(main_window, dialog_button)
    assert main_window.dialog.defendant_first_name_lineEdit.text() == ''
    assert main_window.dialog.defendant_last_name_lineEdit.text() == ''


@pytest.mark.parametrize(DIALOG_BUTTON, CRIMTRAFFIC_ALL_DIALOG_BUTTONS)
def test_cmsloader_withcase_case_number(main_window, dialog_button):
    """Tests that base CmsLoader with case selected loads case number field."""
    dialog_withcase_setup(main_window, dialog_button)
    assert main_window.dialog.case_number_lineEdit.text() == '21TRC05611'


@pytest.mark.parametrize(DIALOG_BUTTON, CRIMTRAFFIC_ALL_DIALOG_BUTTONS)
def test_cmsloader_withcase_defendant_name(main_window, dialog_button):
    """Tests that base CmsLoader with case loads defendant name fields."""
    dialog_withcase_setup(main_window, dialog_button)
    assert main_window.dialog.defendant_first_name_lineEdit.text() == 'Kelly'
    assert main_window.dialog.defendant_last_name_lineEdit.text() == 'Barkschat'


@pytest.mark.parametrize(DIALOG_BUTTON, CRIMTRAFFIC_CHARGE_DIALOG_BUTTONS)
def test_cms_charge_loader(main_window, dialog_button):
    """Tests that CrimTraffic dialogs with charge grids loads charges."""
    dialog_withcase_setup(main_window, dialog_button)
    charge_grid = main_window.dialog.charges_gridLayout
    assert charge_grid.itemAtPosition(0, 2).widget().text() == 'OVI Alcohol / Drugs 3rd'
