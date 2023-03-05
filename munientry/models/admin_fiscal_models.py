from dataclasses import dataclass, field, asdict


@dataclass
class AdminFiscalEntryInformation:
    """Stores information for Admin Fiscal Entry."""

    account_number: str = None
    account_name: str = None
    subaccount_number: str = None
    subaccount_name: str = None
    disbursement_reason: str = None
    disbursement_amount: str = None
    disbursement_vendor: str = None
    invoice_number: str = None
    judicial_officer: object = None
    admin_judge_signature: str = '{{ admin_judge_signature }}'
    time_stamp: str = '{{ time_stamp }}'

    def get_case_information(self) -> dict:
        """Returns a dictionary with all of information required to populate an entry."""
        return asdict(self)

