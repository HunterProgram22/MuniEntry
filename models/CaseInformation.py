# File with classes for storing case information to be used in controllers


class CaseInformation(object):
    """This object stores all the information for a case both at inception and
    as it is populated through the application."""

    def __init__(self):
        self.case_number = None
        self.plaintiff_name = None
        self.plaintiff_attorney_name = None
        self.waived_counsel = False
        self.defendant_name = None
        self.defendant_attorney_name = None
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

    def add_charge(self, charge):
        self.charges_list.append(charge)


    def get_case_information(self):
        """Returns a dictionary with all of case information required
        to populate an entry."""
        self.formatted_case_information = {
            "case_number": self.case_number,
            "defendant_name": self.defendant_name,
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
        self.days_to_pay = None


class CommunityControlTerms(object):
    def __init__(self):
        self.community_control_required = False
        self.term_of_community_control = 0
        self.type_of_community_control = "basic"
        self.not_refuse = False
        self.not_consume = False


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
        self.amending_procedure = None
        self.motion_disposition = "granted"
