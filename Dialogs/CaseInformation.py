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
        charge_to_add = CriminalCharge(charge)
        self.charges_list.append(charge_to_add)


class CriminalCharge(object):
    def __init__(self, charge):
        self.charge = charge
        self.plea = None
        self.finding = None
        self.fines = None
        self.fines_suspended = None
        self.jail_days = None
        self.jail_days_suspended = None
