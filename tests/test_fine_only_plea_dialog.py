import pytest
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore, QtWidgets
from pytestqt.plugin import QtBot
from conftest import mouse_click, enter_data



@pytest.fixture
def fop_dialog(qtbot, main_window):
    """Fine Only Plea Dialog = fop_dialog"""
    mouse_click(main_window.hemmeter_radioButton)
    mouse_click(main_window.arraignments_radioButton)

    def handle_dialog():
        while main_window.dialog is None:
            qApp.processEvents()
        qtbot.addWidget(main_window.dialog)
        mouse_click(main_window.dialog.close_dialog_Button)

    QTimer.singleShot(100, handle_dialog)
    mouse_click(main_window.FineOnlyPleaButton)
    return main_window.dialog

def test_dialog_opens(qtbot, fop_dialog):
    assert fop_dialog.windowTitle() == "Fine Only Plea Case Information"