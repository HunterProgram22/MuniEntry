import pytest




current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


import MuniEntry_app
import main_window
from package.controllers.charges_dialogs import AddChargeDialog
from package.controllers.main_entry_dialogs import DiversionPleaDialog, JailCCPleaDialog, FineOnlyPleaDialog, \
    NotGuiltyBondDialog


def open_daily_case_list_db_connection():
    return QSqlDatabase.database("con_daily_case_lists", open=True)


daily_case_list_database = open_daily_case_list_db_connection()

def enter_data(field, data: str):
    return QtBot.keyClicks(field, data)

def mouse_click(button):
    return QtBot.mouseClick(button, QtCore.Qt.LeftButton)


@pytest.fixture
def app(qtbot):
    app = main_window.Window(daily_case_list_database)
    qtbot.addWidget(app)
    mouse_click(app.bunner_radioButton)
    mouse_click(app.arraignments_radioButton)
    enter_data(app.arraignment_cases_box, 'ROWEDDA - 21TRD09200')
    return app


@pytest.fixture
def app_nocase(qtbot):
    app = main_window.Window(daily_case_list_database)
    qtbot.addWidget(app)
    mouse_click(app.arraignments_radioButton)
    mouse_click(app.bunner_radioButton)
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
    app = FineOnlyPleaDialog(app.judicial_officer, app.case_to_load)
    qtbot.addWidget(app)
    return app


@pytest.fixture
def njp_dialog_nocase(app_nocase, qtbot):
    mouse_click(app_nocase.NoJailPleaButton)
    app_nocase = FineOnlyPleaDialog(app_nocase.judicial_officer, app_nocase.case_to_load)
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
def diversion_dialog(app, qtbot):
    mouse_click(app.DiversionButton)
    app = DiversionPleaDialog(app.judicial_officer, app.case_to_load)
    qtbot.addWidget(app)
    return app


@pytest.fixture
def diversion_dialog_nocase(app_nocase, qtbot):
    mouse_click(app_nocase.DiversionButton)
    app_nocase = DiversionPleaDialog(app_nocase.judicial_officer, app_nocase.case_to_load)
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
def njp_add_case_information(njp_dialog_nocase):
    enter_data(njp_dialog_nocase.case_number_lineEdit, "21TRC1234")
    enter_data(njp_dialog_nocase.defendant_first_name_lineEdit, "John")
    enter_data(njp_dialog_nocase.defendant_last_name_lineEdit, "Smith")

@pytest.fixture
def ngb_add_case_information(ngb_dialog_nocase):
    enter_data(ngb_dialog_nocase.case_number_lineEdit, "21TRC1234")
    enter_data(ngb_dialog_nocase.defendant_first_name_lineEdit, "John")
    enter_data(ngb_dialog_nocase.defendant_last_name_lineEdit, "Smith")