import pytest
import os
import sys
import inspect
from PyQt5.QtSql import QSqlDatabase
from pytestqt.plugin import QtBot
from PyQt5 import QtCore

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import MuniEntry_app
from controllers.not_guilty_bond_dialogs import NotGuiltyBondDialog
from controllers.sentencing_dialogs import NoJailPleaDialog, JailCCPleaDialog
from controllers.leap_plea_dialogs import LeapPleaShortDialog, LeapPleaLongDialog

# Home Path - Comment out when at work
DB_PATH = "C:\\Users\\Justin Kudela\\AppData\\Local\\Programs\\Python\\Python39\\MuniEntry\\resources\\db\\arraignments.sqlite"
# Work Path - Comment out when at home
# DB_PATH = "C:\\Users\\jkudela\\AppData\\Local\\Programs\\Python\\Python310\\MuniEntry\\resources\\db\\arraignments.sqlite"

def create_arraignments_database_connection():
    """This is a duplicate version of the function in settings.py. It is used because of issues with Path.
    Opens a connection to the database and returns that connection to the arraignments_database."""
    arraignments_database_connection = QSqlDatabase.addDatabase("QSQLITE", "cases")
    arraignments_database_connection.setDatabaseName(DB_PATH)
    return arraignments_database_connection

arraignments_database = create_arraignments_database_connection()

def enter_data(field, data: str):
    return QtBot.keyClicks(field, data)

def mouse_click(button):
    return QtBot.mouseClick(button, QtCore.Qt.LeftButton)


@pytest.fixture
def app(qtbot):
    app = MuniEntry_app.Window(arraignments_database)
    qtbot.addWidget(app)
    mouse_click(app.bunner_radioButton)
    enter_data(app.arraignment_cases_box, '21TRD09200')
    return app


@pytest.fixture
def app_nocase(qtbot):
    app = MuniEntry_app.Window(arraignments_database)
    qtbot.addWidget(app)
    mouse_click(app.bunner_radioButton)
    return app


@pytest.fixture
def ngb_dialog(app, qtbot):
    mouse_click(app.NotGuiltyBondButton)
    app = NotGuiltyBondDialog(app.judicial_officer, app.case_to_load)
    qtbot.addWidget(app)
    return app


@pytest.fixture
def leap_long_dialog(app, qtbot):
    mouse_click(app.LeapPleaLongButton)
    app = LeapPleaLongDialog(app.judicial_officer, app.case_to_load)
    qtbot.addWidget(app)
    return app


@pytest.fixture
def leap_short_dialog(app, qtbot):
    mouse_click(app.LeapPleaShortButton)
    app = LeapPleaShortDialog(app.judicial_officer, app.case_to_load)
    qtbot.addWidget(app)
    return app


@pytest.fixture
def ngb_dialog(app, qtbot):
    mouse_click(app.NotGuiltyBondButton)
    app = NotGuiltyBondDialog(app.judicial_officer, app.case_to_load)
    qtbot.addWidget(app)
    return app


@pytest.fixture
def ngb_dialog_nocase(app_nocase, qtbot):
    mouse_click(app_nocase.NotGuiltyBondButton)
    app_nocase = NotGuiltyBondDialog(app_nocase.judicial_officer, app_nocase.case_to_load)
    qtbot.addWidget(app_nocase)
    return app_nocase


@pytest.fixture
def njp_dialog(app, qtbot):
    mouse_click(app.NoJailPleaButton)
    app = NoJailPleaDialog(app.judicial_officer, app.case_to_load)
    qtbot.addWidget(app)
    return app


@pytest.fixture
def njp_dialog_nocase(app_nocase, qtbot):
    mouse_click(app_nocase.NoJailPleaButton)
    app_nocase = NoJailPleaDialog(app_nocase.judicial_officer, app_nocase.case_to_load)
    qtbot.addWidget(app_nocase)
    return app_nocase


@pytest.fixture
def jail_dialog(app, qtbot):
    mouse_click(app.JailCCButton)
    app = JailCCPleaDialog(app.judicial_officer, app.case_to_load)
    qtbot.addWidget(app)
    return app


@pytest.fixture
def jail_dialog_nocase(app_nocase, qtbot):
    mouse_click(app_nocase.JailCCButton)
    app_nocase = JailCCPleaDialog(app_nocase.judicial_officer, app_nocase.case_to_load)
    qtbot.addWidget(app_nocase)
    return app_nocase


@pytest.fixture
def ngbd_check_special_conditions(ngb_dialog):
    mouse_click(ngb_dialog.domestic_violence_checkBox)
    mouse_click(ngb_dialog.admin_license_suspension_checkBox)
    mouse_click(ngb_dialog.custodial_supervision_checkBox)
    mouse_click(ngb_dialog.vehicle_seizure_checkBox)
    mouse_click(ngb_dialog.no_contact_checkBox)
    mouse_click(ngb_dialog.other_conditions_checkBox)
    mouse_click(ngb_dialog.add_special_conditions_Button)


@pytest.fixture
def add_case_information(dialog):
    enter_data(dialog.case_number_lineEdit, "21TRC1234")
    enter_data(dialog.defendant_first_name_lineEdit, "John")
    enter_data(dialog.defendant_last_name_lineEdit, "Smith")