"""Module containing all data structures for everything at the moment."""
from dataclasses import asdict, dataclass, field

from package.models.conditions_models import (
    AdminLicenseSuspensionConditions,
    BondConditions,
    CommunityControl,
    CommunityControlViolationBondConditions,
    CommunityService,
    CourtCosts,
    CustodialSupervision,
    Diversion,
    DomesticViolenceBondConditions,
    FailureToAppearConditions,
    FutureSentencing,
    Impoundment,
    JailTerms,
    LicenseSuspension,
    NoContact,
    OtherConditions,
    VehicleSeizure,
    VictimNotification,
)
from package.models.party_types import Defendant


@dataclass
class CriminalCaseInformation(object):
    case_number: str = None
    judicial_officer: object = None
    plea_trial_date: str = None
    appearance_reason: str = None
    plaintiff: str = "State of Ohio"
    defendant: object = field(default_factory=Defendant)

    defense_counsel: str = None
    defense_counsel_type: str = None
    defense_counsel_waived: bool = False

    offense_of_violence: bool = False

    charges_list: list = field(default_factory=list)
    amended_charges_list: list = field(default_factory=list)
    amend_offense_details: object = None

    fra_in_file: bool = None
    fra_in_court: bool = None
    court_costs: object = field(default_factory=CourtCosts)

    def add_charge_to_list(self, charge):
        self.charges_list.append(charge)

    def get_case_information(self):
        """Returns a dictionary with all of cms_case information required
        to populate an entry."""
        return asdict(self)


@dataclass
class FineOnlyEntryCaseInformation(CriminalCaseInformation):
    fines_and_costs_jail_credit: bool = False
    fine_jail_days: str = None
    total_fines: int = 0
    total_fines_suspended: int = 0
    community_service: object = field(default_factory=CommunityService)
    license_suspension: object = field(default_factory=LicenseSuspension)
    other_conditions: object = field(default_factory=OtherConditions)


@dataclass
class JailCCEntryCaseInformation(FineOnlyEntryCaseInformation):
    victim_statements: bool = False
    sentencing_date: str = None
    community_control: object = field(default_factory=CommunityControl)
    jail_terms: object = field(default_factory=JailTerms)
    victim_notification: object = field(default_factory=VictimNotification)
    impoundment: object = field(default_factory=Impoundment)


@dataclass
class TrialSentencingEntryCaseInformation(JailCCEntryCaseInformation):
    pass


@dataclass
class NotGuiltyBondEntryCaseInformation(CriminalCaseInformation):
    bond_conditions: object = field(default_factory=BondConditions)
    no_contact: object = field(default_factory=NoContact)
    custodial_supervision: object = field(default_factory=CustodialSupervision)
    domestic_violence_conditions: object = field(default_factory=DomesticViolenceBondConditions)
    admin_license_suspension: object = field(default_factory=AdminLicenseSuspensionConditions)
    vehicle_seizure: object = field(default_factory=VehicleSeizure)
    other_conditions: object = field(default_factory=OtherConditions)


@dataclass
class BondHearingEntryCaseInformation(NotGuiltyBondEntryCaseInformation):
    pass


@dataclass
class NoPleaBondEntryCaseInformation(NotGuiltyBondEntryCaseInformation):
    pass


@dataclass
class PleaOnlyEntryCaseInformation(CriminalCaseInformation):
    future_sentencing: object = field(default_factory=FutureSentencing)


@dataclass
class CommunityControlViolationEntryCaseInformation(CriminalCaseInformation):
    cc_violation_probable_cause: str = None
    cc_bond_conditions: object = field(default_factory=CommunityControlViolationBondConditions)


@dataclass
class FailureToAppearEntryCaseInformation(CriminalCaseInformation):
    fta_conditions: object = field(default_factory=FailureToAppearConditions)


@dataclass
class LeapAdmissionEntryCaseInformation(CriminalCaseInformation):
    leap_sentencing_date: str = None


@dataclass
class LeapSentencingEntryCaseInformation(FineOnlyEntryCaseInformation):
    leap_plea_date: str = None


@dataclass
class DiversionEntryCaseInformation(CriminalCaseInformation):
    diversion: object = field(default_factory=Diversion)
    other_conditions: object = field(default_factory=OtherConditions)
