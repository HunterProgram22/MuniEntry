from munientry.appsettings.settings import config

DAY_DICT = {
    'Monday': 1,
    'Tuesday': 2,
    'Wednesday': 3,
    'Thursday': 4,
    'Friday': 5,
}
EVENT_DICT = {
    'Trial': 2,
    'Final Pretrial': 2,
    'Pretrial': 28,
}
SPEEDY_TRIAL_TIME_DICT = {
    'M1': 90,
    'M2': 90,
    'M3': 45,
    'M4': 45,
    'MM': 30,
    'UCM': 30,
}
PRETRIAL_TIME_DICT = {
    'Pretrial 4 weeks before trial': 28,
    'Pretrial 3 weeks before trial': 21,
    'Pretrial 2 weeks before trial': 14,
    'No Pretrial': 0,
}
costs = config['costs']
MOVING_COURT_COSTS = int(costs['moving'])
CRIMINAL_COURT_COSTS = int(costs['criminal'])
NONMOVING_COURT_COSTS = int(costs['non_moving'])
SPECIAL_DOCKETS_COSTS = [
    'while on Community Control',
    'while on the OVI Docket',
    'while on Mission Court',
    'while on the Mental Health Docket',
]
