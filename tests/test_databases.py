import pytest
from PyQt5.QtSql import QSqlDatabase

from munientry.settings import DB_PATH, EXCEL_DAILY_CASE_LISTS
from munientry.data.databases import (
    CriminalCaseSQLRetriever,
    open_db_connection,
    create_db_connection,
    remove_db_connection,
    check_if_db_open,
    query_offense_statute_data,
    query_daily_case_list_data,
    create_charges_sql_table,
    load_charges_data,
    create_daily_case_list_sql_tables,
    load_daily_case_list_data,
)


@pytest.fixture
def crim_sql_retriever():
    return CriminalCaseSQLRetriever("20TRC09471", "pleas")

@pytest.fixture
def crim_sql_special_character():
    return CriminalCaseSQLRetriever("21CRB01597", "pleas")


def test_create_CriminalCaseSQLRetriever(crim_sql_retriever):
    assert crim_sql_retriever.case_number == "20TRC09471"
    assert crim_sql_retriever.case_table == "pleas"

def test_special_character_create_CriminalCaseSQLRetriever(crim_sql_special_character):
    assert crim_sql_special_character.case_number == "21CRB01597"
    assert crim_sql_special_character.case_table == "pleas"

def test_get_case_data_works(crim_sql_retriever):
    case = crim_sql_retriever.case
    assert case.case_number == "20TRC09471"
    assert case.defendant.last_name == "Henderson"
    assert case.defendant.first_name == "Chase"
    assert case.fra_in_file == "U"
    assert case.defense_counsel == "Chris Junga"
    assert case.defense_counsel_type == "1"
    assert len(case.charges_list) == 5
    assert case.charges_list[0][0] == "OVI Alcohol / Drugs 1st"

def test_get_case_data_special_character(crim_sql_special_character):
    case = crim_sql_special_character.case
    assert case.case_number == "21CRB01597"
    assert case.defendant.last_name == "O'Reilly"
    assert case.defendant.first_name == "Jacob"
    assert case.fra_in_file == "U"
    assert case.defense_counsel == "Chase Mallory"
    assert case.defense_counsel_type == "No Data"
    assert len(case.charges_list) == 1
    assert case.charges_list[0][0] == "Possession Of Marihuana"


test_offense_list = [
    ("OVI ALCOHOL / DRUGS 1st", "OVI Alcohol / Drugs 1st"),
    ("DUS FTA, FINES OR CHILD SUPPORT", "DUS Fta, Fines Or Child Support"),
    ("BMV SUSPENSION", "BMV Suspension"),
]


@pytest.mark.parametrize("test_input, expected_output", test_offense_list)
def test_clean_offense_name(crim_sql_retriever, test_input, expected_output):
    assert crim_sql_retriever.clean_offense_name(test_input) == expected_output


db_connection_list = [
    "con_daily_case_lists",
    "con_charges",
]

@pytest.mark.parametrize("connection", db_connection_list)
def test_open_db_connections(connection):
    assert open_db_connection(connection).isOpen()
    remove_db_connection(connection)


db_name_list = [
    (f"{DB_PATH}daily_case_lists.sqlite", "con_daily_case_lists"),
    (f"{DB_PATH}charges.sqlite", "con_charges"),
]

@pytest.mark.parametrize("database_name, connection_name", db_name_list)
def test_if_create_db_connection_returns_db_instance(database_name, connection_name):
    con = create_db_connection(database_name, connection_name)
    assert isinstance(con, QSqlDatabase)


@pytest.mark.parametrize("database_name, connection_name", db_name_list)
def test_if_check_if_db_open_works(database_name, connection_name):
    """This test may be unnecessary as test_open_db_connection uses a function that
    runs this check."""
    db_connection = open_db_connection(connection_name)
    assert check_if_db_open(db_connection, connection_name)


def test_total_daily_case_lists_is_six():
    assert len(EXCEL_DAILY_CASE_LISTS) == 6


query_list = [
    ("offense", "con_charges"),
    ("statute", "con_charges"),
]

@pytest.mark.parametrize("query, connection_name", query_list)
def test_query_offense_statute_data(query, connection_name):
    db_connection = open_db_connection(connection_name)
    assert len(query_offense_statute_data(db_connection, query)) == 45


daily_case_lists = [
    ("arraignments", 9),
    ("slated", 12),
    ("final_pretrials", 12),
    ("pleas", 12),
    ("trials_to_court", 7),
    ("pcvh_fcvh", 14),
]

@pytest.mark.parametrize("table, total_cases", daily_case_lists)
def test_query_daily_case_list_data(table, total_cases):
    """The assertion for total cases needs to be one more than the total cases in the
    test/db cases table because a blank is inserted at the top of the list."""
    db_connection = open_db_connection('con_daily_case_lists')
    assert len(query_daily_case_list_data(table, db_connection)) == total_cases


def test_create_charges_db():
    """This test uses the charges db in the test/db, also code below is copied
    from the main() of databases.py - not ideal test."""
    create_db_connection(f"{DB_PATH}charges.sqlite", "con_charges")
    con_charges = open_db_connection("con_charges")
    create_charges_sql_table(con_charges)
    load_charges_data(con_charges)
    assert isinstance(con_charges, QSqlDatabase)


def test_create_daily_case_lists_db():
    """This test uses the charges db in the test/db, also code below is copied
    from the main() of databases.py - not ideal test."""
    create_db_connection(f"{DB_PATH}daily_case_lists.sqlite", "con_daily_case_lists")
    con_daily_case_lists = open_db_connection("con_daily_case_lists")
    create_daily_case_list_sql_tables(con_daily_case_lists)
    load_daily_case_list_data(con_daily_case_lists)
    assert isinstance(con_daily_case_lists, QSqlDatabase)