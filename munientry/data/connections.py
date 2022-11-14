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
from munientry.paths import DB_PATH
from munientry.widgets.message_boxes import InfoBox

MUNIENTRY_DB = 'MuniEntryDB.sqlite'


def set_server_and_database() -> tuple:
    """Sets the server and database name for the SQL Server connections.

    This function is used to set a local instance of the database for Justin to test at home
    without being connected to the delcity network.

    Returns:
        tuple: (crim_server, crim_database, civil_server, civil_database)

            crim_server & civil_server (str): The names of the server for the database connection.

            crim_database & civil_database (str): The names of the database object.

    """
    if socket.gethostname() == 'RooberryPrime':
        crim_server = r'ROOBERRYPRIME\SQLEXPRESS'
        crim_database = 'AuthorityCourt'
        civil_server = r'ROOBERRYPRIME\SQLEXPRESS'
        civil_database = 'AuthorityCivil'
    else:
        crim_server = r'CLERKCRTR\CMI'
        crim_database = 'AuthorityCourt'
        civil_server = r'CLERKSQL\CMI'
        civil_database = 'AuthorityCivil'
    return (crim_server, crim_database, civil_server, civil_database)


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
    db_connection.setDatabaseName(database_path)
    return db_connection


def create_odbc_db_connection(connection_name: str) -> QSqlDatabase:
    """Creates a SQL Server database connection.

    The QODBC3 driver is used to create the connection.
    See https://doc.qt.io/qt-5/sql-driver.html#qodbc
    See https://stackoverflow.com/questions/16515420/connecting-to-ms-sql-server-with-windows-authentication-using-python/

    Args:
        connection_name (str): A string set to identify the database connection.

    Returns:
        QSqlDatabase: The connection to the database as a QSqlDatabase object.
    """
    db_connection = QSqlDatabase.addDatabase('QODBC', connection_name)
    crim_server, crim_database, civil_server, civil_database = set_server_and_database()
    if connection_name == 'con_authority_court':
        server = crim_server
        database = crim_database
    elif connection_name == 'con_authority_civil':
        server = civil_server
        database = civil_database
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
    if check_if_db_open(db_connection, connection_name):
        logger.database(f'{db_connection.connectionName()} database connection open.')
        return db_connection
    logger.database(f'{db_connection.connectionName()} database connection failed.')


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


def check_if_db_open(db_connection: QSqlDatabase, connection_name: str) -> bool:
    """Checks if a database connection is open.

    Args:
        db_connection (QSqlDatabase): The connection to the database as a QSqlDatabase object.

        connection_name (str): A string set to identify the database connection.

    Returns:
        bool: True if open, False if not open.
    """
    if not db_connection.isOpen():
        logger.warning(f'Unable to connect to {connection_name} database')
        message = None
        if connection_name == 'con_authority_court':
            message = 'A connection to the Authority Court database could not be made.'
        if connection_name == 'con_authority_civil':
            message = 'A connection to the Authority Civil database could not be made.'
        if connection_name == 'con_munientry_db':
            message = 'A connection to the MuniEntry Sqlite database could not be made.'
        InfoBox(message).exec()
        return False
    return True


def main():
    """The main function called when the module is imported.

    Creates one connection to the SQL Server external database.

    Creates three connections to the MuniEntryDB Sqlite internal database. Creating multiple
    connections is likely unnecessary but helps when referencing the connection to determine what
    table in the database the connection is supposed to reference.
    """
    authority_court_db = create_odbc_db_connection('con_authority_court')
    open_db_connection('con_authority_court')
    authority_court_is_open = check_if_db_open(authority_court_db, 'con_authority_court')
    logger.database(f'Connection to Authority Court is: {authority_court_is_open}')
    authority_civil_db = create_odbc_db_connection('con_authority_civil')
    open_db_connection('con_authority_civil')
    authority_civil_is_open = check_if_db_open(authority_civil_db, 'con_authority_civil')
    logger.database(f'Connection to Authority Civil is: {authority_civil_is_open}')
    create_sqlite_db_connection(f'{DB_PATH}{MUNIENTRY_DB}', 'con_munientry_db')

    conn = open_db_connection('con_munientry_db')
    load_daily_case_list_data(conn)
    close_db_connection(conn)

    create_sqlite_db_connection(f'{DB_PATH}{MUNIENTRY_DB}', 'con_daily_case_lists')
    create_sqlite_db_connection(f'{DB_PATH}{MUNIENTRY_DB}', 'con_charges')
    create_sqlite_db_connection(f'{DB_PATH}{MUNIENTRY_DB}', 'con_attorneys')


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
else:
    logger.level('DATABASE', no=21, color='<green>')
    logger.__class__.database = partialmethod(logger.__class__.log, 'DATABASE')
    main()
    logger.info(f'{__name__} imported.')
