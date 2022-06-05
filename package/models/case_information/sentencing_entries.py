from dataclasses import dataclass, field

from package.models.case_information.criminal_case_information import CriminalCaseInformation
from package.models.conditions_models import (
    CourtCosts,
    CommunityService,
    LicenseSuspension,
    OtherConditions,
    Diversion,
    CommunityControl,
    JailTerms,
    VictimNotification,
    Impoundment,
)


@dataclass
class CriminalSentencingCaseInformation(CriminalCaseInformation):
    fra_in_file: bool = None
    fra_in_court: bool = None
    court_costs: object = field(default_factory=CourtCosts)


@dataclass
class FineOnlyEntryCaseInformation(CriminalSentencingCaseInformation):
    fines_and_costs_jail_credit: bool = False
    fine_jail_days: str = None
    total_fines: int = 0
    total_fines_suspended: int = 0
    community_service: object = field(default_factory=CommunityService)
    license_suspension: object = field(default_factory=LicenseSuspension)
    other_conditions: object = field(default_factory=OtherConditions)


@dataclass
class DiversionEntryCaseInformation(CriminalSentencingCaseInformation):
    diversion: object = field(default_factory=Diversion)
    other_conditions: object = field(default_factory=OtherConditions)


@dataclass
class LeapSentencingEntryCaseInformation(FineOnlyEntryCaseInformation):
    leap_plea_date: str = None


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
