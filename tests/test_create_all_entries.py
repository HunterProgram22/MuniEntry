import pytest
from PyQt5.QtCore import QTimer
from tests.conftest import mouse_click, enter_data, check_barkschat


@pytest.fixture
def fop_dialog(qtbot, main_window):
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, "Barkschat - 21TRC05611")
    mouse_click(main_window.FineOnlyPleaButton)
    return main_window.dialog


@pytest.mark.create_entry_test
def test_create_fine_only_entry(qtbot, fop_dialog):
    """Tests selecting all options on Fine Only Dialog then creates an actual entry
    to confirm everything works and is transferred to the entry."""
    mouse_click(fop_dialog.no_contest_all_Button)
    mouse_click(fop_dialog.credit_for_jail_checkBox)
    enter_data(fop_dialog.jail_time_credit_box, "2")
    enter_data(fop_dialog.fra_in_court_box, "Yes")

    mouse_click(fop_dialog.license_suspension_checkBox)
    mouse_click(fop_dialog.community_service_checkBox)
    mouse_click(fop_dialog.other_conditions_checkBox)

    def add_conditions():
        qtbot.addWidget(fop_dialog.popup_dialog)
        enter_data(fop_dialog.popup_dialog.term_of_suspension_box, "12 months")
        enter_data(fop_dialog.popup_dialog.community_service_hours_ordered_box, "50")
        enter_data(fop_dialog.popup_dialog.community_service_days_to_complete_box, "60")
        enter_data(fop_dialog.popup_dialog.other_conditions_textEdit, "Stay away from Big Bird!")
        mouse_click(fop_dialog.popup_dialog.add_conditions_Button)

    QTimer.singleShot(50, add_conditions)
    mouse_click(fop_dialog.add_conditions_Button)
    mouse_click(fop_dialog.create_entry_Button)
    assert fop_dialog.entry_case_information.case_number == "21TRC05611"