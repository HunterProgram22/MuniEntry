"""A module containing common variables used throughout the application."""
import configparser
import socket
import pathlib
from typing import TYPE_CHECKING


PATH = str(pathlib.Path().absolute())
config = configparser.ConfigParser()
config.read(f'{PATH}\config.ini')

# Version Information
version = config['version']
VERSION_NUMBER = version['version_number']


def get_host() -> str:
    """Gets the host name of the PC that launches the application.

    If there is no key and value for the socket in the config file it sets the host to the
    socket name.
    """
    sockets = config['sockets']
    key = socket.gethostname()
    return sockets.get(key, key)


HOST_NAME = get_host()


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
