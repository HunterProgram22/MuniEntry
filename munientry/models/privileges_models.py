from dataclasses import dataclass, field, asdict

from munientry.models.party_types import DefendantDriver


@dataclass
class DrivingPrivilegesInformation:
    """Stores information for driving privileges entry."""

    case_number: str = None
    judicial_officer: object = None
    plea_trial_date: str = None
    defendant: object = field(default_factory=DefendantDriver)
    suspension_type: str = None
    suspension_start_date: str = None
    suspension_end_date: str = None
    ignition_interlock: bool = False
    restricted_tags: bool = False
    employer_school_list: list = field(default_factory=list)

    def add_employer_school_to_list(self, employer):
        self.employer_school_list.append(employer)

    def get_case_information(self) -> dict:
        """Returns a dictionary with all of information required to populate an entry."""
        return asdict(self)


@dataclass
class EmployerSchoolInformation:
    """Stores employer or school information used for driving privileges."""

    name: str = None
    address: str = None
    city: str = None
    state: str = None
    zipcode: str = None
    privileges_type: str = None
    driving_days: str = None
    driving_hours: str = None
    other_conditions: str = None
