from dataclasses import dataclass, field
from loguru import logger

from munientry.models.party_types import Defendant, DefendantDriver


@dataclass
class CmsCaseInformation:
    """Stores the data that is loaded from the Case Management System so that it can be loaded
    into the Dialog view."""

    case_number: str = None
    defendant: object = field(default_factory=Defendant)
    defense_counsel: str = None
    defense_counsel_type: str = None
    charges_list: list = field(default_factory=list)
    fra_in_file: str = None


@dataclass
class DrivingPrivilegesInformation:
    """Stores the data that is loaded from the Case Management System so that it can be loaded
    into the Dialog view."""

    case_number: str = None
    defendant: object = field(default_factory=DefendantDriver)


if __name__ == "__main__":
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
