"""Module containing all data structures for everything at the moment."""
from dataclasses import dataclass, field, asdict

from package.models.party_types import Defendant


@dataclass
class CaseLoadData:
    """This object is used to store data from the arraignments database that is loaded. The data can
    then be passed to the specific dialog selected and will be transferred to cms_case information."""
    case_number: str = None
    defendant_last_name: str = None
    defendant_first_name: str = None
    charges_list: list = field(default_factory=list)
    fra_in_file: str = None


@dataclass
class CriminalCharge:
    """Class for keeping track of all information that is specific to each
    individual charge in a cms_case."""
    offense: str = None
    statute: str = None
    degree: str = None
    plea: str = None
    type: str = None
    finding: str = None
    fines_amount: str = None
    fines_suspended: str = None
    jail_days: str = None
    jail_days_suspended: str = None


@dataclass
class AmendOffenseDetails:
    """TODO: This should be refactored to a pure function most likely."""
    original_charge: str = None
    amended_charge: str = None
    motion_disposition: str = "granted"


@dataclass
class FTABondConditions:
    """Conditions specific to an FTA Bond Dialog. They are an object
    that is then part of CriminalCaseInformation."""
    appearance_reason: str = None
    forfeit_bond: str = None
    issue_warrant: str = None
    forfeit_license: str = None
    vehicle_registration_block: str = None
    bond_type: str = None
    bond_amount: str = None
    no_contact: bool = False
    no_alcohol_drugs: bool = False
    alcohol_drugs_assessment: bool = False
    alcohol_test_kiosk: bool = False
    specialized_docket: bool = False
    specialized_docket_type: str = None
    monitoring: bool = False
    monitoring_type: str = None


@dataclass
class DomesticViolenceBondConditions:
    """Domestic Violence Bond Conditions for Special Bond Conditions."""
    ordered: bool = False
    vacate_residence: bool = False
    residence_address: str = None
    exclusive_possession_to: str = None
    surrender_weapons: bool = False
    surrender_weapons_date: str = None


@dataclass
class AdminLicenseSuspensionConditions:
    """Admin License Suspension Conditions for Special Bond Conditions."""
    ordered: bool = False
    objection: str = None
    disposition: str = None
    explanation: str = None


@dataclass
class NoContact:
    """No Contact conditions for Special Bond Conditions."""
    ordered: bool = False
    name: str = None


@dataclass
class CustodialSupervision:
    """Custodial Supervision conditions for Special Bond Conditions."""
    ordered: bool = False
    supervisor: str = None


@dataclass
class CommunityService:
    """Class for keeping track of all community service terms that are tied to
    a specific cms_case."""
    ordered: bool = False
    hours_of_service: int = 0
    days_to_complete_service: int = 0
    due_date_for_service: str = None


@dataclass
class CommunityControl:
    ordered: bool = False
    type_of_control: str = "basic"
    term_of_control: str = None
    not_within_500_feet_ordered: bool = False
    not_within_500_feet_person: str = None
    no_contact_with_ordered: bool = False
    no_contact_with_person: str = None
    alcohol_monitoring: bool = False
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
    gps_exclusion_radius: str = None
    gps_exclusion_location: str = None
    daily_reporting: bool = False


@dataclass
class VehicleSeizure:
    """Class for vehicle seizure terms in special bond conditions."""
    ordered: bool = False
    vehicle_make_model: str = None
    vehicle_license_plate: str = None
    tow_to_residence: bool = False
    motion_to_return_vehicle: bool = False
    state_opposes: str = None
    disposition_motion_to_return: str = None


@dataclass
class LicenseSuspension:
    """Class for keeping track of the license suspension terms that are tied to
    a specific cms_case."""
    ordered: bool = False
    license_type: str = None
    suspended_date: str = None
    suspension_term: str = None
    remedial_driving_class_required: bool = False


@dataclass
class JailTerms:
    """Class for keeping track of jail terms."""
    ordered: bool = False
    report_type: str = None
    report_date: str = None
    report_time: str = None
    jail_report_days_notes: str = None
    jail_term_type: str = None
    jail_sentence_execution_type: str = None
    dip_ordered: bool = False
    companion_cases_exist: bool = False
    companion_case_numbers: str = None


@dataclass
class OtherConditions:
    """Class for keeping track of other conditions that are tied to
    a specific cms_case. This condition is a freeform text entry box in the UI."""
    ordered: bool = False
    terms: str = None


@dataclass
class Diversion:
    """Dataclass for tracking diversion programs."""
    ordered: bool = False
    marijuana_diversion: bool = False
    theft_diversion: bool = False
    program_name: str = None
    diversion_fine_pay_date: str = None
    diversion_jail_report_date: str = None

    def get_program_name(self):
        if self.marijuana_diversion is True:
            return "Marijuana Diversion Program"
        if self.theft_diversion is True:
            return "Theft Diversion Program"

@dataclass
class CourtCosts:
    """Class for data related to court costs. The ability to pay and balance due date apply in entries to
    fines as well."""
    ordered: str = None
    amount: int = 0
    ability_to_pay_time: str = None
    balance_due_date: str = None


@dataclass
class CriminalCaseInformation:
    """This object stores all the information for a cms_case both at inception and
    as it is populated through the application.
    TODO: Should also still refactor amend_offense_details to object of dataclass.
    :days_in_jail: - this is jail time credit but it is not part of jail commitment because
    it can be applied to fines if no jail days imposed.
    """
    judicial_officer: object = None
    case_number: str = None
    plea_trial_date: str = None
    appearance_reason: str = None
    sentencing_date: str = None
    defendant: object = Defendant()
    defense_counsel: str = None
    defense_counsel_type: str = None
    defense_counsel_waived: bool = False
    fra_in_file: bool = None
    fra_in_court: bool = None
    days_in_jail: str = None
    apply_jtc: str = None
    charges_list: list = field(default_factory=list)
    amended_charges_list: list = field(default_factory=list)
    amend_offense_details: object = None
    total_fines: int = 0
    total_fines_suspended: int = 0
    court_costs: object = CourtCosts()
    diversion: object = Diversion()
    community_control: object = CommunityControl()
    jail_terms: object = JailTerms()
    no_contact: object = NoContact()
    custodial_supervision: object = CustodialSupervision()
    fta_bond_conditions: object = FTABondConditions()
    community_service: object = CommunityService()
    license_suspension: object = LicenseSuspension()
    other_conditions: object = OtherConditions()
    domestic_violence_conditions: object = DomesticViolenceBondConditions()
    admin_license_suspension: object = AdminLicenseSuspensionConditions()
    vehicle_seizure: object = VehicleSeizure()

    def add_charge_to_list(self, charge):
        self.charges_list.append(charge)

    def get_case_information(self):
        """Returns a dictionary with all of cms_case information required
        to populate an entry."""
        return asdict(self)