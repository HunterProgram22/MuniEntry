"""Module containing all the data structures for parties in cases."""
from dataclasses import dataclass, field
from loguru import logger


class Person:
    """A base class for all people of any party type."""

    def __init__(self) -> None:
        self.first_name = None
        self.last_name = None


class Defendant(Person):
    """Class for defendants that inherits from Person class."""


class CivilParty(object):
    """A base class for civil parties."""

    def __init__(self) -> None:
        self.individual: bool = None
        self.party_name: str = None
        self.party_type: str = None


class JudicialOfficer(Person):
    """
    A subclass of a person that is for all different types of judicial
    officers: Judges, Visiting Judges, Acting Judges, Magistrates.

    In the future may want to add attorney registration number to this class.
    """

    def __init__(self, first_name: str, last_name: str, officer_type: str) -> None:
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.officer_type = officer_type


@dataclass
class DefendantDriver:
    """Class for storing data for a defendant that has necessary data for driving privileges."""

    first_name: str = None
    last_name: str = None
    birth_date: str = None
    license_number: str = None
    address: str = None
    city: str = None
    state: str = None
    zipcode: str = None


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
