"""Test module for creating admin entries.

Module Level Parameters - fixtures setup and imported automatically from the conftest file.
    main_window
"""
from tests.conftest import enter_data, mouse_click, MUNI10_SAVE_PATH
from munientry.entrycreators.entry_creator import AdminFiscalEntryCreator, JuryPaymentEntryCreator, \
    DrivingPrivilegesEntryCreator


def test_create_driving_privileges_entry(monkeypatch, main_window):
    """Tests the creation of a driving privileges entry from case search.

    Passes even if no entry is opened b/c it checks data.
    """
    data = DrivingPrivilegesEntryCreator
    monkeypatch.setattr(data, 'save_path', MUNI10_SAVE_PATH)
    mouse_click(main_window.assn_comm_1_admin_radio_btn)
    main_window.cases_tab_widget.setCurrentWidget(main_window.crim_case_search_tab)
    enter_data(main_window.crim_case_search_box, '22TRD01955')
    mouse_click(main_window.crim_get_case_btn)
    mouse_click(main_window.limited_driving_privilegesButton)
    enter_data(main_window.dialog.defendant_driver_license_lineEdit, 'TEST')
    mouse_click(main_window.dialog.create_entry_Button)
    assert main_window.dialog.entry_case_information.defendant.state == 'OH'
    assert main_window.dialog.entry_case_information.case_number == '22TRD01955'


def test_create_fiscal_entry(monkeypatch, main_window):
    """Tests the creation of a fiscal entry.

    Passes even if no entry is opened b/c it checks data.
    """
    data = AdminFiscalEntryCreator
    monkeypatch.setattr(data, 'save_path', MUNI10_SAVE_PATH)
    mouse_click(main_window.court_admin_admin_radio_btn)
    mouse_click(main_window.fiscal_entriesButton)
    mouse_click(main_window.dialog.create_entry_Button)
    assert main_window.dialog.entry_case_information.account_number == '24115000'


def test_create_jury_pay_entry(monkeypatch, main_window):
    """Tests the creation of a jury payment entry.

    Passes even if no entry is opened b/c it checks data.
    """
    data = JuryPaymentEntryCreator
    monkeypatch.setattr(data, 'save_path', MUNI10_SAVE_PATH)
    mouse_click(main_window.jury_comm_1_admin_radio_btn)
    main_window.cases_tab_widget.setCurrentWidget(main_window.crim_case_search_tab)
    enter_data(main_window.crim_case_search_box, '22TRD01944')
    mouse_click(main_window.crim_get_case_btn)
    mouse_click(main_window.juror_paymentButton)
    enter_data(main_window.dialog.jurors_reported_lineEdit, '20')
    enter_data(main_window.dialog.case_number_lineEdit, 'TEST')
    mouse_click(main_window.dialog.calculate_payment_Button)
    mouse_click(main_window.dialog.create_entry_Button)
    assert main_window.dialog.entry_case_information.jury_panel_total_pay == '635'
    assert main_window.dialog.entry_case_information.case_number == '22TRD01944TEST'
