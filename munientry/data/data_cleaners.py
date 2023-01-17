"""Functions used for sanitizing data transferred into the application from an external source.

**munientry.data.data_cleaners**

Functions:
    clean_last_name(last_name) -> str

    clean_offense_name(offense) -> str

    clean_statute_name(statute) -> str
"""
from types import MappingProxyType

from loguru import logger

OFFENSE_CLEAN_DICT = MappingProxyType({
    'UCM': '',
    'M1': '',
    'M2': '',
    'M3': '',
    'M4': '',
    'MM': '',
    'PETTY': '',
    '(UCM)': '',
    'ACDA': 'ACDA',
    'FTY': 'FTY',
    'FTY/ROW': 'FTY / ROW',
    'DUS': 'DUS',
    'OVI': 'OVI',
    'BMV': 'BMV',
    'OBMV': 'BMV',
    'FRA': 'FRA',
    'OL': 'OL',
    'OMVI': 'OVI',
    'FRA/JUDGMENT': 'FRA / Judgment',
    'OR': '/',
    'W/O': 'Without',
    'A': 'a',
    'TO': 'to',
    'SUSP': 'Suspension',
    '-': '',
    'OF': 'of',
    'IN': 'in',
    'AND': 'and',
})


def clean_last_name(last_name: str) -> str:
    """Removes spaces between hyphenated last names.

    This is used when last names are loaded from external databases because certain functions
    used to check for companion cases compare the last name and the daily case lists in the
    application identify cases with the format 'last_name - case_number'. Having spaces surrounding
    a hyphen in a last name would cause the checks to fail, by removing spaces around hyphens in
    last names checks will work properly.

    Args:
        last_name (str): The last name of a person.

    Returns:
        str: The cleaned version of the last name with no spaces between a hyphen.
    """
    return last_name.replace(' - ', '-')


def clean_offense_name(offense: str) -> str:
    """Sanitizes offense names loaded from external databases.

    The data in the AuthorityCourt database is inconsistent in its formatting, this function
    provides consistency to capitalization and formatting.

    Sets offense name to title case, except for abbreviations identified in OFFENSE_CLEAN_DICT
    which need to remain capitalized, and removes degree of charge.

    Args:
        offense: The offense name from the external database.

    Returns:
        str: The cleaned version of the offense name.
    """
    offense_word_list = offense.split()
    clean_offense_word_list = []
    for word in offense_word_list:
        if OFFENSE_CLEAN_DICT.get(word) is not None:
            clean_offense_word_list.append(OFFENSE_CLEAN_DICT.get(word))
            continue
        clean_offense_word_list.append(word.capitalize())
    clean_offense = ' '.join([str(clean_word) for clean_word in clean_offense_word_list])
    return clean_offense.rstrip(' ')


def clean_statute_name(statute: str) -> str:
    """Sanitizes the statute strings loaded from external databases.

    The data in the AuthorityCourt database often uses asteriks to match the same statute
    to multiple different offense names. This function removes the asteriks.

    Args:
        statute: The statute name from the external database.

    Returns:
        str: The cleaned version of the statute name without asteriks.
    """
    return statute.rstrip('*')


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
