import pytest
import os
import sys
import inspect

from pytestqt.plugin import QtBot
from PyQt5 import QtCore

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import MuniEntry_app
from controllers.no_jail_plea_dialogs import (
    NoJailPleaDialog,
    AmendOffenseDialog,
)
from settings import create_arraignments_database_connection

arraignments_database = create_arraignments_database_connection()

"""Functions for Testing"""
def start_no_jail_plea_dialog(qtbot, judicial_officer, case):
    dialog = NoJailPleaDialog(judicial_officer, case)
    qtbot.addWidget(dialog)
    return dialog

def start_amend_offense_dialog(qtbot, dialog):
    button_index = 0  # Set to 0 for first charge in list for texting
    dialog = AmendOffenseDialog(dialog, dialog.entry_case_information, button_index)
    qtbot.addWidget(dialog)
    return dialog

@pytest.fixture
def app(qtbot):
    test_MuniEntry_app = MuniEntry_app.Window(arraignments_database)
    qtbot.addWidget(test_MuniEntry_app)
    return test_MuniEntry_app

@pytest.fixture
def dialog(app, qtbot):
    QtBot.mouseClick(app.bunner_radioButton, QtCore.Qt.LeftButton)
    QtBot.keyClicks(app.arraignment_cases_box, '21TRD09200')
    QtBot.mouseClick(app.NoJailPleaButton, QtCore.Qt.LeftButton)
    dialog = start_no_jail_plea_dialog(qtbot, app.judicial_officer, app.case_to_load)
    return dialog


"""TESTING"""
def test_amend_offense_title(qtbot, dialog):
    QtBot.mouseClick(dialog.charges_gridLayout.itemAtPosition(8, 2).widget(), QtCore.Qt.LeftButton)
    dialog = start_amend_offense_dialog(qtbot, dialog)
    assert dialog.windowTitle() == "Amend Charge"


def test_case_information_dialog(qtbot, dialog):
    QtBot.mouseClick(dialog.charges_gridLayout.itemAtPosition(8, 2).widget(), QtCore.Qt.LeftButton)
    dialog = start_amend_offense_dialog(qtbot, dialog)
    assert dialog.case_number_label.text() == "21TRD09200"
    assert dialog.defendant_name_label.text() == "State of Ohio v. BRANDON ROWEDDA"


def test_amend_offense_granted(qtbot, dialog):
    QtBot.mouseClick(dialog.charges_gridLayout.itemAtPosition(8, 2).widget(), QtCore.Qt.LeftButton)
    dialog_amend = start_amend_offense_dialog(qtbot, dialog)
    dialog_amend.motion_decision_box.setCurrentText("Granted")
    assert dialog_amend.motion_decision_box.currentText() == "Granted"
    QtBot.mouseClick(dialog_amend.amend_offense_Button, QtCore.Qt.LeftButton)
    QtBot.mouseClick(dialog.guilty_all_Button, QtCore.Qt.LeftButton)
    QtBot.mouseClick(dialog.create_entry_Button, QtCore.Qt.LeftButton)


def test_amend_offense_denied(qtbot, dialog):
    QtBot.mouseClick(dialog.charges_gridLayout.itemAtPosition(8, 2).widget(), QtCore.Qt.LeftButton)
    dialog_amend = start_amend_offense_dialog(qtbot, dialog)
    dialog_amend.motion_decision_box.setCurrentText("Denied")
    assert dialog_amend.motion_decision_box.currentText() == "Denied"
    QtBot.mouseClick(dialog_amend.amend_offense_Button, QtCore.Qt.LeftButton)
    QtBot.mouseClick(dialog.no_contest_all_Button, QtCore.Qt.LeftButton)
    QtBot.mouseClick(dialog.create_entry_Button, QtCore.Qt.LeftButton)
