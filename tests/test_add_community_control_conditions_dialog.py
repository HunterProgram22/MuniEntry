from conftest import mouse_click
from package.controllers import AddCommunityControlDialog


def start_add_conditions_dialog(jail_dialog, qtbot):
    mouse_click(jail_dialog.add_conditions_Button)
    add_conditions = AddCommunityControlDialog(jail_dialog)
    qtbot.addWidget(add_conditions)
    return add_conditions


def test_add_conditions(jail_dialog, qtbot):
    add_conditions = start_add_conditions_dialog(jail_dialog, qtbot)
    assert add_conditions.windowTitle() == "Community Control Terms"


def test_license_suspension_conditions_checked(jail_dialog, qtbot):
    mouse_click(jail_dialog.license_suspension_checkBox)
    add_conditions = start_add_conditions_dialog(jail_dialog, qtbot)
    assert add_conditions.license_suspension_frame.isEnabled() == True


def test_license_suspension_conditions_unchecked(jail_dialog, qtbot):
    add_conditions = start_add_conditions_dialog(jail_dialog, qtbot)
    assert add_conditions.license_suspension_frame.isEnabled() == False


def test_community_service_conditions_checked(jail_dialog, qtbot):
    mouse_click(jail_dialog.community_service_checkBox)
    add_conditions = start_add_conditions_dialog(jail_dialog, qtbot)
    assert add_conditions.community_service_frame.isEnabled() == True


def test_community_service_conditions_unchecked(jail_dialog, qtbot):
    add_conditions = start_add_conditions_dialog(jail_dialog, qtbot)
    assert add_conditions.community_service_frame.isEnabled() == False


def test_other_conditions_checked(jail_dialog, qtbot):
    mouse_click(jail_dialog.other_conditions_checkBox)
    add_conditions = start_add_conditions_dialog(jail_dialog, qtbot)
    assert add_conditions.other_conditions_frame.isEnabled() == True


def test_other_conditions_unchecked(jail_dialog, qtbot):
    add_conditions = start_add_conditions_dialog(jail_dialog, qtbot)
    assert add_conditions.other_conditions_frame.isEnabled() == False


def test_community_control_checked(jail_dialog, qtbot):
    mouse_click(jail_dialog.community_control_checkBox)
    add_conditions = start_add_conditions_dialog(jail_dialog, qtbot)
    assert add_conditions.community_control_frame.isEnabled() == True


def test_community_control_unchecked(jail_dialog, qtbot):
    add_conditions = start_add_conditions_dialog(jail_dialog, qtbot)
    assert add_conditions.community_control_frame.isEnabled() == False