import pytest
import os, sys, inspect
from time import sleep

from pytestqt.plugin import QtBot
from PyQt5 import QtCore

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import MuniEntry_app
from controllers.MinorMisdemeanorDialogs import MinorMisdemeanorDialog


"""Functions for Testing"""
def start_MinorMisdemeanorDialog(qtbot, judicial_officer, judicial_officer_type):
    dialog = MinorMisdemeanorDialog(judicial_officer, judicial_officer_type)
    qtbot.addWidget(dialog)
    return dialog

@pytest.fixture
def app(qtbot):
    test_MuniEntry_app = MuniEntry_app.Window()
    qtbot.addWidget(test_MuniEntry_app)
    return test_MuniEntry_app


"""TESTING"""
def test_title(app):
    assert app.windowTitle() == "MuniEntry"

def test_judicial_officer_buttons(app):
    QtBot.mouseClick(app.hemmeter_radioButton, QtCore.Qt.LeftButton)
    assert app.judicial_officer == "Hemmeter"
    QtBot.mouseClick(app.rohrer_radioButton, QtCore.Qt.LeftButton)
    assert app.judicial_officer == "Rohrer"
    QtBot.mouseClick(app.pelanda_radioButton, QtCore.Qt.LeftButton)
    assert app.judicial_officer == "Pelanda"
    QtBot.mouseClick(app.bunner_radioButton, QtCore.Qt.LeftButton)
    assert app.judicial_officer == "Bunner"

def test_minor_misdemeanor_traffic_buton(app, qtbot):
    QtBot.mouseClick(app.bunner_radioButton, QtCore.Qt.LeftButton)
    QtBot.mouseClick(app.MinorMisdemeanorTrafficButton, QtCore.Qt.LeftButton)
    dialog = start_MinorMisdemeanorDialog(qtbot, app.judicial_officer, app.judicial_officer_type)
    assert dialog.windowTitle() == "Minor Misdemeanor Case Information"

def test_green_sheet_buton(app, qtbot):
    QtBot.mouseClick(app.bunner_radioButton, QtCore.Qt.LeftButton)
    QtBot.mouseClick(app.GreenSheetButton, QtCore.Qt.LeftButton)
    dialog = start_MinorMisdemeanorDialog(qtbot, app.judicial_officer, app.judicial_officer_type)
    assert dialog.windowTitle() == "Minor Misdemeanor Case Information"
