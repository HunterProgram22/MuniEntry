"""A module containing common variables used throughout the application."""
import pathlib
import socket
from datetime import datetime
from loguru import logger


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
VERSION_NUMBER = '0.27.2'

# Court Cost Constants
MOVING_COURT_COSTS = 137
CRIMINAL_COURT_COSTS = 127
NONMOVING_COURT_COSTS = 108


# Logging Settings
# Logger levels are placed in MuniEntry_app.py so tests will run properly.
# logger.level('DIALOG', no=22, color='<green>')
# logger.level('CHOICE', no=26, color='<cyan>')
# logger.level('CHECKFAIL', no=27, color='<magenta>')
# logger.level('REQUIRED', no=28, color='<magenta>')
fmt = '{time:YYYY-MM-DD HH:mm:ss:SSS} | {level: <10} | {message: <50} | {function}:{name}:{line}'
now = datetime.now()
now_string = now.strftime('%Y_%m_%d__%H_%M_%S')
LOG_TIME = f'{now_string}'
SOCKET_NAME = socket.gethostname()
LOG_NAME = f'Log_{SOCKET_NAME}_{LOG_TIME}.log'
logger.add(f'./resources/logs/{LOG_NAME}', format=fmt)


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
    'QRadioButton': 'setChecked',
    'QLineEdit': 'setText',
    'QTextEdit': 'setPlainText',
    'NoScrollDateEdit': 'set_date',
    'NoScrollTimeEdit': 'set_time',
}
