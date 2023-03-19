"""Module containing internal and external paths for the application."""
import os
import pathlib

from munientry.settings.config_settings import load_config

# Internal Path Information #

PATH = str(pathlib.Path().absolute())
TEMPLATE_PATH = os.path.join(PATH, 'resources', 'templates')
ICON_PATH = os.path.join(PATH, 'resources', 'icons')
GAVEL_PATH = os.path.join(ICON_PATH, 'gavel.ico')
GAVEL_SPLASH = os.path.join(ICON_PATH, 'gavel_main_splash.png')
APPROVED_STAMP_PATH = os.path.join(ICON_PATH, 'Approved_Stamp.docx')

# End Internal Path Information #


config_file = load_config()
path_dict = dict(config_file.items('paths'))

# External Path Information #

# Save Path Information
LOG_PATH = path_dict['logs_save_path']
BATCH_SAVE_PATH = path_dict['batch_save_path']
DEFAULT_SAVE_PATH = path_dict['default_entries_save_path']
CRIMTRAFFIC_SAVE_PATH = path_dict['crimtraffic_save_path']
CIVIL_SAVE_PATH = path_dict['civil_save_path']
FISCAL_SAVE_PATH = path_dict['fiscal_save_path']
DRIVE_SAVE_PATH = path_dict['drive_save_path']
SCHEDULING_SAVE_PATH = path_dict['scheduling_save_path']
JURY_PAY_SAVE_PATH = path_dict['jury_pay_save_path']
PROBATION_SAVE_PATH = path_dict['probation_save_path']

# Database Path Information for MuniEntryDB.Sqlite Internal Database
DB_PATH = path_dict['munientry_sqlite_db']
TEST_DELCITY_DB_PATH = path_dict['test_delcity_munientry_sqlite_db']
CASE_LISTS_PATH = path_dict['daily_case_lists']

# Digital Workflow Path Information
DW_PATH = path_dict['digital_workflow_base_path']
DW_ADMIN_JUDGE = path_dict['digital_workflow_admin_judge_path']
DW_ADMIN_JUDGE_ADMIN = path_dict['digital_workflow_admin_judge_admin_entry_path']
DW_ROHRER = path_dict['digital_workflow_rohrer_path']
DW_BUNNER = path_dict['digital_workflow_bunner_path']
DW_PROBATION = path_dict['digital_workflow_probation_path']
DW_APPROVED_DIR = path_dict['digital_workflow_approved_path']
DW_REJECTED_DIR = path_dict['digital_workflow_rejected_path']

# End External Path Information #
