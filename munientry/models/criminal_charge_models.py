from dataclasses import dataclass
from loguru import logger


@dataclass
class CriminalCharge:
    """Class for keeping track of all information that is specific to each
    individual charge in a cms_case."""

    offense: str = None
    statute: str = None
    degree: str = None
    violation_date: str = None
    plea: str = None
    type: str = None
    finding: str = None
    fines_amount: str = None
    fines_suspended: str = None
    jail_days: str = None
    jail_days_suspended: str = None


@dataclass
class AmendOffenseDetails:
    """Class for tracking data when an offense/charge is amended."""

    original_charge: str = None
    amended_charge: str = None
    motion_disposition: str = "granted"
