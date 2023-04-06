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

DEFENSE_COUNSEL_CLEAN_DICT = ({
    'III': 'III',
})


def clean_last_name(last_name: str) -> str:
    """Removes spaces between hyphenated last names."""
    return last_name.replace(' - ', '-')


def clean_offense_name(offense: str) -> str:
    """Sanitizes offense names loaded from external databases."""
    words = offense.split()
    clean_words = [OFFENSE_CLEAN_DICT.get(word, word.capitalize()) for word in words]
    clean_offense = ' '.join(clean_words)
    return clean_offense.rstrip(' ')


def clean_defense_counsel_name(def_counsel_name: str) -> str:
    """Sanitizes defense counsel names loaded from external databases."""
    words = def_counsel_name.split()
    clean_words = [DEFENSE_COUNSEL_CLEAN_DICT.get(word, word.capitalize()) for word in words]
    clean_name = ' '.join(clean_words)
    return clean_name.rstrip(' ')


def clean_statute_name(statute: str) -> str:
    """Sanitizes the statute strings loaded from external databases."""
    return statute.rstrip('*')
