"""Module that contains all functions for connecting to databases - internal and external.

See https://doc.qt.io/qtforpython/overviews/sql-connecting.html
"""
from functools import partialmethod

from loguru import logger
from PyQt6.QtSql import QSqlDatabase

from munientry.data.sql_lite_functions import load_daily_case_list_data
from munientry.settings import set_server_and_database
from munientry.paths import DB_PATH
from munientry.widgets.message_boxes import InfoBox

MUNIENTRY_DB = 'MuniEntryDB.sqlite'


def create_sqlite_db_connection(database_path: str, connection_name: str) -> QSqlDatabase:
    """Creates a SQLite database connection.

    The QSLITE driver is used to create the connection.
    See https://doc.qt.io/qt-5/sql-driver.html#qsqlite
    See https://realpython.com/python-pyqt-database/

    :database_path: The absolute path to the location of the database. The absolute path should
        be set using a sys.path object so that it references the actual location of the database,
        which will be dependent on the location of the application. Uses DB_PATH constant
        from settings which sets the absolute path based on the location of the application.

    :connection_name: A string that is assigned for future reference to the connection.

    Returns the connection as a QSqlDatabase object.
    """
    db_connection = QSqlDatabase.addDatabase('QSQLITE', connection_name)
    db_connection.setDatabaseName(database_path)
    return db_connection


def create_odbc_db_connection(connection_name: str) -> QSqlDatabase:
    """Creates a SQL Server database connection.

    The QODBC3 driver is used to create the connection.
    See https://doc.qt.io/qt-5/sql-driver.html#qodbc
    This also helped establishing the connection even though it references the pyodbc module.
    See 'https://stackoverflow.com/questions/16515420/
    connecting-to-ms-sql-server-with-windows-authentication-using-python/'

    :connection_name: A string that is assigned for future reference to the connection.

    Returns the connection as a QSqlDatabase object.
    """
    db_connection = QSqlDatabase.addDatabase('QODBC', connection_name)
    server, database = set_server_and_database()
    connection_string = (
        'DRIVER=SQL Server;'
        + f'SERVER={server};'
        + f'DATABASE={database};'
        + 'TRUSTED_CONNECTION=yes;'
    )
    db_connection.setDatabaseName(connection_string)
    return db_connection


def open_db_connection(connection_name: str) -> QSqlDatabase:
    """Opens a connection to a database and checks if it is open.

    :connection_name: A string provided when the function is called. The string is assigned to the
        database object to allow reference to the database by the connection name.

    Returns the connection as a QSqlDatabase object with an open connection.
    """
    db_connection = QSqlDatabase.database(connection_name, open=True)
    check_if_db_open(db_connection, connection_name)
    logger.database(f'{db_connection.connectionName()} database connection open.')
    return db_connection


def close_db_connection(db_connection: QSqlDatabase) -> None:
    """Closes a connection to a database, but does not remove the connection from the system.

    :db_connection: The QSqlDatabase object that is the API driver connection to the database.

    TODO: This should be refactored to accept a string of the connection name to mirror the
    open_db_connection function.
    """
    db_connection.close()
    logger.database(f'{db_connection.connectionName()} database connection closed.')


def remove_db_connection(connection_name: str) -> None:
    """Removes a connection to a database.

    If a connection is removed it would need to be created again to be used again. This should
    only be used upon close of the application to clean up connections.
    """
    QSqlDatabase.removeDatabase(connection_name)
    logger.database(f'{connection_name} database connection removed.')


def check_if_db_open(db_connection: QSqlDatabase, connection_name: str) -> bool:
    """Checks if a database connection is open.

    :db_connection: The QSqlDatabase object that is the API driver connection to the database.

    :connection_name: The string assigned to the connection for reference.
    """
    if not db_connection.isOpen():
        logger.warning(f'Unable to connect to {connection_name} database')
        if connection_name == 'con_authority_court':
            InfoBox(
                'The Case Search feature is not available because a connection to the '
                + 'AuthorityCourt database could not be made.',
            ).exec()
        if connection_name == 'con_munientry_db':
            InfoBox(
                'A connection to the MuniEntryDB could not be made. Contact Justin '
                + 'immediately.',
            ).exec()
    return True


def main():
    """The main function called when the module is imported.

    Creates one connection to the SQL Server external database.

    Creates three connections to the MuniEntryDB Sqlite internal database. Creating multiple
    connections is likely unnecessary but helps when referencing the connection to determine what
    table in the database the connection is supposed to reference.
    """
    create_odbc_db_connection('con_authority_court')
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
