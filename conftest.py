import os
import sys
import inspect

import pytest
from pytestqt.plugin import QtBot
from PyQt5.QtWidgets import QApplication
from PyQt5.QtSql import QSqlDatabase
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QTimer

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import MuniEntry_app
from main_window import Window


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

    def close_main_dialog():
        qtbot.addWidget(window.dialog)
        mouse_click(window.dialog.close_dialog_Button)

    QTimer.singleShot(100, close_main_dialog)
    return window


@pytest.fixture
def main_window_noclose(qtbot):
    daily_case_list_database = open_daily_case_list_db_connection()
    window = Window(daily_case_list_database)
    qtbot.addWidget(window)
    return window

