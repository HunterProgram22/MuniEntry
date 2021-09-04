import pytest

import os, sys, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import MuniEntry_app

from time import sleep
from pytestqt.plugin import QtBot
from PyQt5 import QtCore

from controllers.CriminalDialogs import (
    CaseInformationDialog,
)
from controllers.MinorMisdemeanorDialogs import (
    TrafficCaseInformationDialog,
)

"""Functions for Testing"""

@pytest.fixture
def app(qtbot):
    test_MuniEntry_app = MuniEntry_app.Window()
    qtbot.addWidget(test_MuniEntry_app)
    return test_MuniEntry_app


"""TESTING"""
def test_title(app):
    assert app.windowTitle() == "MuniEntry"

def test_judicial_officer_buttons(app):
    assert app.judicial_officer == "Bunner"
    QtBot.mouseClick(app.hemmeter_radioButton, QtCore.Qt.LeftButton)
    assert app.judicial_officer == "Hemmeter"
    QtBot.mouseClick(app.rohrer_radioButton, QtCore.Qt.LeftButton)
    assert app.judicial_officer == "Rohrer"
    QtBot.mouseClick(app.pelanda_radioButton, QtCore.Qt.LeftButton)
    assert app.judicial_officer == "Pelanda"
    QtBot.mouseClick(app.bunner_radioButton, QtCore.Qt.LeftButton)
    assert app.judicial_officer == "Bunner"

def test_minor_misdemeanor_traffic_buton(app):
    QtBot.mouseClick(app.MinorMisdemeanorTrafficButton, QtCore.Qt.LeftButton)

#def test_green_sheet_buton(app):
    #QtBot.mouseClick(app.GreenSheetButton, QtCore.Qt.LeftButton)
