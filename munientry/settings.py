"""A module containing common variables used throughout the application."""
import configparser
import socket
from typing import TYPE_CHECKING
from loguru import logger

from munientry.appsettings.user_settings import UserSettings, GeneralUserSettings, \
    AdminUserSettings, ProbationUserSettings, CommissionerUserSettings, CourtroomUserSettings

config = configparser.ConfigParser()
config.read('config.ini')

# Version Information
version = config['version']
VERSION_NUMBER = version['version_number']


# Court Cost Constants
costs = config['costs']
MOVING_COURT_COSTS = int(costs['moving'])
CRIMINAL_COURT_COSTS = int(costs['criminal'])
NONMOVING_COURT_COSTS = int(costs['non_moving'])


def get_host() -> str:
    """Gets the host name of the PC that launches the application.

    If there is no key and value for the socket in the config file it sets the host to the
    socket name.
    """
    sockets = config['sockets']
    key = socket.gethostname()
    return sockets.get(key, key)


HOST_NAME = get_host()


def load_user_settings(mainwindow) -> 'UserSettings':
    """Returns the user settings based on the computer that is loading the application."""
    user_settings_config = config['user_settings']
    user_settings_key = user_settings_config.get(HOST_NAME, 'GeneralUserSettings')
    user_settings = USER_SETTINGS.get(user_settings_key, GeneralUserSettings)
    return user_settings(mainwindow)


USER_SETTINGS = {
    'AdminUserSettings': AdminUserSettings,
    'CommissionerUserSettings': CommissionerUserSettings,
    'CourtroomUserSettings': CourtroomUserSettings,
    'GeneralUserSettings': GeneralUserSettings,
    'ProbationUserSettings': ProbationUserSettings,
}

# Costs Settings
SPECIAL_DOCKETS_COSTS = [
    'while on Community Control',
    'while on the OVI Docket',
    'while on Mission Court',
    'while on the Mental Health Docket',
]

# Case List Settings
EXCEL_DAILY_CASE_LISTS = [
    ('Arraignments.xlsx', 'arraignments'),
    ('Slated.xlsx', 'slated'),
    ('Final_Pretrials.xlsx', 'final_pretrials'),
    ('Pleas.xlsx', 'pleas'),
    ('Trials_to_Court.xlsx', 'trials_to_court'),
    ('PCVH_FCVH.xlsx', 'pcvh_fcvh'),
]

# Dictionary that provides name of method to access the data in the widget.
# TODO: THIS IS DANGEROUS NEED TO FIX CHANGING METHOD NAME REQUIRES UPDATE HERE
WIDGET_TYPE_ACCESS_DICT = {
    'NoScrollComboBox': 'currentText',
    'ConditionCheckbox': 'isChecked',
    'QCheckBox': 'isChecked',
    'QRadioButton': 'isChecked',
    'QLineEdit': 'text',
    'QTextEdit': 'toPlainText',
    'NoScrollDateEdit': 'get_date_as_string',
    'NoScrollTimeEdit': 'get_time_as_string',
}

# Dictionary that provides the name of the method to set the data in the widget.
# TODO: THIS IS DANGEROUS NEED TO FIX CHANGING METHOD NAME REQUIRES UPDATE HERE
WIDGET_TYPE_SET_DICT = {
    'NoScrollComboBox': 'setCurrentText',
    'QCheckBox': 'setChecked',
    'ConditionCheckbox': 'setChecked',
    'QRadioButton': 'setChecked',
    'QLineEdit': 'setText',
    'QTextEdit': 'setPlainText',
    'NoScrollDateEdit': 'set_date_from_string',
    'NoScrollTimeEdit': 'set_time_from_string',
}


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


