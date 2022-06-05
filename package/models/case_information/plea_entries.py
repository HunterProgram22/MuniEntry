"""Contains all dataclasses for entries that do not contain FRA or Court Costs."""
from dataclasses import dataclass, field

from package.models.case_information.criminal_case_information import (
    CriminalCaseInformation,
)
from package.models.conditions_models import (
    AdminLicenseSuspensionConditions,
    BondConditions,
    CommunityControlViolationBondConditions,
    CustodialSupervision,
    DomesticViolenceBondConditions,
    FailureToAppearConditions,
    FutureSentencing,
    NoContact,
    OtherConditions,
    VehicleSeizure,
)


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
