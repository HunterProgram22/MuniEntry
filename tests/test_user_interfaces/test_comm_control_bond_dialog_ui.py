import pytest
from loguru import logger
from tests.conftest import enter_data, mouse_click


@pytest.fixture
def pcv_dialog(qtbot, main_window):
    """Prelminary Community Control Violation Dialog is pcv_dialog"""
    mouse_click(main_window.judge_1_radio_btn)
    mouse_click(main_window.arraignments_radioButton)
    mouse_click(main_window.ProbationViolationBondButton)
    return main_window.dialog


def test_dialog_opens(pcv_dialog):
    assert pcv_dialog.windowTitle() == 'Community Control Violation Bond Case Information'


bond_types = [
    'Recognizance (OR) Bond',
    '10% Deposit, Cash or Surety Bond',
    'Cash or Surety Bond',
]


@pytest.mark.parametrize('bond_type', bond_types)
def test_combo_box_updates(pcv_dialog, bond_type):
    """Tests if updating combo box works."""
    enter_data(pcv_dialog.bond_type_box, bond_type)
    assert pcv_dialog.bond_type_box.currentText() == bond_type
