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

    def add_charge(self, charge):
        self.charges_list.append(charge)

    def get_case_information(self):
        """Returns a dictionary with all of case information required
        to populate an entry."""
        return {
            "defendant_name": self.defendant_name,
            "case_number": self.case_number,
            "plea_trial_date": self.plea_trial_date,
            # "days_to_pay": self.days_to_pay,
            "offense_1": self.charges_list[0].offense,
            "degree_1": self.charges_list[0].degree,
            "plea_1": self.charges_list[0].plea,
            "fines_amount_1": self.charges_list[0].fines_amount,
            "fines_suspended_1": self.charges_list[0].fines_suspended,
            "jail_days_1": self.charges_list[0].jail_days,
            "jail_days_suspended_1": self.charges_list[0].jail_days_suspended,
        }


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
