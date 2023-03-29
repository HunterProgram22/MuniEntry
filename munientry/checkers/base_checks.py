"""Base module for all checks."""
from typing import Any, Generator, Callable

from loguru import logger
from PyQt6.QtCore import QDate

from munientry.widgets.message_boxes import FAIL, PASS, RequiredBox


class RequiredCheck(object):
    """Checks that hard stop the user if failed."""

    def __init__(self, title: str, message: str) -> None:
        self.title = title
        self.message = message

    def __call__(self, func: Callable) -> Callable:
        """Returns False if a check fails and hard stops the user with a message about the error."""
        def wrapper(*args, **kwargs) -> str:
            func_result = func(*args, **kwargs)
            if func_result == False:
                RequiredBox(self.message, self.title).exec()
            return func_result
        return wrapper


class BaseChecks(object):
    """Class for initializing Checks for Dialogs."""

    check_list: list = []

    def __init__(self, dialog) -> None:
        self.dialog = dialog
        self.today = QDate.currentDate()
        self.check_status = self.perform_check_list()

    def perform_check_list(self) -> str:
        """Loops through a list of checks and logs checks that fail.

        The method is called prior to the entry creation process for a dialog. If any of the checks
        fail it will show a message and either abort the entry creation process by returning FAIL or
        show a message that allows the user to correct the failed check.

        TODO: check result in (True, FAIL) should be temporary for refactor only.
        """
        check_results = self.run_checks()
        for check_name, check_result in check_results:
            if check_result in (False, FAIL):
                self.log_failed_checks(check_name)
                return FAIL
        return PASS

    def run_checks(self) -> Generator[tuple[str, Any], None, None]:
        """Returns a list of results of PASS or FAIL for each check in the check_list."""
        return ((check_method, getattr(self, check_method)()) for check_method in self.check_list)

    def log_failed_checks(self, check_name: str) -> None:
        """Logs failed checks with warning."""
        logger.warning(f'{check_name} FAILED')
