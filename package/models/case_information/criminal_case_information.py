"""Module that contains dataclasses for data common to all criminal cases."""
from dataclasses import asdict, dataclass, field

from package.models.party_types import Defendant


@dataclass
class CriminalCaseInformation(object):
    """Base Criminal Case Information data class."""

    case_number: str = None
    judicial_officer: object = None
    plea_trial_date: str = None
    appearance_reason: str = None
    plaintiff: str = 'State of Ohio'
    defendant: object = field(default_factory=Defendant)

    defense_counsel: str = None
    defense_counsel_type: str = None
    defense_counsel_waived: bool = False

    offense_of_violence: bool = False

    charges_list: list = field(default_factory=list)
    amended_charges_list: list = field(default_factory=list)
    amend_offense_details: object = None

    def add_charge_to_list(self, charge) -> None:
        self.charges_list.append(charge)

    def get_case_information(self) -> dict:
        """Returns a dictionary with all case information.

        Keys of the dict are variable names and are used in templates to populate the values
        into fields using Jinja tags.

        Example: {{ plaintiff }} populates State of Ohio in a template.
        """
        return asdict(self)
