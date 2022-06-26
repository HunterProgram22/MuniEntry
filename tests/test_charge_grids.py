import pytest

from tests.conftest import mouse_click, enter_data, right_click

charge_grids_with_dismissed = [
    ("FineOnlyPleaButton"),
    ("JailCCPleaButton"),
    ("DiversionButton"),
    ("PleaOnlyButton"),
    ("LeapSentencingButton"),
    ("TrialSentencingButton"),
]


@pytest.mark.parametrize("test_input", charge_grids_with_dismissed)
def test_dismissed_button_ovverides_plea(qtbot, main_window, test_input):
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, "Barkschat - 21TRC05611")
    mouse_click(getattr(main_window, test_input))
    mouse_click(main_window.dialog.guilty_all_Button)
    mouse_click(main_window.dialog.charges_gridLayout.itemAtPosition(3, 4).widget())
    assert main_window.dialog.charges_gridLayout.itemAtPosition(5, 4).widget().currentText() == 'Dismissed'


@pytest.mark.parametrize("test_input", charge_grids_with_dismissed)
def test_dismissed_button_holds_if_plea_all_button_used(qtbot, main_window, test_input):
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, "Barkschat - 21TRC05611")
    mouse_click(getattr(main_window, test_input))
    mouse_click(main_window.dialog.charges_gridLayout.itemAtPosition(3, 4).widget())
    mouse_click(main_window.dialog.guilty_all_Button)
    assert main_window.dialog.charges_gridLayout.itemAtPosition(5, 4).widget().currentText() == 'Dismissed'


@pytest.mark.parametrize("test_input", charge_grids_with_dismissed)
def test_allied_box_overrides_plea_all_button(qtbot, main_window, test_input):
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, "Barkschat - 21TRC05611")
    mouse_click(getattr(main_window, test_input))
    mouse_click(main_window.dialog.guilty_all_Button)
    mouse_click(main_window.dialog.charges_gridLayout.itemAtPosition(4, 4).widget())
    assert main_window.dialog.charges_gridLayout.itemAtPosition(6, 4).widget().currentText() == 'Guilty - Allied Offense'


@pytest.mark.parametrize("test_input", charge_grids_with_dismissed)
def test_allied_box_holds_if_plea_all_button_used(qtbot, main_window, test_input):
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, "Barkschat - 21TRC05611")
    mouse_click(getattr(main_window, test_input))
    mouse_click(main_window.dialog.charges_gridLayout.itemAtPosition(4, 4).widget())
    mouse_click(main_window.dialog.guilty_all_Button)
    assert main_window.dialog.charges_gridLayout.itemAtPosition(6, 4).widget().currentText() == 'Guilty - Allied Offense'
