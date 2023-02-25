"""Contains all dataclasses for entries that do not contain FRA or Court Costs."""
from loguru import logger
from dataclasses import dataclass, field

from munientry.models import conditions_models as cm
from munientry.models.case_information.criminal_case_information import (
    CriminalCaseInformation,
)


@dataclass
class PleaOnlyEntryCaseInformation(CriminalCaseInformation):
    """General case information data variables and data for plea only entry."""

    future_sentencing: object = field(default_factory=cm.FutureSentencing)


@dataclass
class ProbationViolationEntryCaseInformation(CriminalCaseInformation):
    """General case information data variables and data for community control violation entry."""

    cc_violation_probable_cause: str = None
    cc_bond_conditions: object = field(default_factory=cm.ProbationViolationBondConditions)


@dataclass
class FailureToAppearEntryCaseInformation(CriminalCaseInformation):
    """General case information data variables and data for failure to appear entry."""

    fta_conditions: object = field(default_factory=cm.FailureToAppearConditions)


@dataclass
class ArraignmentContinueEntryCaseInformation(CriminalCaseInformation):
    """General case information data variables and data for arraignment continuance entry."""

    continuance_conditions: object = field(default_factory=cm.ContinuanceConditions)


@dataclass
class FreeformEntryCaseInformation(CriminalCaseInformation):
    """General case information data variables for freeform entry."""

    entry_content_text: str = None


@dataclass
class CriminalSealingEntryCaseInformation(CriminalCaseInformation):
    """General case information data variables for criminal sealing entry."""


@dataclass
class LeapAdmissionEntryCaseInformation(CriminalCaseInformation):
    """General case information data variables and data for Leap Admission entry."""

    leap_sentencing_date: str = None


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


@dataclass
class NoPleaBondEntryCaseInformation(NotGuiltyBondEntryCaseInformation):
    """General case information data variables and data for no plea bond entry."""


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
