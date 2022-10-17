"""A module containing common variables used throughout the application."""
import configparser
import pathlib
import socket
from datetime import datetime
from typing import (
    TYPE_CHECKING,  # Import used so TYPE_CHECKING can be imported with other settings
)

from PyQt6.QtCore import QDate

config = configparser.SafeConfigParser()
config.read('config.ini')

# Version Information
version = config['version']
VERSION_NUMBER = version['version_number']


# Court Cost Constants
costs = config['costs']
MOVING_COURT_COSTS = int(costs['moving'])
CRIMINAL_COURT_COSTS = int(costs['criminal'])
NONMOVING_COURT_COSTS = int(costs['non_moving'])


# Save Path Information
paths = config['paths']

LOG_PATH = paths['logs_save_path']
BATCH_SAVE_PATH = paths['batch_save_path']
DEFAULT_SAVE_PATH = paths['default_entries_save_path']
CRIMTRAFFIC_SAVE_PATH = paths['crimtraffic_save_path']
FISCAL_SAVE_PATH = paths['fiscal_save_path']
DRIVE_SAVE_PATH = paths['drive_save_path']
SCHEDULING_SAVE_PATH = paths['scheduling_save_path']


# Digital Workflow Path Information
DW_PATH = paths['digital_workflow_base_path']
DW_HEMMETER = paths['digital_workflow_hemmeter_path']
DW_ROHRER = paths['digital_workflow_rohrer_path']
DW_APPROVED_DIR = paths['digital_workflow_approved_path']


# Resources Path Information
# Path strings require double backslash even with raw f-strings (fr)
# otherwise the string is not properly terminated.
PATH = str(pathlib.Path().absolute())
TEMPLATE_PATH = fr'{PATH}\resources\templates\\'
ICON_PATH = fr'{PATH}\resources\icons\\'
DB_PATH = fr'{PATH}\db\\'
CHARGES_DATABASE = fr'{DB_PATH}\Charges.sqlite'
CHARGES_TABLE = fr'{DB_PATH}\Charges.xlsx'
GAVEL_PATH = fr'{ICON_PATH}\gavel.ico'


# Logging Settings
now = datetime.now()
now_string = now.strftime('%m_%d_%Y__%H_%M_%S')
LOG_TIME = f'{now_string}'


def get_host() -> str:
    """Gets the host name of the PC that launches the application."""
    sockets = config['sockets']
    key = socket.gethostname()
    return sockets.get(key, key)


SOCKET_NAME = get_host()
FULL_LOG_NAME = f'Full_Log_{SOCKET_NAME}_{LOG_TIME}.log'
USER_LOG_NAME = f'{SOCKET_NAME}_User_Log_{LOG_TIME}.log'


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
WIDGET_TYPE_ACCESS_DICT = {
    'NoScrollComboBox': 'currentText',
    'ConditionCheckbox': 'isChecked',
    'QCheckBox': 'isChecked',
    'QRadioButton': 'isChecked',
    'QLineEdit': 'text',
    'QTextEdit': 'toPlainText',
    'NoScrollDateEdit': 'get_date',
    'NoScrollTimeEdit': 'get_time',
}

# Dictionary that provides the name of the method to set the data in the widget.
WIDGET_TYPE_SET_DICT = {
    'NoScrollComboBox': 'setCurrentText',
    'QCheckBox': 'setChecked',
    'ConditionCheckbox': 'setChecked',
    'QRadioButton': 'setChecked',
    'QLineEdit': 'setText',
    'QTextEdit': 'setPlainText',
    'NoScrollDateEdit': 'set_date',
    'NoScrollTimeEdit': 'set_time',
}

TODAY = QDate.currentDate()

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


def set_server_and_database() -> tuple:
    """Sets the server and database name for the SQL Server connection.

    This function is used to set a local instance of the database for Justin to test at home
    without being connected to the delcity network.
    """
    if socket.gethostname() == 'RooberryPrime':
        server = r'ROOBERRYPRIME\SQLEXPRESS'
        database = 'AuthorityCourt'
    else:
        server = r'CLERKCRTR\CMI'
        database = 'AuthorityCourt'
    return (server, database)
