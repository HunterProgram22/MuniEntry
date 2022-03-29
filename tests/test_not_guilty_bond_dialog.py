import pytest
from PyQt5.QtCore import QTimer
from conftest import mouse_click, enter_data


@pytest.fixture
def ngb_dialog(qtbot, main_window):
    """Not Guilty Bond Dialog is ngb_dialog"""
    mouse_click(main_window.hemmeter_radioButton)
    mouse_click(main_window.arraignments_radioButton)

    def handle_dialog():
        while main_window.dialog is None:
            qApp.processEvents()
        qtbot.addWidget(main_window.dialog)
        mouse_click(main_window.dialog.close_dialog_Button)

    QTimer.singleShot(100, handle_dialog)
    mouse_click(main_window.NotGuiltyBondButton)
    return main_window.dialog

def test_dialog_opens(ngb_dialog):
    assert ngb_dialog.windowTitle() == "Not Guilty Bond Case Information"


all_ngb_bond_conditions_test_list = [
    "no_alcohol_drugs_checkBox",
    "alcohol_drugs_assessment_checkBox",
    "mental_health_assessment_checkBox",
    "comply_protection_order_checkBox",
    "monitoring_checkBox",
    "specialized_docket_checkBox",
    "alcohol_test_kiosk_checkBox",
]

@pytest.mark.parametrize("checkBox", all_ngb_bond_conditions_test_list)
def test_all_checkbox_conditions(qtbot, ngb_dialog, checkBox):
    mouse_click(getattr(ngb_dialog, checkBox))
    assert getattr(ngb_dialog, checkBox).isChecked()
