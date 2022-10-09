from dataclasses import dataclass, field, asdict


@dataclass
class AdminFiscalEntryInformation:
    """Stores information for Admin Fiscal Entry."""

    account_number: str = None
    account_name: str = None
    subaccount_number: str = None
    subaccount_name: str = None
    disbursement_reason: str = None
    judicial_officer: object = None
    plea_trial_date: str = None

    def get_case_information(self) -> dict:
        """Returns a dictionary with all of information required to populate an entry."""
        return asdict(self)

