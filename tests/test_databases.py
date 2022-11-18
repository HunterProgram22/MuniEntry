"""Test module for database connections.

All tests in this module use the charges db in the tests/db folder.
"""
import pytest
from PyQt6.QtSql import QSqlDatabase

from munientry.data.connections import (
    create_sqlite_db_connection,
    open_db_connection,
    remove_db_connection,
)
from munientry.data.excel_getters import clean_offense_name
from munientry.data.sql_lite_functions import (
    load_daily_case_list_data,
    query_daily_case_list_data,
    query_offense_statute_data,
)
from munientry.data.sql_lite_getters import CriminalCaseSQLLite
from munientry.paths import DB_PATH
from munientry.settings import EXCEL_DAILY_CASE_LISTS

MUNIENTRY_DB = 'con_munientry_db'
PLEAS = 'pleas'
TOTAL_STATUTES = 46


@pytest.fixture(name='crim_sql_retriever')
def crim_sql_retriever_setup():
    """Fixture that returns criminal case loaded from Sqllite."""
    return CriminalCaseSQLLite('20TRC09471', PLEAS)


@pytest.fixture(name='crim_sql_special_character')
def crim_sql_special_character_setup():
    """Fixture that returns criminal case with special character (') case loaded from Sqllite."""
    return CriminalCaseSQLLite('21CRB01597', PLEAS)


def test_load_criminal_case(crim_sql_retriever):
    """Tests that criminal case loads successfully."""
    assert crim_sql_retriever.case_number == '20TRC09471'
    assert crim_sql_retriever.case_table == PLEAS


def test_load_criminal_case_with_special_char(crim_sql_special_character):
    """Tests that criminal case with special char in name (') loads succesfully."""
    assert crim_sql_special_character.case_number == '21CRB01597'
    assert crim_sql_special_character.case_table == PLEAS


def test_get_case_data_works(crim_sql_retriever):
    """Tests that all data collected with loader class (CriminalCaseSQLLite)."""
    case = crim_sql_retriever.case
    assert case.case_number == '20TRC09471'
    assert case.defendant.last_name == 'Henderson'
    assert case.defendant.first_name == 'Chase'
    assert case.fra_in_file == 'U'
    assert case.defense_counsel == 'Chris Junga'
    assert case.defense_counsel_type == '1'
    assert len(case.charges_list) == 5
    assert case.charges_list[0][0] == 'OVI Alcohol / Drugs 1st'


def test_get_case_data_special_character(crim_sql_special_character):
    """Tests all data collected with loader class (CriminalCaseSQLLite) with special char (')."""
    case = crim_sql_special_character.case
    assert case.case_number == '21CRB01597'
    assert case.defendant.last_name == "O'Reilly"
    assert case.defendant.first_name == 'Jacob'
    assert case.fra_in_file == 'U'
    assert case.defense_counsel == 'Chase Mallory'
    assert case.defense_counsel_type == 'No Data'
    assert len(case.charges_list) == 1
    assert case.charges_list[0][0] == 'Possession of Marihuana'


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


def test_total_daily_case_lists_is_six():
    """Tests that there are 6 daily case lists to load."""
    assert len(EXCEL_DAILY_CASE_LISTS) == 6


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
    ('arraignments', 9),
    ('slated', 12),
    ('final_pretrials', 12),
    (PLEAS, 12),
    ('trials_to_court', 12),
    ('pcvh_fcvh', 14),
]


@pytest.mark.parametrize('table, total_cases', daily_case_lists)
def test_query_daily_case_list_data(table, total_cases):
    """Tests correct number of cases loaded from daily case lists.

    The assertion for total cases needs to be one more than the total cases. This is because in
    the test/db cases table a blank is inserted at the top of the list.
    """
    db_connection = open_db_connection(MUNIENTRY_DB)
    assert len(query_daily_case_list_data(table, db_connection)) == total_cases


def test_charges_connection_to_db():
    """Tests connection to charges table."""
    con_charges = open_db_connection(MUNIENTRY_DB)
    assert isinstance(con_charges, QSqlDatabase)


def test_create_daily_case_lists_db():
    """Tests connection to daily case list tables."""
    con_daily_case_lists = open_db_connection(MUNIENTRY_DB)
    load_daily_case_list_data(con_daily_case_lists)
    assert isinstance(con_daily_case_lists, QSqlDatabase)
