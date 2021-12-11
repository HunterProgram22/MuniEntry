import pytest
import os, sys, inspect
from time import sleep

from pytestqt.plugin import QtBot
from PyQt5 import QtCore

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import MuniEntry_app
from controllers.no_jail_plea_dialogs import NoJailPleaDialog
from controllers.leap_plea_dialogs import LeapPleaLongDialog, LeapPleaShortDialog
from controllers.fta_bond_dialogs import FTABondDialog
from controllers.not_guilty_bond_dialogs import NotGuiltyBondDialog
from settings import create_arraignments_database_connection

arraignments_database = create_arraignments_database_connection()

"""Functions for Testing"""
def start_NoJailPleaDialog(qtbot, judicial_officer, case):
    dialog = NoJailPleaDialog(judicial_officer, case)
    qtbot.addWidget(dialog)
    return dialog

def start_LeapPleaLongDialog(qtbot, judicial_officer, case):
    dialog = LeapPleaLongDialog(judicial_officer, case)
    qtbot.addWidget(dialog)
    return dialog

def start_LeapPleaShortDialog(qtbot, judicial_officer, case):
    dialog = LeapPleaShortDialog(judicial_officer, case)
    qtbot.addWidget(dialog)
    return dialog

def start_FTABondDialog(qtbot, judicial_officer, case):
    dialog = FTABondDialog(judicial_officer, case)
    qtbot.addWidget(dialog)
    return dialog

def start_NotGuiltyBondDialog(qtbot, judicial_officer, case):
    dialog = NotGuiltyBondDialog(judicial_officer, case)
    qtbot.addWidget(dialog)
    return dialog

@pytest.fixture
def app(qtbot):
    test_MuniEntry_app = MuniEntry_app.Window(arraignments_database)
    qtbot.addWidget(test_MuniEntry_app)
    return test_MuniEntry_app


"""TESTING"""
def test_title(app):
    assert app.windowTitle() == "MuniEntry - ver 0.4.0-alpha"

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

def test_no_jail_plea_button(app, qtbot):
    QtBot.mouseClick(app.bunner_radioButton, QtCore.Qt.LeftButton)
    QtBot.mouseClick(app.NoJailPleaButton, QtCore.Qt.LeftButton)
    case = "16TRC00001"
    dialog = start_NoJailPleaDialog(qtbot, app.judicial_officer, case)
    assert dialog.windowTitle() == "No Jail Plea Case Information"

def test_leap_plea_button(app, qtbot):
    QtBot.mouseClick(app.hemmeter_radioButton, QtCore.Qt.LeftButton)
    QtBot.mouseClick(app.LeapPleaLongButton, QtCore.Qt.LeftButton)
    case = "16TRC00001"
    dialog = start_LeapPleaLongDialog(qtbot, app.judicial_officer, case)
    assert dialog.windowTitle() == "Leap Plea Case Information"

def test_leap_plea_court_complete_button(app, qtbot):
    QtBot.mouseClick(app.hemmeter_radioButton, QtCore.Qt.LeftButton)
    QtBot.mouseClick(app.LeapPleaShortButton, QtCore.Qt.LeftButton)
    case = "16TRC00001"
    dialog = start_LeapPleaShortDialog(qtbot, app.judicial_officer, case)
    assert dialog.windowTitle() == "Leap Plea Pre-Court Completion Case Information"

def test_fta_bond_button(app, qtbot):
    QtBot.mouseClick(app.rohrer_radioButton, QtCore.Qt.LeftButton)
    QtBot.mouseClick(app.FTABondButton, QtCore.Qt.LeftButton)
    case = "16TRC00001"
    dialog = start_FTABondDialog(qtbot, app.judicial_officer, case)
    assert dialog.windowTitle() == "FTA Bond Case Information"

def test_not_guilty_bond_button(app, qtbot):
    QtBot.mouseClick(app.pelanda_radioButton, QtCore.Qt.LeftButton)
    QtBot.mouseClick(app.NotGuiltyBondButton, QtCore.Qt.LeftButton)
    case = "16TRC00001"
    dialog = start_NotGuiltyBondDialog(qtbot, app.judicial_officer, case)
    assert dialog.windowTitle() == "Not Guilty Bond Case Information"
