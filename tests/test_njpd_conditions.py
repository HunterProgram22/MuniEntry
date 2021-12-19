import pytest

import MuniEntry_app
from helper_functions import mouse_click, enter_data
from controllers.no_jail_plea_dialogs import NoJailPleaDialog
from controllers.conditions_dialogs import AddConditionsDialog
from settings import create_arraignments_database_connection

arraignments_database = create_arraignments_database_connection()


@pytest.fixture
def app(qtbot):
    app = MuniEntry_app.Window(arraignments_database)
    qtbot.addWidget(app)
    mouse_click(app.bunner_radioButton)
    enter_data(app.arraignment_cases_box, '21TRD09200')
    mouse_click(app.NoJailPleaButton)
    app = NoJailPleaDialog(app.judicial_officer, app.case_to_load)
    qtbot.addWidget(app)
    return app


# TESTS
def test_no_jail_plea_dialog_with_arraignment_case(app):
    assert app.windowTitle() == "No Jail Plea Case Information"


def test_no_jail_plea_dialog_add_all_conditions_frames_work(app, qtbot):
    mouse_click(app.license_suspension_checkBox)
    mouse_click(app.community_service_checkBox)
    mouse_click(app.other_conditions_checkBox)
    app = AddConditionsDialog(app)
    qtbot.addWidget(app)
    assert app.license_suspension_frame.isEnabled() == True
    assert app.community_service_frame.isEnabled() == True
    assert app.other_conditions_frame.isEnabled() == True


def test_no_jail_plea_dialog_add_all_conditions_check_data(app, qtbot):
    mouse_click(app.license_suspension_checkBox)
    mouse_click(app.community_service_checkBox)
    mouse_click(app.other_conditions_checkBox)
    app_conditions = AddConditionsDialog(app)
    qtbot.addWidget(app_conditions)
    enter_data(app_conditions.license_type_box, 'hunting')
    enter_data(app_conditions.community_service_hours_ordered_box, '30')
    enter_data(app_conditions.other_conditions_plainTextEdit, 'This is a test!')
    mouse_click(app_conditions.add_conditions_Button)
    assert app.entry_case_information.community_service.hours_of_service == 30
    assert app.entry_case_information.license_suspension.license_type == 'hunting'
    assert app.entry_case_information.other_conditions.terms == 'This is a test!'
    mouse_click(app.guilty_all_Button)
    mouse_click(app.create_entry_Button)
