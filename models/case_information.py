"""Module containing all data structures for everything at the moment."""
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
        self.ability_to_pay_details = None  # Use Class
        self.ability_to_pay_time = None  # Use Class
        self.balance_due_date = None  # Use Class
        self.amend_offense_details = None
        self.total_charges = 0
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
            "defendant_attorney_name": self.defendant_attorney_name,
            "plea_trial_date": self.plea_trial_date,
            "amend_offense_details": self.amend_offense_details,
            "charges_list": self.charges_list,
            "ability_to_pay_details": self.ability_to_pay_details,
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
        }
        return self.formatted_case_information


class CriminalCharge(object):
    def __init__(self):
        self.offense = None
        self.statute = None
        self.degree = None
        self.plea = None
        self.type = None
        self.finding = None
        self.fines_amount = None
        self.fines_suspended = None
        self.court_costs = None
        self.jail_days = None
        self.jail_days_suspended = None


class CommunityControlTerms(object):
    def __init__(self):
        self.community_control_required = False
        self.term_of_community_control = 0
        self.type_of_community_control = "basic"
        self.not_refuse = False
        self.not_consume = False


class CommunityServiceTerms(object):
    def __init__(self):
        self.community_service_ordered = False
        self.hours_of_service = 0
        self.days_to_complete_service = 0
        self.due_date_for_service = None


class OviDetails(object):
    def __init__(self):
        self.ovi_offenses_within_ten_years = 0
        self.ovi_high_bac_test = False
        self.ovi_refused_breathylizer = False
        self.ovi_offenses_within_twenty_years = 0


class AbilityToPayDetails(object):
    def __init__(self):
        self.ability_to_pay_details = None
        self.ability_to_pay_time = None
        self.balance_due_date = None


class AmendOffenseDetails(object):
    def __init__(self):
        self.original_charge = None
        self.amended_charge = None
        self.motion_disposition = "granted"


class LicenseSuspension(object):
    def __init__(self):
        self.license_suspension_ordered = False
        self.license_type = None
        self.license_suspended_date = None
        self.license_suspension_term = None
        self.remedial_driving_class_required = False


class OtherConditionsDetails(object):
    def __init__(self):
        self.other_conditions_ordered = False
        self.other_conditions_terms = None
