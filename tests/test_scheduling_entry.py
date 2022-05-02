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


def test_scheduing_entry_rohrer_opens(qtbot, sch_dialog_rohrer):
    assert sch_dialog_rohrer.windowTitle() == "Rohrer Scheduling Entry Case Information"

def test_scheduing_entry_hemmeter_opens(qtbot, sch_dialog_hemmeter):
    assert sch_dialog_hemmeter.windowTitle() == "Hemmeter Scheduling Entry Case Information"

