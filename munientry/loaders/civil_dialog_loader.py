"""Loader for CMS information for Civil cases."""
from __future__ import annotations

from munientry.sqlserver.civil_getters import CivilCaseSqlServer


def load_single_case(case_number: str) -> CivCmsCaseInformation:
    """Loads a single case into the CivCmsCaseInformation model.

    Args:
        case_number (str): A string of the case number to be loaded.

    Returns:
        CivCmsCaseInformation: An instance of a CivCmsCaseInformation object with data from a single case.
    """
    return CivilCaseSqlServer(case_number).load_case()


class CivilDialogLoader(object):
    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        self.dialog = self.load_dialog()

    def load_dialog(self):
        self.button_dict = self.mainwindow.dialog_buttons_dict
        return self._load_civil_dialog_process()

    def _get_cms_case_data(self):
        case_number = self.mainwindow.civil_case_search_box.text()
        return load_single_case(case_number)

    def _load_civil_dialog_process(self):
        judicial_officer = self.mainwindow.judicial_officer
        cms_case_data = self._get_cms_case_data()
        return self.button_dict.get(self.mainwindow.sender())(
            judicial_officer,
            cms_case=cms_case_data,
        )
