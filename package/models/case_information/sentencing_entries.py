"""Contains all dataclasses for entries that include FRA and Court Costs."""
from dataclasses import dataclass, field

from package.models import conditions_models as cm
from package.models.case_information.criminal_case_information import (
    CriminalCaseInformation,
)


@dataclass
class CriminalSentencingCaseInformation(CriminalCaseInformation):
    """Case information for insurance and court costs that is included in sentencing entries."""

    fra_in_file: bool = None
    fra_in_court: bool = None
    court_costs: object = field(default_factory=cm.CourtCosts)


@dataclass
class DiversionEntryCaseInformation(CriminalSentencingCaseInformation):
    """General case information data variables for diversion entry."""

    diversion: object = field(default_factory=cm.Diversion)
    other_conditions: object = field(default_factory=cm.OtherConditions)


@dataclass
class FineOnlyEntryCaseInformation(CriminalSentencingCaseInformation):
    """General case information data variables for fine only entry."""

    fines_and_costs_jail_credit: bool = False
    fine_jail_days: str = None
    total_fines: int = 0
    total_fines_suspended: int = 0
    community_service: object = field(default_factory=cm.CommunityService)
    license_suspension: object = field(default_factory=cm.LicenseSuspension)
    other_conditions: object = field(default_factory=cm.OtherConditions)


@dataclass
class LeapSentencingEntryCaseInformation(FineOnlyEntryCaseInformation):
    """General case information data variables and data for LEAP sentencing."""

    leap_plea_date: str = None


@dataclass
class JailCCEntryCaseInformation(FineOnlyEntryCaseInformation):
    """General case information data variables and data for jail and comm. control entry."""

    victim_statements: bool = False
    sentencing_date: str = None
    community_control: object = field(default_factory=cm.CommunityControl)
    jail_terms: object = field(default_factory=cm.JailTerms)
    victim_notification: object = field(default_factory=cm.VictimNotification)
    impoundment: object = field(default_factory=cm.Impoundment)


@dataclass
class TrialSentencingEntryCaseInformation(JailCCEntryCaseInformation):
    """General case information data variables and data for trial sentencing entry."""
