"""Module containing internal and external paths for the application."""
import configparser
import pathlib

config = configparser.ConfigParser()
config.read('config.ini')
paths = config['paths']


# Save Path Information

LOG_PATH = paths['logs_save_path']
BATCH_SAVE_PATH = paths['batch_save_path']
DEFAULT_SAVE_PATH = paths['default_entries_save_path']
CRIMTRAFFIC_SAVE_PATH = paths['crimtraffic_save_path']
FISCAL_SAVE_PATH = paths['fiscal_save_path']
DRIVE_SAVE_PATH = paths['drive_save_path']
SCHEDULING_SAVE_PATH = paths['scheduling_save_path']
JURY_PAY_SAVE_PATH = paths['jury_pay_save_path']


# Database Path Information for MuniEntryDB.Sqlite Internal Database
DB_PATH = paths['munientry_sqlite_db']
# CASE_LISTS_PATH = paths['daily_case_lists']


# Digital Workflow Path Information
DW_PATH = paths['digital_workflow_base_path']
DW_HEMMETER = paths['digital_workflow_hemmeter_path']
DW_ROHRER = paths['digital_workflow_rohrer_path']
DW_BUNNER = paths['digital_workflow_bunner_path']
DW_MATTOX = paths['digital_workflow_mattox_path']
DW_APPROVED_DIR = paths['digital_workflow_approved_path']
DW_REJECTED_DIR = paths['digital_workflow_rejected_path']


# Resources Path Information
# Path strings require double backslash even with raw f-strings (fr)
# otherwise the string is not properly terminated.
PATH = str(pathlib.Path().absolute())
CASE_LISTS_PATH = fr'{PATH}\db\\'
TEMPLATE_PATH = fr'{PATH}\resources\templates\\'
ICON_PATH = fr'{PATH}\resources\icons\\'
GAVEL_PATH = fr'{ICON_PATH}\gavel.ico'
