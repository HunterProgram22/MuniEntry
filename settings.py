"""A module containing common variables used throughout the application."""
import pathlib

PATH = str(pathlib.Path().absolute())

TEMPLATE_PATH = PATH + "\\resources\\templates\\"
SAVE_PATH = PATH + "\\resources\\saved\\"
DB_PATH = PATH + "\\db\\"
ICON_PATH = PATH + "\\icons\\"
CHARGES_DATABASE = DB_PATH + "charges.sqlite"
CHARGES_TABLE = DB_PATH + "Charges.xlsx"

VERSION_NUMBER = '0.23.1'

MOVING_COURT_COSTS = 137
CRIMINAL_COURT_COSTS = 127
NONMOVING_COURT_COSTS = 108

EXCEL_DAILY_CASE_LISTS = [
    ("Arraignments.xlsx", "arraignments"),
    ("Slated.xlsx", "slated"),
    ("Final_Pretrials.xlsx", "final_pretrials"),
    ("Pleas.xlsx", "pleas"),
    ("Trials_to_Court.xlsx", "trials_to_court"),
    ("PCVH_FCVH.xlsx", "pcvh_fcvh"),
]

WIDGET_TYPE_ACCESS_DICT = {
    "NoScrollComboBox": "currentText",
    "QCheckBox": "isChecked",
    "QRadioButton": "isChecked",
    "QLineEdit": "text",
    "QTextEdit": "toPlainText",
    "NoScrollDateEdit": "get_date",
    "NoScrollTimeEdit": "get_time",
}

WIDGET_TYPE_SET_DICT = {
    "NoScrollComboBox": "setCurrentText",
    "QCheckBox": "setChecked",
    "QRadioButton": "setChecked",
    "QLineEdit": "setText",
    "QTextEdit": "setPlainText",
    "NoScrollDateEdit": "set_date",
    "NoScrollTimeEdit": "set_time",
}