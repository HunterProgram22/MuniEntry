"""Functions for connecting to databases - internal and external.

**munientry.data.connections**

See https://doc.qt.io/qtforpython/overviews/sql-connecting.html

Functions:
    set_server_and_database() -> tuple

    create_sqlite_db_connection(database_path, connection_name) -> QSqlDatabase

    create_odbc_db_connection(connection_name) -> QSqlDatabase

    open_db_connection(connection_name) -> QSqlDatabase

    no_db_connection_alert(connection_name) -> str

    close_db_connection(db_connection) -> None

    remove_db_connection(connection_name) -> None

    establish_database_connections() -> None
"""
import socket
from functools import partialmethod
from typing import Union

from loguru import logger
from PyQt6.QtSql import QSqlDatabase

from munientry.settings.paths import DB_PATH, TEST_DELCITY_DB_PATH
from munientry.widgets.message_boxes import TwoChoiceQuestionBox

# Database Constants
DATABASE_LOG_LEVEL = 21

MUNIENTRY_DB_CONN = 'con_munientry_db'
MUNIENTRY_DB = 'MuniEntryDB.sqlite'
TEST_MUNIENTRY_DB = 'TEST_MuniEntryDB.sqlite'

CRIM_TRAFFIC_DB_CONN = 'con_authority_court'
CRIM_TRAFFIC_DATABASE = 'AuthorityCourt'
CRIM_TRAFFIC_DB_SERVER = r'CLERKCRTR\CMI'

CIVIL_DB_CONN = 'con_authority_civil'
CIVIL_DATABASE = 'AuthorityCivil'
CIVIL_DB_SERVER = r'CLERKSQL\CMI'

HOME_DB_SERVER = r'ROOBERRYPRIME\SQLEXPRESS'
HOME_PC_SOCKET = 'RooberryPrime'
TEST_COMPUTER_SOCKETS = ('Muni10', 'RooberryPrime')

DATABASE_WARNINGS_SETTINGS = {
    CRIM_TRAFFIC_DB_CONN: True,
    CIVIL_DB_CONN: True,
    MUNIENTRY_DB_CONN: True,
}
# End Database Constants


def set_server_and_database(connection_name: str) -> tuple:
    """Sets the server and database name for the SQL Server connections.

    If not on delcity network sets local instance of the database for Justin to test at home.

    Args:
        connection_name (str): The name of the database connection.

    Returns:
        tuple: (server, database)

            server (str): The name of the server for the database connection.

            database (str): The name of the database.
    """
    if connection_name == CRIM_TRAFFIC_DB_CONN:
        server = CRIM_TRAFFIC_DB_SERVER
        database = CRIM_TRAFFIC_DATABASE

    if connection_name == CIVIL_DB_CONN:
        server = CIVIL_DB_SERVER
        database = CIVIL_DATABASE

    # SETS Testing Server for Justin to test at home
    if socket.gethostname() == HOME_PC_SOCKET:
        server = HOME_DB_SERVER

    logger.info(f'Database for {connection_name} set to {database} on server {server}.')
    return (server, database)


def create_sqlite_db_connection(database_path: str, connection_name: str) -> QSqlDatabase:
    """Creates a SQLite database connection.

    The QSLITE driver is used to create the connection.
    See https://doc.qt.io/qt-5/sql-driver.html#qsqlite
    See https://realpython.com/python-pyqt-database/

    Args:
        database_path (str): The absolute path to the location of the database.

        connection_name (str): A string set to identify the database connection.

    Returns:
        QSqlDatabase: The connection to the database as a QSqlDatabase object.
    """
    db_connection = QSqlDatabase.addDatabase('QSQLITE', connection_name)
    if socket.gethostname() in TEST_COMPUTER_SOCKETS:
        database_path = f'{TEST_DELCITY_DB_PATH}{TEST_MUNIENTRY_DB}'
    db_connection.setDatabaseName(database_path)
    logger.info(f'Database for {connection_name} set to: {database_path}')
    return db_connection


def create_odbc_db_connection(connection_name: str) -> QSqlDatabase:
    """Creates a SQL Server database connection.

    The QODBC driver is used to create the connection.
    See https://doc.qt.io/qt-6/sql-driver.html#qodbc

    Args:
        connection_name (str): A string set to identify the database connection.

    Returns:
        QSqlDatabase: The connection to the database as a QSqlDatabase object.
    """
    db_connection = QSqlDatabase.addDatabase('QODBC', connection_name)
    server, database = set_server_and_database(connection_name)
    connection_string = (
        'DRIVER=SQL Server;'
        + f'SERVER={server};'
        + f'DATABASE={database};'
        + 'TRUSTED_CONNECTION=yes;'
    )
    db_connection.setDatabaseName(connection_string)
    return db_connection


def open_db_connection(connection_name: str) -> Union[QSqlDatabase, str]:
    """Attempts to open a database and returns connection.

    If connection is not open, then returns an alert for the user.

    Args:
        connection_name (str): A string set to identify the database connection.

    Returns (either):
        QSqlDatabase: The connection to the database as a QSqlDatabase object.

        str: 'NO_Connection'
    """
    db_connection = QSqlDatabase.database(connection_name, open=True)
    if not db_connection.isOpen():
        return no_db_connection_alert(connection_name)
    logger.database(f'{connection_name} database connection open.')
    return db_connection


def no_db_connection_alert(connection_name: str) -> str:
    """Alers user that a connection to the database could not be made.

    Also asks if the user wants to turn off the warnings for future failed connections.

    If the user responds to the inquiry with 'Yes' (int 0 is returned) to turn off
    warnings, it updates dict that tracks connection warnings.

    Args:
        connection_name (str): A string set to identify the database connection.

    Returns:
        str: 'NO_Connection'
    """
    if DATABASE_WARNINGS_SETTINGS[connection_name] is True:
        message = (
            f'A connection to the {connection_name} database could not be made. Certain features'
            + ' will be unavailable.'
            + f'\n\nDo you want to turn off the warning for the {connection_name} failed'
            + ' connection?'
        )
        response = TwoChoiceQuestionBox(
            message,
            'Yes',
            'No',
            'Turn Off Database Warning',
        ).exec()
        if response == 0:
            DATABASE_WARNINGS_SETTINGS[connection_name] = False
    logger.warning(f'Unable to connect to {connection_name} database')
    return 'NO_Connection'


def close_db_connection(db_connection: QSqlDatabase) -> None:
    """Closes database connection, but does not remove the connection from the system.

    Args:
        db_connection (QSqlDatabase): The connection to the database as a QSqlDatabase object.
    """
    try:
        db_connection.close()
    except AttributeError as err:
        logger.warning(err)
    else:
        logger.database(f'{db_connection.connectionName()} database connection closed.')


def remove_db_connection(connection_name: str) -> None:
    """Removes database connection from application.

    If a connection is removed it would need to be created again to be used again. This should
    only be used upon close of the application to clean up connections.

    Args:
        connection_name (str): A string set to identify the database connection.
    """
    QSqlDatabase.removeDatabase(connection_name)
    logger.database(f'{connection_name} database connection removed.')


def establish_database_connections():
    """Establishes database connections for the application, tests all connections open.

    Also loads the SSRS reports with the daily case lists into the application database.
    """
    logger.database('Establishing database connections.')

    create_odbc_db_connection(CRIM_TRAFFIC_DB_CONN)
    authority_court_db = open_db_connection(CRIM_TRAFFIC_DB_CONN)
    close_db_connection(authority_court_db)

    create_odbc_db_connection(CIVIL_DB_CONN)
    authority_civil_db = open_db_connection(CIVIL_DB_CONN)
    close_db_connection(authority_civil_db)

    create_sqlite_db_connection(f'{DB_PATH}{MUNIENTRY_DB}', MUNIENTRY_DB_CONN)
    munientry_db = open_db_connection(MUNIENTRY_DB_CONN)
    close_db_connection(munientry_db)


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
else:
    logger.level('DATABASE', no=DATABASE_LOG_LEVEL, color='<green>')
    logger.__class__.database = partialmethod(logger.__class__.log, 'DATABASE')
    establish_database_connections()
