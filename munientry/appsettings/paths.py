"""Module containing internal and external paths for the application."""
import configparser
import pathlib
import os

# Internal Path Information #

PATH = str(pathlib.Path().absolute())
TEMPLATE_PATH = os.path.join(PATH, 'resources', 'templates')
ICON_PATH = os.path.join(PATH, 'resources', 'icons')
GAVEL_PATH = os.path.join(ICON_PATH, 'gavel.ico')
GAVEL_SPLASH = os.path.join(ICON_PATH, 'gavel_main_splash.png')
APPROVED_STAMP_PATH = os.path.join(ICON_PATH, 'Approved_Stamp.docx')

# End Internal Path Information #


def load_config() -> configparser.ConfigParser:
    """Loads the app config file."""
    path = str(pathlib.Path().absolute())
    config = configparser.ConfigParser()
    config.read(f'{path}/config.ini')
    return config


config_file = load_config()
paths = dict(config_file.items('paths'))

# External Path Information #

# Save Path Information
LOG_PATH = paths['logs_save_path']
BATCH_SAVE_PATH = paths['batch_save_path']
DEFAULT_SAVE_PATH = paths['default_entries_save_path']
CRIMTRAFFIC_SAVE_PATH = paths['crimtraffic_save_path']
CIVIL_SAVE_PATH = paths['civil_save_path']
FISCAL_SAVE_PATH = paths['fiscal_save_path']
DRIVE_SAVE_PATH = paths['drive_save_path']
SCHEDULING_SAVE_PATH = paths['scheduling_save_path']
JURY_PAY_SAVE_PATH = paths['jury_pay_save_path']
PROBATION_SAVE_PATH = paths['probation_save_path']


# Database Path Information for MuniEntryDB.Sqlite Internal Database
DB_PATH = paths['munientry_sqlite_db']
TEST_DELCITY_DB_PATH = paths['test_delcity_munientry_sqlite_db']
CASE_LISTS_PATH = paths['daily_case_lists']


# Digital Workflow Path Information
DW_PATH = paths['digital_workflow_base_path']
DW_ADMIN_JUDGE = paths['digital_workflow_admin_judge_path']
DW_ADMIN_JUDGE_ADMIN = paths['digital_workflow_admin_judge_admin_entry_path']
DW_ROHRER = paths['digital_workflow_rohrer_path']
DW_BUNNER = paths['digital_workflow_bunner_path']
DW_PROBATION = paths['digital_workflow_probation_path']
DW_APPROVED_DIR = paths['digital_workflow_approved_path']
DW_REJECTED_DIR = paths['digital_workflow_rejected_path']
