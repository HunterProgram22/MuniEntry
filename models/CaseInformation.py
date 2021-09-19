"""Module containing all data structures for everything at the moment."""


class CaseInformation(object):
    """This object stores all the information for a case both at inception and
    as it is populated through the application."""

    def __init__(self, judicial_officer, judicial_officer_type):
        self.judicial_officer = judicial_officer
        self.judicial_officer_type = judicial_officer_type
        self.case_number = None
        self.plaintiff_name = None
        self.plaintiff_attorney_name = None
        self.waived_counsel = False
        self.defendant_last_name = None
        self.defendant_first_name = None
        self.defendant_attorney_name = None
        self.defendant_date_of_birth = None
        self.operator_license_number = None
        self.fra_in_file = None
        self.fra_in_court = None
        self.plea_trial_date = None
        self.charges_list = []
        self.community_control_terms = None
        self.ovi_details = None
        self.ability_to_pay_details = None
        self.ability_to_pay_time = None
        self.amend_offense_details = None
        self.is_citizen = False
        self.understood_plea = True
        self.citizen_deportation = False
        self.total_charges = 0
        self.community_service_terms = None
        self.hours_of_service = None
        self.days_to_complete_service = None
        self.due_date_for_service = None
        self.license_suspension_details = None

    def add_charge_to_list(self, charge):
        self.charges_list.append(charge)


    def get_case_information(self):
        """Returns a dictionary with all of case information required
        to populate an entry."""
        self.formatted_case_information = {
            "case_number": self.case_number,
            "defendant_last_name": self.defendant_last_name,
            "defendant_first_name": self.defendant_first_name,
            "waived_counsel": self.waived_counsel,
            "defendant_attorney_name": self.defendant_attorney_name,
            "plea_trial_date": self.plea_trial_date,
            "is_citizen": self.is_citizen,
            "understood_plea": self.understood_plea,
            "citizen_deportation": self.citizen_deportation,
            "ovi_details": self.ovi_details,
            "amend_offense_details": self.amend_offense_details,
            "charges_list": self.charges_list,
            "ability_to_pay_details": self.ability_to_pay_details,
            "ability_to_pay_time": self.ability_to_pay_time,
            "community_control_terms": self.community_control_terms,
            "balance_due_date": self.balance_due_date,
            "fra_in_file": self.fra_in_file,
            "fra_in_court": self.fra_in_court,
            "community_service_terms": self.community_service_terms,
            "hours_of_service": self.hours_of_service,
            "days_to_complete_service": self.days_to_complete_service,
            "due_date_for_service": self.due_date_for_service,
            "judicial_officer": self.judicial_officer,
            "judicial_officer_type": self.judicial_officer_type,
            "license_suspension_details": self.license_suspension_details,
        }
        return self.formatted_case_information


class CriminalCharge(object):
    def __init__(self):
        self.offense = None
        self.statute = None
        self.degree = None
        self.plea = None
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
        self.ability_to_pay_time = 0
        self.pretrial_jail_days_credit = True
        self.community_service_for_fines = True
        self.fines_suspended_for_valid_license = False


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
        self.driving_privileges = None
        self.driving_privileges_term = None
        self.remedial_driving_class_required = False
