from dataclasses import dataclass, field, asdict

from munientry.models.party_types import Defendant


@dataclass
class EventInfo:
    date: str = None
    time: str = None
    type: str = None
    location: str = None


@dataclass
class SchedulingCaseInformation:
    case_number: str = None
    judicial_officer: object = None
    assigned_judge: str = None
    courtroom: str = None
    entry_date: str = None
    defendant: object = field(default_factory=Defendant)
    defense_counsel: str = None
    defense_counsel_type: str = None
    pretrial_scheduled: bool = True
    jury_trial_only: str = None
    interpreter_required: bool = False
    interpreter_language: str = None

    jury_trial: EventInfo = field(default_factory=lambda: EventInfo(time='8:15 AM'))
    trial_to_court: EventInfo = field(default_factory=EventInfo)
    pretrial: EventInfo = field(default_factory=lambda: EventInfo(time='3:00 PM'))
    final_pretrial: EventInfo = field(default_factory=EventInfo)
    hearing: EventInfo = field(default_factory=EventInfo)

    def get_case_information(self):
        """Returns a dictionary with all of cms_case information required
        to populate an entry."""
        return asdict(self)
