import pytest
from conftest import mouse_click, enter_data

from db.databases import CriminalCaseSQLRetriever


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