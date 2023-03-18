"""A module containing common variables used throughout the application."""
from __future__ import annotations

import configparser
import socket
import pathlib
from typing import TYPE_CHECKING, Any

from loguru import logger

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


# Daily Case List Settings
DAILY_CASE_LIST_STORED_PROCS = {
    'arraignments_cases_box': '[reports].[DMCMuniEntryArraignment]',
    'slated_cases_box': '[reports].[DMCMuniEntrySlated]',
    'pleas_cases_box': '[reports].[DMCMuniEntryPleas]',
    'pcvh_fcvh_cases_box': '[reports].[DMCMuniEntryPrelimCommContViolHearings]',
    'final_pretrial_cases_box': '[reports].[DMCMuniEntryFinalPreTrials]',
    'trials_to_court_cases_box': '[reports].[DMCMuniEntryBenchTrials]',
}

# Dictionary that provides name of method to access the data in the widget.
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

def get_view_field_data(view: Any, widget_type: str) -> Any:
    return getattr(view, WIDGET_TYPE_ACCESS_DICT.get(widget_type, 'None'))()


# Dictionary that provides the name of the method to set the data in the widget.
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

def set_view_field_data(view: Any, widget_type: str, model_data: Any) -> None:
    getattr(view, WIDGET_TYPE_SET_DICT.get(widget_type))(model_data)


def log_transfer(model_class: type[Any], model_attribute: str, view_field_data: Any) -> None:
    class_name = model_class.__class__.__name__
    logger.info(f'{class_name} {model_attribute} set to: {view_field_data}.')
