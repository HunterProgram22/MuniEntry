"""Contains all dataclasses for entries that do not contain FRA or Court Costs."""
from dataclasses import dataclass, field

from package.models import conditions_models as cm
from package.models.case_information.criminal_case_information import (
    CriminalCaseInformation,
)


@dataclass
class NotGuiltyBondEntryCaseInformation(CriminalCaseInformation):
    """General case information data variables and data for not guilty plea entry."""

    bond_conditions: object = field(default_factory=cm.BondConditions)
    no_contact: object = field(default_factory=cm.NoContact)
    custodial_supervision: object = field(default_factory=cm.CustodialSupervision)
    domestic_violence_conditions: object = field(default_factory=cm.DomesticViolenceBondConditions)
    admin_license_suspension: object = field(default_factory=cm.AdminLicenseSuspensionConditions)
    vehicle_seizure: object = field(default_factory=cm.VehicleSeizure)
    other_conditions: object = field(default_factory=cm.OtherConditions)


@dataclass
class BondHearingEntryCaseInformation(NotGuiltyBondEntryCaseInformation):
    """General case information data variables and data for bond hearing entry."""

    def __init__(self):
        """Only inherits no new attributes."""


@dataclass
class NoPleaBondEntryCaseInformation(NotGuiltyBondEntryCaseInformation):
    """General case information data variables and data for no plea bond entry."""

    def __init__(self):
        """Only inherits no new attributes."""


@dataclass
class PleaOnlyEntryCaseInformation(CriminalCaseInformation):
    """General case information data variables and data for plea only entry."""

    future_sentencing: object = field(default_factory=cm.FutureSentencing)


@dataclass
class CommunityControlViolationEntryCaseInformation(CriminalCaseInformation):
    """General case information data variables and data for community control violation entry."""

    cc_violation_probable_cause: str = None
    cc_bond_conditions: object = field(default_factory=cm.CommunityControlViolationBondConditions)


@dataclass
class FailureToAppearEntryCaseInformation(CriminalCaseInformation):
    """General case information data variables and data for failure to appear entry."""

    fta_conditions: object = field(default_factory=cm.FailureToAppearConditions)


@dataclass
class LeapAdmissionEntryCaseInformation(CriminalCaseInformation):
    """General case information data variables and data for Leap Admission entry."""

    leap_sentencing_date: str = None
