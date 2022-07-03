"""A module containing common variables used throughout the application."""
import pathlib
import socket
from datetime import datetime


# Path Information
# Path strings require double backslash even with raw f-strings (fr) otherwise the string is
# not properly terminated.
PATH = str(pathlib.Path().absolute())
TEMPLATE_PATH = fr'{PATH}\resources\templates\\'
SAVE_PATH = fr'{PATH}\resources\saved\\'
LOG_PATH = fr'{PATH}\resources\logs\\'
DB_PATH = fr'{PATH}\db\\'
ICON_PATH = fr'{PATH}\icons\\'
CHARGES_DATABASE = fr'{DB_PATH}\Charges.sqlite'
CHARGES_TABLE = fr'{DB_PATH}\Charges.xlsx'

# Version Information
VERSION_NUMBER = '0.28.0'

# Court Cost Constants
MOVING_COURT_COSTS = 137
CRIMINAL_COURT_COSTS = 127
NONMOVING_COURT_COSTS = 108

# Logging Settings
now = datetime.now()
now_string = now.strftime('%Y_%m_%d__%H_%M_%S')
LOG_TIME = f'{now_string}'
SOCKET_NAME = socket.gethostname()
FULL_LOG_NAME = f'Full_Log_{SOCKET_NAME}_{LOG_TIME}.log'
USER_LOG_NAME = f'User_Log_{SOCKET_NAME}_{LOG_TIME}.log'


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
