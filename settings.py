"""A module containing common variables used throughout the application."""
import pathlib

PATH = str(pathlib.Path().absolute())

TEMPLATE_PATH = PATH + "\\resources\\templates\\"
SAVE_PATH = PATH + "\\resources\\saved\\"
DB_PATH = PATH + "\\db\\"
ICON_PATH = PATH + "\\icons\\"
CHARGES_DATABASE = DB_PATH + "charges.sqlite"
CHARGES_TABLE = DB_PATH + "Charges.xlsx"

MOVING_COURT_COSTS = 137
CRIMINAL_COURT_COSTS = 127
NONMOVING_COURT_COSTS = 108


