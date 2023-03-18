"""Module for testing CmsDrivingInfoLoader."""
from tests.conftest import BLANK, enter_data, mouse_click


def test_cmsdrivinginfoloader_nocase(main_window):
    """Tests CmsDrivingInfoLoader loads empty with no case."""
    mouse_click(main_window.assn_comm_2_admin_radio_btn)
    mouse_click(main_window.arraignments_radio_btn)
    mouse_click(main_window.limited_driving_privilegesButton)
    assert main_window.dialog.case_number_lineEdit.text() == BLANK
    assert main_window.dialog.defendant_first_name_lineEdit.text() == BLANK
    assert main_window.dialog.defendant_last_name_lineEdit.text() == BLANK


def test_cmsdrivinginfoloader_withcase(main_window):
    """Tests CmsDrivingInfoLoader loads with test case."""
    mouse_click(main_window.assn_comm_1_admin_radio_btn)
    mouse_click(main_window.arraignments_radio_btn)
    enter_data(main_window.arraignments_cases_box, 'Conkey - 22TRD01944')
    mouse_click(main_window.limited_driving_privilegesButton)
    assert main_window.dialog.case_number_lineEdit.text() == '22TRD01944'
    assert main_window.dialog.defendant_first_name_lineEdit.text() == 'Scott'
    assert main_window.dialog.defendant_last_name_lineEdit.text() == 'Conkey'
