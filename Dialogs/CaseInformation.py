# File with classes for storing case information to be used in Dialogs


class CaseInformation(object):
    """This object stores all the information for a case both at inception and
    as it is populated through the application."""

    def __init__(self):
        self.case_number = None
        self.plaintiff_name = None
        self.plaintiff_attorney_name = None
        self.defendant_name = None
        self.defendant_attorney_name = None
        self.plea_trial_date = None
        self.charges_list = []
        self.community_control_terms = None
        self.ovi_details = None

    def add_charge(self, charge):
        self.charges_list.append(charge)

    def add_community_control(self, community_control_terms):
        self.community_control_terms = community_control_terms

    def get_case_information(self):
        """Returns a dictionary with all of case information required
        to populate an entry."""
        self.formatted_case_information = {
            "defendant_name": self.defendant_name,
            "case_number": self.case_number,
            "plea_trial_date": self.plea_trial_date,
            "ovi_details": self.ovi_details,
            "charges_list": self.charges_list,
            }
        return self.formatted_case_information


class CriminalCharge(object):
    def __init__(self):
        self.offense = None
        self.degree = None
        self.plea = None
        self.finding = None
        self.fines_amount = None
        self.fines_suspended = None
        self.jail_days = None
        self.jail_days_suspended = None
        self.days_to_pay = None


class CommunityControlTerms(object):
    def __init__(self):
        self.term_of_community_control = 0
        self.type_of_community_control = "basic"


class OviDetails(object):
    def __init__(self):
        self.ovi_offenses_within_ten_years = 0
        self.ovi_high_bac_test = False
        self.ovi_refused_breathylizer = False
        self.ovi_offenses_within_twenty_years = 0
