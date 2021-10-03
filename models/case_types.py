"""Module containing all the data structures for cases."""

from PartyTypes import Party

class Case(object):
    """The base object from which all other objects are connected. Any matter
    before the court will have at a minimum some type of case."""

    def __init__(self, case_number: str) -> None:
        self.case_number = case_number
        self.case_type_code = case_number[2:5]
        self.case_parties = []

    def add_party_to_case(self, party_type: str) -> None:
        """The party_type will generally be either "Plaintiff" or "Defendant."""
        self.party_type = party_type
        self.case_parties.append(self.party_type)


class TrafficCase(Case):
    """
    A case type for traffic cases. The format for the case number will be
    either YYTRCXXXX or YYTRDXXXX.

    YY = last two digits of the year the case was filed.
    TRC = is for OVI offense cases.
    TRD = is for all other traffic cases (non-OVI).
    XXXX = the case number assigned to the case.

    """

    def __init__(self, case_number):
        """
        The initializion of a TrafficCase takes the case number and strips
        out the case numbers to create a case_type_code (i.e. TRC or TRD).
        """
        super().__init__(case_number)
        self.case_charges: list = []

    def add_charge_to_case(self, traffic_charge: TrafficCharge) -> None:
        self.traffic_charge: TrafficCharge = traffic_charge
        self.case_charges.append(self.traffic_charge)


class CriminalCase(Case):
    """
    A case type for criminal cases. The format for the case number will be
    either YYCRBXXXX

    YY = last two digits of the year the case was filed.
    CRB = is for all criminal cases.
    XXXX = the case number assigned to the case.

    """

    def __init__(self, case_number):
        """
        The initializion of a CriminalCase takes the case number and strips
        out the case numbers to create a case_type_code CRB.
        """
        super().__init__(case_number)


test = CriminalCase("21CRB0123")
print(test.case_type_code)
test.add_party_to_case(Party("Plaintiff"))
print(test.case_parties)
print(test.case_parties[0].party_type)
