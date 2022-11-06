"""Test module for Add Charge Dialog UI Functionality.

Module Level Parameters - fixtures setup and imported automatically from the conftest file.
    main_window
    add_charge_dialog
"""
import pytest
from PyQt6.QtCore import QTimer

from tests.conftest import CLOSE_TIMER, mouse_click

dialogs_with_add_charge = [
    'FineOnlyPleaButton',
    'JailCCPleaButton',
    'NotGuiltyBondButton',
    'DiversionButton',
    'PleaOnlyButton',
    'LeapSentencingButton',
    'LeapAdmissionButton',
    'LeapAdmissionValidButton',
    'TrialSentencingButton',
    'SentencingOnlyButton',
]


@pytest.mark.parametrize('test_input', dialogs_with_add_charge)
def test_add_charge_works_all_dialogs(main_window, test_input):
    """Tests the Add Charge button opens the Add Charge Dialog and adds a charge.

    Test is run for all Main Entry Dialogs that have an Add Charge button.

    The column count on open is 3 and when add charge is pressed it should add 2 columns.
    """
    mouse_click(main_window.hemmeter_radioButton)
    mouse_click(main_window.arraignments_radioButton)
    dialog_button = getattr(main_window, test_input)
    mouse_click(dialog_button)

    def close_popup_dialog():
        mouse_click(main_window.dialog.popup_dialog.add_charge_Button)

    QTimer.singleShot(CLOSE_TIMER, close_popup_dialog)
    mouse_click(main_window.dialog.add_charge_Button)
    assert main_window.dialog.popup_dialog.windowTitle() == 'Add Charge'
    assert main_window.dialog.charges_gridLayout.columnCount() == 3
    mouse_click(main_window.dialog.popup_dialog.add_charge_Button)
    assert main_window.dialog.charges_gridLayout.columnCount() == 5
