import pytest
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from conftest import mouse_click, enter_data


@pytest.fixture
def com_control_dialog(qtbot, main_window):
    """Add Community Control is comcontrol_dialog. Uses the Jail Dialog
    as the main dialog because that is required."""
    mouse_click(main_window.hemmeter_radioButton)
    mouse_click(main_window.final_pretrial_radioButton)
    mouse_click(main_window.JailCCPleaButton)

    def close_popup_dialog():
        qtbot.addWidget(main_window.dialog.popup_dialog)
        mouse_click(main_window.dialog.popup_dialog.add_conditions_Button)

    QTimer.singleShot(100, close_popup_dialog)
    mouse_click(main_window.dialog.add_conditions_Button)
    return main_window.dialog.popup_dialog


def test_dialog_opens(com_control_dialog):
    assert com_control_dialog.windowTitle() == "Community Control Terms"