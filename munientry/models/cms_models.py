"""Base models for storing data from a case management system database."""
from dataclasses import dataclass, field
from typing import Optional

from munientry.models import party_types


@dataclass
class CriminalCmsCaseInformation(object):
    """Stores criminal/traffic data loaded from the Case Management System/Criminal Database."""

    case_number: Optional[str] = None
    defendant: object = field(default_factory=party_types.Defendant)
    defense_counsel: Optional[str] = None
    defense_counsel_type: Optional[str] = None
    charges_list: list = field(default_factory=list)
    fra_in_file: Optional[str] = None


@dataclass
class CivilCmsCaseInformation(object):
    """Stores civil data loaded from the Case Management System/Civil Database."""

    case_number: Optional[str] = None
    case_type: Optional[str] = None
    primary_plaintiff: object = field(default_factory=party_types.CivilParty)
    primary_defendant: object = field(default_factory=party_types.CivilParty)
