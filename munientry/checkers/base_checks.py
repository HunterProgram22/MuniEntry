"""Base module for all checks."""
from functools import wraps
from typing import Any, Generator, Callable

from loguru import logger
from PyQt6.QtCore import QDate

from munientry.checkers.check_messages import ADD_CONDITIONS_MSG, ADD_CONDITIONS_TITLE
from munientry.widgets.message_boxes import FAIL, PASS, RequiredBox, WarningBox


def WarningCheck(title: str, message: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_result = func(*args, **kwargs)
            if func_result is False:
                msg_response = WarningBox(message, title).exec()
                func_result = func(*args, msg_response=msg_response, **kwargs)
            return func_result
        return wrapper
    return decorator


def RequiredCheck(title: str, message: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            func_result = func(*args, **kwargs)
            if func_result == False:
                RequiredBox(message, title).exec()
            return func_result
        return wrapper
    return decorator


def RequiredConditionCheck(func):
    @wraps(func)
    def wrapper(*args, **kwargs) -> bool:
        self, primary_condition, condition_name = args[:3]
        title = ADD_CONDITIONS_TITLE
        message = ADD_CONDITIONS_MSG.format(condition_name)
        func_result = func(*args, **kwargs)
        if func_result == False:
            RequiredBox(message, title).exec()
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
