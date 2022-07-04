import pytest
from tests.conftest import mouse_click, enter_data


@pytest.fixture
def sch_dialog_rohrer(qtbot, main_window):
    mouse_click(main_window.arraignments_radioButton)
    mouse_click(main_window.rohrer_schedulingEntryButton)
    return main_window.dialog


@pytest.fixture
def sch_dialog_hemmeter(qtbot, main_window):
    mouse_click(main_window.arraignments_radioButton)
    mouse_click(main_window.hemmeter_schedulingEntryButton)
    return main_window.dialog


@pytest.fixture
def jury_final_hearing_notice_rohrer(qtbot, main_window):
    mouse_click(main_window.arraignments_radioButton)
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.final_jury_hearingEntryButton)
    return main_window.dialog


@pytest.fixture
def jury_final_hearing_notice_hemmeter(qtbot, main_window):
    mouse_click(main_window.arraignments_radioButton)
    mouse_click(main_window.hemmeter_radioButton)
    mouse_click(main_window.final_jury_hearingEntryButton)
    return main_window.dialog


@pytest.fixture
def trial_to_court_hearing_notice(qtbot, main_window):
    mouse_click(main_window.arraignments_radioButton)
    mouse_click(main_window.hemmeter_radioButton)
    mouse_click(main_window.trial_to_court_hearingEntryButton)
    return main_window.dialog


def test_scheduing_entry_rohrer_opens(qtbot, sch_dialog_rohrer):
    assert sch_dialog_rohrer.windowTitle() == "Rohrer Scheduling Entry Case Information"


def test_scheduing_entry_hemmeter_opens(qtbot, sch_dialog_hemmeter):
    assert sch_dialog_hemmeter.windowTitle() == "Hemmeter Scheduling Entry Case Information"


def test_jury_final_hearing_notice_roher_opens(qtbot, jury_final_hearing_notice_rohrer):
    assert jury_final_hearing_notice_rohrer.windowTitle() == "Final and Jury Notice of Hearing Information"


def test_jury_final_hearing_notice_hemmeter_opens(qtbot, jury_final_hearing_notice_hemmeter):
    assert jury_final_hearing_notice_hemmeter.windowTitle() == "Final and Jury Notice of Hearing Information"


def test_trial_to_court_hearing_notice_opens(qtbot, trial_to_court_hearing_notice):
    assert trial_to_court_hearing_notice.windowTitle() == "Trial To Court Hearing Notice Case Information"
