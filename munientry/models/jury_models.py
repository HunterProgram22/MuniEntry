from dataclasses import dataclass, field, asdict

from munientry.models.party_types import Defendant

@dataclass
class JuryPaymentInformation:
    """Stores information for Jury Payment entry."""

    case_number: str = None
    judicial_officer: object = None
    defendant: object = field(default_factory=Defendant)
    entry_date: str = None
    trial_date: str = None
    jurors_reported: str = None
    jurors_reported_word: str = None
    jurors_seated: str = None
    jurors_seated_word: str = None
    jurors_not_seated: str = None
    jurors_not_seated_word: str = None
    jurors_pay_not_seated: str = None
    jurors_pay_not_seated_word: str = None
    jurors_pay_seated: str = None
    jurors_pay_seated_word: str = None
    jury_panel_total_pay: str = None
    jury_panel_total_pay_word: str = None

    def get_case_information(self) -> dict:
        """Returns a dictionary with all of information required to populate an entry."""
        return asdict(self)
