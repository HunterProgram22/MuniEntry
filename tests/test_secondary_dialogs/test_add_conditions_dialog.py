"""Test module for Conditions Dialog functionality.

Module Level Parameters - fixtures setup and imported automatically from the conftest file.
    main_window
"""
import pytest
from PyQt6.QtCore import QTimer

from tests.conftest import CLOSE_TIMER, enter_data, mouse_click

dialogs_with_conditions = [
    'FineOnlyPleaButton',
    'LeapSentencingButton',
]


@pytest.mark.parametrize('dialog_button', dialogs_with_conditions)
def test_dialog_opens(main_window, dialog_button):
    """Tests Add Conditions Dialog opens from all main Dialogs for which it is used."""
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, 'Barkschat - 21TRC05611')
    mouse_click(getattr(main_window, dialog_button))

    def close_popup_dialog():
        mouse_click(main_window.dialog.popup_dialog.add_conditions_Button)

    QTimer.singleShot(CLOSE_TIMER, close_popup_dialog)
    mouse_click(main_window.dialog.add_conditions_Button)
    assert main_window.dialog.popup_dialog.windowTitle() == 'Additional Conditions'
