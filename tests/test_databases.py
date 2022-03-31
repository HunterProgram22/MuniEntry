import pytest
from conftest import mouse_click, enter_data

from db.databases import CriminalCaseSQLRetriever


@pytest.fixture
def crim_sql_retriever():
    return CriminalCaseSQLRetriever("12TEST34", "arraignments")


def test_create_CriminalCaseSQLRetriever(crim_sql_retriever):
    assert crim_sql_retriever.case_number == "12TEST34"
    assert crim_sql_retriever.case_table == "arraignment"