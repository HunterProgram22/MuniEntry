"""This module provides handlers for the search_tab_widget."""
from __future__ import annotations

from collections import namedtuple
from typing import TYPE_CHECKING

from loguru import logger
from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt6.QtWidgets import QTableWidgetItem

from munientry.helper_functions import update_civil_case_number, update_crim_case_number
from munientry.sqlserver.civil_getters import CivilCaseData
from munientry.sqlserver.crim_getters import (
    CrimCaseData,
    CrimCaseDocket,
    get_daily_case_list,
)
from munientry.widgets.table_widgets import TableReportWindow

if TYPE_CHECKING:
    from munientry.widgets.combo_boxes import DailyCaseListComboBox


def add_cases_to_daily_case_list(cases: list[str], case_list: DailyCaseListComboBox) -> None:
    """Clears cases from existing case list and adds new cases for the day."""
    case_list.clear()
    case_list.addItems(cases)


class CaseDocketHandler(QObject):
    """Class for handling generation of case dockets."""
    docket_report_delivered = pyqtSignal(TableReportWindow)

    def __init__(self, mainwindow) -> None:
        super().__init__()
        self.mw = mainwindow
        self.mw.crim_case_docket_requested.connect(self.get_crim_case_docket)

    @pyqtSlot(str)
    def get_crim_case_docket(self, case_number: str) -> None:
        data_list = CrimCaseDocket(case_number).get_docket()
        self.create_docket_report(case_number, data_list)

    def create_docket_report(self, case_number: str, data_list: list[tuple]) -> None:
        rows = len(data_list)
        window_title = f'Docket Report for {case_number}'
        self.docket_report = TableReportWindow(window_title)
        self.create_table(rows, window_title)
        self.populate_table(data_list)
        self.docket_report_delivered.emit(self.docket_report)

    def create_table(self, rows: int, window_title: str) -> None:
        self.docket_report.table = self.docket_report.add_table(rows, 2, window_title, self.docket_report)
        header_labels = ['Date', 'Docket Description']
        self.docket_report.table.setHorizontalHeaderLabels(header_labels)

    def populate_table(self, data_list: list[tuple]) -> None:
        for row, docket_item in enumerate(data_list):
            docket_text = ' '.join(docket_item[1].splitlines())
            docket_text = docket_text.title()
            docket_date = QTableWidgetItem(docket_item[0])
            docket_text_container = QTableWidgetItem()
            docket_text_container.setText(docket_text)
            docket_text_container.setToolTip(docket_item[1])
            self.docket_report.table.setItem(row, 0, docket_date)
            self.docket_report.table.setItem(row, 1, docket_text_container)


class CaseSearchHandler(QObject):
    """Class for handling a case search for a case and querying the database for case data."""
    crim_case_data_delivered = pyqtSignal(tuple)
    civil_case_data_delivered = pyqtSignal(tuple)

    def __init__(self, mainwindow) -> None:
        super().__init__()
        self.mw = mainwindow
        self.mw.crim_case_data_requested.connect(self.query_crim_case_info)
        self.mw.civil_case_data_requested.connect(self.query_civil_case_info)

    @pyqtSlot(str)
    def query_crim_case_info(self, case_number: str) -> None:
        case_data = CrimCaseData(case_number).load_case()
        display_data = self.set_crim_display_data(case_data)
        self.crim_case_data_delivered.emit(display_data)

    @pyqtSlot(str)
    def query_civil_case_info(self, case_number: str) -> None:
        case_data = CivilCaseData(case_number).load_case()
        display_data = self.set_civil_display_data(case_data)
        self.civil_case_data_delivered.emit(display_data)

    def set_crim_display_data(self, case_data: CrimCaseData) -> tuple(str):
        def_first_name = case_data.defendant.first_name
        def_last_name = case_data.defendant.last_name
        case_number = case_data.case_number
        case_name = f'State of Ohio v. {def_first_name} v. {def_last_name}'
        case_charges = ', '.join(str(charge[0]) for charge in case_data.charges_list)
        return (case_number, case_name, case_charges)

    def set_civil_display_data(self, case_data: CivilCaseData) -> tuple(str):
        plaintiff = case_data.primary_plaintiff.party_name
        defendant = case_data.primary_defendant.party_name
        case_number = case_data.case_number
        case_name = f'{plaintiff} v. {defendant}'
        case_type = case_data.case_type
        return (case_number, case_name, case_type)


class CaseListHandler(QObject):
    """Class for loading Criminal Traffic Daily Case Lists."""

    def __init__(self, daily_case_lists: list) -> None:
        super().__init__()
        self.daily_case_lists = daily_case_lists
        self.load_case_lists()
        self.hide_daily_case_lists()

    def load_case_lists(self) -> None:
        for case_list in self.daily_case_lists:
            daily_cases = get_daily_case_list(case_list.objectName())
            add_cases_to_daily_case_list(daily_cases, case_list)
            preload_cases = str(len(case_list) - 1)
            postload_cases = str(len(daily_cases) - 1)
            logger.info(
                f'{case_list.name}: Preload Cases: {preload_cases};'
                + f' Postload Cases {postload_cases}',
            )

    def reload_case_lists(self) -> None:
        """This method is connected to the reload cases button and calls load_case_lists."""
        logger.info('Reload cases button pressed.')
        self.load_case_lists()

    def hide_daily_case_lists(self) -> None:
        for case_list in self.daily_case_lists:
            case_list.setCurrentText('')
            case_list.setHidden(True)
            case_list.setEnabled(False)
