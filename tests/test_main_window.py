import pytest
from PyQt5 import QtCore

from munientry.settings import VERSION_NUMBER
from tests.conftest import mouse_click, enter_data

main_window_all_button_test_list = [
    ("FineOnlyPleaButton", "Fine Only Plea Case Information"),
    ("JailCCPleaButton", "Jail Community Control Plea Case Information"),
    ("DiversionButton", "Diversion Plea Case Information"),

    ("NotGuiltyBondButton", "Not Guilty Bond Case Information"),
    ("PleaOnlyButton", "Plea Future Sentencing Case Information"),

    ("NoPleaBondButton", "No Plea Bond Case Information"),
    ("BondHearingButton", "Bond Hearing Case Information"),
    ("ProbationViolationBondButton", "Community Control Violation Bond Case Information"),

    ("LeapAdmissionButton", "LEAP Admission Plea Case Information"),
    ("LeapAdmissionValidButton", "LEAP Plea - Already Valid Case Information"),
    ("LeapSentencingButton", "LEAP Sentencing Case Information"),

    ("TrialSentencingButton", "Trial Sentencing Case Information"),
    ("SentencingOnlyButton", "Sentencing Only Case Information"),

    ("FailureToAppearButton", "Failure To Appear Case Information"),
    ("FreeformEntryButton", "Freeform Entry Case Information"),

    ("final_jury_hearingEntryButton", "Notice Of Hearing Entry Hemmeter Case Information"),
    ("general_hearingEntryButton", "General Notice of Hearing Information"),
    ("trial_to_court_hearingEntryButton", "Trial To Court Hearing Notice Case Information"),
    ("rohrer_schedulingEntryButton", "Rohrer Scheduling Entry Case Information"),
    ("hemmeter_schedulingEntryButton", "Hemmeter Scheduling Entry Case Information"),
]


def test_window_opens(qtbot, main_window_noclose):
    """Use main_window_no_close here because this already closes the window and using
    the main_window fixture causes the next test to error because the window is closed
    when it runs."""
    main_window_noclose.show()
    assert main_window_noclose.windowTitle() == f"MuniEntry - Version {VERSION_NUMBER}"


@pytest.mark.parametrize("test_input, dialog_title", main_window_all_button_test_list)
def test_all_entry_buttons_with_no_case(qtbot, main_window, test_input, dialog_title):
    mouse_click(main_window.hemmeter_radioButton)
    mouse_click(main_window.arraignments_radioButton)
    mouse_click(getattr(main_window, test_input))
    assert main_window.dialog.windowTitle() == dialog_title
    assert main_window.dialog.case_number_lineEdit.text() == ""


@pytest.mark.parametrize("test_input, dialog_title", main_window_all_button_test_list)
def test_all_entry_buttons_with_case(qtbot, main_window, test_input, dialog_title):
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, "Barkschat - 21TRC05611")
    mouse_click(getattr(main_window, test_input))
    assert main_window.dialog.case_number_lineEdit.text() == "21TRC05611"


main_window_all_daily_case_lists = [
    ("arraignments_radioButton", "Conkey - 22TRD01944", "arraignments_cases_box"),
    ("slated_radioButton", "Henderson - 20TRC09471", "slated_cases_box"),
    ("final_pretrial_radioButton", "Coyan - 21TRC08121", "final_pretrial_cases_box"),
    ("pleas_radioButton", "Barkschat - 21TRC05611", "pleas_cases_box"),
    ("trials_to_court_radioButton", "Borham - 17TRD22590", "trials_to_court_cases_box"),
    ("pcvh_fcvh_radioButton", "Miller - 21TRD09812", "pcvh_fcvh_cases_box"),
]


@pytest.mark.parametrize("case_list_button, case_number, case_list_box", main_window_all_daily_case_lists)
def test_all_daily_cases_lists_load(qtbot, main_window_noclose, case_list_button, case_number, case_list_box):
    mouse_click(main_window_noclose.kudela_radioButton)
    mouse_click(getattr(main_window_noclose, case_list_button))
    enter_data(getattr(main_window_noclose, case_list_box), case_number)
    assert getattr(main_window_noclose, case_list_box).currentText() == case_number


daily_case_list_appearance_reasons = [
    ("arraignments_radioButton", "Borham - 17TRD22590", "arraignments_cases_box", "arraignment", "FineOnlyPleaButton"),
    ("slated_radioButton", "Henderson - 20TRC09471", "slated_cases_box", "arraignment", "NotGuiltyBondButton"),
    ("final_pretrial_radioButton", "Ansley - 21CRB01597", "final_pretrial_cases_box", "a change of plea", "JailCCPleaButton"),
    ("pleas_radioButton", "Barkschat - 21TRC05611", "pleas_cases_box", "a change of plea", "JailCCPleaButton"),
    ("trials_to_court_radioButton", "Gregory - 22TRC00568", "trials_to_court_cases_box", "a change of plea", "JailCCPleaButton"),
    ("pcvh_fcvh_radioButton", "Miller - 21TRD09812", "pcvh_fcvh_cases_box", "Preliminary Community Control Violation Hearing", "ProbationViolationBondButton"),
]


@pytest.mark.parametrize("case_list_button, case_number, case_list_box, appearance_reason, entry_button", daily_case_list_appearance_reasons)
def test_correct_appearance_reason_is_set(qtbot, main_window, case_list_button, case_number, case_list_box, appearance_reason, entry_button):
    mouse_click(main_window.bunner_radioButton)
    mouse_click(getattr(main_window, case_list_button))
    enter_data(getattr(main_window, case_list_box), case_number)
    mouse_click(getattr(main_window, entry_button))
    assert main_window.dialog.appearance_reason_box.currentText() == appearance_reason


def test_delete_case_from_daily_case_list(qtbot, main_window_noclose):
    """This test uses the test databases so counts may differ if compared to main databases."""
    mouse_click(main_window_noclose.bunner_radioButton)
    mouse_click(main_window_noclose.final_pretrial_radioButton)
    enter_data(main_window_noclose.final_pretrial_cases_box, "Barkschat - 21TRC05611")
    qtbot.keyPress(main_window_noclose.final_pretrial_cases_box, QtCore.Qt.Key_Delete)
    assert len(main_window_noclose.final_pretrial_cases_box) == 11


daily_case_list_case_counts = [
    ("arraignments_radioButton", "Borham - 17TRD22590", "arraignments_cases_box", 9, 8),
    ("slated_radioButton", "Henderson - 20TRC09471", "slated_cases_box", 12, 11),
    ("final_pretrial_radioButton", "Ansley - 21CRB01597", "final_pretrial_cases_box", 12, 11),
    ("pleas_radioButton", "Barkschat - 21TRC05611", "pleas_cases_box", 12, 11),
    ("trials_to_court_radioButton", "Gregory - 22TRC00568", "trials_to_court_cases_box", 7, 6),
    ("pcvh_fcvh_radioButton", "Miller - 21TRD09812", "pcvh_fcvh_cases_box", 14, 13),
]

@pytest.mark.parametrize("case_list_button, case_number, case_list_box, initial_count, delete_count", daily_case_list_case_counts)
def test_reload_case_lists(qtbot, main_window_noclose, case_list_button, case_list_box, case_number, initial_count, delete_count):
    """This test uses the test databases so counts may differ if compared to main databases."""
    mouse_click(main_window_noclose.rohrer_radioButton)
    mouse_click(getattr(main_window_noclose, case_list_button))
    enter_data(getattr(main_window_noclose, case_list_box), case_number)
    assert len(getattr(main_window_noclose, case_list_box)) == initial_count
    qtbot.keyPress(getattr(main_window_noclose, case_list_box), QtCore.Qt.Key_Delete)
    assert len(getattr(main_window_noclose, case_list_box)) == delete_count
    mouse_click(main_window_noclose.reload_cases_Button)
    assert len(getattr(main_window_noclose, case_list_box)) == initial_count

