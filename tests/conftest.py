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


"""
INSTRUCTIONS:

Use pytest -m 'not manual' to skip tests that require manual interaction
Use pytest -m 'not create_entry_test' to skip tests that open actual Word docx files

"""


def open_daily_case_list_db_connection():
    return QSqlDatabase.database("con_daily_case_lists", open=True)

def enter_data(field, data: str):
    return QtBot.keyClicks(field, data)

def mouse_click(button):
    return QtBot.mouseClick(button, QtCore.Qt.LeftButton)

def right_click(button):
    return QtBot.mouseClick(button, QtCore.Qt.RightButton)


@pytest.fixture
def main_window(qtbot):
    window = Window()
    qtbot.addWidget(window)

    def close_main_dialog():
        qtbot.addWidget(window.dialog)
        mouse_click(window.dialog.close_dialog_Button)

    QTimer.singleShot(50, close_main_dialog)
    return window


@pytest.fixture
def main_window_noclose(qtbot):
    window = Window()
    qtbot.addWidget(window)
    return window


def check_barkschat(charges, plea):
    assert charges[0].offense == "OVI Alcohol / Drugs 3rd"
    assert charges[0].statute == "4511.19A1A***"
    assert charges[0].degree == "UCM"
    assert charges[0].plea == plea
    assert charges[1].offense == "OVI Refusal 3rd/10yr Prior 20yr"
    assert charges[1].statute == "4511.19A2***"
    assert charges[1].degree == "UCM"
    assert charges[1].plea == plea
    assert charges[2].offense == "Driving In Marked Lanes"
    assert charges[2].statute == "4511.33"
    assert charges[2].degree == "MM"
    assert charges[2].plea == plea

