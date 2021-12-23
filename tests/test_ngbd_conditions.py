from conftest import mouse_click, enter_data
from controllers.conditions_dialogs import AddSpecialBondConditionsDialog


# TESTS
def test_not_guilty_bond_dialog_with_arraignment_case(ngb_dialog):
    assert ngb_dialog.windowTitle() == "Not Guilty Bond Case Information"


def test_not_guilty_bond_conditions_all(ngb_dialog):
    mouse_click(ngb_dialog.alcohol_test_kiosk_checkBox)
    mouse_click(ngb_dialog.alcohol_drugs_assessment_checkBox)
    mouse_click(ngb_dialog.no_alcohol_drugs_checkBox)
    mouse_click(ngb_dialog.monitoring_checkBox)
    mouse_click(ngb_dialog.specialized_docket_checkBox)
    mouse_click(ngb_dialog.not_guilty_all_Button)
    mouse_click(ngb_dialog.create_entry_Button)
    assert ngb_dialog.entry_case_information.fta_bond_conditions.alcohol_test_kiosk == True
    assert ngb_dialog.entry_case_information.fta_bond_conditions.alcohol_drugs_assessment == True
    assert ngb_dialog.entry_case_information.fta_bond_conditions.no_alcohol_drugs == True
    assert ngb_dialog.entry_case_information.fta_bond_conditions.monitoring == True
    assert ngb_dialog.entry_case_information.fta_bond_conditions.monitoring_type == "GPS Only"
    assert ngb_dialog.entry_case_information.fta_bond_conditions.specialized_docket == True
    assert ngb_dialog.entry_case_information.fta_bond_conditions.specialized_docket_type == "OVI Docket"


def test_not_guilty_bond_special_conditions_checkboxes_all(ngb_dialog, ngbd_check_special_conditions, qtbot):
    special_conditions = AddSpecialBondConditionsDialog(ngb_dialog)
    qtbot.addWidget(special_conditions)
    assert special_conditions.admin_license_suspension_frame.isEnabled() == True
    assert special_conditions.domestic_violence_frame.isEnabled() == True
    assert special_conditions.no_contact_frame.isEnabled() == True
    assert special_conditions.vehicle_seizure_frame.isEnabled() == True
    assert special_conditions.other_conditions_frame.isEnabled() == True
    assert special_conditions.custodial_supervision_frame.isEnabled() == True


def test_not_guilty_bond_special_conditions_data(ngb_dialog, ngbd_check_special_conditions, qtbot):
    special_conditions = AddSpecialBondConditionsDialog(ngb_dialog)
    qtbot.addWidget(special_conditions)
    enter_data(special_conditions.admin_license_suspension_objection_box, 'Yes')
    enter_data(special_conditions.admin_license_suspension_disposition_box, 'Denied')
    enter_data(special_conditions.admin_license_suspension_explanation_box, 'Because I said so!')
    mouse_click(special_conditions.add_special_conditions_Button)
    mouse_click(ngb_dialog.not_guilty_all_Button)
    mouse_click(ngb_dialog.create_entry_Button)
