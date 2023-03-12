"""Module containing common information checks used on multiple dialogs."""
from loguru import logger
from munientry.checkers.base_checks import BaseChecker


class ProbationDialogInfoChecker(BaseChecker):
    """Class with all checks for Probation Dialogs."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.dialog_check_list = [
        ]
        self.check_status = self.perform_check_list()
