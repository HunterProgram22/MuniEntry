import pytest
from tests.conftest import mouse_click, enter_data


@pytest.fixture
def sch_dialog_rohrer(qtbot, main_window):
    mouse_click(main_window.arraignments_radioButton)
    mouse_click(main_window.dattilo_radioButton)
    mouse_click(main_window.rohrer_schedulingEntryButton)
    return main_window.dialog


@pytest.fixture
def sch_dialog_hemmeter(qtbot, main_window):
    mouse_click(main_window.arraignments_radioButton)
    mouse_click(main_window.patterson_radioButton)
    mouse_click(main_window.hemmeter_schedulingEntryButton)
    return main_window.dialog


@pytest.fixture
def jury_final_hearing_notice_rohrer(qtbot, main_window):
    mouse_click(main_window.arraignments_radioButton)
    mouse_click(main_window.dattilo_radioButton)
    mouse_click(main_window.rohrer_final_jury_hearingButton)
    return main_window.dialog


@pytest.fixture
def jury_final_hearing_notice_hemmeter(qtbot, main_window):
    mouse_click(main_window.arraignments_radioButton)
    mouse_click(main_window.patterson_radioButton)
    mouse_click(main_window.hemmeter_final_jury_hearingButton)
    return main_window.dialog


@pytest.fixture
def trial_to_court_hearing_notice_rohrer(qtbot, main_window):
    mouse_click(main_window.arraignments_radioButton)
    mouse_click(main_window.dattilo_radioButton)
    mouse_click(main_window.rohrer_trial_court_hearingButton)
    return main_window.dialog


@pytest.fixture
def trial_to_court_hearing_notice_hemmeter(qtbot, main_window):
    mouse_click(main_window.arraignments_radioButton)
    mouse_click(main_window.patterson_radioButton)
    mouse_click(main_window.hemmeter_trial_court_hearingButton)
    return main_window.dialog


def test_scheduing_entry_rohrer_opens(qtbot, sch_dialog_rohrer):
    assert sch_dialog_rohrer.windowTitle() == "Rohrer Scheduling Entry Case Information"


def test_scheduing_entry_hemmeter_opens(qtbot, sch_dialog_hemmeter):
    assert sch_dialog_hemmeter.windowTitle() == "Hemmeter Scheduling Entry Case Information"


def test_hemmeter_jury_final_hearing_notice_hemmeter_opens(qtbot, jury_final_hearing_notice_hemmeter):
    assert jury_final_hearing_notice_hemmeter.windowTitle() == "Final And Jury Notice Of Hearing Entry Case Information - Judge Marianne T. Hemmeter"


def test_rohrer_jury_final_hearing_notice_roher_opens(qtbot, jury_final_hearing_notice_rohrer):
    assert jury_final_hearing_notice_rohrer.windowTitle() == "Final And Jury Notice Of Hearing Entry Case Information - Judge Kyle E. Rohrer"


def test_hemmeter_trial_to_court_hearing_notice_opens(qtbot, trial_to_court_hearing_notice_hemmeter):
    assert trial_to_court_hearing_notice_hemmeter.windowTitle() == "Trial To Court Notice Of Hearing Entry Case Information - Judge Marianne T. Hemmeter"


def test_rohrer_trial_to_court_hearing_notice_opens(qtbot, trial_to_court_hearing_notice_rohrer):
    assert trial_to_court_hearing_notice_rohrer.windowTitle() == "Trial To Court Notice Of Hearing Entry Case Information - Judge Kyle E. Rohrer"
