from conftest import mouse_click, enter_data
from controllers.conditions_dialogs import AddSpecialBondConditionsDialog


# TESTS
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


def test_not_guilty_bond_special_conditions_checkboxes_all(app, check_special_conditions, qtbot):
    app = AddSpecialBondConditionsDialog(app)
    qtbot.addWidget(app)
    assert app.admin_license_suspension_frame.isEnabled() == True
    assert app.domestic_violence_frame.isEnabled() == True
    assert app.no_contact_frame.isEnabled() == True
    assert app.vehicle_seizure_frame.isEnabled() == True
    assert app.other_conditions_frame.isEnabled() == True
    assert app.custodial_supervision_frame.isEnabled() == True


def test_not_guilty_bond_special_conditions_data(app, check_special_conditions, qtbot):
    app_conditions = AddSpecialBondConditionsDialog(app)
    qtbot.addWidget(app_conditions)
    enter_data(app_conditions.admin_license_suspension_objection_box, 'Yes')
    enter_data(app_conditions.admin_license_suspension_disposition_box, 'Denied')
    enter_data(app_conditions.admin_license_suspension_explanation_box, 'Because I said so!')
    mouse_click(app_conditions.add_special_conditions_Button)
    mouse_click(app.not_guilty_all_Button)
    mouse_click(app.create_entry_Button)
