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


@pytest.fixture
def bhd_dialog(qtbot, main_window):
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, "Barkschat - 21TRC05611")
    mouse_click(main_window.BondHearingButton)
    return main_window.dialog


@pytest.mark.create_entry_test
def test_create_bond_hearing_entry(qtbot, bhd_dialog):
    enter_data(bhd_dialog.case_number_lineEdit, "bhd_test")

    # Bond Conditions
    mouse_click(bhd_dialog.no_alcohol_drugs_checkBox)
    mouse_click(bhd_dialog.alcohol_drugs_assessment_checkBox)
    mouse_click(bhd_dialog.monitoring_checkBox)
    mouse_click(bhd_dialog.comply_protection_order_checkBox)
    mouse_click(bhd_dialog.alcohol_test_kiosk_checkBox)
    mouse_click(bhd_dialog.mental_health_assessment_checkBox)
    mouse_click(bhd_dialog.specialized_docket_checkBox)

    # Create and Open Word Document - Passes even if no entry is opened b/c it checks data
    mouse_click(bhd_dialog.create_entry_Button)
    assert bhd_dialog.entry_case_information.case_number == "21TRC05611bhd_test"


@pytest.mark.create_entry_test
def test_create_fine_only_entry(qtbot, fop_dialog):
    enter_data(fop_dialog.case_number_lineEdit, "fop_test")

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

    # Create and Open Word Document - Passes even if no entry is opened b/c it checks data
    mouse_click(fop_dialog.create_entry_Button)
    assert fop_dialog.entry_case_information.case_number == "21TRC05611fop_test"