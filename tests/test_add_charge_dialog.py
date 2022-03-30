import pytest
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from conftest import mouse_click, enter_data


@pytest.fixture
def add_charge_dialog(qtbot, main_window):
    """Add Charge Dialog is add_charge_dialog"""
    mouse_click(main_window.hemmeter_radioButton)
    mouse_click(main_window.arraignments_radioButton)
    mouse_click(main_window.JailCCPleaButton)

    def close_popup_dialog():
        qtbot.addWidget(main_window.dialog.popup_dialog)
        mouse_click(main_window.dialog.popup_dialog.add_charge_Button)

    QTimer.singleShot(100, close_popup_dialog)
    mouse_click(main_window.dialog.add_charge_Button)
    return main_window.dialog.popup_dialog

def test_dialog_opens(add_charge_dialog):
    assert add_charge_dialog.windowTitle() == "Add Charge"
