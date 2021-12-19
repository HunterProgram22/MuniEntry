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


def mouse_click(button):
    return QtBot.mouseClick(button, QtCore.Qt.LeftButton)

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


@pytest.fixture
def conditions(app):
    QtBot.mouseClick(app.domestic_violence_checkBox, QtCore.Qt.LeftButton)
    QtBot.mouseClick(app.admin_license_suspension_checkBox, QtCore.Qt.LeftButton)
    QtBot.mouseClick(app.custodial_supervision_checkBox, QtCore.Qt.LeftButton)
    QtBot.mouseClick(app.vehicle_seizure_checkBox, QtCore.Qt.LeftButton)
    QtBot.mouseClick(app.no_contact_checkBox, QtCore.Qt.LeftButton)
    QtBot.mouseClick(app.other_conditions_checkBox, QtCore.Qt.LeftButton)
    QtBot.mouseClick(app.add_special_conditions_Button, QtCore.Qt.LeftButton)

"""TESTING"""


def test_not_guilty_bond_dialog_with_arraignment_case(app):
    assert app.windowTitle() == "Not Guilty Bond Case Information"


def test_not_guilty_bond_conditions_all(app):
    mouse_click(app.alcohol_test_kiosk_checkBox)
    mouse_click(app.alcohol_drugs_assessment_checkBox)
    mouse_click(app.no_alcohol_drugs_checkBox)
    mouse_click(app.monitoring_checkBox)
    mouse_click(app.specialized_docket_checkBox)
    mouse_click(app.not_guilty_all_Button)
    mouse_click(app.create_entry_Button)
    assert app.entry_case_information.fta_bond_conditions.alcohol_test_kiosk == True
    assert app.entry_case_information.fta_bond_conditions.alcohol_drugs_assessment == True
    assert app.entry_case_information.fta_bond_conditions.no_alcohol_drugs == True
    assert app.entry_case_information.fta_bond_conditions.monitoring == True
    assert app.entry_case_information.fta_bond_conditions.monitoring_type == "GPS Only"
    assert app.entry_case_information.fta_bond_conditions.specialized_docket == True
    assert app.entry_case_information.fta_bond_conditions.specialized_docket_type == "OVI Docket"


def test_not_guilty_bond_special_conditions_checkboxes_all(app, conditions, qtbot):
    app = AddSpecialBondConditionsDialog(app)
    qtbot.addWidget(app)
    assert app.admin_license_suspension_frame.isEnabled() == True
    assert app.domestic_violence_frame.isEnabled() == True
    assert app.no_contact_frame.isEnabled() == True
    assert app.vehicle_seizure_frame.isEnabled() == True
    assert app.other_conditions_frame.isEnabled() == True
    assert app.custodial_supervision_frame.isEnabled() == True


def test_not_guilty_bond_special_conditions_data(app, conditions, qtbot):
    app_conditions = AddSpecialBondConditionsDialog(app)
    qtbot.addWidget(app_conditions)
    QtBot.keyClicks(app_conditions.admin_license_suspension_objection_box, 'Yes')
    QtBot.keyClicks(app_conditions.admin_license_suspension_disposition_box, 'Denied')
    QtBot.keyClicks(app_conditions.admin_license_suspension_explanation_box, 'Because I said so!')
    mouse_click(app_conditions.add_special_conditions_Button)
    mouse_click(app.not_guilty_all_Button)
    mouse_click(app.create_entry_Button)