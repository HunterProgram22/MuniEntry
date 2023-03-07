"""Test module for Amend Charge Dialog functionality.

Module Level Parameters - fixtures setup and imported automatically from the conftest file.
    main_window
"""
import pytest
from PyQt6.QtCore import QTimer

from tests.conftest import CLOSE_TIMER, enter_data, mouse_click

dialogs_with_amend_charge = [
    'FineOnlyPleaButton',
    'JailCCPleaButton',
    'DiversionButton',
    'PleaOnlyButton',
    'LeapSentencingButton',
    'LeapAdmissionButton',
    'TrialSentencingButton',
    'SentencingOnlyButton',
]


@pytest.mark.parametrize('dialog_button', dialogs_with_amend_charge)
def test_amend_charge_works_all_dialogs(main_window, dialog_button):
    """Tests the Amend Charge button opens the Amend Charge Dialog for dialogs that have it."""
    mouse_click(main_window.judge_2_radio_btn)
    mouse_click(main_window.final_pretrial_radioButton)
    enter_data(main_window.final_pretrial_cases_box, 'Barkschat - 21TRC05611')
    mouse_click(getattr(main_window, dialog_button))

    def close_popup_dialog():
        mouse_click(main_window.dialog.popup_dialog.amend_charge_Button)

    QTimer.singleShot(CLOSE_TIMER, close_popup_dialog)
    amend_button = main_window.dialog.charges_gridLayout.itemAtPosition(
        main_window.dialog.charges_gridLayout.row_amend_button, 2,
    ).widget()
    mouse_click(amend_button)
    assert main_window.dialog.popup_dialog.windowTitle() == 'Amend Charge'


def test_amend_charge_updates_charge_grid():
    """Tests that amending a charge updates the text of the charge on mainwindow charge grid."""
