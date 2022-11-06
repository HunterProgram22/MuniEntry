"""Test module for creating crimtraffic entries.

Module Level Parameters - fixtures setup and imported automatically from the conftest file.
    main_window

WARNING: All tests likely pass even if entry doesn't open because test only asserts a check
of case_information data. Need to manually confirm the correct number of entries were created.

TODO: Setup a folder for saving entries and clear folder prior to tests then count files after
tests are complete.
"""
import pytest
from PyQt6.QtCore import QTimer

from tests.conftest import CLOSE_TIMER, mouse_click, enter_data, check_barkschat


def entry_dialog(main_window):
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, 'Barkschat - 21TRC05611')


@pytest.fixture
def trial_sentencing_dialog(qtbot, main_window):
    """Trial Sentencing Entry."""
    entry_dialog(qtbot, main_window)
    mouse_click(main_window.TrialSentencingButton)
    return main_window.dialog


@pytest.fixture
def div_dialog(qtbot, main_window):
    """Diversion Plea."""
    entry_dialog(qtbot, main_window)
    mouse_click(main_window.DiversionButton)
    return main_window.dialog


@pytest.fixture
def fta_dialog(qtbot, main_window):
    """Failure to Appear / Issue Warrant Dialog."""
    entry_dialog(qtbot, main_window)
    mouse_click(main_window.FailureToAppearButton)
    return main_window.dialog


@pytest.fixture
def pfs_dialog(qtbot, main_window):
    """Plea Future Sentence Date Dialog."""
    entry_dialog(qtbot, main_window)
    mouse_click(main_window.PleaOnlyButton)
    return main_window.dialog


@pytest.fixture
def leap_dialog(qtbot, main_window):
    """LEAP Admission Plea Dialog."""
    entry_dialog(qtbot, main_window)
    mouse_click(main_window.LeapAdmissionButton)
    return main_window.dialog


@pytest.fixture
def leap_valid_dialog(qtbot, main_window):
    """LEAP Admission Plea - Already Valid Dialog."""
    entry_dialog(qtbot, main_window)
    mouse_click(main_window.LeapAdmissionValidButton)
    return main_window.dialog


@pytest.fixture
def pve_dialog(qtbot, main_window):
    """Preliminary Probation Violation Bond Entry."""
    entry_dialog(qtbot, main_window)
    mouse_click(main_window.ProbationViolationBondButton)
    return main_window.dialog


@pytest.fixture
def freeform_dialog(qtbot, main_window):
    """Freeform Entry."""
    entry_dialog(qtbot, main_window)
    mouse_click(main_window.FreeformEntryButton)
    return main_window.dialog


@pytest.fixture
def sentencing_only_dialog(qtbot, main_window):
    """Sentencing Only Entry."""
    entry_dialog(qtbot, main_window)
    mouse_click(main_window.SentencingOnlyButton)
    return main_window.dialog


def test_create_no_plea_bond_entry(main_window):
    """Tests the creation of an Appear on Warrant (No Plea) / Bond entry."""
    entry_dialog(main_window)
    mouse_click(main_window.NoPleaBondButton)
    npb_dialog = main_window.dialog
    enter_data(npb_dialog.case_number_lineEdit, 'npb_test')
    mouse_click(npb_dialog.no_alcohol_drugs_checkBox)
    mouse_click(npb_dialog.alcohol_drugs_assessment_checkBox)
    mouse_click(npb_dialog.monitoring_checkBox)
    mouse_click(npb_dialog.comply_protection_order_checkBox)
    mouse_click(npb_dialog.alcohol_test_kiosk_checkBox)
    mouse_click(npb_dialog.mental_health_assessment_checkBox)
    mouse_click(npb_dialog.specialized_docket_checkBox)
    mouse_click(npb_dialog.public_safety_suspension_checkBox)
    npb_dialog.appearance_reason_box.setCurrentText('was arrested on a warrant for failure to appear')

    mouse_click(npb_dialog.create_entry_Button)
    assert npb_dialog.entry_case_information.case_number == '21TRC05611npb_test'


def test_create_bond_modification_entry(main_window):
    """Tests the creation of a Bond Modification / Revocation entry."""
    entry_dialog(main_window)
    mouse_click(main_window.BondHearingButton)
    bhd_dialog = main_window.dialog
    enter_data(bhd_dialog.case_number_lineEdit, 'bhd_test')
    mouse_click(bhd_dialog.no_alcohol_drugs_checkBox)
    mouse_click(bhd_dialog.alcohol_drugs_assessment_checkBox)
    mouse_click(bhd_dialog.monitoring_checkBox)
    mouse_click(bhd_dialog.comply_protection_order_checkBox)
    mouse_click(bhd_dialog.alcohol_test_kiosk_checkBox)
    mouse_click(bhd_dialog.mental_health_assessment_checkBox)
    mouse_click(bhd_dialog.specialized_docket_checkBox)
    mouse_click(bhd_dialog.public_safety_suspension_checkBox)
    bhd_dialog.bond_modification_decision_box.setCurrentText('request to modify bond is granted')

    mouse_click(bhd_dialog.create_entry_Button)
    assert bhd_dialog.entry_case_information.case_number == '21TRC05611bhd_test'


def test_create_leap_sentencing_entry(qtbot, main_window):
    """Tests the creation of a LEAP Sentencing entry."""
    entry_dialog(main_window)
    mouse_click(main_window.LeapSentencingButton)
    leap_sentence_dialog = main_window.dialog
    enter_data(leap_sentence_dialog.case_number_lineEdit, 'leap_sentence_test')
    enter_data(leap_sentence_dialog.leap_plea_date, '5/1/2021')
    mouse_click(leap_sentence_dialog.no_contest_all_Button)
    mouse_click(leap_sentence_dialog.credit_for_jail_checkBox)
    enter_data(leap_sentence_dialog.jail_time_credit_box, '2')
    enter_data(leap_sentence_dialog.fra_in_court_box, 'Yes')
    mouse_click(leap_sentence_dialog.license_suspension_checkBox)
    mouse_click(leap_sentence_dialog.community_service_checkBox)
    mouse_click(leap_sentence_dialog.other_conditions_checkBox)

    def add_conditions():
        qtbot.addWidget(leap_sentence_dialog.popup_dialog)
        enter_data(leap_sentence_dialog.popup_dialog.term_of_suspension_box, '12 months')
        enter_data(leap_sentence_dialog.popup_dialog.community_service_hours_ordered_box, '50')
        enter_data(leap_sentence_dialog.popup_dialog.community_service_days_to_complete_box, '60')
        enter_data(
            leap_sentence_dialog.popup_dialog.other_conditions_textEdit, 'Stay away from Big Bird!'
        )
        mouse_click(leap_sentence_dialog.popup_dialog.add_conditions_Button)

    QTimer.singleShot(CLOSE_TIMER, add_conditions)
    mouse_click(leap_sentence_dialog.add_conditions_Button)
    mouse_click(leap_sentence_dialog.create_entry_Button)
    assert leap_sentence_dialog.entry_case_information.case_number == '21TRC05611leap_sentence_test'


def test_create_fine_only_entry(qtbot, main_window):
    """Tests the creation of a Fine Only Plea entry."""
    entry_dialog(main_window)
    mouse_click(main_window.FineOnlyPleaButton)
    fop_dialog = main_window.dialog
    enter_data(fop_dialog.case_number_lineEdit, 'fop_test')
    mouse_click(fop_dialog.no_contest_all_Button)
    mouse_click(fop_dialog.credit_for_jail_checkBox)
    enter_data(fop_dialog.jail_time_credit_box, '2')
    enter_data(fop_dialog.fra_in_court_box, 'Yes')
    mouse_click(fop_dialog.license_suspension_checkBox)
    mouse_click(fop_dialog.community_service_checkBox)
    mouse_click(fop_dialog.other_conditions_checkBox)

    def add_conditions():
        qtbot.addWidget(fop_dialog.popup_dialog)
        enter_data(fop_dialog.popup_dialog.term_of_suspension_box, '12 months')
        enter_data(fop_dialog.popup_dialog.community_service_hours_ordered_box, '50')
        enter_data(fop_dialog.popup_dialog.community_service_days_to_complete_box, '60')
        enter_data(fop_dialog.popup_dialog.other_conditions_textEdit, 'Stay away from Big Bird!')
        mouse_click(fop_dialog.popup_dialog.add_conditions_Button)

    QTimer.singleShot(CLOSE_TIMER, add_conditions)
    mouse_click(fop_dialog.add_conditions_Button)
    mouse_click(fop_dialog.create_entry_Button)
    assert fop_dialog.entry_case_information.case_number == '21TRC05611fop_test'


def test_create_not_guilty_bond_entry(qtbot, main_window):
    """Tests the creation of a Not Guilty Plea / Bond entry.

    TODO: Add Special Bond Conditions to entry.
    """
    entry_dialog(main_window)
    mouse_click(main_window.NotGuiltyBondButton)
    ngb_dialog = main_window.dialog
    enter_data(ngb_dialog.case_number_lineEdit, 'ngb_test')
    mouse_click(ngb_dialog.not_guilty_all_Button)
    enter_data(ngb_dialog.bond_type_box, 'Cash or Surety Bond')
    enter_data(ngb_dialog.bond_amount_box, '$5,000')
    mouse_click(ngb_dialog.no_alcohol_drugs_checkBox)
    mouse_click(ngb_dialog.alcohol_drugs_assessment_checkBox)
    mouse_click(ngb_dialog.monitoring_checkBox)
    mouse_click(ngb_dialog.comply_protection_order_checkBox)
    mouse_click(ngb_dialog.alcohol_test_kiosk_checkBox)
    mouse_click(ngb_dialog.mental_health_assessment_checkBox)
    mouse_click(ngb_dialog.specialized_docket_checkBox)
    mouse_click(ngb_dialog.public_safety_suspension_checkBox)

    # Add Special Bond Conditions here

    mouse_click(ngb_dialog.create_entry_Button)
    assert ngb_dialog.entry_case_information.case_number == '21TRC05611ngb_test'


def test_create_jail_cc_plea_entry(qtbot, main_window):
    """Tests the creation of a Jail CC Plea entry."""
    entry_dialog(main_window)
    mouse_click(main_window.JailCCPleaButton)
    jcp_dialog =  main_window.dialog
    enter_data(jcp_dialog.case_number_lineEdit, 'jcp_test')
    mouse_click(jcp_dialog.offense_of_violence_checkBox)
    mouse_click(jcp_dialog.no_contest_all_Button)
    enter_data(jcp_dialog.fra_in_court_box, 'Yes')
    mouse_click(jcp_dialog.license_suspension_checkBox)
    mouse_click(jcp_dialog.community_service_checkBox)
    mouse_click(jcp_dialog.other_conditions_checkBox)
    mouse_click(jcp_dialog.community_control_checkBox)
    mouse_click(jcp_dialog.victim_notification_checkBox)
    mouse_click(jcp_dialog.impoundment_checkBox)

    def add_conditions():
        qtbot.addWidget(jcp_dialog.popup_dialog)
        mouse_click(jcp_dialog.popup_dialog.als_terminated_checkBox)
        mouse_click(jcp_dialog.popup_dialog.license_susp_interlock_checkBox)
        mouse_click(jcp_dialog.popup_dialog.remedial_driving_class_checkBox)
        enter_data(jcp_dialog.popup_dialog.term_of_suspension_box, '12 months')
        enter_data(jcp_dialog.popup_dialog.community_service_hours_ordered_box, '50')
        enter_data(jcp_dialog.popup_dialog.community_service_days_to_complete_box, '60')
        mouse_click(jcp_dialog.popup_dialog.daily_reporting_checkBox)
        enter_data(jcp_dialog.popup_dialog.other_conditions_textEdit, 'Stay away from Big Bird!')
        mouse_click(jcp_dialog.popup_dialog.community_control_not_within_500_feet_checkBox)
        enter_data(jcp_dialog.popup_dialog.community_control_not_within_500_feet_person_box, 'Justin Kudela')
        mouse_click(jcp_dialog.popup_dialog.community_control_no_contact_checkBox)
        enter_data(jcp_dialog.popup_dialog.community_control_no_contact_with_box, 'John Smith')
        mouse_click(jcp_dialog.popup_dialog.house_arrest_checkBox)
        enter_data(jcp_dialog.popup_dialog.house_arrest_time_box, '15 days')
        mouse_click(jcp_dialog.popup_dialog.gps_exclusion_checkBox)
        enter_data(jcp_dialog.popup_dialog.gps_exclusion_radius_box, '1 mile')
        enter_data(jcp_dialog.popup_dialog.gps_exclusion_location_box, '1773 Little Bear Loop')
        mouse_click(jcp_dialog.popup_dialog.antitheft_checkBox)
        mouse_click(jcp_dialog.popup_dialog.alcohol_evaluation_checkBox)
        mouse_click(jcp_dialog.popup_dialog.anger_management_checkBox)
        mouse_click(jcp_dialog.popup_dialog.domestic_violence_program_checkBox)
        mouse_click(jcp_dialog.popup_dialog.driver_intervention_program_checkBox)
        mouse_click(jcp_dialog.popup_dialog.mental_health_evaluation_checkBox)
        mouse_click(jcp_dialog.popup_dialog.specialized_docket_checkBox)
        mouse_click(jcp_dialog.popup_dialog.scram_remove_checkBox)
        mouse_click(jcp_dialog.popup_dialog.alcohol_monitoring_checkBox)
        enter_data(jcp_dialog.popup_dialog.alcohol_monitoring_time_box, '30 days')
        mouse_click(jcp_dialog.popup_dialog.alcohol_monitoring_court_pay_checkBox)
        mouse_click(jcp_dialog.popup_dialog.interlock_vehicles_checkBox)
        mouse_click(jcp_dialog.popup_dialog.pay_restitution_checkBox)
        enter_data(jcp_dialog.popup_dialog.pay_restitution_amount_box, '4,000')
        enter_data(jcp_dialog.popup_dialog.pay_restitution_to_box, 'Meijer')
        mouse_click(jcp_dialog.popup_dialog.community_control_community_service_checkBox)
        enter_data(jcp_dialog.popup_dialog.community_control_community_service_hours_box, '100 hours')
        mouse_click(jcp_dialog.popup_dialog.other_community_control_checkBox)
        enter_data(jcp_dialog.popup_dialog.other_community_control_conditions_box, 'Pick up trash')
        enter_data(jcp_dialog.popup_dialog.vehicle_make_model_box, '2017 Acura MDX')
        enter_data(jcp_dialog.popup_dialog.vehicle_license_plate_box, 'EAF 4253')
        enter_data(jcp_dialog.popup_dialog.vehicle_impound_time_box, '60 days')
        enter_data(jcp_dialog.popup_dialog.vehicle_impound_action_box, 'have its vehicle IT tags seized and sent to the BMV')
        mouse_click(jcp_dialog.popup_dialog.fingerprinting_checkBox)
        mouse_click(jcp_dialog.popup_dialog.victim_prosecutor_notification_checkBox)
        mouse_click(jcp_dialog.popup_dialog.victim_reparation_checkBox)
        mouse_click(jcp_dialog.popup_dialog.add_conditions_Button)

    QTimer.singleShot(CLOSE_TIMER, add_conditions)
    mouse_click(jcp_dialog.add_conditions_Button)
    mouse_click(jcp_dialog.create_entry_Button)
    assert jcp_dialog.entry_case_information.case_number == '21TRC05611jcp_test'


def test_sentencing_only_entry(qtbot, sentencing_only_dialog):
    enter_data(sentencing_only_dialog.case_number_lineEdit, 'sentencing_only_test')

    enter_data(sentencing_only_dialog.plea_date, '5/1/2021')
    mouse_click(sentencing_only_dialog.victim_statements_checkBox)
    mouse_click(sentencing_only_dialog.offense_of_violence_checkBox)
    mouse_click(sentencing_only_dialog.no_contest_all_Button)
    enter_data(sentencing_only_dialog.fra_in_court_box, 'Yes')

    mouse_click(sentencing_only_dialog.license_suspension_checkBox)
    mouse_click(sentencing_only_dialog.community_service_checkBox)
    mouse_click(sentencing_only_dialog.other_conditions_checkBox)
    mouse_click(sentencing_only_dialog.community_control_checkBox)
    mouse_click(sentencing_only_dialog.victim_notification_checkBox)
    mouse_click(sentencing_only_dialog.impoundment_checkBox)

    def add_conditions():
        qtbot.addWidget(sentencing_only_dialog.popup_dialog)
        mouse_click(sentencing_only_dialog.popup_dialog.als_terminated_checkBox)
        mouse_click(sentencing_only_dialog.popup_dialog.license_susp_interlock_checkBox)
        mouse_click(sentencing_only_dialog.popup_dialog.remedial_driving_class_checkBox)
        enter_data(sentencing_only_dialog.popup_dialog.term_of_suspension_box, '12 months')
        enter_data(sentencing_only_dialog.popup_dialog.community_service_hours_ordered_box, '50')
        enter_data(sentencing_only_dialog.popup_dialog.community_service_days_to_complete_box, '60')
        mouse_click(sentencing_only_dialog.popup_dialog.daily_reporting_checkBox)
        enter_data(sentencing_only_dialog.popup_dialog.other_conditions_textEdit, 'Stay away from Big Bird!')
        mouse_click(sentencing_only_dialog.popup_dialog.community_control_not_within_500_feet_checkBox)
        enter_data(sentencing_only_dialog.popup_dialog.community_control_not_within_500_feet_person_box, 'Justin Kudela')
        mouse_click(sentencing_only_dialog.popup_dialog.community_control_no_contact_checkBox)
        enter_data(sentencing_only_dialog.popup_dialog.community_control_no_contact_with_box, 'John Smith')
        mouse_click(sentencing_only_dialog.popup_dialog.house_arrest_checkBox)
        enter_data(sentencing_only_dialog.popup_dialog.house_arrest_time_box, '15 days')
        mouse_click(sentencing_only_dialog.popup_dialog.gps_exclusion_checkBox)
        enter_data(sentencing_only_dialog.popup_dialog.gps_exclusion_radius_box, '1 mile')
        enter_data(sentencing_only_dialog.popup_dialog.gps_exclusion_location_box, '1773 Little Bear Loop')
        mouse_click(sentencing_only_dialog.popup_dialog.antitheft_checkBox)
        mouse_click(sentencing_only_dialog.popup_dialog.alcohol_evaluation_checkBox)
        mouse_click(sentencing_only_dialog.popup_dialog.anger_management_checkBox)
        mouse_click(sentencing_only_dialog.popup_dialog.domestic_violence_program_checkBox)
        mouse_click(sentencing_only_dialog.popup_dialog.driver_intervention_program_checkBox)
        mouse_click(sentencing_only_dialog.popup_dialog.mental_health_evaluation_checkBox)
        mouse_click(sentencing_only_dialog.popup_dialog.specialized_docket_checkBox)
        mouse_click(sentencing_only_dialog.popup_dialog.scram_remove_checkBox)
        mouse_click(sentencing_only_dialog.popup_dialog.alcohol_monitoring_checkBox)
        enter_data(sentencing_only_dialog.popup_dialog.alcohol_monitoring_time_box, '30 days')
        mouse_click(sentencing_only_dialog.popup_dialog.alcohol_monitoring_court_pay_checkBox)
        mouse_click(sentencing_only_dialog.popup_dialog.interlock_vehicles_checkBox)
        mouse_click(sentencing_only_dialog.popup_dialog.pay_restitution_checkBox)
        enter_data(sentencing_only_dialog.popup_dialog.pay_restitution_amount_box, '4,000')
        enter_data(sentencing_only_dialog.popup_dialog.pay_restitution_to_box, 'Meijer')
        mouse_click(sentencing_only_dialog.popup_dialog.community_control_community_service_checkBox)
        enter_data(sentencing_only_dialog.popup_dialog.community_control_community_service_hours_box, '100 hours')
        mouse_click(sentencing_only_dialog.popup_dialog.other_community_control_checkBox)
        enter_data(sentencing_only_dialog.popup_dialog.other_community_control_conditions_box, 'Pick up trash')
        enter_data(sentencing_only_dialog.popup_dialog.vehicle_make_model_box, '2017 Acura MDX')
        enter_data(sentencing_only_dialog.popup_dialog.vehicle_license_plate_box, 'EAF 4253')
        enter_data(sentencing_only_dialog.popup_dialog.vehicle_impound_time_box, '60 days')
        enter_data(sentencing_only_dialog.popup_dialog.vehicle_impound_action_box, 'have its vehicle IT tags seized and sent to the BMV')
        mouse_click(sentencing_only_dialog.popup_dialog.fingerprinting_checkBox)
        mouse_click(sentencing_only_dialog.popup_dialog.victim_prosecutor_notification_checkBox)
        mouse_click(sentencing_only_dialog.popup_dialog.victim_reparation_checkBox)
        mouse_click(sentencing_only_dialog.popup_dialog.add_conditions_Button)

    QTimer.singleShot(50, add_conditions)
    mouse_click(sentencing_only_dialog.add_conditions_Button)

    # Create and Open Word Document - Passes even if no entry is opened b/c it checks data
    mouse_click(sentencing_only_dialog.create_entry_Button)
    assert sentencing_only_dialog.entry_case_information.case_number == '21TRC05611sentencing_only_test'


def test_trial_sentencing_entry(qtbot, trial_sentencing_dialog):
    enter_data(trial_sentencing_dialog.case_number_lineEdit, 'trial_sentencing')

    mouse_click(trial_sentencing_dialog.guilty_all_Button)
    enter_data(trial_sentencing_dialog.fra_in_court_box, 'Yes')

    mouse_click(trial_sentencing_dialog.license_suspension_checkBox)
    mouse_click(trial_sentencing_dialog.community_service_checkBox)
    mouse_click(trial_sentencing_dialog.other_conditions_checkBox)
    mouse_click(trial_sentencing_dialog.community_control_checkBox)
    mouse_click(trial_sentencing_dialog.victim_notification_checkBox)
    mouse_click(trial_sentencing_dialog.impoundment_checkBox)

    def add_conditions():
        qtbot.addWidget(trial_sentencing_dialog.popup_dialog)
        mouse_click(trial_sentencing_dialog.popup_dialog.als_terminated_checkBox)
        mouse_click(trial_sentencing_dialog.popup_dialog.license_susp_interlock_checkBox)
        mouse_click(trial_sentencing_dialog.popup_dialog.remedial_driving_class_checkBox)
        enter_data(trial_sentencing_dialog.popup_dialog.term_of_suspension_box, '12 months')
        enter_data(trial_sentencing_dialog.popup_dialog.community_service_hours_ordered_box, '50')
        enter_data(trial_sentencing_dialog.popup_dialog.community_service_days_to_complete_box, '60')
        mouse_click(trial_sentencing_dialog.popup_dialog.daily_reporting_checkBox)
        enter_data(trial_sentencing_dialog.popup_dialog.other_conditions_textEdit, 'Stay away from Big Bird!')
        mouse_click(trial_sentencing_dialog.popup_dialog.community_control_not_within_500_feet_checkBox)
        enter_data(trial_sentencing_dialog.popup_dialog.community_control_not_within_500_feet_person_box, 'Justin Kudela')
        mouse_click(trial_sentencing_dialog.popup_dialog.community_control_no_contact_checkBox)
        enter_data(trial_sentencing_dialog.popup_dialog.community_control_no_contact_with_box, 'John Smith')
        mouse_click(trial_sentencing_dialog.popup_dialog.house_arrest_checkBox)
        enter_data(trial_sentencing_dialog.popup_dialog.house_arrest_time_box, '15 days')
        mouse_click(trial_sentencing_dialog.popup_dialog.gps_exclusion_checkBox)
        enter_data(trial_sentencing_dialog.popup_dialog.gps_exclusion_radius_box, '1 mile')
        enter_data(trial_sentencing_dialog.popup_dialog.gps_exclusion_location_box, '1773 Little Bear Loop')
        mouse_click(trial_sentencing_dialog.popup_dialog.antitheft_checkBox)
        mouse_click(trial_sentencing_dialog.popup_dialog.alcohol_evaluation_checkBox)
        mouse_click(trial_sentencing_dialog.popup_dialog.anger_management_checkBox)
        mouse_click(trial_sentencing_dialog.popup_dialog.domestic_violence_program_checkBox)
        mouse_click(trial_sentencing_dialog.popup_dialog.driver_intervention_program_checkBox)
        mouse_click(trial_sentencing_dialog.popup_dialog.mental_health_evaluation_checkBox)
        mouse_click(trial_sentencing_dialog.popup_dialog.specialized_docket_checkBox)
        mouse_click(trial_sentencing_dialog.popup_dialog.scram_remove_checkBox)
        mouse_click(trial_sentencing_dialog.popup_dialog.alcohol_monitoring_checkBox)
        enter_data(trial_sentencing_dialog.popup_dialog.alcohol_monitoring_time_box, '30 days')
        mouse_click(trial_sentencing_dialog.popup_dialog.alcohol_monitoring_court_pay_checkBox)
        mouse_click(trial_sentencing_dialog.popup_dialog.interlock_vehicles_checkBox)
        mouse_click(trial_sentencing_dialog.popup_dialog.pay_restitution_checkBox)
        enter_data(trial_sentencing_dialog.popup_dialog.pay_restitution_amount_box, '4,000')
        enter_data(trial_sentencing_dialog.popup_dialog.pay_restitution_to_box, 'Meijer')
        mouse_click(trial_sentencing_dialog.popup_dialog.community_control_community_service_checkBox)
        enter_data(trial_sentencing_dialog.popup_dialog.community_control_community_service_hours_box, '100 hours')
        mouse_click(trial_sentencing_dialog.popup_dialog.other_community_control_checkBox)
        enter_data(trial_sentencing_dialog.popup_dialog.other_community_control_conditions_box, 'Pick up trash')
        enter_data(trial_sentencing_dialog.popup_dialog.vehicle_make_model_box, '2017 Acura MDX')
        enter_data(trial_sentencing_dialog.popup_dialog.vehicle_license_plate_box, 'EAF 4253')
        enter_data(trial_sentencing_dialog.popup_dialog.vehicle_impound_time_box, '60 days')
        enter_data(trial_sentencing_dialog.popup_dialog.vehicle_impound_action_box, 'have its vehicle IT tags seized and sent to the BMV')
        mouse_click(trial_sentencing_dialog.popup_dialog.fingerprinting_checkBox)
        mouse_click(trial_sentencing_dialog.popup_dialog.victim_prosecutor_notification_checkBox)
        mouse_click(trial_sentencing_dialog.popup_dialog.victim_reparation_checkBox)
        mouse_click(trial_sentencing_dialog.popup_dialog.add_conditions_Button)

    QTimer.singleShot(50, add_conditions)
    mouse_click(trial_sentencing_dialog.add_conditions_Button)

    # Create and Open Word Document - Passes even if no entry is opened b/c it checks data
    mouse_click(trial_sentencing_dialog.create_entry_Button)
    assert trial_sentencing_dialog.entry_case_information.case_number == '21TRC05611trial_sentencing'


def test_create_diversion_entry(qtbot, div_dialog):
    enter_data(div_dialog.case_number_lineEdit, 'div_test')
    mouse_click(div_dialog.marijuana_diversion_radioButton)
    mouse_click(div_dialog.diversion_jail_imposed_checkBox)
    mouse_click(div_dialog.pay_restitution_checkBox)
    enter_data(div_dialog.pay_restitution_to_box, 'Justin Kudela')
    enter_data(div_dialog.pay_restitution_amount_box, '$5,000')
    mouse_click(div_dialog.other_conditions_checkBox)
    enter_data(div_dialog.other_conditions_textEdit, 'Be good or else!')
    mouse_click(div_dialog.guilty_all_Button)
    enter_data(div_dialog.fra_in_court_box, 'Yes')

    # Create and Open Word Document - Passes even if no entry is opened b/c it checks data
    mouse_click(div_dialog.create_entry_Button)
    assert div_dialog.entry_case_information.case_number == '21TRC05611div_test'


def test_create_freeform_entry(qtbot, freeform_dialog):
    enter_data(freeform_dialog.case_number_lineEdit, 'freeform_test')
    enter_data(freeform_dialog.entry_content_textEdit, 'The Detroit Lions Rock!')

    mouse_click(freeform_dialog.create_entry_Button)
    assert freeform_dialog.entry_case_information.case_number == '21TRC05611freeform_test'


def test_create_failure_to_appear_entry(qtbot, fta_dialog):
    enter_data(fta_dialog.case_number_lineEdit, 'fta_test')
    mouse_click(fta_dialog.arrest_warrant_checkBox)
    mouse_click(fta_dialog.bond_forfeited_checkBox)
    mouse_click(fta_dialog.set_no_trial_checkBox)
    mouse_click(fta_dialog.operator_license_checkBox)
    mouse_click(fta_dialog.surety_appear_checkBox)
    mouse_click(fta_dialog.non_resident_license_checkBox)
    mouse_click(fta_dialog.supplemental_summons_checkBox)
    mouse_click(fta_dialog.proof_of_service_checkBox)
    mouse_click(fta_dialog.registration_block_checkBox)
    mouse_click(fta_dialog.set_bond_checkBox)

    # Create and Open Word Document - Passes even if no entry is opened b/c it checks data
    mouse_click(fta_dialog.create_entry_Button)
    assert fta_dialog.entry_case_information.case_number == '21TRC05611fta_test'


def test_leap_admission_plea_entry(qtbot, leap_dialog):
    enter_data(leap_dialog.case_number_lineEdit, 'leap_admission_test')
    mouse_click(leap_dialog.guilty_all_Button)

    # Create and Open Word Document - Passes even if no entry is opened b/c it checks data
    mouse_click(leap_dialog.create_entry_Button)
    assert leap_dialog.entry_case_information.case_number == '21TRC05611leap_admission_test'


def test_leap_admission_plea_valid_entry(qtbot, leap_valid_dialog):
    enter_data(leap_valid_dialog.case_number_lineEdit, 'leap_admission_valid_test')
    mouse_click(leap_valid_dialog.guilty_all_Button)

    # Create and Open Word Document - Passes even if no entry is opened b/c it checks data
    mouse_click(leap_valid_dialog.create_entry_Button)
    assert leap_valid_dialog.entry_case_information.case_number == '21TRC05611leap_admission_valid_test'


def test_create_plea_future_sentence_entry(qtbot, pfs_dialog):
    enter_data(pfs_dialog.case_number_lineEdit, 'plea_only_test')
    mouse_click(pfs_dialog.guilty_all_Button)
    mouse_click(pfs_dialog.prepare_psi_checkBox)
    mouse_click(pfs_dialog.set_restitution_checkBox)
    mouse_click(pfs_dialog.victim_appearance_checkBox)

    # Create and Open Word Document - Passes even if no entry is opened b/c it checks data
    mouse_click(pfs_dialog.create_entry_Button)
    assert pfs_dialog.entry_case_information.case_number == '21TRC05611plea_only_test'


def test_create_prelim_probation_violation_entry(qtbot, pve_dialog):
    enter_data(pve_dialog.case_number_lineEdit, 'probation_violation_test')
    enter_data(pve_dialog.bond_type_box, 'Cash or Surety Bond')
    enter_data(pve_dialog.bond_amount_box, '$2,500')
    mouse_click(pve_dialog.no_alcohol_drugs_checkBox)
    mouse_click(pve_dialog.comply_protection_order_checkBox)
    mouse_click(pve_dialog.alcohol_test_kiosk_checkBox)
    mouse_click(pve_dialog.monitoring_checkBox)
    mouse_click(pve_dialog.cc_violation_other_conditions_checkBox)
    enter_data(pve_dialog.cc_violation_other_conditions_terms_box, 'Dont be bad!')

    # Create and Open Word Document - Passes even if no entry is opened b/c it checks data
    mouse_click(pve_dialog.create_entry_Button)
    assert pve_dialog.entry_case_information.case_number == '21TRC05611probation_violation_test'
