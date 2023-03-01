"""This module provides a CaseSearchHandler class that handles querying a SQL Server database."""
from munientry.helper_functions import update_civil_case_number, update_crim_case_number
from munientry.sqlserver.civil_getters import CivilCaseData
from munientry.sqlserver.crim_getters import CrimCaseData


class CaseSearchHandler(object):
    """Class for querying the SQL Server Databases and retreiving case data."""

    def __init__(self, mainwindow):
        self.mw = mainwindow

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
