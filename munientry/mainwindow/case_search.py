"""This module provides handlers for the search_tab_widget."""
from __future__ import annotations

from loguru import logger
from munientry.helper_functions import update_civil_case_number, update_crim_case_number
from munientry.sqlserver.civil_getters import CivilCaseData
from munientry.sqlserver.crim_getters import CrimCaseData, get_daily_case_list
from munientry.widgets.combo_boxes import DailyCaseListComboBox


def add_cases_to_daily_case_list(cases: list[str], case_list: DailyCaseListComboBox) -> None:
    """Clears cases from existing case list and adds new cases for the day."""
    case_list.clear()
    case_list.addItems(cases)


class CaseSearchHandler(object):
    """Class for querying the SQL Server Databases and retreiving case data."""

    def __init__(self, mainwindow):
        self.mw = mainwindow

    def set_entries_tab(self) -> None:
        logger.action('Search Tab Changed')
        if self.mw.search_tabWidget.currentWidget().objectName() == 'civil_case_search_tab':
            self.mw.tabWidget.setCurrentWidget(self.mw.civil_Tab)

    def query_case_info(self) -> None:
        """Queries SQL Server database (AuthorityCourt/AuthorityCivil) and retrieves case data."""
        widget_name = self.mw.search_tabWidget.currentWidget().objectName()
        if widget_name == 'case_search_tab':
            search_box = self.mw.case_search_box
            case_data = CrimCaseData(update_crim_case_number(search_box.text())).load_case()
            self.set_crimtraffic_case_info_from_search(case_data)
        elif widget_name == 'civil_case_search_tab':
            search_box = self.mw.civil_case_search_box
            case_data = CivilCaseData(update_civil_case_number(search_box.text())).load_case()
            self.set_civil_case_info_from_search(case_data)
        search_box.setText(case_data.case_number)

    def set_crimtraffic_case_info_from_search(self, case_data: CrimCaseData) -> None:
        """Sets the case search fields on the UI with data from the case that is retrieved."""
        self.mw.case_number_label_field.setText(case_data.case_number)
        def_first_name = case_data.defendant.first_name
        def_last_name = case_data.defendant.last_name
        self.mw.case_name_label_field.setText(f'State of Ohio v. {def_first_name} {def_last_name}')
        charge_list_text = ', '.join(str(charge[0]) for charge in case_data.charges_list)
        self.mw.case_charges_label_field.setText(charge_list_text)

    def set_civil_case_info_from_search(self, case_data: CivilCaseData):
        """Sets the case search fields on the UI with data from the case that is retrieved."""
        plaintiff = case_data.primary_plaintiff.party_name
        defendant = case_data.primary_defendant.party_name
        self.mw.case_number_label_field.setText(case_data.case_number)
        self.mw.civil_case_number_field.setText(case_data.case_number)
        self.mw.civil_case_name_field.setText(f'{plaintiff} vs. {defendant}')
        self.mw.civil_case_type_field.setText(case_data.case_type)


class CaseListHandler(object):
    """Class for loading Criminal Traffic Daily Case Lists."""

    def __init__(self, mainwindow):
        self.mainwindow = mainwindow

    def load_case_lists(self) -> None:
        for case_list in self.mainwindow.daily_case_lists:
            daily_cases = get_daily_case_list(case_list.objectName())
            add_cases_to_daily_case_list(daily_cases, case_list)
            preload_cases = str(len(case_list) - 1)
            postload_cases = str(len(daily_cases) - 1)
            logger.info(
                f'{case_list.name}: Preload Cases: {preload_cases};'
                + f'Postload Cases {postload_cases}',
            )

    def reload_case_lists(self) -> None:
        """This method is connected to the reload cases button and calls load_case_lists."""
        logger.info('Reload cases button pressed.')
        self.load_case_lists()

    def show_hide_daily_case_lists(self) -> None:
        for case_list in self.mainwindow.daily_case_lists:
            case_list.setCurrentText('')
            case_list.setHidden(True)
            case_list.setEnabled(False)
