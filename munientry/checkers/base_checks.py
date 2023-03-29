"""Module containing common information checks used on multiple dialogs."""
from loguru import logger
from PyQt6.QtCore import QDate

from munientry.widgets.message_boxes import FAIL, PASS


class BaseChecks(object):
    """Class for initializing Checks for Dialogs."""

    conditions_list = []

    def __init__(self, dialog) -> None:
        self.dialog = dialog
        self.check_list: list = []
        self.today = QDate.currentDate()

    def perform_check_list(self) -> str:
        for check_method in self.check_list:
            if getattr(self, check_method)() == FAIL:
                logger.checkfail(check_method)
                return FAIL
        return PASS
