"""Test module for database connections.

All tests in this module use the charges db in the tests/db folder.
"""
import pytest
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

from munientry.data.connections import (
    create_sqlite_db_connection,
    open_db_connection,
    close_db_connection,
    remove_db_connection,
)
from munientry.data.data_cleaners import clean_offense_name
from munientry.sqlserver.sql_server_queries import daily_case_list_query
from munientry.sqllite.sql_lite_functions import (
    query_daily_case_list_data,
    query_offense_statute_data,
)
from munientry.sqlserver.sql_server_getters import CriminalCaseSQLServer
from munientry.appsettings.paths import DB_PATH

MUNIENTRY_DB = 'con_munientry_db'
AUTHORITY_COURT_DB = 'con_authority_court'
PLEAS = 'pleas'
TOTAL_STATUTES = 46


@pytest.fixture(name='crim_sql_retriever')
def crim_sql_retriever_setup():
    """Fixture that returns criminal case loaded from Sqllite."""
    return CriminalCaseSQLServer('22TRC01734')


@pytest.fixture(name='crim_sql_special_character')
def crim_sql_special_character_setup():
    """Fixture that returns criminal case with special character (') case loaded from Sqllite."""
    return CriminalCaseSQLServer('22TRD01605')


def test_load_criminal_case(crim_sql_retriever):
    """Tests that criminal case loads successfully."""
    assert crim_sql_retriever.case_number == '22TRC01734'


def test_load_criminal_case_with_special_char(crim_sql_special_character):
    """Tests that criminal case with special char in name (') loads succesfully."""
    assert crim_sql_special_character.case_number == '22TRD01605'


def test_get_case_data_works(crim_sql_retriever):
    """Tests that all data collected with loader class (CriminalCaseSQLServer)."""
    case = crim_sql_retriever.case
    assert case.case_number == '22TRC01734'
    assert case.defendant.last_name == 'Rosero Pacheco'
    assert case.defendant.first_name == 'Pablo'
    assert case.fra_in_file == 'U'
    assert case.defense_counsel == ' '
    assert case.defense_counsel_type == 0
    assert len(case.charges_list) == 4
    assert case.charges_list[0][0] == 'OVI Alcohol / Drugs 1st'


def test_get_case_data_special_character(crim_sql_special_character):
    """Tests all data collected with loader class (CriminalCaseSQLServer) with special char (')."""
    case = crim_sql_special_character.case
    assert case.case_number == '22TRD01605'
    assert case.defendant.last_name == "O'Metz"
    assert case.defendant.first_name == 'Sara'
    assert case.fra_in_file == 'N'
    assert case.defense_counsel == ' '
    assert case.defense_counsel_type == 0
    assert len(case.charges_list) == 2
    assert case.charges_list[0][0] == 'Driving Under FRA Suspension / Cancel / Judgment'


test_offense_list = [
    ('OVI ALCOHOL / DRUGS 1st', 'OVI Alcohol / Drugs 1st'),
    ('DUS FTA, FINES OR CHILD SUPPORT', 'DUS Fta, Fines / Child Support'),
    ('BMV SUSPENSION', 'BMV Suspension'),
]


@pytest.mark.parametrize('test_input, expected_output', test_offense_list)
def test_clean_offense_name(crim_sql_retriever, test_input, expected_output):
    """Tests that clean_offense_name function properly cleans data."""
    assert clean_offense_name(test_input) == expected_output


db_connection_list = [
    MUNIENTRY_DB,
]


@pytest.mark.parametrize('connection', db_connection_list)
def test_open_db_connections(connection):
    """Tests that database connection opens properly."""
    assert open_db_connection(connection).isOpen()
    remove_db_connection(connection)


db_name_list = [
    (f'{DB_PATH}MuniEntryDB.sqlite', MUNIENTRY_DB),
]


@pytest.mark.parametrize('database_name, connection_name', db_name_list)
def test_create_db_connection_returns_db(database_name, connection_name):
    """Tests database connection return database instance."""
    con = create_sqlite_db_connection(database_name, connection_name)
    assert isinstance(con, QSqlDatabase)


query_list = [
    ('offense', MUNIENTRY_DB),
    ('statute', MUNIENTRY_DB),
]


@pytest.mark.parametrize('query, connection_name', query_list)
def test_query_offense_statute_data(query, connection_name):
    """Tests that the correct number of statutes and offenses available in charges table.

    Must update TOTAL_STATUTES if new charges are added to charges table in MuniEntry_DB.
    """
    db_connection = open_db_connection(connection_name)
    assert len(query_offense_statute_data(db_connection, query)) == TOTAL_STATUTES


daily_case_lists = [
    ('[reports].[DMCMuniEntryArraignment]', 8),
    ('[reports].[DMCMuniEntrySlated]', 11),
    ('[reports].[DMCMuniEntryFinalPreTrials]', 11),
    ('[reports].[DMCMuniEntryPleas]', 11),
    ('[reports].[DMCMuniEntryBenchTrials]', 11),
    ('[reports].[DMCMuniEntryPrelimCommContViolHearings]', 13),
]


@pytest.mark.parametrize('reports, total_cases', daily_case_lists)
def test_query_daily_case_list_data(reports, total_cases):
    """Tests correct number of cases loaded test database (AuthorityCourt) Stored Procs."""
    db_connection = open_db_connection(AUTHORITY_COURT_DB)
    query = QSqlQuery(db_connection)
    query_string = daily_case_list_query(reports)
    query.prepare(query_string)
    query.exec()
    count = 0
    while query.next():
        count += 1
    assert count == total_cases
    query.finish()
    close_db_connection(db_connection)


def test_charges_connection_to_db():
    """Tests connection to charges table."""
    con_charges = open_db_connection(MUNIENTRY_DB)
    assert isinstance(con_charges, QSqlDatabase)
