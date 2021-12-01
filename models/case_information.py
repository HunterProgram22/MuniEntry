"""Module containing all data structures for everything at the moment."""
from dataclasses import dataclass, field, asdict

from models.party_types import Defendant


@dataclass
class CaseLoadData:
    """This object is used to store data from the arraignments database that is loaded. The data can
    then be passed to the specific dialog selected and will be transferred to case information."""
    case_number: str = None
    defendant_last_name: str = None
    defendant_first_name: str = None
    charges_list: list = field(default_factory=list)
    fra_in_file: str = None


@dataclass
class CriminalCharge:
    """Class for keeping track of all information that is specific to each
    individual charge in a case.
    TODO: Perhaps switch fine/jail to int/float?"""
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
class FTABondConditions:
    """Conditions specific to an FTA Bond Dialog. They are an object
    that is then part of CaseInformation."""
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
    exclusive_possession: str = None
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
class AmendOffenseDetails:
    """TODO: This should be refactored to a pure function most likely."""
    original_charge: str = None
    amended_charge: str = None
    motion_disposition: str = "granted"


@dataclass
class CommunityControlTerms:
    """Class for keeping track of all community control terms that are tied to
    a specific case."""
    community_control_required: bool = False
    term_of_community_control: int = 0
    type_of_community_control: str = "basic"


@dataclass
class CommunityServiceTerms:
    """Class for keeping track of all community service terms that are tied to
    a specific case."""
    community_service_ordered: bool = False
    hours_of_service: int = 0
    days_to_complete_service: int = 0
    due_date_for_service: str = None


@dataclass
class LicenseSuspensionTerms:
    """Class for keeping track of the license suspension terms that are tied to
    a specific case."""
    ordered: bool = False
    license_type: str = None
    license_suspended_date: str = None
    license_suspension_term: str = None
    remedial_driving_class_required: bool = False


@dataclass
class OtherConditionsTerms:
    """Class for keeping track of other conditions that are tied to
    a specific case. This condition is a freeform text entry box in the UI."""
    other_conditions_ordered: bool = False
    other_conditions_terms: str = None


@dataclass
class CaseInformation:
    """This object stores all the information for a case both at inception and
    as it is populated through the application."""
    judicial_officer: object
    case_number: str = None
    defendant: object = Defendant()
    fra_in_file: bool = None
    fra_in_court: bool = None
    plea_trial_date: str = None
    charges_list: list = field(default_factory=list)
    ability_to_pay_time: str = None
    balance_due_date: str = None
    sentencing_date: str = None
    amend_offense_details: str = None
    court_costs_ordered: str = None
    court_costs: int = 0
    total_fines: int = 0
    total_fines_suspended: int = 0
    appearance_reason: str = None
    not_guilty_conditions: object = None
    fta_bond_conditions: object = FTABondConditions()
    community_control_terms: object = CommunityControlTerms()
    community_service_terms: object = CommunityServiceTerms()
    license_suspension_details: object = LicenseSuspensionTerms()
    other_conditions_details: object = OtherConditionsTerms()
    domestic_violence_conditions: object = DomesticViolenceBondConditions()
    admin_license_suspension: object = AdminLicenseSuspensionConditions()

    def add_charge_to_list(self, charge):
        self.charges_list.append(charge)

    def get_case_information(self):
        """Returns a dictionary with all of case information required
        to populate an entry."""
        return asdict(self)
