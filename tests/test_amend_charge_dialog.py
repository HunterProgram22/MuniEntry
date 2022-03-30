import pytest
from PyQt5 import QtWidgets

from PyQt5.QtCore import QTimer
from conftest import mouse_click, enter_data


@pytest.fixture
def amend_charge_dialog(qtbot, main_window):
    """Amend Charge Dialog is amend_charge_dialog. Uses the Jail dialog as that
    is the most common."""
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.final_pretrial_radioButton)
    enter_data(main_window.final_pretrial_cases_box, "H")
    mouse_click(main_window.JailCCPleaButton)

    def close_popup_dialog():
        qtbot.addWidget(main_window.dialog.popup_dialog)
        mouse_click(main_window.dialog.popup_dialog.amend_charge_Button)

    QTimer.singleShot(100, close_popup_dialog)
    amend_button = main_window.dialog.charges_gridLayout.itemAtPosition(11, 2).widget()
    mouse_click(amend_button)
    return main_window.dialog.popup_dialog


all_amend_charge_dialogs_test_list = [
    "FineOnlyPleaButton",
    "JailCCPleaButton",
    "DiversionButton",
]

@pytest.mark.parametrize("test_input", all_amend_charge_dialogs_test_list)
def test_amend_charge_works_all_dialogs(qtbot, main_window, test_input):
    """Tests to make sure the Amend Charge button opens the Amend Charge Dialog for any
    Main Entry Dialog that has an Amend Charge button."""
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.final_pretrial_radioButton)
    enter_data(main_window.final_pretrial_cases_box, "H")
    dialog_button = getattr(main_window, test_input)
    mouse_click(dialog_button)

    def close_popup_dialog():
        qtbot.addWidget(main_window.dialog.popup_dialog)
        mouse_click(main_window.dialog.popup_dialog.amend_charge_Button)

    QTimer.singleShot(100, close_popup_dialog)
    amend_button = main_window.dialog.charges_gridLayout.itemAtPosition(main_window.dialog.charges_gridLayout.row_amend_button, 2).widget()
    mouse_click(amend_button)
    assert main_window.dialog.popup_dialog.windowTitle() == "Amend Charge"


def test_add_charge_dialog_opens(amend_charge_dialog):
    assert amend_charge_dialog.windowTitle() == "Amend Charge"