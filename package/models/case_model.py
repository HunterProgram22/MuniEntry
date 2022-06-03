from dataclasses import dataclass, field, asdict

from package.models.party_types import Defendant


@dataclass
class CriminalCharge:
    """Class for keeping track of all information that is specific to each
    individual charge in a cms_case."""
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
class CaseInformation(object):
    case_number: str = None

    def get_case_information(self):
        """Returns a dictionary with all of cms_case information required
        to populate an entry."""
        return asdict(self)

    def add_charge_to_list(self, charge):
        self.charges_list.append(charge)


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


@dataclass
class LeapEntryCaseInformation(CriminalCaseInformation):
    leap_plea_date: str = None
    leap_sentencing_date: str = None