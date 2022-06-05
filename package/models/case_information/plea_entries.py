"""Contains all dataclasses for entries that do not contain FRA or Court Costs."""
from dataclasses import dataclass, field

from package.models import conditions_models as cm
from package.models.case_information.criminal_case_information import (
    CriminalCaseInformation,
)


@dataclass
class NotGuiltyBondEntryCaseInformation(CriminalCaseInformation):
    bond_conditions: object = field(default_factory=cm.BondConditions)
    no_contact: object = field(default_factory=cm.NoContact)
    custodial_supervision: object = field(default_factory=cm.CustodialSupervision)
    domestic_violence_conditions: object = field(default_factory=cm.DomesticViolenceBondConditions)
    admin_license_suspension: object = field(default_factory=cm.AdminLicenseSuspensionConditions)
    vehicle_seizure: object = field(default_factory=cm.VehicleSeizure)
    other_conditions: object = field(default_factory=cm.OtherConditions)


@dataclass
class BondHearingEntryCaseInformation(NotGuiltyBondEntryCaseInformation):
    pass


@dataclass
class NoPleaBondEntryCaseInformation(NotGuiltyBondEntryCaseInformation):
    pass


@dataclass
class PleaOnlyEntryCaseInformation(CriminalCaseInformation):
    future_sentencing: object = field(default_factory=cm.FutureSentencing)


@dataclass
class CommunityControlViolationEntryCaseInformation(CriminalCaseInformation):
    cc_violation_probable_cause: str = None
    cc_bond_conditions: object = field(default_factory=cm.CommunityControlViolationBondConditions)


@dataclass
class FailureToAppearEntryCaseInformation(CriminalCaseInformation):
    fta_conditions: object = field(default_factory=cm.FailureToAppearConditions)


@dataclass
class LeapAdmissionEntryCaseInformation(CriminalCaseInformation):
    leap_sentencing_date: str = None
