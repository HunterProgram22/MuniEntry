"""Checks for Probation Dialogs."""
from munientry.checkers.base_checks import BaseChecks


class ProbationBaseChecks(BaseChecks):
    """Class with all checks for Probation Dialogs."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.check_list = []
        self.check_status = self.perform_check_list()
