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
    bmv_suspension: bool = False
    bmv_cases: str = None
    bmv_payment_plan: bool = False
    related_traffic_case: bool = False
    related_traffic_case_number: str = None
    suspension_start_date: str = None
    suspension_end_date: str = None
    additional_information_ordered: bool = False
    additional_information_text: str = None
    ignition_interlock: bool = False
    restricted_tags: bool = False
    employer_school_list: list = field(default_factory=list)

    def add_employer_school_to_list(self, employer):
        self.employer_school_list.append(employer)

    def get_case_information(self) -> dict:
        """Returns a dictionary with all of information required to populate an entry."""
        return asdict(self)


@dataclass
class DenyPrivilegesInformation(DrivingPrivilegesInformation):
    """Stores information used for denying driving privileges or other entries not granting driving
    privileges.
    """

    deny_privileges: bool = False
    permit_test_or_renew: bool = False
    permit_renew_expired: bool = False
    hard_time: bool = False
    no_insurance: bool = False
    petition_incomplete: bool = False
    no_jurisdiction: bool = False
    no_employer_info: bool = False
    prohibited_activities: bool = False
    out_of_state_license: bool = False
    permanent_id: bool = False
    license_expiration_date: str = None
    no_pay_plan: bool = False


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
