import pytest
from PyQt5.QtCore import QTimer
from conftest import mouse_click, enter_data


main_window_all_button_test_list = [
    ("FineOnlyPleaButton", "Fine Only Plea Case Information"),
    ("JailCCPleaButton", "Jail Community Control Plea Case Information"),
    ("NotGuiltyBondButton", "Not Guilty Bond Case Information"),
    ("FailureToAppearButton", "Failure To Appear Case Information"),
    ("DiversionButton", "Diversion Plea Case Information"),
    ("ProbationViolationBondButton", "Community Control Violation Bond Case Information"),
]


def test_window_opens(qtbot, main_window):
    main_window.show()
    assert main_window.windowTitle() == "MuniEntry - ver 0.15.2"


def test_judicial_officer_required_warning(qtbot, main_window):
    mouse_click(main_window.JailCCPleaButton)


def test_daily_case_list_required_warning(qtbot, main_window):
    mouse_click(main_window.bunner_radioButton)
    mouse_click(main_window.FineOnlyPleaButton)


@pytest.mark.parametrize("test_input, dialog_title", main_window_all_button_test_list)
def test_all_entry_buttons_with_no_case(qtbot, main_window, test_input, dialog_title):
    mouse_click(main_window.hemmeter_radioButton)
    mouse_click(main_window.arraignments_radioButton)

    def handle_dialog():
        while main_window.dialog is None:
            qApp.processEvents()
        qtbot.addWidget(main_window.dialog)
        mouse_click(main_window.dialog.close_dialog_Button)

    QTimer.singleShot(100, handle_dialog)
    mouse_click(getattr(main_window, test_input))
    assert main_window.dialog.windowTitle() == dialog_title
    assert main_window.dialog.case_number_lineEdit.text() == ""


@pytest.mark.parametrize("test_input, dialog_title", main_window_all_button_test_list)
def test_all_entry_buttons_with_case(qtbot, main_window, test_input, dialog_title):
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, "Barkschat - 21TRC05611")

    def handle_dialog():
        while main_window.dialog is None:
            qApp.processEvents()
        qtbot.addWidget(main_window.dialog)
        mouse_click(main_window.dialog.close_dialog_Button)

    QTimer.singleShot(100, handle_dialog)
    mouse_click(getattr(main_window, test_input))
    assert main_window.dialog.case_number_lineEdit.text() == "21TRC05611"
