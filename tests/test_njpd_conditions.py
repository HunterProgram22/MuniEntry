import pytest
import os
import sys
import inspect
from datetime import date

from pytestqt.plugin import QtBot
from PyQt5 import QtCore

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import MuniEntry_app
from controllers.no_jail_plea_dialogs import (
    NoJailPleaDialog,
)
from controllers.conditions_dialogs import AddConditionsDialog, AmendOffenseDialog
from settings import create_arraignments_database_connection

TODAY = date.today()
arraignments_database = create_arraignments_database_connection()

"""Functions for Testing"""
def add_case_information(dialog):
    QtBot.keyClicks(dialog.case_number_lineEdit, "21TRC1234")
    QtBot.keyClicks(dialog.defendant_first_name_lineEdit, "John")
    QtBot.keyClicks(dialog.defendant_last_name_lineEdit, "Smith")

def start_no_jail_plea_dialog(qtbot, judicial_officer, case):
    dialog = NoJailPleaDialog(judicial_officer, case)
    qtbot.addWidget(dialog)
    # add_case_information(dialog)
    return dialog

def start_amendment_dialog(qtbot, case_information):
    dialog = AmendOffenseDialog(case_information)
    qtbot.addWidget(dialog)
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
    QtBot.mouseClick(app.bunner_radioButton, QtCore.Qt.LeftButton)
    QtBot.mouseClick(app.NoJailPleaButton, QtCore.Qt.LeftButton)
    dialog = start_no_jail_plea_dialog(qtbot, app.judicial_officer, app.case_to_load)
    return dialog

@pytest.fixture
def set_case(app, qtbot):
    QtBot.mouseClick(app.bunner_radioButton, QtCore.Qt.LeftButton)
    QtBot.keyClicks(app.arraignment_cases_box, '21TRD09200')
    QtBot.mouseClick(app.NoJailPleaButton, QtCore.Qt.LeftButton)


"""TESTING"""

def test_no_jail_plea_dialog_with_arraignment_case(app, qtbot, set_case):
    dialog = start_no_jail_plea_dialog(qtbot, app.judicial_officer, app.case_to_load)
    assert dialog.windowTitle() == "No Jail Plea Case Information"


def test_no_jail_plea_dialog_add_all_conditions_frames_work(app, qtbot, set_case):
    dialog = start_no_jail_plea_dialog(qtbot, app.judicial_officer, app.case_to_load)
    QtBot.mouseClick(dialog.license_suspension_checkBox, QtCore.Qt.LeftButton)
    QtBot.mouseClick(dialog.community_service_checkBox, QtCore.Qt.LeftButton)
    QtBot.mouseClick(dialog.other_conditions_checkBox, QtCore.Qt.LeftButton)
    dialog_conditions = start_add_conditions_dialog(qtbot, dialog)
    assert dialog_conditions.license_suspension_frame.isEnabled() == True
    assert dialog_conditions.community_service_frame.isEnabled() == True
    assert dialog_conditions.other_conditions_frame.isEnabled() == True


def test_no_jail_plea_dialog_add_all_conditions_check_data(app, qtbot, set_case):
    dialog = start_no_jail_plea_dialog(qtbot, app.judicial_officer, app.case_to_load)
    QtBot.mouseClick(dialog.license_suspension_checkBox, QtCore.Qt.LeftButton)
    QtBot.mouseClick(dialog.community_service_checkBox, QtCore.Qt.LeftButton)
    QtBot.mouseClick(dialog.other_conditions_checkBox, QtCore.Qt.LeftButton)
    dialog_conditions = start_add_conditions_dialog(qtbot, dialog)
    QtBot.keyClicks(dialog_conditions.license_type_box, 'hunting')
    QtBot.keyClicks(dialog_conditions.community_service_hours_ordered_box, '30')
    QtBot.keyClicks(dialog_conditions.other_conditions_plainTextEdit, 'This is a test!')
    QtBot.mouseClick(dialog_conditions.add_conditions_Button, QtCore.Qt.LeftButton)
    assert dialog.entry_case_information.community_service.hours_of_service == 30
    assert dialog.entry_case_information.license_suspension.license_type == 'hunting'
    assert dialog.entry_case_information.other_conditions.terms == 'This is a test!'
    QtBot.mouseClick(dialog.guilty_all_Button, QtCore.Qt.LeftButton)
    QtBot.mouseClick(dialog.create_entry_Button, QtCore.Qt.LeftButton)









