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


def test_create_fiscal_entry(main_window):
    """Tests the creation of a fiscal entry.

    Passes even if no entry is opened b/c it checks data.
    """
    mouse_click(main_window.court_admin_kudela_radioButton)
    mouse_click(main_window.fiscal_entriesButton)
    mouse_click(main_window.dialog.create_entry_Button)
    assert main_window.dialog.entry_case_information.account_number == '24115000'


def test_create_jury_pay_entry(main_window):
    """Tests the creation of a jury payment entry.

    Passes even if no entry is opened b/c it checks data.
    """
    mouse_click(main_window.jury_comm_patterson_radioButton)
    mouse_click(main_window.arraignments_radioButton)
    enter_data(main_window.arraignments_cases_box, 'Conkey - 22TRD01944')
    mouse_click(main_window.juror_paymentButton)
    enter_data(main_window.dialog.jurors_reported_lineEdit, '20')
    enter_data(main_window.dialog.case_number_lineEdit, 'TEST')
    mouse_click(main_window.dialog.calculate_payment_Button)
    mouse_click(main_window.dialog.create_entry_Button)
    assert main_window.dialog.entry_case_information.jury_panel_total_pay == '635'
    assert main_window.dialog.entry_case_information.case_number == '22TRD01944TEST'
