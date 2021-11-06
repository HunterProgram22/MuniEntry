"""Module containing all data structures for everything at the moment."""
from dataclasses import dataclass, field, asdict

from models.party_types import JudicialOfficer, Defendant


@dataclass
class CaseInformation:
    """This object stores all the information for a case both at inception and
    as it is populated through the application."""
    judicial_officer: object
    case_number: str  = None
    defendant: object = Defendant()
    fra_in_file: str  = None
    fra_in_court: str  = None
    plea_trial_date: str  = None
    charges_list: list = field(default_factory=list)
    community_control_terms: str  = None
    ability_to_pay_time: str  = None
    balance_due_date: str  = None
    sentencing_date: str  = None
    amend_offense_details: str  = None
    community_service_terms: str  = None
    hours_of_service: str  = None
    days_to_complete_service: str  = None
    due_date_for_service: str  = None
    license_suspension_details: str  = None
    other_conditions_details: str  = None
    court_costs_ordered: str  = None
    court_costs: int  = 0
    total_fines: int  = 0

    def add_charge_to_list(self, charge):
        self.charges_list.append(charge)

    def get_case_information(self):
        """Returns a dictionary with all of case information required
        to populate an entry."""
        return asdict(self)


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
class AmendOffenseDetails(object):
    """TODO: This should be refactored to a pure function most likely."""
    original_charge: str = None
    amended_charge: str = None
    motion_disposition: str = "granted"


@dataclass
class CommunityControlTerms(object):
    """Class for keeping track of all community control terms that are tied to
    a specific case."""
    community_control_required: bool = False
    term_of_community_control: int = 0
    type_of_community_control: str = "basic"


@dataclass
class CommunityServiceTerms(object):
    """Class for keeping track of all community service terms that are tied to
    a specific case."""
    community_service_ordered: bool = False
    hours_of_service: int = 0
    days_to_complete_service: int = 0
    due_date_for_service: str = None


@dataclass
class LicenseSuspensionTerms(object):
    """Class for keeping track of the license suspension terms that are tied to
    a specific case."""
    license_suspension_ordered: bool = False
    license_type: str = None
    license_suspended_date: str = None
    license_suspension_term: str = None
    remedial_driving_class_required: bool = False


@dataclass
class OtherConditionsTerms(object):
    """Class for keeping track of other conditions that are tied to
    a specific case. This condition is a freeform text entry box in the UI."""
    other_conditions_ordered: bool = False
    other_conditions_terms: str = None
