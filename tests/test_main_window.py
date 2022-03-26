from conftest import mouse_click


dialog_all_title_list = [
    (pytest.lazy_fixture("njp_dialog"), "Fine Only Plea Case Information"),
    (pytest.lazy_fixture("njp_dialog_nocase"), "Fine Only Plea Case Information"),
    (pytest.lazy_fixture("jail_dialog"), "Jail Community Control Plea Case Information"),
    (pytest.lazy_fixture("jail_dialog_nocase"), "Jail Community Control Plea Case Information"),
    (pytest.lazy_fixture("ngb_dialog"), "Not Guilty Bond Case Information"),
    (pytest.lazy_fixture("ngb_dialog_nocase"), "Not Guilty Bond Case Information"),
    (pytest.lazy_fixture("diversion_dialog"), "Diversion Plea Case Information"),
    (pytest.lazy_fixture("diversion_dialog_nocase"), "Diversion Plea Case Information"),
]

def test_window_opens(qtbot, main_window):
    main_window.show()
    assert main_window.windowTitle() == "MuniEntry - ver 0.15.2"

def test_judicial_officer_required_warning(qtbot, main_window):
    mouse_click(main_window.JailCCButton)

def test_fine_only_dialog_no_case_open(qtbot, main_window):
    mouse_click(main_window.hemmeter_radioButton)
    mouse_click(main_window.arraignments_radioButton)
    mouse_click(main_window.NoJailPleaButton)
    qtbot.addWidget(main_window.dialog)
    assert main_window.dialog.windowTitle() == "Fine Only Plea Case Information"
    mouse_click(main_window.dialog.create_entry_Button)

@pytest.mark.parametrize("test_input, expected", dialog_all_title_list)
def test_dialog_window_title(test_input, expected):
    assert test_input.windowTitle() == expected