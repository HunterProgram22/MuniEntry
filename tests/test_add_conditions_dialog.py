import pytest
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from conftest import mouse_click, enter_data


@pytest.fixture
def conditions_dialog(qtbot, main_window):
    """Add Conditions is comcontrol_dialog. Uses the Fine Only
    as the main dialog because that is required."""
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.arraignments_radioButton)
    mouse_click(main_window.FineOnlyPleaButton)

    def close_popup_dialog():
        qtbot.addWidget(main_window.dialog.popup_dialog)
        mouse_click(main_window.dialog.popup_dialog.add_conditions_Button)

    QTimer.singleShot(100, close_popup_dialog)
    mouse_click(main_window.dialog.add_conditions_Button)
    return main_window.dialog.popup_dialog


def test_dialog_opens(conditions_dialog):
    assert conditions_dialog.windowTitle() == "Additional Conditions"