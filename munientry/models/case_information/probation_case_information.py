from loguru import logger
from dataclasses import dataclass, field

from munientry.models.case_information.criminal_case_information import CriminalCaseInformation


@dataclass
class TermsCommControlEntryCaseInformation(CriminalCaseInformation):
    """General case information data variables and data for community control violation entry."""

    length_of_probation: str = None
