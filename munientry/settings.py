"""A module containing common variables used throughout the application."""
import pathlib
import socket
from datetime import datetime
from typing import TYPE_CHECKING # Import used so TYPE_CHECKING can be imported with other settings
from PyQt5.QtCore import QDate

# Path Information
# Path strings require double backslash even with raw f-strings (fr) otherwise the string is
# not properly terminated.
PATH = str(pathlib.Path().absolute())
TEMPLATE_PATH = fr'{PATH}\resources\templates\\'
SAVE_PATH = fr'{PATH}\resources\saved\\'
LOG_PATH = fr'{PATH}\resources\logs\\'
ICON_PATH = fr'{PATH}\resources\icons\\'

DB_PATH = fr'{PATH}\db\\'
CHARGES_DATABASE = fr'{DB_PATH}\Charges.sqlite'
CHARGES_TABLE = fr'{DB_PATH}\Charges.xlsx'

# Version Information
VERSION_NUMBER = '0.33.0'

# Court Cost Constants
MOVING_COURT_COSTS = 137
CRIMINAL_COURT_COSTS = 127
NONMOVING_COURT_COSTS = 108

# Logging Settings
now = datetime.now()
now_string = now.strftime('%m_%d_%Y__%H_%M_%S')
LOG_TIME = f'{now_string}'

def get_host():
    socket_dict = {
        'RooberryPrime': 'Justin_Home_PC',
        'MUNI14': 'Justin_Work_Desktop_PC',
        'Muni03': 'Kathryn_Patterson_PC',
        'Muni05': 'Pat_Dattilo_PC',
        'Muni20': 'Courtroom_A_PC',
        'Muni21': 'Courtroom_B_PC',
        'Muni22': 'Courtroom_C_PC',
        'Clerk07': 'Nick_Lockhart_PC',
        'Clerk08': 'Ryan_Levering_PC',
        'Muni10': 'Justin_Work_Laptop_PC',
    }
    key = socket.gethostname()
    host = socket_dict.get(key, key)
    return host

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
