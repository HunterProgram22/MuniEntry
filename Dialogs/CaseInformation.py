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
        self.offense_1 = None
        self.plea_1 = None
        self.finding_1 = None
        self.fines_1 = None
        self.fines_suspended_1 = None
        self.jail_days_1 = None
        self.jail_days_suspended_1 = None
        self.offense_2 = None
        self.plea_2 = None
        self.finding_2 = None
        self.fines_2 = None
        self.fines_suspended_2 = None
        self.jail_days_2 = None
        self.jail_days_suspended_2 = None
        self.offense_3 = None
        self.plea_3 = None
        self.finding_3 = None
        self.fines_3 = None
        self.fines_suspended_3 = None
        self.jail_days_3 = None
        self.jail_days_suspended_3 = None
