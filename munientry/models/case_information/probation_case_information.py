from loguru import logger
from dataclasses import asdict, dataclass, field

from munientry.models.party_types import Defendant


@dataclass
class ProbationCaseInformation(object):
    """Base Probation Case Information data class."""

    case_number: str = None
    judicial_officer: object = None
    entry_date: str = None
    plaintiff: str = 'State of Ohio'
    defendant: object = field(default_factory=Defendant)

    def get_case_information(self) -> dict:
        """Returns a dictionary with all case information.

        Keys of the dict are variable names and are used in templates to populate the values
        into fields using Jinja tags.

        Example: {{ plaintiff }} populates State of Ohio in a template.
        """
        return asdict(self)


@dataclass
class TermsCommControlEntryCaseInformation(ProbationCaseInformation):
    """General case information data variables and data for community control violation entry."""

    term_of_control: str = None
    report_frequency: str = None
    jail_ordered: bool = False
    jail_days: str = None
    jail_report_time: str = None
    jail_report_date: str = None
    no_contact_with_ordered: bool = False
    no_contact_with_person: str = None
    gps_exclusion_ordered: bool = False
    no_alcohol_ordered: bool = False
    scram_ordered: bool = False
    scram_days: str = None
    interlock_vehicles_ordered: bool = False
    specialized_docket_ordered: bool = False
    specialized_docket_type: str = None
    pay_restitution: bool = False
    antitheft_program: bool = False
    anger_management_program: bool = False
    alcohol_treatment_ordered: bool = False
    domestic_violence_program: bool = False
    driver_intervention_program: bool = False
    mental_health_evaluation: bool = False
    community_service_ordered: bool = False
    community_service_hours: str = None
    terms_list = [
        ('term_of_control', 'term_of_control_box'),
        ('report_frequency', 'report_frequency_box'),
        ('jail_ordered', 'report_to_jail_check_box'),
        ('jail_days', 'jail_days_box'),
        ('jail_report_time', 'jail_report_time_box'),
        ('jail_report_date', 'jail_report_date_box'),
        ('no_contact_with_ordered', 'no_contact_check_box'),
        ('no_contact_with_person', 'no_contact_with_box'),
        ('gps_exclusion_ordered', 'gps_exclusion_check_box'),
        ('no_alcohol_ordered', 'no_alcohol_ordered_check_box'),
        ('scram_ordered', 'scram_ordered_check_box'),
        ('scram_days', 'scram_days_box'),
        ('interlock_vehicles_ordered', 'interlock_vehicles_check_box'),
        ('specialized_docket_ordered', 'specialized_docket_check_box'),
        ('specialized_docket_type', 'specialized_docket_box'),
        ('pay_restitution', 'pay_restitution_check_box'),
        ('antitheft_program', 'antitheft_check_box'),
        ('anger_management_program', 'anger_management_check_box'),
        ('alcohol_treatment_ordered', 'alcohol_treatment_check_box'),
        ('domestic_violence_program', 'domestic_violence_program_check_box'),
        ('driver_intervention_program', 'driver_intervention_program_check_box'),
        ('mental_health_treatment', 'mental_health_treatment_check_box'),
        ('community_service_ordered', 'community_service_check_box'),
        ('community_service_hours', 'community_service_hours_box'),
    ]
