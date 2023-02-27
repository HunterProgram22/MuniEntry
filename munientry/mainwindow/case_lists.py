"""The modules handles the functions of the daily cases lists for the application."""
from __future__ import annotations

from typing import TYPE_CHECKING

from loguru import logger

from munientry.sqlserver.crim_getters import get_daily_case_list

if TYPE_CHECKING:
    from munientry.widgets.combo_boxes import DailyCaseListComboBox


def add_cases_to_daily_case_list(cases: list[str], case_list: DailyCaseListComboBox) -> None:
    """Clears cases from existing case list and adds new cases for the day."""
    case_list.clear()
    case_list.addItems(cases)


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
