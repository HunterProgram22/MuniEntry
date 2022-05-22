import pytest
from PyQt5.QtCore import QTimer
from tests.conftest import mouse_click, enter_data


def test_dialog_opens(conditions_dialog):
    assert conditions_dialog.windowTitle() == "Additional Conditions"


all_conditions_checkbox_test_list = [
    ("license_suspension_checkBox", "license_suspension_frame"),
    ("community_service_checkBox", "community_service_frame"),
    ("other_conditions_checkBox", "other_conditions_frame"),
]

@pytest.mark.parametrize("checkBox, frame", all_conditions_checkbox_test_list)
def test_conditions_frames_work_when_condition_checked(qtbot, fop_dialog, checkBox, frame):
    mouse_click(getattr(fop_dialog, checkBox))
    mouse_click(fop_dialog.add_conditions_Button)
    assert getattr(fop_dialog.popup_dialog, frame).isEnabled() == True
