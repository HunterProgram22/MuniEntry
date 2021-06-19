import pytest

from pytestqt.plugin import QtBot
from PyQt5 import QtCore

import MuniEntry_app


@pytest.fixture
def app(qtbot):
    test_MuniEntry_app = MuniEntry_app.Window()
    qtbot.addWidget(test_MuniEntry_app)
    return test_MuniEntry_app


def test_title(app):
    assert app.windowTitle() == "MuniEntry"


def test_final_judgment_buton(app):
    QtBot.mouseClick(app.FinalJudgmentEntryButton, QtCore.Qt.LeftButton)
