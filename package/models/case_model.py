from dataclasses import dataclass, field, asdict

from package.models.party_types import Defendant



@dataclass
class CaseInformation(object):
    case_number: str = None

    def get_case_information(self):
        """Returns a dictionary with all of cms_case information required
        to populate an entry."""
        return asdict(self)



@dataclass
class CriminalCaseInformation(CaseInformation):
    judicial_officer: object = None
    plea_trial_date: str = None
    appearance_reason: str = None
    plaintiff: str = "State of Ohio"
    defendant: object = field(default_factory=Defendant)

    defense_counsel: str = None
    defense_counsel_type: str = None
    defense_counsel_waived: bool = False

    charges_list: list = field(default_factory=list)
    amended_charges_list: list = field(default_factory=list)
    amend_offense_details: object = None

    def add_charge_to_list(self, charge):
        print('charge appended')
        self.charges_list.append(charge)

@dataclass
class LeapEntryCaseInformation(CriminalCaseInformation):
    leap_plea_date: str = None
    leap_sentencing_date: str = None