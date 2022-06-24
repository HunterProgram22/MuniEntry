"""Module containing all the data structures for parties in cases."""
from loguru import logger


class Person:
    """A base class for all people of any party type."""

    def __init__(self) -> None:
        self.first_name = None
        self.last_name = None


class Defendant(Person):
    """Class for defendants that inherits from Person class."""


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


if __name__ == "__main__":
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
