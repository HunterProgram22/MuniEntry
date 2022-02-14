"""A module containing common variables used throughout the application."""

import pathlib


def set_save_path():
    """This is going to be used to set SAVE and DB Paths for the production version so it saves outside
    of the executable file that is on the M: Drive."""
    if PATH == r"C:\Users\Justin Kudela\appdata\local\programs\python\python39\MuniEntry":
        return f"{PATH}\\resources\\saved\\"
    elif PATH == r"C:\Users\Justin Kudela\appdata\local\programs\python\python39\MuniEntry":
        return f"{PATH}\\resources\\saved\\"
    elif PATH == r"M:\Admin\Information_Technology\MuniEntry_files":
        return f"{PATH}\\resources\\saved\\"


PATH = str(pathlib.Path().absolute())

TEMPLATE_PATH = PATH + "\\resources\\templates\\"
SAVE_PATH = PATH + "\\resources\\saved\\"
# SAVE_PATH = set_save_path()
DB_PATH = PATH + "\\db\\"
ICON_PATH = PATH + "\\icons\\"
CHARGES_DATABASE = DB_PATH + "charges.sqlite"
CHARGES_TABLE = DB_PATH + "Charges.xlsx"


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


