import pytest
from PyQt6 import QtCore

from munientry.settings.app_settings import VERSION_NUMBER
from tests.conftest import mouse_click, enter_data


def test_window_opens(qtbot, main_window_noclose):
    """Use main_window_no_close here because this already closes the window and using
    the main_window fixture causes the next test to error because the window is closed
    when it runs."""
    main_window_noclose.show()
    assert main_window_noclose.windowTitle() == f"MuniEntry - Version {VERSION_NUMBER}"


main_window_all_daily_case_lists = [
    ("arraignments_radio_btn", "Conkey - 22TRD01944", "arraignments_cases_box"),
    ("slated_radio_btn", "Henderson - 20TRC09471", "slated_cases_box"),
    ("final_pretrial_radio_btn", "Coyan - 21TRC08121", "final_pretrial_cases_box"),
    ("pleas_radio_btn", "Barkschat - 21TRC05611", "pleas_cases_box"),
    ("trials_to_court_radio_btn", "Borham - 17TRD22590", "trials_to_court_cases_box"),
    ("pcvh_fcvh_radio_btn", "Miller - 21TRD09812", "pcvh_fcvh_cases_box"),
]


@pytest.mark.parametrize("case_list_button, case_number, case_list_box", main_window_all_daily_case_lists)
def test_all_daily_cases_lists_load(qtbot, main_window_noclose, case_list_button, case_number, case_list_box):
    mouse_click(main_window_noclose.mag_3_radio_btn)
    mouse_click(getattr(main_window_noclose, case_list_button))
    enter_data(getattr(main_window_noclose, case_list_box), case_number)
    assert getattr(main_window_noclose, case_list_box).currentText() == case_number


daily_case_list_appearance_reasons = [
    ("arraignments_radio_btn", "Borham - 17TRD22590", "arraignments_cases_box", "arraignment", "FineOnlyPleaButton"),
    ("slated_radio_btn", "Henderson - 20TRC09471", "slated_cases_box", "arraignment", "NotGuiltyBondButton"),
    ("final_pretrial_radio_btn", "Henderson - 20TRC09471", "final_pretrial_cases_box", "a change of plea", "JailCCPleaButton"),
    ("pleas_radio_btn", "Barkschat - 21TRC05611", "pleas_cases_box", "a change of plea", "JailCCPleaButton"),
    ("trials_to_court_radio_btn", "Gregory - 22TRC00568", "trials_to_court_cases_box", "a change of plea", "JailCCPleaButton"),
    ("pcvh_fcvh_radio_btn", "Gregory - 22TRC00568", "pcvh_fcvh_cases_box", "Preliminary Community Control Violation Hearing", "ProbationViolationBondButton"),
]


@pytest.mark.parametrize("case_list_button, case_number, case_list_box, appearance_reason, entry_button", daily_case_list_appearance_reasons)
def test_correct_appearance_reason_is_set(qtbot, main_window, case_list_button, case_number, case_list_box, appearance_reason, entry_button):
    mouse_click(main_window.mag_1_radio_btn)
    mouse_click(getattr(main_window, case_list_button))
    enter_data(getattr(main_window, case_list_box), case_number)
    mouse_click(getattr(main_window, entry_button))
    assert main_window.dialog.appearance_reason_box.currentText() == appearance_reason


def test_delete_case_from_daily_case_list(qtbot, main_window_noclose):
    """This test uses the test databases so counts may differ if compared to main databases."""
    mouse_click(main_window_noclose.mag_1_radio_btn)
    mouse_click(main_window_noclose.final_pretrial_radio_btn)
    enter_data(main_window_noclose.final_pretrial_cases_box, "Barkschat - 21TRC05611")
    qtbot.keyPress(main_window_noclose.final_pretrial_cases_box, QtCore.Qt.Key.Key_Delete)
    assert len(main_window_noclose.final_pretrial_cases_box) == 11


daily_case_list_case_counts = [
    ("arraignments_radio_btn", "Borham - 17TRD22590", "arraignments_cases_box", 9, 8),
    ("slated_radio_btn", "Henderson - 20TRC09471", "slated_cases_box", 12, 11),
    ("final_pretrial_radio_btn", "Ansley - 21CRB01597", "final_pretrial_cases_box", 12, 11),
    ("pleas_radio_btn", "Barkschat - 21TRC05611", "pleas_cases_box", 12, 11),
    ("trials_to_court_radio_btn", "Gregory - 22TRC00568", "trials_to_court_cases_box", 12, 11),
    ("pcvh_fcvh_radio_btn", "Miller - 21TRD09812", "pcvh_fcvh_cases_box", 14, 13),
]

@pytest.mark.parametrize("case_list_button, case_number, case_list_box, initial_count, delete_count", daily_case_list_case_counts)
def test_reload_case_lists(qtbot, main_window_noclose, case_list_button, case_list_box, case_number, initial_count, delete_count):
    """This test uses the test databases so counts may differ if compared to main databases."""
    mouse_click(main_window_noclose.judge_2_radio_btn)
    mouse_click(getattr(main_window_noclose, case_list_button))
    enter_data(getattr(main_window_noclose, case_list_box), case_number)
    assert len(getattr(main_window_noclose, case_list_box)) == initial_count
    qtbot.keyPress(getattr(main_window_noclose, case_list_box), QtCore.Qt.Key.Key_Delete)
    assert len(getattr(main_window_noclose, case_list_box)) == delete_count
    mouse_click(main_window_noclose.reload_cases_Button)
    assert len(getattr(main_window_noclose, case_list_box)) == initial_count
