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
def test_amend_offense(qtbot, dialog):
    QtBot.mouseClick(dialog.amend_offense_Button, QtCore.Qt.LeftButton)
    dialog = start_amend_offense_dialog(qtbot, dialog)
    dialog.windowTitle() == "Amend Charge"

#def test_license_suspension_conditions_checked(dialog, qtbot):
#    QtBot.mouseClick(dialog.license_suspension_checkBox, QtCore.Qt.LeftButton)
#    dialog = start_add_conditions_dialog(qtbot, dialog)
#    assert dialog.license_suspension_frame.isEnabled() == True
#    QtBot.mouseClick(dialog.continue_Button, QtCore.Qt.LeftButton)
