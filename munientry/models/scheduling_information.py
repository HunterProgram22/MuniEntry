from dataclasses import dataclass, field, asdict
from loguru import logger

from munientry.models.party_types import Defendant

@dataclass
class SchedulingCaseInformation:
    case_number: str = None
    judicial_officer: object = None
    assigned_judge: str = None
    courtroom: str = None
    plea_trial_date: str = None
    defendant: object = field(default_factory=Defendant)
    defense_counsel: str = None
    defense_counsel_type: str = None
    jury_trial_date: str = None
    jury_trial_time: str = '8:15 AM'
    trial_to_court_date: str = None
    trial_to_court_time: str = None
    pretrial_date: str = None
    pretrial_time: str = '3:00 PM'
    final_pretrial_date: str = None
    final_pretrial_time: str = None
    pretrial_scheduled: bool = True
    jury_trial_only: str = None
    hearing_date: str = None
    hearing_time: str = None
    hearing_type: str = None
    hearing_location: str = None

    def get_case_information(self):
        """Returns a dictionary with all of cms_case information required
        to populate an entry."""
        return asdict(self)


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
