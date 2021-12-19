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
from controllers.not_guilty_bond_dialogs import NotGuiltyBondDialog
from controllers.conditions_dialogs import AddSpecialBondConditionsDialog
from settings import create_arraignments_database_connection

TODAY = date.today()
arraignments_database = create_arraignments_database_connection()

"""Functions for Testing"""


@pytest.fixture
def app(qtbot):
    app = MuniEntry_app.Window(arraignments_database)
    qtbot.addWidget(app)
    QtBot.mouseClick(app.bunner_radioButton, QtCore.Qt.LeftButton)
    QtBot.keyClicks(app.arraignment_cases_box, '21TRD09200')
    QtBot.mouseClick(app.NotGuiltyBondButton, QtCore.Qt.LeftButton)
    app = NotGuiltyBondDialog(app.judicial_officer, app.case_to_load)
    qtbot.addWidget(app)
    return app


"""TESTING"""


def test_not_guilty_bond_dialog_with_arraignment_case(app):
    assert app.windowTitle() == "Not Guilty Bond Case Information"


def test_not_guilty_bond_conditions_all(app):
    QtBot.mouseClick(app.alcohol_test_kiosk_checkBox, QtCore.Qt.LeftButton)
    QtBot.mouseClick(app.alcohol_drugs_assessment_checkBox, QtCore.Qt.LeftButton)
    QtBot.mouseClick(app.no_alcohol_drugs_checkBox, QtCore.Qt.LeftButton)
    QtBot.mouseClick(app.monitoring_checkBox, QtCore.Qt.LeftButton)
    QtBot.mouseClick(app.specialized_docket_checkBox, QtCore.Qt.LeftButton)
    QtBot.mouseClick(app.not_guilty_all_Button, QtCore.Qt.LeftButton)
    QtBot.mouseClick(app.create_entry_Button, QtCore.Qt.LeftButton)
    assert app.entry_case_information.fta_bond_conditions.alcohol_test_kiosk == True
    assert app.entry_case_information.fta_bond_conditions.alcohol_drugs_assessment == True
    assert app.entry_case_information.fta_bond_conditions.no_alcohol_drugs == True
    assert app.entry_case_information.fta_bond_conditions.monitoring == True
    assert app.entry_case_information.fta_bond_conditions.monitoring_type == "GPS Only"
    assert app.entry_case_information.fta_bond_conditions.specialized_docket == True



# def test_no_jail_plea_dialog_add_all_conditions_check_data(app, qtbot, set_case):
#     dialog = start_no_jail_plea_dialog(qtbot, app.judicial_officer, app.case_to_load)
#     QtBot.mouseClick(dialog.license_suspension_checkBox, QtCore.Qt.LeftButton)
#     QtBot.mouseClick(dialog.community_service_checkBox, QtCore.Qt.LeftButton)
#     QtBot.mouseClick(dialog.other_conditions_checkBox, QtCore.Qt.LeftButton)
#     dialog_conditions = start_add_conditions_dialog(qtbot, dialog)
#     QtBot.keyClicks(dialog_conditions.license_type_box, 'hunting')
#     QtBot.keyClicks(dialog_conditions.community_service_hours_ordered_box, '30')
#     QtBot.keyClicks(dialog_conditions.other_conditions_plainTextEdit, 'This is a test!')
#     QtBot.mouseClick(dialog_conditions.add_conditions_Button, QtCore.Qt.LeftButton)
#     assert dialog.entry_case_information.community_service.hours_of_service == 30
#     assert dialog.entry_case_information.license_suspension.license_type == 'hunting'
#     assert dialog.entry_case_information.other_conditions.terms == 'This is a test!'
#     QtBot.mouseClick(dialog.guilty_all_Button, QtCore.Qt.LeftButton)
#     QtBot.mouseClick(dialog.create_entry_Button, QtCore.Qt.LeftButton)
