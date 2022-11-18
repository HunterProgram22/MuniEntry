"""Functions for connecting to databases - internal and external.

**munientry.data.connections**

See https://doc.qt.io/qtforpython/overviews/sql-connecting.html

Functions:
    set_server_and_database() -> tuple

    create_sqlite_db_connection(database_path, connection_name) -> QSqlDatabase

    create_odbc_db_connection(connection_name) -> QSqlDatabase

    open_db_connection(connection_name) -> QSqlDatabase

    close_db_connection(db_connection) -> None

    remove_db_connection(connection_name) -> None

    check_if_db_open(db_connection, connection_name) -> bool
"""
import socket
from functools import partialmethod

from loguru import logger
from PyQt6.QtSql import QSqlDatabase

from munientry.data.sql_lite_functions import load_daily_case_list_data
from munientry.paths import DB_PATH, TEST_DELCITY_DB_PATH
from munientry.widgets.message_boxes import InfoBox

DATABASE_LOG_LEVEL = 21
MUNIENTRY_DB = 'MuniEntryDB.sqlite'
TEST_MUNIENTRY_DB = 'TEST_MuniEntryDB.sqlite'


def set_server_and_database(connection_name: str) -> tuple:
    """Sets the server and database name for the SQL Server connections.

    This function is used to set a local instance of the database for Justin to test at home
    without being connected to the delcity network.

    Args:
        connection_name (str): The name of the database connection.

    Returns:
        tuple: (server, database)

            server (str): The name of the server for the database connection.

            database (str): The name of the database.

    """
    if connection_name == 'con_authority_court':
        if socket.gethostname() == 'RooberryPrime':
            server = r'ROOBERRYPRIME\SQLEXPRESS'
            database = 'AuthorityCourt'
        else:
            server = r'CLERKCRTR\CMI'
            database = 'AuthorityCourt'
    elif connection_name == 'con_authority_civil':
        if socket.gethostname() == 'RooberryPrime':
            server = r'ROOBERRYPRIME\SQLEXPRESS'
            database = 'AuthorityCivil'
        else:
            server = r'CLERKSQL\CMI'
            database = 'AuthorityCivil'
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
    if socket.gethostname() == 'Muni10':
        db_connection = QSqlDatabase.addDatabase('QSQLITE', connection_name)
        db_connection.setDatabaseName(f'{TEST_DELCITY_DB_PATH}{TEST_MUNIENTRY_DB}')
        logger.info(f'TEST Database Set to: {TEST_DELCITY_DB_PATH}')
    else:
        db_connection = QSqlDatabase.addDatabase('QSQLITE', connection_name)
        db_connection.setDatabaseName(database_path)
        logger.info(f'Database Set to: {database_path}')
    return db_connection


def create_odbc_db_connection(connection_name: str) -> QSqlDatabase:
    """Creates a SQL Server database connection.

    The QODBC3 driver is used to create the connection.
    See https://doc.qt.io/qt-5/sql-driver.html#qodbc

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


def open_db_connection(connection_name: str) -> QSqlDatabase:
    """Attempts to open a database and returns connection if open.

    Args:
        connection_name (str): A string set to identify the database connection.

    Returns:
        QSqlDatabase: The connection to the database as a QSqlDatabase object.
    """
    db_connection = QSqlDatabase.database(connection_name, open=True)
    if db_connection.isOpen():
        logger.database(f'{connection_name} database connection open.')
    else:
        logger.warning(f'Unable to connect to {connection_name} database')
        message = f'A connection to the {connection_name} database could not be made.'
        InfoBox(message).exec()
    return db_connection


def close_db_connection(db_connection: QSqlDatabase) -> None:
    """Closes database connection, but does not remove the connection from the system.

    Args:
        db_connection (QSqlDatabase): The connection to the database as a QSqlDatabase object.

    Todo:
        Refactor to accept a string of connection name to mirror open_db_connection function.
    """
    db_connection.close()
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
    """Establishes database connections for the application and tests all connections open."""
    logger.database('Establishing database connections.')

    create_odbc_db_connection('con_authority_court')
    authority_court_db = open_db_connection('con_authority_court')
    close_db_connection(authority_court_db)

    create_odbc_db_connection('con_authority_civil')
    authority_civil_db = open_db_connection('con_authority_civil')
    close_db_connection(authority_civil_db)

    create_sqlite_db_connection(f'{DB_PATH}{MUNIENTRY_DB}', 'con_munientry_db')
    conn = open_db_connection('con_munientry_db')
    load_daily_case_list_data(conn)
    close_db_connection(conn)


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
else:
    logger.level('DATABASE', no=DATABASE_LOG_LEVEL, color='<green>')
    logger.__class__.database = partialmethod(logger.__class__.log, 'DATABASE')
    establish_database_connections()
