"""Test module for Add Charge Dialog functionality.

Module Level Parameters - fixtures setup and imported automatically from the conftest file.
    main_window
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


@pytest.mark.parametrize('dialog_button', dialogs_with_add_charge)
def test_add_charge_works_all_dialogs(main_window, dialog_button):
    """Tests the Add Charge button opens the Add Charge Dialog and adds a charge.

    Test is run for all Main Entry Dialogs that have an Add Charge button.

    The column count on open is 3 and when add charge is pressed it should add 2 columns.
    """
    mouse_click(main_window.judge_1_radio_btn)
    mouse_click(main_window.arraignments_radio_btn)
    mouse_click(getattr(main_window, dialog_button))

    def close_popup_dialog():
        mouse_click(main_window.dialog.popup_dialog.add_charge_Button)

    QTimer.singleShot(CLOSE_TIMER, close_popup_dialog)
    mouse_click(main_window.dialog.add_charge_Button)
    assert main_window.dialog.popup_dialog.windowTitle() == 'Add Charge'
    assert main_window.dialog.charges_gridLayout.columnCount() == 3
    mouse_click(main_window.dialog.popup_dialog.add_charge_Button)
    assert main_window.dialog.charges_gridLayout.columnCount() == 5
