import pytest
from tests.conftest import mouse_click


@pytest.fixture
def pcv_dialog(qtbot, main_window):
    """Prelminary Community Control Violation Dialog is pcv_dialog"""
    mouse_click(main_window.hemmeter_radioButton)
    mouse_click(main_window.arraignments_radioButton)
    mouse_click(main_window.ProbationViolationBondButton)
    return main_window.dialog


def test_dialog_opens(pcv_dialog):
    assert pcv_dialog.windowTitle() == "Community Control Violation Bond Case Information"