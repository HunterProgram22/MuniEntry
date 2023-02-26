"""This module contains tests for searching for criminal and civil cases in a main window."""
import pytest

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
    main_window.search_tabWidget.setCurrentWidget(main_window.case_search_tab)
    enter_data(main_window.case_search_box, case_number)

    # Perform the search and assert the results
    mouse_click(main_window.get_case_Button)
    assert main_window.case_search_box.text() == expected_output
    assert main_window.case_number_label_field.text() == expected_output


@pytest.mark.parametrize('case_number, expected_output', CIVIL_TEST_CASES)
def test_civil_case_search(main_window, case_number, expected_output):
    """Test for searching by a civil case number."""
    # Set up the main window for civil case search
    main_window.search_tabWidget.setCurrentWidget(main_window.civil_case_search_tab)
    enter_data(main_window.civil_case_search_box, case_number)

    # Perform the search and assert the results
    mouse_click(main_window.civil_get_case_Button)
    assert main_window.civil_case_search_box.text() == expected_output
    assert main_window.civil_case_number_field.text() == expected_output
