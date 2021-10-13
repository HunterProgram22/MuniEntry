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
from controllers.minor_misdemeanor_dialogs import (
    MinorMisdemeanorDialog,
    AddConditionsDialog,
    AmendOffenseDialog,
)


"""Functions for Testing"""
def start_minor_misdemeanor_dialog(qtbot, judicial_officer, judicial_officer_type):
    dialog = MinorMisdemeanorDialog(judicial_officer, judicial_officer_type)
    qtbot.addWidget(dialog)
    add_case_information(dialog)
    return dialog

def add_case_information(dialog):
    QtBot.keyClicks(dialog.case_number_lineEdit, "21TRC1234")
    QtBot.keyClicks(dialog.defendant_first_name_lineEdit, "John")
    QtBot.keyClicks(dialog.defendant_last_name_lineEdit, "Smith")
    QtBot.keyClicks(dialog.operator_license_number_lineEdit, "TF180780")

def start_amend_offense_dialog(qtbot, dialog):
    dialog = AmendOffenseDialog(dialog.case_information)
    qtbot.addWidget(dialog)
    return dialog

@pytest.fixture
def app(qtbot):
    test_MuniEntry_app = MuniEntry_app.Window()
    qtbot.addWidget(test_MuniEntry_app)
    return test_MuniEntry_app

@pytest.fixture
def dialog(app, qtbot):
    QtBot.mouseClick(app.bunner_radioButton, QtCore.Qt.LeftButton)
    QtBot.mouseClick(app.MinorMisdemeanorTrafficButton, QtCore.Qt.LeftButton)
    dialog = start_minor_misdemeanor_dialog(qtbot, app.judicial_officer, app.judicial_officer_type)
    return dialog


"""TESTING"""
def test_amend_offense_title(qtbot, dialog):
    QtBot.mouseClick(dialog.amend_offense_Button, QtCore.Qt.LeftButton)
    dialog = start_amend_offense_dialog(qtbot, dialog)
    dialog.windowTitle() == "Amend Charge"

def test_case_information_dialog(qtbot, dialog):
    QtBot.mouseClick(dialog.amend_offense_Button, QtCore.Qt.LeftButton)
    dialog = start_amend_offense_dialog(qtbot, dialog)
    assert dialog.case_number_label.text() == "21TRC1234"
    assert dialog.defendant_name_label.text() == "State of Ohio v. John Smith"
    assert dialog.defendant_attorney_name_label.text() == "Attorney: None"

def test_amend_offense_granted(qtbot, dialog):
    QtBot.mouseClick(dialog.amend_offense_Button, QtCore.Qt.LeftButton)
    dialog = start_amend_offense_dialog(qtbot, dialog)
    dialog.motion_decision_box.setCurrentText("Granted")
    assert dialog.motion_decision_box.currentText() == "Granted"

def test_amend_offense_denied(qtbot, dialog):
    QtBot.mouseClick(dialog.amend_offense_Button, QtCore.Qt.LeftButton)
    dialog = start_amend_offense_dialog(qtbot, dialog)
    dialog.motion_decision_box.setCurrentText("Denied")
    assert dialog.motion_decision_box.currentText() == "Denied"
