from dataclasses import dataclass, field, asdict

from package.models.party_types import Defendant

@dataclass
class SchedulingCaseInformation:
    case_number: str = None
    plea_trial_date: str = None
    defendant: object = field(default_factory=Defendant)
    defense_counsel: str = None
    defense_counsel_type: str = None
    trial_date: str = None
    final_pretrial_date: str = None
    final_pretrial_time: str = None


    def get_case_information(self):
        """Returns a dictionary with all of cms_case information required
        to populate an entry."""
        return asdict(self)
