"""A module containing common variables used throughout the application."""

import pathlib

PATH = str(pathlib.Path().absolute())

TEMPLATE_PATH = PATH + "\\resources\\templates\\"
SAVE_PATH = PATH + "\\resources\\saved\\"
DB_PATH = PATH + "\\db\\"
ICON_PATH = PATH + "\\icons\\"
CHARGES_DATABASE = DB_PATH + "\\charges.sqlite"
ARRAIGNMENTS_DATABASE = DB_PATH + "\\arraignments.sqlite"
SLATED_DATABASE = DB_PATH + "\\slated.sqlite"

PAY_DATE_DICT = {
    "forthwith": 0,
    "within 30 days": 30,
    "within 60 days": 60,
    "within 90 days": 90,
}

LEAP_COMPLETE_DATE_DICT = {
    "forthwith": 0,
    "120 days": 120,
}
