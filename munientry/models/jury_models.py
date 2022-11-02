from dataclasses import dataclass, field, asdict


@dataclass
class JuryPaymentInformation:
    """Stores information for Jury Payment entry."""

    case_number: str = None
    judicial_officer: object = None
    plea_trial_date: str = None

    def get_case_information(self) -> dict:
        """Returns a dictionary with all of information required to populate an entry."""
        return asdict(self)
