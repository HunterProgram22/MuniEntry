"""Constants specific do the Delaware Municipal Court."""
from types import MappingProxyType

from munientry.settings.config_settings import load_config

DAY_DICT = MappingProxyType({
    'Monday': 1,
    'Tuesday': 2,
    'Wednesday': 3,
    'Thursday': 4,
    'Friday': 5,
})

EVENT_DICT = MappingProxyType({
    'Trial': 2,
    'Final Pretrial': 2,
    'Pretrial': 28,
})

PRETRIAL_TIME_DICT = MappingProxyType({
    'Pretrial 4 weeks before trial': 28,
    'Pretrial 3 weeks before trial': 21,
    'Pretrial 2 weeks before trial': 14,
    'No Pretrial': 0,
})

SPECIAL_DOCKETS_COSTS = (
    'while on Community Control',
    'while on the OVI Docket',
    'while on Mission Court',
    'while on the Mental Health Docket',
)

SPEEDY_TRIAL_TIME_DICT = MappingProxyType({
    'M1': 90,
    'M2': 90,
    'M3': 45,
    'M4': 45,
    'MM': 30,
    'UCM': 45,
    'UCM - 3rd OVI': 90,
})

config = load_config()
costs_dict = dict(config.items('costs'))
MOVING_COURT_COSTS = int(costs_dict['moving'])
CRIMINAL_COURT_COSTS = int(costs_dict['criminal'])
NONMOVING_COURT_COSTS = int(costs_dict['non_moving'])
