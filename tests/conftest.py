import pytest
from PyQt5.QtSql import QSqlDatabase
from pytestqt.plugin import QtBot
from PyQt5 import QtCore


import MuniEntry_app
from controllers.not_guilty_bond_dialogs import NotGuiltyBondDialog
from controllers.no_jail_plea_dialogs import NoJailPleaDialog

DB_PATH = "C:\\Users\\Justin Kudela\\AppData\\Local\\Programs\\Python\\Python39\\MuniEntry\\resources\\db\\arraignments.sqlite"

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


"""
app = main application window
ngbd = NotGuiltyBondDialog
njpd = NoJailPleaDialog
"""


@pytest.fixture
def app(qtbot):
    app = MuniEntry_app.Window(arraignments_database)
    qtbot.addWidget(app)
    mouse_click(app.bunner_radioButton)
    enter_data(app.arraignment_cases_box, '21TRD09200')
    return app


@pytest.fixture()
def ngb_dialog(app, qtbot):
    mouse_click(app.NotGuiltyBondButton)
    app = NotGuiltyBondDialog(app.judicial_officer, app.case_to_load)
    qtbot.addWidget(app)
    return app


@pytest.fixture()
def njpd(app, qtbot):
    mouse_click(app.NoJailPleaButton)
    app = NoJailPleaDialog(app.judicial_officer, app.case_to_load)
    qtbot.addWidget(app)
    return app


@pytest.fixture
def ngbd_check_special_conditions(ngb_dialog):
    mouse_click(ngb_dialog.domestic_violence_checkBox)
    mouse_click(ngb_dialog.admin_license_suspension_checkBox)
    mouse_click(ngb_dialog.custodial_supervision_checkBox)
    mouse_click(ngb_dialog.vehicle_seizure_checkBox)
    mouse_click(ngb_dialog.no_contact_checkBox)
    mouse_click(ngb_dialog.other_conditions_checkBox)
    mouse_click(ngb_dialog.add_special_conditions_Button)