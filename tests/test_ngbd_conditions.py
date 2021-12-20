from conftest import mouse_click, enter_data
from controllers.conditions_dialogs import AddSpecialBondConditionsDialog


# TESTS
def test_not_guilty_bond_dialog_with_arraignment_case(app, ngbd):
    assert ngbd.windowTitle() == "Not Guilty Bond Case Information"


def test_not_guilty_bond_conditions_all(app, ngbd):
    mouse_click(ngbd.alcohol_test_kiosk_checkBox)
    mouse_click(ngbd.alcohol_drugs_assessment_checkBox)
    mouse_click(ngbd.no_alcohol_drugs_checkBox)
    mouse_click(ngbd.monitoring_checkBox)
    mouse_click(ngbd.specialized_docket_checkBox)
    mouse_click(ngbd.not_guilty_all_Button)
    mouse_click(ngbd.create_entry_Button)
    assert ngbd.entry_case_information.fta_bond_conditions.alcohol_test_kiosk == True
    assert ngbd.entry_case_information.fta_bond_conditions.alcohol_drugs_assessment == True
    assert ngbd.entry_case_information.fta_bond_conditions.no_alcohol_drugs == True
    assert ngbd.entry_case_information.fta_bond_conditions.monitoring == True
    assert ngbd.entry_case_information.fta_bond_conditions.monitoring_type == "GPS Only"
    assert ngbd.entry_case_information.fta_bond_conditions.specialized_docket == True
    assert ngbd.entry_case_information.fta_bond_conditions.specialized_docket_type == "OVI Docket"


def test_not_guilty_bond_special_conditions_checkboxes_all(app, ngbd, ngbd_check_special_conditions, qtbot):
    sbcd = AddSpecialBondConditionsDialog(ngbd)
    qtbot.addWidget(sbcd)
    assert sbcd.admin_license_suspension_frame.isEnabled() == True
    assert sbcd.domestic_violence_frame.isEnabled() == True
    assert sbcd.no_contact_frame.isEnabled() == True
    assert sbcd.vehicle_seizure_frame.isEnabled() == True
    assert sbcd.other_conditions_frame.isEnabled() == True
    assert sbcd.custodial_supervision_frame.isEnabled() == True


def test_not_guilty_bond_special_conditions_data(app, ngbd, ngbd_check_special_conditions, qtbot):
    sbcd = AddSpecialBondConditionsDialog(ngbd)
    qtbot.addWidget(sbcd)
    enter_data(sbcd.admin_license_suspension_objection_box, 'Yes')
    enter_data(sbcd.admin_license_suspension_disposition_box, 'Denied')
    enter_data(sbcd.admin_license_suspension_explanation_box, 'Because I said so!')
    mouse_click(sbcd.add_special_conditions_Button)
    mouse_click(ngbd.not_guilty_all_Button)
    mouse_click(ngbd.create_entry_Button)
