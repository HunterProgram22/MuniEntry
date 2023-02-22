"""Test module for creating crimtraffic entries.

Module Level Parameters - fixtures setup and imported automatically from the conftest file.
    main_window

WARNING: All tests likely pass even if entry doesn't open because test only asserts a check
of case_information data. Need to manually confirm the correct number of entries were created.

TODO: Setup a folder for saving entries and clear folder prior to tests then count files after
tests are complete.
"""
from PyQt6.QtCore import QTimer

from tests.conftest import CLOSE_TIMER, enter_data, mouse_click, MUNI10_SAVE_PATH
from munientry.entrycreators.entry_creator import CrimTrafficEntryCreator


def entry_dialog(monkeypatch, main_window):
    """The preliminary setup for creating an entry."""
    data = CrimTrafficEntryCreator
    monkeypatch.setattr(data, 'save_path', MUNI10_SAVE_PATH)
    mouse_click(main_window.rohrer_radioButton)
    main_window.search_tabWidget.setCurrentWidget(main_window.case_search_tab)
    enter_data(main_window.case_search_box, '21TRC05611')
    mouse_click(main_window.get_case_Button)


def test_create_no_plea_bond_entry(monkeypatch, main_window):
    """Tests the creation of an Appear on Warrant (No Plea) / Bond entry."""
    entry_dialog(monkeypatch, main_window)
    mouse_click(main_window.NoPleaBondButton)
    dialog = main_window.dialog
    enter_data(dialog.case_number_lineEdit, 'npb_test')
    mouse_click(dialog.no_alcohol_drugs_checkBox)
    mouse_click(dialog.alcohol_drugs_assessment_checkBox)
    mouse_click(dialog.monitoring_checkBox)
    mouse_click(dialog.comply_protection_order_checkBox)
    mouse_click(dialog.alcohol_test_kiosk_checkBox)
    mouse_click(dialog.mental_health_assessment_checkBox)
    mouse_click(dialog.specialized_docket_checkBox)
    mouse_click(dialog.public_safety_suspension_checkBox)
    dialog.appearance_reason_box.setCurrentText(
        'was arrested on a warrant for failure to appear'
    )
    mouse_click(dialog.create_entry_Button)
    assert dialog.entry_case_information.case_number == '21TRC05611npb_test'


def test_create_bond_modification_entry(monkeypatch, main_window):
    """Tests the creation of a Bond Modification / Revocation entry."""
    entry_dialog(monkeypatch, main_window)
    mouse_click(main_window.BondHearingButton)
    dialog = main_window.dialog
    enter_data(dialog.case_number_lineEdit, 'bhd_test')
    mouse_click(dialog.no_alcohol_drugs_checkBox)
    mouse_click(dialog.alcohol_drugs_assessment_checkBox)
    mouse_click(dialog.monitoring_checkBox)
    mouse_click(dialog.comply_protection_order_checkBox)
    mouse_click(dialog.alcohol_test_kiosk_checkBox)
    mouse_click(dialog.mental_health_assessment_checkBox)
    mouse_click(dialog.specialized_docket_checkBox)
    mouse_click(dialog.public_safety_suspension_checkBox)
    dialog.bond_modification_decision_box.setCurrentText('request to modify bond is granted')

    mouse_click(dialog.create_entry_Button)
    assert dialog.entry_case_information.case_number == '21TRC05611bhd_test'


def test_create_leap_sentencing_entry(monkeypatch, qtbot, main_window):
    """Tests the creation of a LEAP Sentencing entry."""
    entry_dialog(monkeypatch, main_window)
    mouse_click(main_window.LeapSentencingButton)
    dialog = main_window.dialog
    enter_data(dialog.case_number_lineEdit, 'leap_sentence_test')
    enter_data(dialog.leap_plea_date, '5/1/2021')
    mouse_click(dialog.no_contest_all_Button)
    mouse_click(dialog.credit_for_jail_checkBox)
    enter_data(dialog.jail_time_credit_box, '2')
    enter_data(dialog.fra_in_court_box, 'Yes')
    mouse_click(dialog.license_suspension_checkBox)
    mouse_click(dialog.community_service_checkBox)
    mouse_click(dialog.other_conditions_checkBox)

    def add_conditions():
        qtbot.addWidget(dialog.popup_dialog)
        enter_data(dialog.popup_dialog.term_of_suspension_box, '12 months')
        enter_data(dialog.popup_dialog.community_service_hours_ordered_box, '50')
        enter_data(dialog.popup_dialog.community_service_days_to_complete_box, '60')
        enter_data(
            dialog.popup_dialog.other_conditions_textEdit, 'Stay away from Big Bird!',
        )
        mouse_click(dialog.popup_dialog.add_conditions_Button)

    QTimer.singleShot(CLOSE_TIMER, add_conditions)
    mouse_click(dialog.add_conditions_Button)
    mouse_click(dialog.create_entry_Button)
    assert dialog.entry_case_information.case_number == '21TRC05611leap_sentence_test'


def test_create_fine_only_entry(monkeypatch, qtbot, main_window):
    """Tests the creation of a Fine Only Plea entry."""
    entry_dialog(monkeypatch, main_window)
    mouse_click(main_window.FineOnlyPleaButton)
    dialog = main_window.dialog
    enter_data(dialog.case_number_lineEdit, 'fop_test')
    mouse_click(dialog.no_contest_all_Button)
    mouse_click(dialog.credit_for_jail_checkBox)
    enter_data(dialog.jail_time_credit_box, '2')
    enter_data(dialog.fra_in_court_box, 'Yes')
    mouse_click(dialog.license_suspension_checkBox)
    mouse_click(dialog.community_service_checkBox)
    mouse_click(dialog.other_conditions_checkBox)

    def add_conditions():
        qtbot.addWidget(dialog.popup_dialog)
        enter_data(dialog.popup_dialog.term_of_suspension_box, '12 months')
        enter_data(dialog.popup_dialog.community_service_hours_ordered_box, '50')
        enter_data(dialog.popup_dialog.community_service_days_to_complete_box, '60')
        enter_data(dialog.popup_dialog.other_conditions_textEdit, 'Stay away from Big Bird!')
        mouse_click(dialog.popup_dialog.add_conditions_Button)

    QTimer.singleShot(CLOSE_TIMER, add_conditions)
    mouse_click(dialog.add_conditions_Button)
    mouse_click(dialog.create_entry_Button)
    assert dialog.entry_case_information.case_number == '21TRC05611fop_test'


def test_create_not_guilty_bond_entry(monkeypatch, qtbot, main_window):
    """Tests the creation of a Not Guilty Plea / Bond entry.

    TODO: Add Special Bond Conditions to entry.
    """
    entry_dialog(monkeypatch, main_window)
    mouse_click(main_window.NotGuiltyBondButton)
    dialog = main_window.dialog
    enter_data(dialog.case_number_lineEdit, 'ngb_test')
    mouse_click(dialog.not_guilty_all_Button)
    enter_data(dialog.bond_type_box, 'Cash or Surety Bond')
    enter_data(dialog.bond_amount_box, '$5,000')
    mouse_click(dialog.no_alcohol_drugs_checkBox)
    mouse_click(dialog.alcohol_drugs_assessment_checkBox)
    mouse_click(dialog.monitoring_checkBox)
    mouse_click(dialog.comply_protection_order_checkBox)
    mouse_click(dialog.alcohol_test_kiosk_checkBox)
    mouse_click(dialog.mental_health_assessment_checkBox)
    mouse_click(dialog.specialized_docket_checkBox)
    mouse_click(dialog.public_safety_suspension_checkBox)
    mouse_click(dialog.domestic_violence_checkBox)
    mouse_click(dialog.admin_license_suspension_checkBox)
    mouse_click(dialog.custodial_supervision_checkBox)
    mouse_click(dialog.vehicle_seizure_checkBox)
    mouse_click(dialog.no_contact_checkBox)
    mouse_click(dialog.other_conditions_checkBox)

    # Add Special Bond Conditions here
    def add_conditions():
        qtbot.addWidget(dialog.popup_dialog)
        enter_data(dialog.popup_dialog.admin_license_suspension_explanation_box, 'Do Right!')
        mouse_click(dialog.popup_dialog.domestic_violence_vacate_checkBox)
        enter_data(dialog.popup_dialog.domestic_violence_residence_box, '1773 Little Bear Loop')
        enter_data(dialog.popup_dialog.domestic_violence_exclusive_possession_to_box, 'Justin')
        mouse_click(dialog.popup_dialog.domestic_violence_surrender_weapons_checkBox)
        enter_data(dialog.popup_dialog.no_contact_name_box, 'Justin')
        enter_data(dialog.popup_dialog.vehicle_make_model_box, '2012 Kia')
        enter_data(dialog.popup_dialog.vehicle_license_plate_box, 'EAF 4253')
        mouse_click(dialog.popup_dialog.tow_to_residence_checkBox)
        mouse_click(dialog.popup_dialog.motion_to_return_vehicle_checkBox)
        enter_data(dialog.popup_dialog.custodial_supervision_supervisor_box, 'Judge Dredd')
        enter_data(dialog.popup_dialog.other_conditions_textEdit, 'Do not run away.')
        mouse_click(dialog.popup_dialog.add_conditions_Button)

    QTimer.singleShot(CLOSE_TIMER, add_conditions)
    mouse_click(dialog.add_special_conditions_Button)
    mouse_click(dialog.create_entry_Button)
    assert dialog.entry_case_information.case_number == '21TRC05611ngb_test'


def test_create_jail_cc_plea_entry(monkeypatch, qtbot, main_window):
    """Tests the creation of a Jail CC Plea entry."""
    entry_dialog(monkeypatch, main_window)
    mouse_click(main_window.JailCCPleaButton)
    dialog =  main_window.dialog
    enter_data(dialog.case_number_lineEdit, 'jcp_test')
    mouse_click(dialog.offense_of_violence_checkBox)
    mouse_click(dialog.no_contest_all_Button)
    enter_data(dialog.fra_in_court_box, 'Yes')
    mouse_click(dialog.license_suspension_checkBox)
    mouse_click(dialog.community_service_checkBox)
    mouse_click(dialog.other_conditions_checkBox)
    mouse_click(dialog.community_control_checkBox)
    mouse_click(dialog.victim_notification_checkBox)
    mouse_click(dialog.impoundment_checkBox)

    def add_conditions():
        qtbot.addWidget(dialog.popup_dialog)
        mouse_click(dialog.popup_dialog.als_terminated_checkBox)
        mouse_click(dialog.popup_dialog.license_susp_interlock_checkBox)
        mouse_click(dialog.popup_dialog.remedial_driving_class_checkBox)
        enter_data(dialog.popup_dialog.term_of_suspension_box, '12 months')
        enter_data(dialog.popup_dialog.community_service_hours_ordered_box, '50')
        enter_data(dialog.popup_dialog.community_service_days_to_complete_box, '60')
        mouse_click(dialog.popup_dialog.daily_reporting_checkBox)
        enter_data(dialog.popup_dialog.other_conditions_textEdit, 'Stay away from Big Bird!')
        mouse_click(dialog.popup_dialog.community_control_not_within_500_feet_checkBox)
        enter_data(
            dialog.popup_dialog.community_control_not_within_500_feet_person_box,
            'Justin Kudela',
        )
        mouse_click(dialog.popup_dialog.community_control_no_contact_checkBox)
        enter_data(dialog.popup_dialog.community_control_no_contact_with_box, 'John Smith')
        mouse_click(dialog.popup_dialog.house_arrest_checkBox)
        enter_data(dialog.popup_dialog.house_arrest_time_box, '15 days')
        mouse_click(dialog.popup_dialog.gps_exclusion_checkBox)
        enter_data(dialog.popup_dialog.gps_exclusion_radius_box, '1 mile')
        enter_data(dialog.popup_dialog.gps_exclusion_location_box, '1773 Little Bear Loop')
        mouse_click(dialog.popup_dialog.antitheft_checkBox)
        mouse_click(dialog.popup_dialog.alcohol_evaluation_checkBox)
        mouse_click(dialog.popup_dialog.anger_management_checkBox)
        mouse_click(dialog.popup_dialog.domestic_violence_program_checkBox)
        mouse_click(dialog.popup_dialog.driver_intervention_program_checkBox)
        mouse_click(dialog.popup_dialog.mental_health_evaluation_checkBox)
        mouse_click(dialog.popup_dialog.specialized_docket_checkBox)
        mouse_click(dialog.popup_dialog.scram_remove_checkBox)
        mouse_click(dialog.popup_dialog.alcohol_monitoring_checkBox)
        enter_data(dialog.popup_dialog.alcohol_monitoring_time_box, '30 days')
        mouse_click(dialog.popup_dialog.alcohol_monitoring_court_pay_checkBox)
        mouse_click(dialog.popup_dialog.interlock_vehicles_checkBox)
        mouse_click(dialog.popup_dialog.pay_restitution_checkBox)
        enter_data(dialog.popup_dialog.pay_restitution_amount_box, '4,000')
        enter_data(dialog.popup_dialog.pay_restitution_to_box, 'Meijer')
        mouse_click(dialog.popup_dialog.community_control_community_service_checkBox)
        enter_data(
            dialog.popup_dialog.community_control_community_service_hours_box, '100 hours'
        )
        mouse_click(dialog.popup_dialog.other_community_control_checkBox)
        enter_data(dialog.popup_dialog.other_community_control_conditions_box, 'Pick up trash')
        enter_data(dialog.popup_dialog.vehicle_make_model_box, '2017 Acura MDX')
        enter_data(dialog.popup_dialog.vehicle_license_plate_box, 'EAF 4253')
        enter_data(dialog.popup_dialog.vehicle_impound_time_box, '60 days')
        enter_data(
            dialog.popup_dialog.vehicle_impound_action_box,
            'have its vehicle IT tags seized and sent to the BMV',
        )
        mouse_click(dialog.popup_dialog.fingerprinting_checkBox)
        mouse_click(dialog.popup_dialog.victim_prosecutor_notification_checkBox)
        mouse_click(dialog.popup_dialog.victim_reparation_checkBox)
        mouse_click(dialog.popup_dialog.add_conditions_Button)

    QTimer.singleShot(CLOSE_TIMER, add_conditions)
    mouse_click(dialog.add_conditions_Button)
    mouse_click(dialog.create_entry_Button)
    assert dialog.entry_case_information.case_number == '21TRC05611jcp_test'


def test_create_sentencing_only_entry(monkeypatch, qtbot, main_window):
    """Tests the creation of a Sentencing Only - Already Plead entry."""
    entry_dialog(monkeypatch, main_window)
    mouse_click(main_window.SentencingOnlyButton)
    dialog = main_window.dialog
    enter_data(dialog.case_number_lineEdit, 'sentencing_only_test')
    enter_data(dialog.plea_date, '5/1/2021')
    mouse_click(dialog.victim_statements_checkBox)
    mouse_click(dialog.offense_of_violence_checkBox)
    mouse_click(dialog.no_contest_all_Button)
    enter_data(dialog.fra_in_court_box, 'Yes')
    mouse_click(dialog.license_suspension_checkBox)
    mouse_click(dialog.community_service_checkBox)
    mouse_click(dialog.other_conditions_checkBox)
    mouse_click(dialog.community_control_checkBox)
    mouse_click(dialog.victim_notification_checkBox)
    mouse_click(dialog.impoundment_checkBox)

    def add_conditions():
        qtbot.addWidget(dialog.popup_dialog)
        mouse_click(dialog.popup_dialog.als_terminated_checkBox)
        mouse_click(dialog.popup_dialog.license_susp_interlock_checkBox)
        mouse_click(dialog.popup_dialog.remedial_driving_class_checkBox)
        enter_data(dialog.popup_dialog.term_of_suspension_box, '12 months')
        enter_data(dialog.popup_dialog.community_service_hours_ordered_box, '50')
        enter_data(dialog.popup_dialog.community_service_days_to_complete_box, '60')
        mouse_click(dialog.popup_dialog.daily_reporting_checkBox)
        enter_data(dialog.popup_dialog.other_conditions_textEdit,'Stay away from Big Bird!')
        mouse_click(dialog.popup_dialog.community_control_not_within_500_feet_checkBox)
        enter_data(dialog.popup_dialog.community_control_not_within_500_feet_person_box, 'Justin')
        mouse_click(dialog.popup_dialog.community_control_no_contact_checkBox)
        enter_data(dialog.popup_dialog.community_control_no_contact_with_box, 'John Smith')
        mouse_click(dialog.popup_dialog.house_arrest_checkBox)
        enter_data(dialog.popup_dialog.house_arrest_time_box, '15 days')
        mouse_click(dialog.popup_dialog.gps_exclusion_checkBox)
        enter_data(dialog.popup_dialog.gps_exclusion_radius_box, '1 mile')
        enter_data(dialog.popup_dialog.gps_exclusion_location_box, '1773 Little Bear Loop')
        mouse_click(dialog.popup_dialog.antitheft_checkBox)
        mouse_click(dialog.popup_dialog.alcohol_evaluation_checkBox)
        mouse_click(dialog.popup_dialog.anger_management_checkBox)
        mouse_click(dialog.popup_dialog.domestic_violence_program_checkBox)
        mouse_click(dialog.popup_dialog.driver_intervention_program_checkBox)
        mouse_click(dialog.popup_dialog.mental_health_evaluation_checkBox)
        mouse_click(dialog.popup_dialog.specialized_docket_checkBox)
        mouse_click(dialog.popup_dialog.scram_remove_checkBox)
        mouse_click(dialog.popup_dialog.alcohol_monitoring_checkBox)
        enter_data(dialog.popup_dialog.alcohol_monitoring_time_box, '30 days')
        mouse_click(dialog.popup_dialog.alcohol_monitoring_court_pay_checkBox)
        mouse_click(dialog.popup_dialog.interlock_vehicles_checkBox)
        mouse_click(dialog.popup_dialog.pay_restitution_checkBox)
        enter_data(dialog.popup_dialog.pay_restitution_amount_box, '4,000')
        enter_data(dialog.popup_dialog.pay_restitution_to_box, 'Meijer')
        mouse_click(dialog.popup_dialog.community_control_community_service_checkBox)
        enter_data(dialog.popup_dialog.community_control_community_service_hours_box, '100 hours')
        mouse_click(dialog.popup_dialog.other_community_control_checkBox)
        enter_data(dialog.popup_dialog.other_community_control_conditions_box, 'Pick up trash')
        enter_data(dialog.popup_dialog.vehicle_make_model_box, '2017 Acura MDX')
        enter_data(dialog.popup_dialog.vehicle_license_plate_box, 'EAF 4253')
        enter_data(dialog.popup_dialog.vehicle_impound_time_box, '60 days')
        enter_data(dialog.popup_dialog.vehicle_impound_action_box, 'tags seized and send to BMV')
        mouse_click(dialog.popup_dialog.fingerprinting_checkBox)
        mouse_click(dialog.popup_dialog.victim_prosecutor_notification_checkBox)
        mouse_click(dialog.popup_dialog.victim_reparation_checkBox)
        mouse_click(dialog.popup_dialog.add_conditions_Button)

    QTimer.singleShot(CLOSE_TIMER, add_conditions)
    mouse_click(dialog.add_conditions_Button)
    mouse_click(dialog.create_entry_Button)
    assert dialog.entry_case_information.case_number == '21TRC05611sentencing_only_test'


def test_create_trial_sentencing_entry(monkeypatch, qtbot, main_window):
    """Tests the creation of a Jury Trial / Trial To Court Sentencing entry.

    TODO: Bug here - not all conditions populating in test entry.
    """
    entry_dialog(monkeypatch, main_window)
    mouse_click(main_window.TrialSentencingButton)
    dialog = main_window.dialog
    enter_data(dialog.case_number_lineEdit, 'trial_sentencing')

    mouse_click(dialog.guilty_all_Button)
    enter_data(dialog.fra_in_court_box, 'Yes')

    mouse_click(dialog.license_suspension_checkBox)
    mouse_click(dialog.community_service_checkBox)
    mouse_click(dialog.other_conditions_checkBox)
    mouse_click(dialog.community_control_checkBox)
    mouse_click(dialog.victim_notification_checkBox)
    mouse_click(dialog.impoundment_checkBox)

    def add_conditions():
        qtbot.addWidget(dialog.popup_dialog)
        mouse_click(dialog.popup_dialog.als_terminated_checkBox)
        mouse_click(dialog.popup_dialog.license_susp_interlock_checkBox)
        mouse_click(dialog.popup_dialog.remedial_driving_class_checkBox)
        enter_data(dialog.popup_dialog.term_of_suspension_box, '12 months')
        enter_data(dialog.popup_dialog.community_service_hours_ordered_box, '50')
        enter_data(dialog.popup_dialog.community_service_days_to_complete_box, '60')
        mouse_click(dialog.popup_dialog.daily_reporting_checkBox)
        enter_data(dialog.popup_dialog.other_conditions_textEdit, 'Stay away from Big Bird!')
        mouse_click(dialog.popup_dialog.community_control_not_within_500_feet_checkBox)
        enter_data(dialog.popup_dialog.community_control_not_within_500_feet_person_box, 'Justin')
        mouse_click(dialog.popup_dialog.community_control_no_contact_checkBox)
        enter_data(dialog.popup_dialog.community_control_no_contact_with_box, 'John Smith')
        mouse_click(dialog.popup_dialog.house_arrest_checkBox)
        enter_data(dialog.popup_dialog.house_arrest_time_box, '15 days')
        mouse_click(dialog.popup_dialog.gps_exclusion_checkBox)
        enter_data(dialog.popup_dialog.gps_exclusion_radius_box, '1 mile')
        enter_data(dialog.popup_dialog.gps_exclusion_location_box, '1773 Little Bear Loop')
        mouse_click(dialog.popup_dialog.antitheft_checkBox)
        mouse_click(dialog.popup_dialog.alcohol_evaluation_checkBox)
        mouse_click(dialog.popup_dialog.anger_management_checkBox)
        mouse_click(dialog.popup_dialog.domestic_violence_program_checkBox)
        mouse_click(dialog.popup_dialog.driver_intervention_program_checkBox)
        mouse_click(dialog.popup_dialog.mental_health_evaluation_checkBox)
        mouse_click(dialog.popup_dialog.specialized_docket_checkBox)
        mouse_click(dialog.popup_dialog.scram_remove_checkBox)
        mouse_click(dialog.popup_dialog.alcohol_monitoring_checkBox)
        enter_data(dialog.popup_dialog.alcohol_monitoring_time_box, '30 days')
        mouse_click(dialog.popup_dialog.alcohol_monitoring_court_pay_checkBox)
        mouse_click(dialog.popup_dialog.interlock_vehicles_checkBox)
        mouse_click(dialog.popup_dialog.pay_restitution_checkBox)
        enter_data(dialog.popup_dialog.pay_restitution_amount_box, '4,000')
        enter_data(dialog.popup_dialog.pay_restitution_to_box, 'Meijer')
        mouse_click(dialog.popup_dialog.community_control_community_service_checkBox)
        enter_data(dialog.popup_dialog.community_control_community_service_hours_box, '100 hours')
        mouse_click(dialog.popup_dialog.other_community_control_checkBox)
        enter_data(dialog.popup_dialog.other_community_control_conditions_box, 'Pick up trash')
        enter_data(dialog.popup_dialog.vehicle_make_model_box, '2017 Acura MDX')
        enter_data(dialog.popup_dialog.vehicle_license_plate_box, 'EAF 4253')
        enter_data(dialog.popup_dialog.vehicle_impound_time_box, '60 days')
        enter_data(dialog.popup_dialog.vehicle_impound_action_box, 'tags seize and send to the BMV')
        mouse_click(dialog.popup_dialog.fingerprinting_checkBox)
        mouse_click(dialog.popup_dialog.victim_prosecutor_notification_checkBox)
        mouse_click(dialog.popup_dialog.victim_reparation_checkBox)
        mouse_click(dialog.popup_dialog.add_conditions_Button)

    QTimer.singleShot(CLOSE_TIMER, add_conditions)
    mouse_click(dialog.add_conditions_Button)
    mouse_click(dialog.create_entry_Button)
    assert dialog.entry_case_information.case_number == '21TRC05611trial_sentencing'


def test_create_diversion_entry(monkeypatch, main_window):
    """Tests the creation of a Diversion entry.

    TODO: Bug here - not all conditions showing up in entry.
    Commented out other_conditions_checkBox and textEdit are conditions that won't
    populate correctly.
    """
    entry_dialog(monkeypatch, main_window)
    mouse_click(main_window.DiversionButton)
    dialog = main_window.dialog
    enter_data(dialog.case_number_lineEdit, 'div_test')
    mouse_click(dialog.marijuana_diversion_radioButton)
    mouse_click(dialog.diversion_jail_imposed_checkBox)
    mouse_click(dialog.pay_restitution_checkBox)
    enter_data(dialog.pay_restitution_to_box, 'Justin Kudela')
    enter_data(dialog.pay_restitution_amount_box, '$5,000')
    # mouse_click(dialog.other_conditions_checkBox)
    # enter_data(dialog.other_conditions_textEdit, 'Be good or else!')
    mouse_click(dialog.guilty_all_Button)
    enter_data(dialog.fra_in_court_box, 'Yes')
    mouse_click(dialog.create_entry_Button)
    assert dialog.entry_case_information.case_number == '21TRC05611div_test'


def test_create_freeform_entry(monkeypatch, main_window):
    """Tests the creation of a Freeform entry."""
    entry_dialog(monkeypatch, main_window)
    mouse_click(main_window.FreeformEntryButton)
    dialog = main_window.dialog
    enter_data(dialog.case_number_lineEdit, 'freeform_test')
    enter_data(dialog.entry_content_textEdit, 'The Detroit Lions Rock!')
    mouse_click(dialog.create_entry_Button)
    assert dialog.entry_case_information.case_number == '21TRC05611freeform_test'


def test_create_failure_to_appear_entry(monkeypatch, main_window):
    """Tests the creation of a failure to appear entry."""
    entry_dialog(monkeypatch, main_window)
    mouse_click(main_window.FailureToAppearButton)
    dialog = main_window.dialog
    enter_data(dialog.case_number_lineEdit, 'fta_test')
    mouse_click(dialog.arrest_warrant_checkBox)
    mouse_click(dialog.bond_forfeited_checkBox)
    mouse_click(dialog.set_no_trial_checkBox)
    mouse_click(dialog.operator_license_checkBox)
    mouse_click(dialog.surety_appear_checkBox)
    mouse_click(dialog.non_resident_license_checkBox)
    mouse_click(dialog.supplemental_summons_checkBox)
    mouse_click(dialog.proof_of_service_checkBox)
    mouse_click(dialog.registration_block_checkBox)
    mouse_click(dialog.set_bond_checkBox)
    mouse_click(dialog.create_entry_Button)
    assert dialog.entry_case_information.case_number == '21TRC05611fta_test'


def test_create_leap_admission_plea_entry(monkeypatch, main_window):
    """Tests the creation of a LEAP plea entry."""
    entry_dialog(monkeypatch, main_window)
    mouse_click(main_window.LeapAdmissionButton)
    dialog = main_window.dialog
    enter_data(dialog.case_number_lineEdit, 'leap_admission_test')
    mouse_click(dialog.guilty_all_Button)
    mouse_click(dialog.create_entry_Button)
    assert dialog.entry_case_information.case_number == '21TRC05611leap_admission_test'


def test_create_leap_admission_plea_valid_entry(monkeypatch, main_window):
    """Tests the creation of a LEAP Plea Already Valid entry."""
    entry_dialog(monkeypatch, main_window)
    mouse_click(main_window.LeapAdmissionValidButton)
    dialog = main_window.dialog
    enter_data(dialog.case_number_lineEdit, 'leap_admission_valid_test')
    mouse_click(dialog.guilty_all_Button)
    mouse_click(dialog.create_entry_Button)
    assert dialog.entry_case_information.case_number == '21TRC05611leap_admission_valid_test'


def test_create_plea_future_sentence_entry(monkeypatch, main_window):
    """Tests the creation of a Plea Future Sentence entry."""
    entry_dialog(monkeypatch, main_window)
    mouse_click(main_window.PleaOnlyButton)
    dialog = main_window.dialog
    enter_data(dialog.case_number_lineEdit, 'plea_only_test')
    mouse_click(dialog.guilty_all_Button)
    mouse_click(dialog.prepare_psi_checkBox)
    mouse_click(dialog.set_restitution_checkBox)
    mouse_click(dialog.victim_appearance_checkBox)
    mouse_click(dialog.create_entry_Button)
    assert dialog.entry_case_information.case_number == '21TRC05611plea_only_test'


def test_create_prelim_probation_violation_entry(monkeypatch, main_window):
    """Tests the creation of Prelim Probation Violation entry.

    TODO: Bug here - some conditions not populating, but works manually.
    Commented out cc_violation_other_conditions_checkBox and terms_box are the conditions that
    for some reason won't populate.
    """
    entry_dialog(monkeypatch, main_window)
    mouse_click(main_window.ProbationViolationBondButton)
    dialog = main_window.dialog
    # mouse_click(dialog.cc_violation_other_conditions_checkBox)
    # enter_data(dialog.cc_violation_other_conditions_terms_box, 'Dont be bad!')
    enter_data(dialog.case_number_lineEdit, 'probation_violation_test')
    enter_data(dialog.bond_type_box, 'Cash or Surety Bond')
    enter_data(dialog.bond_amount_box, '$2,500')
    mouse_click(dialog.monitoring_checkBox)
    mouse_click(dialog.no_alcohol_drugs_checkBox)
    mouse_click(dialog.comply_protection_order_checkBox)
    mouse_click(dialog.alcohol_test_kiosk_checkBox)
    mouse_click(dialog.create_entry_Button)
    assert dialog.entry_case_information.case_number == '21TRC05611probation_violation_test'
