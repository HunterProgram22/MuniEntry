"""A module containing common variables used throughout the application."""
import configparser
import socket

from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import QDate, QDateTime
from PyQt6.QtGui import QIntValidator

from typing import TYPE_CHECKING


MAX_JAIL_TIME_VALIDATOR = QIntValidator(0, 1000)
TODAY = QDate.currentDate()
TIMENOW = QDateTime.currentDateTime()
YES_BUTTON_RESPONSE = QMessageBox.StandardButton.Yes
NO_BUTTON_RESPONSE = QMessageBox.StandardButton.No
CANCEL_BUTTON_RESPONSE = QMessageBox.StandardButton.Cancel

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


SOCKET_NAME = get_host()


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
