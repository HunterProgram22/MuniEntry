import pytest
from PyQt5.QtCore import QTimer
from conftest import mouse_click


# dialog_all_title_list = [
#     (pytest.lazy_fixture("njp_dialog"), "Fine Only Plea Case Information"),
#     (pytest.lazy_fixture("njp_dialog_nocase"), "Fine Only Plea Case Information"),
#     (pytest.lazy_fixture("jail_dialog"), "Jail Community Control Plea Case Information"),
#     (pytest.lazy_fixture("jail_dialog_nocase"), "Jail Community Control Plea Case Information"),
#     (pytest.lazy_fixture("ngb_dialog"), "Not Guilty Bond Case Information"),
#     (pytest.lazy_fixture("ngb_dialog_nocase"), "Not Guilty Bond Case Information"),
#     (pytest.lazy_fixture("diversion_dialog"), "Diversion Plea Case Information"),
#     (pytest.lazy_fixture("diversion_dialog_nocase"), "Diversion Plea Case Information"),
# ]

def test_window_opens(qtbot, main_window):
    main_window.show()
    assert main_window.windowTitle() == "MuniEntry - ver 0.15.2"

# def test_judicial_officer_required_warning(qtbot, main_window):
#     mouse_click(main_window.JailCCButton)

def test_all_entry_buttons_with_no_case(qtbot, main_window):
    mouse_click(main_window.hemmeter_radioButton)
    mouse_click(main_window.arraignments_radioButton)
    def handle_dialog():
        while main_window.dialog is None:
            qApp.processEvents()
        qtbot.addWidget(main_window.dialog)
        mouse_click(main_window.dialog.close_dialog_Button)
    QTimer.singleShot(100, handle_dialog)
    mouse_click(main_window.NoJailPleaButton)
    assert main_window.dialog.windowTitle() == "Fine Only Plea Case Information"

