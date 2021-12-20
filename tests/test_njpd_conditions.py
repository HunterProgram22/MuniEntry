from conftest import mouse_click, enter_data
from controllers.conditions_dialogs import AddConditionsDialog


# TESTS
def test_no_jail_plea_dialog_with_arraignment_case(app, njpd):
    assert njpd.windowTitle() == "No Jail Plea Case Information"


def test_no_jail_plea_dialog_add_all_conditions_frames_work(app, njpd, qtbot):
    mouse_click(njpd.license_suspension_checkBox)
    mouse_click(njpd.community_service_checkBox)
    mouse_click(njpd.other_conditions_checkBox)
    adcd = AddConditionsDialog(njpd)
    qtbot.addWidget(adcd)
    assert adcd.license_suspension_frame.isEnabled() == True
    assert adcd.community_service_frame.isEnabled() == True
    assert adcd.other_conditions_frame.isEnabled() == True


def test_no_jail_plea_dialog_add_all_conditions_check_data(app, njpd, qtbot):
    mouse_click(njpd.license_suspension_checkBox)
    mouse_click(njpd.community_service_checkBox)
    mouse_click(njpd.other_conditions_checkBox)
    app_conditions = AddConditionsDialog(njpd)
    qtbot.addWidget(app_conditions)
    enter_data(app_conditions.license_type_box, 'hunting')
    enter_data(app_conditions.community_service_hours_ordered_box, '30')
    enter_data(app_conditions.other_conditions_plainTextEdit, 'This is a test!')
    mouse_click(app_conditions.add_conditions_Button)
    assert njpd.entry_case_information.community_service.hours_of_service == 30
    assert njpd.entry_case_information.license_suspension.license_type == 'hunting'
    assert njpd.entry_case_information.other_conditions.terms == 'This is a test!'
    mouse_click(njpd.guilty_all_Button)
    mouse_click(njpd.create_entry_Button)
