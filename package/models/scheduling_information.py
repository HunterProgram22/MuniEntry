
from dataclasses import dataclass, field, asdict


@dataclass
class SchedulingCaseInformation:
    case_number: str = None
    plea_trial_date: str = None
    trial_date: str = None