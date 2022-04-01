import pytest
from PyQt5.QtSql import QSqlDatabase

from conftest import mouse_click, enter_data

from db.databases import (
    CriminalCaseSQLRetriever,
    open_daily_case_list_db_connection,
    create_daily_case_list_db_connection,
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


def test_if_open_daily_case_list_db_connection_works():
    assert open_daily_case_list_db_connection().isOpen() == True


def test_if_create_daily_case_list_db_connection_returns_db_instance():
    con = create_daily_case_list_db_connection()
    assert isinstance(con, QSqlDatabase)