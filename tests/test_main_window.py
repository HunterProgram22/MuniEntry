import os
import sys
import inspect

import pytest
from pytestqt.plugin import QtBot
from PyQt5.QtSql import QSqlDatabase
from PyQt5 import QtCore

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import MuniEntry_app
from main_window import Window

from PyQt5.QtWidgets import QMessageBox
from package.views.custom_widgets import (
    WarningBox,
    RequiredBox,
    TwoChoiceQuestionBox,
    JailWarningBox,
)


def open_daily_case_list_db_connection():
    return QSqlDatabase.database("con_daily_case_lists", open=True)

def enter_data(field, data: str):
    return QtBot.keyClicks(field, data)

def mouse_click(button):
    return QtBot.mouseClick(button, QtCore.Qt.LeftButton)


@pytest.fixture
def main_window(qtbot):
    daily_case_list_database = open_daily_case_list_db_connection()
    window = Window(daily_case_list_database)
    qtbot.addWidget(window)
    return window


def test_window_opens(qtbot, main_window):
    assert main_window.windowTitle() == "MuniEntry - ver 0.15.2"

def test_judicial_officer_required_warning(qtbot, monkeypatch, main_window):
    #mouse_click(main_window.JailCCButton)
    message = RequiredBox("test")
    qtbot.addWidget(message)
    assert message.windowTitle() == "Required"
