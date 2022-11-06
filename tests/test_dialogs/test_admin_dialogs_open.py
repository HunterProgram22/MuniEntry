from tests.conftest import mouse_click, enter_data

admin_with_cases_dialog_buttons = [
    # Admin Entries
    ('limited_driving_privilegesButton', 'Driving Privileges Entry Case Information'),
    ('juror_paymentButton', 'Juror Payment'),
]


@pytest.mark.parametrize("test_input, dialog_title", admin_with_cases_dialog_buttons)
def test_admin_dialog_buttons_no_case_selected(qtbot, main_window, test_input, dialog_title):
    mouse_click(main_window.assn_comm_patterson_radioButton)
    mouse_click(main_window.arraignments_radioButton)
    mouse_click(getattr(main_window, test_input))
    assert main_window.dialog.windowTitle() == dialog_title
    assert main_window.dialog.case_number_lineEdit.text() == ""


@pytest.mark.parametrize("test_input, dialog_title", admin_with_cases_dialog_buttons)
def test_all_admin_entry_buttons_with_case_from_daily_case_list(qtbot, main_window, test_input, dialog_title):
    mouse_click(main_window.assn_comm_dattilo_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, "Barkschat - 21TRC05611")
    mouse_click(getattr(main_window, test_input))
    assert main_window.dialog.case_number_lineEdit.text() == "21TRC05611"


main_window_admin_noncase_button_test_list = [
    # Admin Non Case Entries
    ('fiscal_entriesButton', 'Admin Fiscal Entry Information'),
]


@pytest.mark.parametrize("test_input, dialog_title", main_window_admin_noncase_button_test_list)
def test_all_admin_entry_noncase_dialogs(qtbot, main_window, test_input, dialog_title):
    mouse_click(main_window.court_admin_kudela_radioButton)
    mouse_click(getattr(main_window, test_input))
    assert main_window.dialog.account_number_box.currentText() == "Indigent Alcohol Monitoring - 24115000"


@pytest.mark.parametrize("test_input, dialog_title", admin_with_cases_dialog_buttons)
def test_all_admin_entry_buttons_with_case_from_case_search(qtbot, main_window, test_input, dialog_title):
    mouse_click(main_window.assn_comm_patterson_radioButton)
    main_window.search_tabWidget.setCurrentWidget(main_window.case_search_tab)
    enter_data(main_window.case_search_box, "22TRD01955")
    mouse_click(main_window.get_case_Button)
    mouse_click(getattr(main_window, test_input))
    assert main_window.dialog.case_number_lineEdit.text() == "22TRD01955"
    assert main_window.dialog.defendant_last_name_lineEdit.text() == 'Mahan'