"""Module containing data structures for conditions that are part of Case Information models."""
from dataclasses import dataclass


@dataclass
class ConditionsModel(object):
    """Base class for all Conditions Models."""
    ordered: bool = False


@dataclass
class DomesticViolenceBondConditions(ConditionsModel):
    """Domestic Violence Bond Conditions for Special Bond Conditions."""
    vacate_residence: bool = False
    residence_address: str = None
    exclusive_possession_to: str = None
    surrender_weapons: bool = False
    surrender_weapons_date: str = None
    terms_list = [
        ('vacate_residence', 'domestic_violence_vacate_checkBox'),
        ('residence_address', 'domestic_violence_residence_box'),
        ('exclusive_possession_to', 'domestic_violence_exclusive_possession_to_box'),
        ('surrender_weapons', 'domestic_violence_surrender_weapons_checkBox'),
        ('surrender_weapons_date', 'domestic_violence_surrender_weapons_dateBox'),
    ]


@dataclass
class AdminLicenseSuspensionConditions(ConditionsModel):
    """Admin License Suspension Conditions for Special Bond Conditions."""
    objection: str = None
    disposition: str = None
    explanation: str = None
    terms_list = [
        ('objection', 'admin_license_suspension_objection_box'),
        ('disposition', 'admin_license_suspension_disposition_box'),
        ('explanation', 'admin_license_suspension_explanation_box'),
    ]


@dataclass
class NoContact(ConditionsModel):
    """No Contact conditions for Special Bond Conditions."""
    name: str = None
    terms_list = [
        ('name', 'no_contact_name_box'),
    ]


@dataclass
class CustodialSupervision(ConditionsModel):
    """Custodial Supervision conditions for Special Bond Conditions."""
    supervisor: str = None
    terms_list = [
        ('supervisor', 'custodial_supervision_supervisor_box'),
    ]


@dataclass
class CommunityService(ConditionsModel):
    """Class for keeping track of all community service terms that are ordered."""
    hours_of_service: str = None
    days_to_complete_service: str = None
    due_date_for_service: str = None
    terms_list = [
        ('hours_of_service', 'community_service_hours_ordered_box'),
        ('days_to_complete_service', 'community_service_days_to_complete_box'),
        ('due_date_for_service', 'community_service_date_to_complete_box'),
    ]


@dataclass
class CommunityControl(ConditionsModel):
    """Class for all community control terms that are ordered."""
    type_of_control: str = 'basic'
    term_of_control: str = None
    not_within_500_feet_ordered: bool = False
    not_within_500_feet_person: str = None
    postconviction_no_contact_ordered: bool = False
    no_contact_with_ordered: bool = False
    no_contact_with_person: str = None
    alcohol_monitoring: bool = False
    alcohol_monitoring_remove: bool = False
    alcohol_monitoring_court_pay: bool = False
    alcohol_monitoring_time: str = None
    house_arrest: bool = False
    house_arrest_time: str = None
    interlock_vehicles_only: bool = False
    pay_restitution: bool = False
    pay_restitution_to: str = None
    pay_restitution_amount: str = None
    antitheft_program: bool = False
    anger_management_program: bool = False
    alcohol_evaluation: bool = False
    domestic_violence_program: bool = False
    driver_intervention_program: bool = False
    mental_health_evaluation: bool = False
    other_community_control: bool = False
    other_community_control_conditions: str = None
    community_control_community_service: bool = False
    community_control_community_service_hours: str = None
    gps_exclusion: bool = False
    gps_court_pay: bool = False
    gps_prior_to_release: bool = False
    gps_exclusion_radius: str = None
    gps_exclusion_location: str = None
    daily_reporting: bool = False
    specialized_docket_ordered: bool = False
    specialized_docket_type: str = None
    terms_list = [
        ('type_of_control', 'community_control_type_of_control_box'),
        ('term_of_control', 'community_control_term_of_control_box'),
        ('not_within_500_feet_ordered', 'community_control_not_within_500_feet_checkBox'),
        ('not_within_500_feet_person', 'community_control_not_within_500_feet_person_box'),
        ('postconviction_no_contact_ordered', 'community_control_postconviction_no_contact_checkBox'),
        ('no_contact_with_ordered', 'community_control_no_contact_checkBox'),
        ('no_contact_with_person', 'community_control_no_contact_with_box'),
        ('alcohol_monitoring', 'alcohol_monitoring_checkBox'),
        ('alcohol_monitoring_remove', 'scram_remove_checkBox'),
        ('alcohol_monitoring_court_pay', 'alcohol_monitoring_court_pay_checkBox'),
        ('alcohol_monitoring_time', 'alcohol_monitoring_time_box'),
        ('house_arrest', 'house_arrest_checkBox'),
        ('house_arrest_time', 'house_arrest_time_box'),
        ('interlock_vehicles_only', 'interlock_vehicles_checkBox'),
        ('pay_restitution', 'pay_restitution_checkBox'),
        ('pay_restitution_to', 'pay_restitution_to_box'),
        ('pay_restitution_amount', 'pay_restitution_amount_box'),
        ('antitheft_program', 'antitheft_checkBox'),
        ('anger_management_program', 'anger_management_checkBox'),
        ('alcohol_evaluation', 'alcohol_evaluation_checkBox'),
        ('domestic_violence_program', 'domestic_violence_program_checkBox'),
        ('driver_intervention_program', 'driver_intervention_program_checkBox'),
        ('mental_health_evaluation', 'mental_health_evaluation_checkBox'),
        ('other_community_control', 'other_community_control_checkBox'),
        ('other_community_control_conditions', 'other_community_control_conditions_box'),
        ('community_control_community_service', 'community_control_community_service_checkBox'),
        ('community_control_community_service_hours', 'community_control_community_service_hours_box'),
        ('gps_exclusion', 'gps_exclusion_checkBox'),
        ('gps_court_pay', 'gps_court_pay_checkBox'),
        ('gps_prior_to_release', 'gps_prior_to_release_checkBox'),
        ('gps_exclusion_radius', 'gps_exclusion_radius_box'),
        ('gps_exclusion_location', 'gps_exclusion_location_box'),
        ('daily_reporting', 'daily_reporting_checkBox'),
        ('specialized_docket_ordered', 'specialized_docket_checkBox'),
        ('specialized_docket_type', 'specialized_docket_box'),
    ]


@dataclass
class VehicleSeizure(ConditionsModel):
    """Class for vehicle seizure terms in Special Bond Conditions."""
    vehicle_make_model: str = None
    vehicle_license_plate: str = None
    tow_to_residence: bool = False
    motion_to_return_vehicle: bool = False
    state_opposes: str = None
    disposition_motion_to_return: str = None
    terms_list = [
        ('vehicle_make_model', 'vehicle_make_model_box'),
        ('vehicle_license_plate', 'vehicle_license_plate_box'),
        ('tow_to_residence', 'tow_to_residence_checkBox'),
        ('motion_to_return_vehicle', 'motion_to_return_vehicle_checkBox'),
        ('state_opposes', 'state_opposes_box'),
        ('disposition_motion_to_return', 'disposition_motion_to_return_box'),
    ]


@dataclass
class Impoundment(ConditionsModel):
    """Class for vehicle impoundment in Jail CC Plea."""
    vehicle_make_model: str = None
    vehicle_license_plate: str = None
    impound_time: str = None
    impound_action: str = None
    release_vehicle: bool = False
    terms_list = [
        ('vehicle_make_model', 'vehicle_make_model_box'),
        ('vehicle_license_plate', 'vehicle_license_plate_box'),
        ('impound_time', 'vehicle_impound_time_box'),
        ('impound_action', 'vehicle_impound_action_box'),
        ('release_vehicle', 'vehicle_release_checkBox'),
    ]


@dataclass
class LicenseSuspension(ConditionsModel):
    """Class for keeping track of the license suspension terms that are ordered."""
    license_type: str = None
    suspended_date: str = None
    suspension_term: str = None
    remedial_driving_class_required: bool = False
    als_terminated: bool = False
    interlock_required: bool = False
    terms_list = [
        ('license_type', 'license_type_box'),
        ('suspended_date', 'license_suspension_date_box'),
        ('suspension_term', 'term_of_suspension_box'),
        ('remedial_driving_class_required', 'remedial_driving_class_checkBox'),
        ('als_terminated', 'als_terminated_checkBox'),
        ('interlock_required', 'license_susp_interlock_checkBox'),
    ]


@dataclass
class OtherConditions(ConditionsModel):
    """Class for keeping track of other conditions that are ordered.

    This condition is a freeform text entry box in the UI.
    """
    terms: str = None
    terms_list = [
        ('terms', 'other_conditions_textEdit'),
    ]


@dataclass
class VictimNotification(ConditionsModel):
    """Class for tracking Victim Notification requirements that are ordered."""
    fingerprinting_ordered: bool = False
    victim_reparation_notice: bool = False
    victim_prosecutor_notice: bool = False
    terms_list = [
        ('fingerprinting_ordered', 'fingerprinting_checkBox'),
        ('victim_reparation_notice', 'victim_reparation_checkBox'),
        ('victim_prosecutor_notice', 'victim_prosecutor_notification_checkBox'),
    ]


@dataclass
class Diversion(ConditionsModel):
    """Class for tracking diversion program conditions."""
    marijuana_diversion: bool = False
    theft_diversion: bool = False
    other_diversion: bool = False
    jail_imposed: bool = False
    program_name: str = None
    diversion_fine_pay_date: str = None
    diversion_jail_report_date: str = None
    restitution_ordered: bool = False
    pay_restitution_to: str = None
    pay_restitution_amount: str = None
    probation_ordered: bool = False
    other_conditions_ordered: bool = False
    other_conditions_text: str = None
    terms_list = [
        ('marijuana_diversion', 'marijuana_diversion_radio_btn'),
        ('theft_diversion', 'theft_diversion_radio_btn'),
        ('other_diversion', 'other_diversion_radio_btn'),
        ('jail_imposed', 'diversion_jail_imposed_check_box'),
        ('diversion_fine_pay_date', 'diversion_fine_pay_date'),
        ('diversion_jail_report_date', 'diversion_jail_report_date'),
        ('probation_ordered', 'probation_check_box'),
        ('restitution_ordered', 'pay_restitution_check_box'),
        ('pay_restitution_to', 'pay_restitution_to_line'),
        ('pay_restitution_amount', 'pay_restitution_amount_line'),
        ('other_conditions_ordered', 'other_conditions_check_box'),
        ('other_conditions_text', 'other_conditions_text'),
    ]

    def get_program_name(self) -> str:
        if self.marijuana_diversion:
            return 'Marijuana Diversion Program'
        elif self.theft_diversion:
            return 'Theft Diversion Program'
        elif self.other_diversion:
            return 'Prosecutor Diversion Program'
        else:
            return 'No diversion program selected'


# NonCondition Models #

@dataclass
class ProbationViolationBondConditions:
    """Conditions specific to a Probation Violation Bond Dialog.

    They are an object that is then part of CriminalCaseInformation.
    """
    bond_type: str = None
    bond_amount: str = None
    no_alcohol_drugs: bool = False
    alcohol_test_kiosk: bool = False
    monitoring: bool = False
    monitoring_type: str = None
    comply_protection_order: bool = False
    cc_violation_other_conditions_ordered: bool = False
    cc_violation_other_conditions_terms: str = None
    terms_list = [
        ("bond_type", "bond_type_box"),
        ("bond_amount", "bond_amount_box"),
        ("no_alcohol_drugs", "no_alcohol_drugs_checkBox"),
        ("alcohol_test_kiosk", "alcohol_test_kiosk_checkBox"),
        ("monitoring", "monitoring_checkBox"),
        ("monitoring_type", "monitoring_type_box"),
        ("comply_protection_order", "comply_protection_order_checkBox"),
        ("cc_violation_other_conditions_ordered", "cc_violation_other_conditions_checkBox"),
        ("cc_violation_other_conditions_terms", "cc_violation_other_conditions_terms_box"),
    ]


@dataclass
class CourtCosts:
    """Class for data related to court costs."""
    ordered: str = None
    amount: int = 0
    ability_to_pay_time: str = None
    balance_due_date: str = None
    pay_today_amount: str = None
    monthly_pay_amount: str = None


@dataclass
class JailTerms:
    """Class for keeping track of jail terms that are ordered."""
    ordered: bool = False

    report_type: str = None
    report_date: str = None
    report_time: str = None
    jail_sentence_execution_type: str = None
    jail_report_days_notes: str = None

    companion_cases_exist: bool = False
    companion_cases_numbers: str = None
    companion_cases_sentence_type: str = None

    currently_in_jail: str = None
    days_in_jail: str = None
    apply_jtc: str = None

    total_jail_days_imposed: int = None
    total_jail_days_suspended: int = None
    total_jail_days_to_serve: int = None

    terms_list = [
        ('report_type', 'report_type_box'),
        ('report_date', 'report_date_box'),
        ('report_time', 'report_time_box'),
        ('jail_sentence_execution_type', 'jail_sentence_execution_type_box'),
        ('jail_report_days_notes', 'jail_report_days_notes_box'),
    ]


@dataclass
class FailureToAppearConditions:
    arrest_warrant: bool = False
    arrest_warrant_radius: str = None
    set_no_trial: bool = False
    surety_appear: bool = False
    bond_forfeited: bool = False
    forfeit_license: bool = False
    non_resident_license: bool = False
    proof_of_service: bool = False
    supplemental_summons: bool = False
    registration_block: bool = False
    set_bond: bool = False
    bond_type: str = None
    bond_amount: str = None
    terms_list = [
        ("arrest_warrant", "arrest_warrant_checkBox"),
        ("arrest_warrant_radius", "arrest_warrant_radius_box"),
        ("set_no_trial", "set_no_trial_checkBox"),
        ("surety_appear", "surety_appear_checkBox"),
        ("set_bond", "set_bond_checkBox"),
        ("bond_forfeited", "bond_forfeited_checkBox"),
        ("forfeit_license", "operator_license_checkBox"),
        ("non_resident_license", "non_resident_license_checkBox"),
        ("proof_of_service", "proof_of_service_checkBox"),
        ("supplemental_summons", "supplemental_summons_checkBox"),
        ("registration_block", "registration_block_checkBox"),
        ("bond_type", "bond_type_box"),
        ("bond_amount", "bond_amount_box"),
    ]


@dataclass
class FutureSentencing:
    prepare_psi: bool = False
    set_restitution: bool = False
    victim_appearance: bool = False
    plea_only_bond: str = None
    plea_only_bond_amount: str = None
    terms_list = [
        ("plea_only_bond", "plea_only_bond_type_box"),
        ("plea_only_bond_amount", "plea_only_bond_amount_box"),
        ("prepare_psi", "prepare_psi_checkBox"),
        ("set_restitution", "set_restitution_checkBox"),
        ("victim_appearance", "victim_appearance_checkBox"),
    ]


@dataclass
class BondConditions:
    """Conditions specific to a Not Guilty Bond Dialog.

    They are an object that is then part of CriminalCaseInformation.
    """
    bond_type: str = None
    bond_amount: str = None
    no_contact: bool = False
    no_alcohol_drugs: bool = False
    alcohol_drugs_assessment: bool = False
    mental_health_assessment: bool = False
    fingerprint_in_court: bool = False
    specialized_docket: bool = False
    specialized_docket_type: str = None
    monitoring: bool = False
    monitoring_type: str = None
    comply_protection_order: bool = False
    public_safety_suspension: bool = False
    terms_list = [
        ("bond_type", "bond_type_box"),
        ("bond_amount", "bond_amount_box"),
        ("no_alcohol_drugs", "no_alcohol_drugs_checkBox"),
        ("alcohol_drugs_assessment", "alcohol_drugs_assessment_checkBox"),
        ("mental_health_assessment", "mental_health_assessment_checkBox"),
        ("fingerprint_in_court", "fingerprint_in_court_checkBox"),
        ("specialized_docket", "specialized_docket_checkBox"),
        ("specialized_docket_type", "specialized_docket_type_box"),
        ("monitoring", "monitoring_checkBox"),
        ("monitoring_type", "monitoring_type_box"),
        ("comply_protection_order", "comply_protection_order_checkBox"),
        ("public_safety_suspension", "public_safety_suspension_checkBox"),
    ]


@dataclass
class BondModificationConditions(BondConditions):
    """Adds the attribute for bond modification to bond conditions. The terms_list is a copy of
    the BondConditions list so appending bond modification does not alter the BondConditions
    terms_list."""
    bond_modification_decision: str = None
    terms_list = BondConditions.terms_list.copy()
    terms_list.append(("bond_modification_decision", "bond_modification_decision_box"))


@dataclass
class ContinuanceConditions:
    continuance_reason: str = None
    current_arraignment_date: str = None
    new_arraignment_date: str = None
    terms_list = [
        ('continuance_reason', 'continuance_reason_box'),
        ('current_arraignment_date', 'current_arraignment_date_box'),
        ('new_arraignment_date', 'new_arraignment_date_box'),
    ]
