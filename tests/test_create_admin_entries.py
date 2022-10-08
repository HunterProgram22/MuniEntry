"""Test module for creating admin entries.

Module Level Parameters - fixtures setup and imported automatically from the conftest file.
    main_window
"""
from tests.conftest import enter_data, mouse_click


def test_create_driving_privileges_casesearch(main_window):
    """Tests the creation of a driving privileges entry from case search.

    Passes even if no entry is opened b/c it checks data.
    """
    mouse_click(main_window.assn_comm_patterson_radioButton)
    main_window.search_tabWidget.setCurrentWidget(main_window.case_search_tab)
    enter_data(main_window.case_search_box, '22TRD01955')
    mouse_click(main_window.get_case_Button)
    mouse_click(main_window.limited_driving_privilegesButton)
    enter_data(main_window.dialog.defendant_driver_license_lineEdit, 'TEST')
    mouse_click(main_window.dialog.create_entry_Button)
    assert main_window.dialog.entry_case_information.defendant.state == 'OH'
    assert main_window.dialog.entry_case_information.case_number == '22TRD01955'


def test_create_driving_privileges_caselist(main_window):
    """Tests the creation of a driving privileges entry from daily case lists.

    Passes even if no entry is opened b/c it checks data.
    """
    mouse_click(main_window.assn_comm_patterson_radioButton)
    main_window.search_tabWidget.setCurrentWidget(main_window.case_list_tab)
    mouse_click(main_window.arraignments_radioButton)
    enter_data(main_window.arraignments_cases_box, 'Conkey - 22TRD01944')
    mouse_click(main_window.limited_driving_privilegesButton)
    enter_data(main_window.dialog.defendant_driver_license_lineEdit, 'TEST')
    mouse_click(main_window.dialog.create_entry_Button)
    assert main_window.dialog.entry_case_information.defendant.state == 'OH'
    assert main_window.dialog.entry_case_information.case_number == '22TRD01944'
