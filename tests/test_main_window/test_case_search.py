"""This module contains tests for searching for criminal and civil cases in a main window."""
import pytest

from unittest.mock import MagicMock

from munientry.mainwindow.case_search import CaseDocketHandler, CaseSearchHandler, CaseListHandler
from munientry.widgets.table_widgets import TableReportWindow
from munientry.mainwindow.main_window import MainWindow
from tests.conftest import enter_data, mouse_click

CRIM_TEST_CASES = (
    ('22c6', '22TRC00006'),
    ('22b236', '22CRB00236'),
    ('21c5611', '21TRC05611'),
    ('22d1944', '22TRD01944'),
)

CIVIL_TEST_CASES = (
    ('22f2', '22CVF00002'),
    ('22g10', '22CVG00010'),
    ('22i137', '22CVI00137'),
    ('22h1064', '22CVH01064'),
)


@pytest.fixture
def mock_mainwindow():
    mock = MagicMock()
    return mock


@pytest.fixture
def case_docket_handler(mock_mainwindow):
    return CaseDocketHandler(mock_mainwindow)


@pytest.fixture
def case_search_handler(mock_mainwindow):
    return CaseSearchHandler(mock_mainwindow)


@pytest.fixture
def case_list_handler():
    case_list = MagicMock()
    case_list.objectName.return_value = "mock_list"
    daily_case_lists = [case_list]
    return CaseListHandler(daily_case_lists)


@pytest.fixture(name='main_window')
def main_window_fixture(qtbot) -> MainWindow:
    """Fixture to set up the main window for testing."""
    window = MainWindow()
    qtbot.addWidget(window)
    return window


@pytest.mark.parametrize('case_number, expected_output', CRIM_TEST_CASES)
def test_crim_case_search(main_window, case_number, expected_output):
    """Test for searching by a criminal case number."""
    # Set up the main window for the criminal case search
    main_window.cases_tab_widget.setCurrentWidget(main_window.crim_case_search_tab)
    enter_data(main_window.crim_case_search_box, case_number)

    # Perform the search and assert the results
    mouse_click(main_window.crim_get_case_btn)
    assert main_window.crim_case_search_box.text() == expected_output
    assert main_window.crim_case_number_label.text() == expected_output


@pytest.mark.parametrize('case_number, expected_output', CIVIL_TEST_CASES)
def test_civil_case_search(main_window, case_number, expected_output):
    """Test for searching by a civil case number."""
    # Set up the main window for civil case search
    main_window.cases_tab_widget.setCurrentWidget(main_window.civil_case_search_tab)
    enter_data(main_window.civil_case_search_box, case_number)

    # Perform the search and assert the results
    mouse_click(main_window.civil_get_case_btn)
    assert main_window.civil_case_search_box.text() == expected_output
    assert main_window.civil_case_number_label.text() == expected_output

def test_generate_crim_case_docket(case_docket_handler):
    case_number = "123"
    assert case_docket_handler.docket_report is None
    case_docket_handler.generate_crim_case_docket(case_number)
    assert case_docket_handler.docket_report is not None


def test_create_table(case_docket_handler):
    rows = 3
    title = "Test Title"
    case_docket_handler.docket_report = TableReportWindow(title)
    case_docket_handler.create_table(rows, title)
    assert case_docket_handler.docket_report.table.rowCount() == rows
    assert case_docket_handler.docket_report.table.horizontalHeaderItem(0).text() == "Date"
    assert case_docket_handler.docket_report.table.horizontalHeaderItem(1).text() == "Docket Description"

def test_set_crim_display_data(case_search_handler):
    case_data = MagicMock()
    case_data.defendant.first_name = "John"
    case_data.defendant.last_name = "Doe"
    case_data.case_number = "123"
    case_data.charges_list = [("Charge 1",), ("Charge 2",)]
    display_data = case_search_handler.set_crim_display_data(case_data)
    assert display_data == ("123", "State of Ohio v. John v. Doe", "Charge 1, Charge 2")


def test_set_civil_display_data(case_search_handler):
    case_data = MagicMock()
    case_data.primary_plaintiff.party_name = "John Smith"
    case_data.primary_defendant.party_name = "Jane Doe"
    case_data.case_number = "123"
    case_data.case_type = "Civil Case"
    display_data = case_search_handler.set_civil_display_data(case_data)
    assert display_data == ("123", "John Smith v. Jane Doe", "Civil Case")


def test_load_case_lists(case_list_handler):
    case_list_handler.load_case_lists()
    assert case_list_handler.daily_case_lists[0].clear.called
    assert case_list_handler.daily_case_lists[0].addItems.called
    assert case_list_handler.daily_case_lists[0].setHidden.called
    assert case_list_handler.daily_case_lists[0].setEnabled.called


def test_reload_case_lists(case_list_handler):
    case_list_handler.load_case_lists = MagicMock()
    case_list_handler.reload_case_lists()
    assert case_list_handler.load_case_lists.called
