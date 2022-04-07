from tests.conftest import mouse_click, enter_data
from package.controllers import AddConditionsDialog


# TESTS
def test_no_jail_plea_dialog_with_arraignment_case(njp_dialog):
    assert njp_dialog.windowTitle() == "No Jail Plea Case Information"


def test_no_jail_plea_dialog_add_all_conditions_frames_work(njp_dialog, qtbot):
    mouse_click(njp_dialog.license_suspension_checkBox)
    mouse_click(njp_dialog.community_service_checkBox)
    mouse_click(njp_dialog.other_conditions_checkBox)
    add_conditions = AddConditionsDialog(njp_dialog)
    qtbot.addWidget(add_conditions)
    assert add_conditions.license_suspension_frame.isEnabled() == True
    assert add_conditions.community_service_frame.isEnabled() == True
    assert add_conditions.other_conditions_frame.isEnabled() == True


def test_no_jail_plea_dialog_add_all_conditions_check_data(njp_dialog, qtbot):
    mouse_click(njp_dialog.license_suspension_checkBox)
    mouse_click(njp_dialog.community_service_checkBox)
    mouse_click(njp_dialog.other_conditions_checkBox)
    add_conditions = AddConditionsDialog(njp_dialog)
    qtbot.addWidget(add_conditions)
    enter_data(add_conditions.license_type_box, 'hunting')
    enter_data(add_conditions.community_service_hours_ordered_box, '30')
    enter_data(add_conditions.other_conditions_textEdit, 'This is a test!')
    mouse_click(add_conditions.add_conditions_Button)
    assert njp_dialog.entry_case_information.community_service.hours_of_service == '30'
    assert njp_dialog.entry_case_information.license_suspension.license_type == 'hunting'
    assert njp_dialog.entry_case_information.other_conditions.terms == 'This is a test!'
    mouse_click(njp_dialog.guilty_all_Button)
    mouse_click(njp_dialog.create_entry_Button)
