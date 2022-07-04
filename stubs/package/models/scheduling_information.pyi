from munientry.models.party_types import Defendant as Defendant

class SchedulingCaseInformation:
    case_number: str
    plea_trial_date: str
    defendant: object
    defense_counsel: str
    defense_counsel_type: str
    trial_date: str
    pretrial_date: str
    final_pretrial_date: str
    final_pretrial_time: str
    pretrial_scheduled: bool
    def get_case_information(self): ...
    def __init__(self, case_number, plea_trial_date, defendant, defense_counsel, defense_counsel_type, trial_date, pretrial_date, final_pretrial_date, final_pretrial_time, pretrial_scheduled) -> None: ...
