import pytest
from PyQt5.QtCore import QTimer
from conftest import mouse_click, enter_data


@pytest.fixture
def jcp_dialog(qtbot, main_window):
    """Jail CC Plea Dialog is jcp_dialog"""
    mouse_click(main_window.hemmeter_radioButton)
    mouse_click(main_window.arraignments_radioButton)
    #
    # def close_dialog():
    #     qtbot.addWidget(main_window.dialog)
    #     mouse_click(main_window.dialog.close_dialog_Button)
    #
    # QTimer.singleShot(100, close_dialog)
    mouse_click(main_window.JailCCPleaButton)
    return main_window.dialog


def test_dialog_opens(jcp_dialog):
    assert jcp_dialog.windowTitle() == "Jail Community Control Plea Case Information"