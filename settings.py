"""A module containing common variables used throughout the application."""

import pathlib
from loguru import logger

from PyQt5.QtSql import QSqlDatabase

PATH = str(pathlib.Path().absolute())
TEMPLATE_PATH = PATH + "\\resources\\templates\\"
SAVE_PATH = PATH + "\\resources\\saved\\"
DB_PATH = PATH + "\\resources\\db\\"
CHARGES_DATABASE = DB_PATH + "\\charges.sqlite"
CASES_DATABASE = DB_PATH + "\\arraignments.sqlite"

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


@logger.catch
def create_arraignments_database_connection():
    """Opens a connection to the database and returns that connection to the arraignments_database."""
    arraignments_database_connection = QSqlDatabase.addDatabase("QSQLITE", "cases")
    arraignments_database_connection.setDatabaseName(CASES_DATABASE)
    return arraignments_database_connection
