from tests.conftest import mouse_click, enter_data

scheduling_dialog_buttons = [
    # Scheduling Entries
    ("hemmeter_final_jury_hearingButton", "Final And Jury Notice Of Hearing Entry Case Information - Judge Marianne T. Hemmeter"),
    ("rohrer_final_jury_hearingButton", "Final And Jury Notice Of Hearing Entry Case Information - Judge Kyle E. Rohrer"),

    ("hemmeter_general_hearingButton", "General Notice Of Hearing Entry Case Information - Judge Marianne T. Hemmeter"),
    ("rohrer_general_hearingButton", "General Notice Of Hearing Entry Case Information - Judge Kyle E. Rohrer"),

    ("hemmeter_trial_court_hearingButton", "Trial To Court Notice Of Hearing Entry Case Information - Judge Marianne T. Hemmeter"),
    ("rohrer_trial_court_hearingButton", "Trial To Court Notice Of Hearing Entry Case Information - Judge Kyle E. Rohrer"),

    ("rohrer_schedulingEntryButton", "Rohrer Scheduling Entry Case Information"),
    ("hemmeter_schedulingEntryButton", "Hemmeter Scheduling Entry Case Information"),

]


@pytest.mark.parametrize("test_input, dialog_title", scheduling_dialog_buttons)
def test_scheduling_dialog_buttons_no_case_selected(qtbot, main_window, test_input, dialog_title):
    mouse_click(main_window.patterson_radioButton)
    mouse_click(main_window.arraignments_radioButton)
    mouse_click(getattr(main_window, test_input))
    assert main_window.dialog.windowTitle() == dialog_title
    assert main_window.dialog.case_number_lineEdit.text() == ""


@pytest.mark.parametrize("test_input, dialog_title", scheduling_dialog_buttons)
def test_all_scheduling_entry_buttons_with_case_from_daily_case_list(qtbot, main_window, test_input, dialog_title):
    mouse_click(main_window.dattilo_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, "Barkschat - 21TRC05611")
    mouse_click(getattr(main_window, test_input))
    assert main_window.dialog.case_number_lineEdit.text() == "21TRC05611"


@pytest.mark.parametrize("test_input, dialog_title", scheduling_dialog_buttons)
def test_all_scheduling_entry_buttons_with_case_from_case_search(qtbot, main_window, test_input, dialog_title):
    mouse_click(main_window.patterson_radioButton)
    main_window.search_tabWidget.setCurrentWidget(main_window.case_search_tab)
    enter_data(main_window.case_search_box, "22TRD01955")
    mouse_click(main_window.get_case_Button)
    mouse_click(getattr(main_window, test_input))
    assert main_window.dialog.case_number_lineEdit.text() == "22TRD01955"
    assert main_window.dialog.defendant_last_name_lineEdit.text() == 'Mahan'