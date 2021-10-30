"""Module containing all data structures for everything at the moment."""
from dataclasses import dataclass

from models.party_types import JudicialOfficer, Defendant


class CaseInformation(object):
    """This object stores all the information for a case both at inception and
    as it is populated through the application."""

    def __init__(self, judicial_officer):
        self.judicial_officer = judicial_officer
        self.case_number = None
        self.defendant = Defendant()
        self.fra_in_file = None
        self.fra_in_court = None
        self.plea_trial_date = None
        self.charges_list = []
        self.community_control_terms = None
        self.ability_to_pay_time = None
        self.balance_due_date = None
        self.sentencing_date = None
        self.amend_offense_details = None
        self.community_service_terms = None
        self.hours_of_service = None
        self.days_to_complete_service = None
        self.due_date_for_service = None
        self.license_suspension_details = None
        self.other_conditions_details = None
        self.court_costs_ordered = None
        self.court_costs = 0
        self.total_fines = 0

    def add_charge_to_list(self, charge):
        self.charges_list.append(charge)

    def get_case_information(self):
        """Returns a dictionary with all of case information required
        to populate an entry."""
        self.formatted_case_information = {
            "case_number": self.case_number,
            "defendant_last_name": self.defendant.last_name,
            "defendant_first_name": self.defendant.first_name,
            "plea_trial_date": self.plea_trial_date,
            "amend_offense_details": self.amend_offense_details,
            "charges_list": self.charges_list,
            "ability_to_pay_time": self.ability_to_pay_time,
            "balance_due_date": self.balance_due_date,
            "community_control_terms": self.community_control_terms,
            "fra_in_file": self.fra_in_file,
            "fra_in_court": self.fra_in_court,
            "community_service_terms": self.community_service_terms,
            "hours_of_service": self.hours_of_service,
            "days_to_complete_service": self.days_to_complete_service,
            "due_date_for_service": self.due_date_for_service,
            "judicial_officer": self.judicial_officer.first_name
            + " "
            + self.judicial_officer.last_name,
            "judicial_officer_type": self.judicial_officer.officer_type,
            "license_suspension_details": self.license_suspension_details,
            "other_conditions_details": self.other_conditions_details,
            "court_costs_ordered": self.court_costs_ordered,
            "sentencing_date": self.sentencing_date,
        }
        return self.formatted_case_information


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
