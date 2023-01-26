from dataclasses import dataclass, field
from loguru import logger

from munientry.models.party_types import CivilParty, Defendant


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
class CivilCmsCaseInformation:

    case_number: str = None
    primary_plaintiff: object = field(default_factory=CivilParty)
    primary_defendant: object = field(default_factory=CivilParty)


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
