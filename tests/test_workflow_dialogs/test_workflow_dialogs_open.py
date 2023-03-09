"""Module for testing all Workflow Tab dialog buttons on mainwindow open."""
import pytest

from tests.conftest import enter_data, mouse_click

TEST_LIST = 'dialog_button, dialog_title'


crimtraffic_dialog_buttons = [
    ('community_control_workflowButton', 'Community Control Workflow'),
    ('pretrial_workflowButton', 'Pretrial Workflow'),
    ('admin_workflowButton', 'Admin Entries Workflow'),
]


@pytest.mark.parametrize(TEST_LIST, crimtraffic_dialog_buttons)
def test_dialogs_open_nocase_from_caselist(main_window, dialog_button, dialog_title):
    """Tests all Workflow dialog buttons open."""
    mouse_click(getattr(main_window, dialog_button))
    assert main_window.dialog.windowTitle() == dialog_title
