from munientry.models.party_types import Defendant as Defendant
from typing import Any

class CmsCaseInformation:
    case_number: str
    defendant: object
    defense_counsel: str
    defense_counsel_type: str
    charges_list: list
    fra_in_file: str
    def __init__(self, case_number, defendant, defense_counsel, defense_counsel_type, charges_list, fra_in_file) -> None: ...

class CriminalCharge:
    offense: str
    statute: str
    degree: str
    plea: str
    type: str
    finding: str
    fines_amount: str
    fines_suspended: str
    jail_days: str
    jail_days_suspended: str
    def __init__(self, offense, statute, degree, plea, type, finding, fines_amount, fines_suspended, jail_days, jail_days_suspended) -> None: ...

class AmendOffenseDetails:
    original_charge: str
    amended_charge: str
    motion_disposition: str
    def __init__(self, original_charge=None, amended_charge=None, motion_disposition=None) -> None: ...

class BondConditions:
    bond_type: str
    bond_amount: str
    no_contact: bool
    no_alcohol_drugs: bool
    alcohol_drugs_assessment: bool
    mental_health_assessment: bool
    alcohol_test_kiosk: bool
    specialized_docket: bool
    specialized_docket_type: str
    monitoring: bool
    monitoring_type: str
    comply_protection_order: bool
    terms_list: Any
    def __init__(self, bond_type, bond_amount, no_contact, no_alcohol_drugs, alcohol_drugs_assessment, mental_health_assessment, alcohol_test_kiosk, specialized_docket, specialized_docket_type, monitoring, monitoring_type, comply_protection_order) -> None: ...

class BondModificationConditions(BondConditions):
    bond_modification_decision: str
    terms_list: Any
    def __init__(self, bond_type, bond_amount, no_contact, no_alcohol_drugs, alcohol_drugs_assessment, mental_health_assessment, alcohol_test_kiosk, specialized_docket, specialized_docket_type, monitoring, monitoring_type, comply_protection_order, bond_modification_decision) -> None: ...

class CommunityControlViolationBondConditions:
    bond_type: str
    bond_amount: str
    no_alcohol_drugs: bool
    alcohol_test_kiosk: bool
    monitoring: bool
    monitoring_type: str
    comply_protection_order: bool
    cc_violation_other_conditions_ordered: bool
    cc_violation_other_conditions_terms: str
    terms_list: Any
    def __init__(self, bond_type, bond_amount, no_alcohol_drugs, alcohol_test_kiosk, monitoring, monitoring_type, comply_protection_order, cc_violation_other_conditions_ordered, cc_violation_other_conditions_terms) -> None: ...

class DomesticViolenceBondConditions:
    ordered: bool
    vacate_residence: bool
    residence_address: str
    exclusive_possession_to: str
    surrender_weapons: bool
    surrender_weapons_date: str
    terms_list: Any
    def __init__(self, ordered, vacate_residence, residence_address, exclusive_possession_to, surrender_weapons, surrender_weapons_date) -> None: ...

class AdminLicenseSuspensionConditions:
    ordered: bool
    objection: str
    disposition: str
    explanation: str
    terms_list: Any
    def __init__(self, ordered, objection, disposition, explanation) -> None: ...

class NoContact:
    ordered: bool
    name: str
    terms_list: Any
    def __init__(self, ordered, name) -> None: ...

class CustodialSupervision:
    ordered: bool
    supervisor: str
    terms_list: Any
    def __init__(self, ordered, supervisor) -> None: ...

class CommunityService:
    ordered: bool
    hours_of_service: str
    days_to_complete_service: str
    due_date_for_service: str
    terms_list: Any
    def __init__(self, ordered, hours_of_service, days_to_complete_service, due_date_for_service) -> None: ...

class FailureToAppearConditions:
    arrest_warrant: bool
    arrest_warrant_radius: str
    set_no_trial: bool
    surety_appear: bool
    bond_forfeited: bool
    forfeit_license: bool
    non_resident_license: bool
    proof_of_service: bool
    supplemental_summons: bool
    registration_block: bool
    set_bond: bool
    bond_type: str
    bond_amount: str
    terms_list: Any
    def __init__(self, arrest_warrant, arrest_warrant_radius, set_no_trial, surety_appear, bond_forfeited, forfeit_license, non_resident_license, proof_of_service, supplemental_summons, registration_block, set_bond, bond_type, bond_amount) -> None: ...

class CommunityControl:
    ordered: bool
    type_of_control: str
    term_of_control: str
    not_within_500_feet_ordered: bool
    not_within_500_feet_person: str
    no_contact_with_ordered: bool
    no_contact_with_person: str
    alcohol_monitoring: bool
    alcohol_monitoring_court_pay: bool
    alcohol_monitoring_time: str
    house_arrest: bool
    house_arrest_time: str
    interlock_vehicles_only: bool
    pay_restitution: bool
    pay_restitution_to: str
    pay_restitution_amount: str
    antitheft_program: bool
    anger_management_program: bool
    alcohol_evaluation: bool
    domestic_violence_program: bool
    driver_intervention_program: bool
    mental_health_evaluation: bool
    other_community_control: bool
    other_community_control_conditions: str
    community_control_community_service: bool
    community_control_community_service_hours: str
    gps_exclusion: bool
    gps_exclusion_radius: str
    gps_exclusion_location: str
    daily_reporting: bool
    specialized_docket_ordered: bool
    specialized_docket_type: str
    terms_list: Any
    def __init__(self, ordered, type_of_control, term_of_control, not_within_500_feet_ordered, not_within_500_feet_person, no_contact_with_ordered, no_contact_with_person, alcohol_monitoring, alcohol_monitoring_court_pay, alcohol_monitoring_time, house_arrest, house_arrest_time, interlock_vehicles_only, pay_restitution, pay_restitution_to, pay_restitution_amount, antitheft_program, anger_management_program, alcohol_evaluation, domestic_violence_program, driver_intervention_program, mental_health_evaluation, other_community_control, other_community_control_conditions, community_control_community_service, community_control_community_service_hours, gps_exclusion, gps_exclusion_radius, gps_exclusion_location, daily_reporting, specialized_docket_ordered, specialized_docket_type) -> None: ...

class VehicleSeizure:
    ordered: bool
    vehicle_make_model: str
    vehicle_license_plate: str
    tow_to_residence: bool
    motion_to_return_vehicle: bool
    state_opposes: str
    disposition_motion_to_return: str
    terms_list: Any
    def __init__(self, ordered, vehicle_make_model, vehicle_license_plate, tow_to_residence, motion_to_return_vehicle, state_opposes, disposition_motion_to_return) -> None: ...

class Impoundment:
    ordered: bool
    vehicle_make_model: str
    vehicle_license_plate: str
    impound_time: str
    impound_action: str
    terms_list: Any
    def __init__(self, ordered, vehicle_make_model, vehicle_license_plate, impound_time, impound_action) -> None: ...

class LicenseSuspension:
    ordered: bool
    license_type: str
    suspended_date: str
    suspension_term: str
    remedial_driving_class_required: bool
    als_terminated: bool
    terms_list: Any
    def __init__(self, ordered, license_type, suspended_date, suspension_term, remedial_driving_class_required, als_terminated) -> None: ...

class JailTerms:
    ordered: bool
    report_type: str
    report_date: str
    report_time: str
    jail_report_days_notes: str
    jail_term_type: str
    jail_sentence_execution_type: str
    companion_cases_exist: bool
    companion_cases_numbers: str
    companion_cases_sentence_type: str
    currently_in_jail: str
    days_in_jail: str
    apply_jtc: str
    total_jail_days_imposed: int
    total_jail_days_suspended: int
    total_jail_days_to_serve: int
    terms_list: Any
    def __init__(self, ordered, report_type, report_date, report_time, jail_report_days_notes, jail_term_type, jail_sentence_execution_type, companion_cases_exist, companion_cases_numbers, companion_cases_sentence_type, currently_in_jail, days_in_jail, apply_jtc, total_jail_days_imposed, total_jail_days_suspended, total_jail_days_to_serve) -> None: ...

class OtherConditions:
    ordered: bool
    terms: str
    terms_list: Any
    def __init__(self, ordered, terms) -> None: ...

class Diversion:
    ordered: bool
    marijuana_diversion: bool
    theft_diversion: bool
    other_diversion: bool
    jail_imposed: bool
    program_name: str
    diversion_fine_pay_date: str
    diversion_jail_report_date: str
    terms_list: Any
    def get_program_name(self): ...
    def __init__(self, ordered, marijuana_diversion, theft_diversion, other_diversion, jail_imposed, program_name, diversion_fine_pay_date, diversion_jail_report_date) -> None: ...

class CourtCosts:
    ordered: str
    amount: int
    ability_to_pay_time: str
    balance_due_date: str
    def __init__(self, ordered, amount, ability_to_pay_time, balance_due_date) -> None: ...

class FutureSentencing:
    prepare_psi: bool
    set_restitution: bool
    victim_appearance: bool
    plea_only_bond: str
    terms_list: Any
    def __init__(self, prepare_psi, set_restitution, victim_appearance, plea_only_bond) -> None: ...

class VictimNotification:
    ordered: bool
    fingerprinting_ordered: bool
    victim_reparation_notice: bool
    victim_prosecutor_notice: bool
    terms_list: Any
    def __init__(self, ordered, fingerprinting_ordered, victim_reparation_notice, victim_prosecutor_notice) -> None: ...

class CriminalCaseInformation:
    judicial_officer: object
    case_number: str = ...
    plea_trial_date: str
    appearance_reason: str
    victim_statements: bool
    offense_of_violence: bool
    future_sentencing: object
    sentencing_date: str
    defendant: object
    defense_counsel: str
    defense_counsel_type: str
    defense_counsel_waived: bool
    fra_in_file: bool
    fra_in_court: bool
    fines_and_costs_jail_credit: bool
    charges_list: list
    amended_charges_list: list
    amend_offense_details: object
    fine_jail_days: str
    total_fines: int
    total_fines_suspended: int
    cc_violation_probable_cause: str
    cc_bond_conditions: object
    fta_conditions: object
    court_costs: object
    diversion: object
    community_control: object
    jail_terms: object
    bond_conditions: object
    no_contact: object
    custodial_supervision: object
    domestic_violence_conditions: object
    admin_license_suspension: object
    vehicle_seizure: object
    other_conditions: object
    community_service: object
    license_suspension: object
    victim_notification: object
    impoundment: object
    def add_charge_to_list(self, charge) -> None: ...
    def get_case_information(self): ...
    def __init__(self, judicial_officer, case_number, plea_trial_date, appearance_reason, victim_statements, offense_of_violence, future_sentencing, sentencing_date, defendant, defense_counsel, defense_counsel_type, defense_counsel_waived, fra_in_file, fra_in_court, fines_and_costs_jail_credit, charges_list, amended_charges_list, amend_offense_details, fine_jail_days, total_fines, total_fines_suspended, cc_violation_probable_cause, cc_bond_conditions, fta_conditions, court_costs, diversion, community_control, jail_terms, bond_conditions, no_contact, custodial_supervision, domestic_violence_conditions, admin_license_suspension, vehicle_seizure, other_conditions, community_service, license_suspension, victim_notification, impoundment) -> None: ...
