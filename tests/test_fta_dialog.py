import pytest
from PyQt5.QtCore import QTimer
from conftest import mouse_click, enter_data


def test_dialog_opens(qtbot, dialog):

    assert dialog.windowTitle() == "Failure To Appear Case Information"
