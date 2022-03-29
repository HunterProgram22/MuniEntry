import pytest
from PyQt5.QtCore import QTimer
from conftest import mouse_click, enter_data


@pytest.fixture
def div_dialog(qtbot, main_window):
    """Diversion Plea Dialog is div_dialog"""
    mouse_click(main_window.hemmeter_radioButton)
    mouse_click(main_window.arraignments_radioButton)

    def close_dialog():
        qtbot.addWidget(main_window.dialog)
        mouse_click(main_window.dialog.close_dialog_Button)

    QTimer.singleShot(100, close_dialog)
    mouse_click(main_window.DiversionButton)
    return main_window.dialog


def test_dialog_opens(div_dialog):
    assert div_dialog.windowTitle() == "Diversion Plea Case Information"