import os
from os.path import exists
import pytest
from PyQt5.QtSql import QSqlDatabase

from conftest import mouse_click, enter_data
from settings import CHARGES_DATABASE, DB_PATH
from db.databases import (
    CriminalCaseSQLRetriever,
    open_db_connection,
    create_db_connection,
    close_db_connection,
    check_if_db_open,
)


@pytest.fixture
def crim_sql_retriever():
    return CriminalCaseSQLRetriever("20TRC09471", "arraignments")


def test_create_CriminalCaseSQLRetriever(crim_sql_retriever):
    assert crim_sql_retriever.case_number == "20TRC09471"
    assert crim_sql_retriever.case_table == "arraignments"


def test_get_case_data_works(crim_sql_retriever):
    case = crim_sql_retriever.case
    assert case.case_number == "20TRC09471"
    assert case.defendant.last_name == "Henderson"
    assert case.defendant.first_name == "Chase"
    assert case.fra_in_file == "U"
    assert case.defense_counsel == "Chris Junga"
    assert case.defense_counsel_type == "PD"
    assert len(case.charges_list) == 5
    assert case.charges_list[0][0] == "OVI Alcohol / Drugs 1st"


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
    close_db_connection(connection)


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
    assert check_if_db_open(db_connection)
