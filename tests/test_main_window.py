import pytest
import os, sys, inspect
from time import sleep

from pytestqt.plugin import QtBot
from PyQt5 import QtCore

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import MuniEntry_app
from controllers.minor_misdemeanor_dialogs import MinorMisdemeanorDialog
from settings import create_arraignments_database_connection

arraignments_database = create_arraignments_database_connection()

"""Functions for Testing"""
def start_MinorMisdemeanorDialog(qtbot, judicial_officer, case):
    dialog = MinorMisdemeanorDialog(judicial_officer, case)
    qtbot.addWidget(dialog)
    return dialog

@pytest.fixture
def app(qtbot):
    test_MuniEntry_app = MuniEntry_app.Window(arraignments_database)
    qtbot.addWidget(test_MuniEntry_app)
    return test_MuniEntry_app


"""TESTING"""
def test_title(app):
    assert app.windowTitle() == "MuniEntry - ver 0.2.1"

def test_judicial_officer_buttons(app):
    QtBot.mouseClick(app.hemmeter_radioButton, QtCore.Qt.LeftButton)
    assert app.judicial_officer.last_name == "Hemmeter"
    QtBot.mouseClick(app.rohrer_radioButton, QtCore.Qt.LeftButton)
    assert app.judicial_officer.last_name == "Rohrer"
    QtBot.mouseClick(app.pelanda_radioButton, QtCore.Qt.LeftButton)
    assert app.judicial_officer.last_name == "Pelanda"
    QtBot.mouseClick(app.bunner_radioButton, QtCore.Qt.LeftButton)
    assert app.judicial_officer.last_name == "Bunner"
    QtBot.mouseClick(app.kudela_radioButton, QtCore.Qt.LeftButton)
    assert app.judicial_officer.last_name == "Kudela"

def test_minor_misdemeanor_traffic_buton(app, qtbot):
    QtBot.mouseClick(app.bunner_radioButton, QtCore.Qt.LeftButton)
    QtBot.mouseClick(app.MinorMisdemeanorTrafficButton, QtCore.Qt.LeftButton)
    case = "16TRC00001"
    dialog = start_MinorMisdemeanorDialog(qtbot, app.judicial_officer, case)
    assert dialog.windowTitle() == "Minor Misdemeanor Case Information"
