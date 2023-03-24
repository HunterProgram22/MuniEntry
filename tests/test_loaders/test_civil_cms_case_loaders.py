"""Module for testing CivilCmsLoader."""
import pytest

from tests.conftest import (
    BLANK,
    CIVIL_ALL_DIALOG_BUTTONS,
    DIALOG_BUTTON,
    enter_data,
    mouse_click,
)

def civil_dialog_nocase_setup(main_window, dialog_button):
    """Setup for loading civil dialog with no case."""
    mouse_click(main_window.mag_1_radio_btn)
    main_window.cases_tab_widget.setCurrentWidget(main_window.civil_case_search_tab)
    mouse_click(getattr(main_window, dialog_button))

def civil_dialog_withcase_setup(main_window, dialog_button):
    """Setup for loading civil dialog with a test case."""
    mouse_click(main_window.mag_1_radio_btn)
    main_window.cases_tab_widget.setCurrentWidget(main_window.civil_case_search_tab)
    enter_data(main_window.civil_case_search_box, '22CVF00002')
    mouse_click(main_window.civil_get_case_btn)
    mouse_click(getattr(main_window, dialog_button))


@pytest.mark.parametrize(DIALOG_BUTTON, CIVIL_ALL_DIALOG_BUTTONS)
def test_civilcmsloader_nocase_case_number(main_window, dialog_button):
    """Tests that base CivilCmsLoader with no case loads empty case number field."""
    civil_dialog_nocase_setup(main_window, dialog_button)
    assert main_window.dialog.case_number_lineEdit.text() == BLANK


@pytest.mark.parametrize(DIALOG_BUTTON, CIVIL_ALL_DIALOG_BUTTONS)
def test_civilcmsloader_nocase_no_party_names(main_window, dialog_button):
    """Tests that base CivilCmsLoader with no case loads empty party name fields."""
    civil_dialog_nocase_setup(main_window, dialog_button)
    assert main_window.dialog.defendant_lineEdit.text() == BLANK
    assert main_window.dialog.plaintiff_lineEdit.text() == BLANK


@pytest.mark.parametrize(DIALOG_BUTTON, CIVIL_ALL_DIALOG_BUTTONS)
def test_civilcmsloader_withcase_case_number(main_window, dialog_button):
    """Tests that base CivilCmsLoader with case selected loads case number field."""
    civil_dialog_withcase_setup(main_window, dialog_button)
    assert main_window.dialog.case_number_lineEdit.text() == '22CVF00002'


@pytest.mark.parametrize(DIALOG_BUTTON, CIVIL_ALL_DIALOG_BUTTONS)
def test_civilcmsloader_withcase_defendant_name(main_window, dialog_button):
    """Tests that base CivilCmsLoader with case loads party name fields."""
    civil_dialog_withcase_setup(main_window, dialog_button)
    assert main_window.dialog.defendant_lineEdit.text() == 'Jill Belt'
    assert main_window.dialog.plaintiff_lineEdit.text() == 'Surfside Pools and Spas, LLC'
