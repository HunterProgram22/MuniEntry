import pytest
from tests.conftest import mouse_click, enter_data


@pytest.fixture
def sch_dialog(qtbot, main_window):
    mouse_click(main_window.ac_dattilo_radioButton)
    mouse_click(main_window.schedulingEntryButton)
    return main_window.dialog


def test_scheduing_entry_opens(qtbot, sch_dialog):
    assert sch_dialog.windowTitle() == "Scheduling Entry Information"
