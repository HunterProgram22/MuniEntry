"""Module that contains dataclasses for data common to all civil cases."""
from loguru import logger
from dataclasses import asdict, dataclass, field

from munientry.models.party_types import CivilParty


@dataclass
class CivilCaseInformation(object):
    """Base Civil Case Information data class."""

    case_number: str = None
    judicial_officer: object = None
    entry_date: str = None
    appearance_reason: str = None
    plaintiff: object = field(default_factory=CivilParty)
    defendant: object = field(default_factory=CivilParty)

    def get_case_information(self) -> dict:
        """Returns a dictionary with all case information.

        Keys of the dict are variable names and are used in templates to populate the values
        into fields using Jinja tags.
        """
        return asdict(self)


@dataclass
class CivFreeformEntryCaseInformation(CivilCaseInformation):
    """General case information data variables for civil freeform entry."""

    entry_content_text: str = None
