import pytest
from PyQt5.QtCore import QTimer
from conftest import mouse_click, enter_data


@pytest.fixture
def fop_dialog(qtbot, main_window):
    """Fine Only Plea Dialog is fop_dialog"""
    mouse_click(main_window.hemmeter_radioButton)
    mouse_click(main_window.arraignments_radioButton)
    mouse_click(main_window.FineOnlyPleaButton)
    return main_window.dialog


def test_dialog_opens(fop_dialog):
    assert fop_dialog.windowTitle() == "Fine Only Plea Case Information"
