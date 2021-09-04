import pytest
import os, sys, inspect
from time import sleep

from pytestqt.plugin import QtBot
from PyQt5 import QtCore

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import MuniEntry_app
from controllers.CriminalDialogs import (
    CaseInformationDialog,
)
from controllers.MinorMisdemeanorDialogs import (
    MinorMisdemeanorDialog,
)

"""Functions for Testing"""
def add_case_information(dialog):
    QtBot.keyClicks(dialog.case_number_lineEdit, "21TRC1234")
    QtBot.keyClicks(dialog.defendant_first_name_lineEdit, "John")
    QtBot.keyClicks(dialog.defendant_last_name_lineEdit, "Smith")

def start_minor_misdemeanor_dialog(qtbot, judicial_officer):
    dialog = MinorMisdemeanorDialog(judicial_officer)
    qtbot.addWidget(dialog)
    add_case_information(dialog)
    return dialog

@pytest.fixture
def app(qtbot):
    test_MuniEntry_app = MuniEntry_app.Window()
    qtbot.addWidget(test_MuniEntry_app)
    return test_MuniEntry_app

@pytest.fixture
def dialog(app, qtbot):
    QtBot.mouseClick(app.MinorMisdemeanorTrafficButton, QtCore.Qt.LeftButton)
    dialog = start_minor_misdemeanor_dialog(qtbot, app.judicial_officer)
    return dialog

"""TESTING"""
def test_open_minor_misdemeanor_dialog(app, dialog):
    assert dialog.windowTitle() == "Minor Misdemeanor Case Information"

def test_case_information_dialog(app, dialog):
    assert dialog.case_number_lineEdit.text() == "21TRC1234"
    assert dialog.defendant_first_name_lineEdit.text() == "John"
    assert dialog.defendant_last_name_lineEdit.text() == "Smith"

def test_offense_to_statute(app, dialog):
    QtBot.keyClicks(dialog.offense_choice_box, "Speeding > 25 mph")
    assert dialog.statute_choice_box.currentText() == "R.C.4511.21(B)(2)"
    assert dialog.degree_choice_box.currentText() == "MM"
    QtBot.keyClicks(dialog.offense_choice_box, "Driving Under Suspension")
    assert dialog.statute_choice_box.currentText() == "R.C. 4510.11"
    assert dialog.degree_choice_box.currentText() == "M2"
