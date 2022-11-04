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

    def get_case_information(self) -> dict:
        """Returns a dictionary with all of information required to populate an entry."""
        return asdict(self)
