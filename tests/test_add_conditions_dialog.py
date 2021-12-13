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
from models.case_information import CaseLoadData
from controllers.no_jail_plea_dialogs import (
    NoJailPleaDialog,
)
from controllers.conditions_dialogs import AddConditionsDialog, AmendOffenseDialog
from settings import create_arraignments_database_connection

arraignments_database = create_arraignments_database_connection()
"""Functions for Testing"""


def start_no_jail_plea_dialog(qtbot, judicial_officer, judicial_officer_type):
    dialog = NoJailPleaDialog(judicial_officer, judicial_officer_type)
    qtbot.addWidget(dialog)
    # add_case_information(dialog)
    return dialog


def start_add_conditions_dialog(qtbot, case_information):
    dialog = AddConditionsDialog(case_information)
    qtbot.addWidget(dialog)
    return dialog


@pytest.fixture
def app(qtbot):
    test_MuniEntry_app = MuniEntry_app.Window(arraignments_database)
    qtbot.addWidget(test_MuniEntry_app)
    return test_MuniEntry_app


@pytest.fixture
def dialog(app, qtbot):
    case = CaseLoadData()
    QtBot.mouseClick(app.bunner_radioButton, QtCore.Qt.LeftButton)
    QtBot.mouseClick(app.NoJailPleaButton, QtCore.Qt.LeftButton)
    dialog = start_no_jail_plea_dialog(qtbot, app.judicial_officer, case)
    return dialog


"""TESTING"""


def test_add_conditions(dialog, qtbot):
    QtBot.mouseClick(dialog.add_conditions_Button, QtCore.Qt.LeftButton)
    dialog = start_add_conditions_dialog(qtbot, dialog)
    assert dialog.windowTitle() == "Additional Conditions"


def test_license_suspension_conditions_checked(dialog, qtbot):
    QtBot.mouseClick(dialog.license_suspension_checkBox, QtCore.Qt.LeftButton)
    QtBot.mouseClick(dialog.add_conditions_Button, QtCore.Qt.LeftButton)
    dialog = start_add_conditions_dialog(qtbot, dialog)
    assert dialog.license_suspension_frame.isEnabled() == True


def test_license_suspension_conditions_unchecked(dialog, qtbot):
    QtBot.mouseClick(dialog.add_conditions_Button, QtCore.Qt.LeftButton)
    dialog = start_add_conditions_dialog(qtbot, dialog)
    assert dialog.license_suspension_frame.isEnabled() == False


def test_community_service_conditions_checked(dialog, qtbot):
    QtBot.mouseClick(dialog.community_service_checkBox, QtCore.Qt.LeftButton)
    QtBot.mouseClick(dialog.add_conditions_Button, QtCore.Qt.LeftButton)
    dialog = start_add_conditions_dialog(qtbot, dialog)
    assert dialog.community_service_frame.isEnabled() == True


def test_community_service_conditions_unchecked(dialog, qtbot):
    QtBot.mouseClick(dialog.add_conditions_Button, QtCore.Qt.LeftButton)
    dialog = start_add_conditions_dialog(qtbot, dialog)
    assert dialog.community_service_frame.isEnabled() == False


def test_other_conditions_checked(dialog, qtbot):
    QtBot.mouseClick(dialog.other_conditions_checkBox, QtCore.Qt.LeftButton)
    QtBot.mouseClick(dialog.add_conditions_Button, QtCore.Qt.LeftButton)
    dialog = start_add_conditions_dialog(qtbot, dialog)
    assert dialog.other_conditions_frame.isEnabled() == True


def test_other_conditions_unchecked(dialog, qtbot):
    QtBot.mouseClick(dialog.add_conditions_Button, QtCore.Qt.LeftButton)
    dialog = start_add_conditions_dialog(qtbot, dialog)
    assert dialog.other_conditions_frame.isEnabled() == False
