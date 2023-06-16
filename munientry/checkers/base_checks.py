"""Base module for all checks."""
from functools import wraps
from typing import Callable, Generator

from loguru import logger
from PyQt6.QtCore import QDate

from munientry.checkers.check_messages import ADD_CONDITIONS_MSG, ADD_CONDITIONS_TITLE
from munientry.widgets.message_boxes import JailWarningBox, RequiredBox, WarningBox, \
    MinimumsQuestionBox


def warning_check(title: str, message: str) -> Callable:
    """Wraps a check function and displays a warning message if the check fails.

    The Warning Box allows a user to modify the data by responding with Yes or No and based on the
    response the data is updated and teh check is run again.

    Args:
        title (str): The title of the warning message box.
        message (str): The message to display in the warning message box.

    Returns:
        Callable: A decorator that wraps a check function.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_result = func(*args, **kwargs)
            if func_result is False:
                msg_response = WarningBox(message, title).exec()
                kwargs['msg_response'] = msg_response
                return func(*args, **kwargs)
            return func_result
        return wrapper
    return decorator


def min_charge_check(title: str, message: str) -> Callable:
    """Wraps a check function and displays a warning message if the check fails.

    The Warning Box allows a user to modify the data by responding with Yes or No and based on the
    response the data is updated and teh check is run again.

    Args:
        title (str): The title of the warning message box.
        message (str): The message to display in the warning message box.

    Returns:
        Callable: A decorator that wraps a check function.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_result = func(*args, **kwargs)
            if func_result is False:
                msg_response = MinimumsQuestionBox(message, title).exec()
                kwargs['msg_response'] = msg_response
                return func(*args, **kwargs)
            return func_result
        return wrapper
    return decorator


def jail_warning_check(title: str, message: str) -> Callable:
    """Wraps a check function and displays a warning message if the check fails.

    The Jail Warning Box allows a user to modify the data by responding with Yes or No and based on
    the response the data is updated and the check is run again.

    Args:
        title (str): The title of the warning message box.
        message (str): The message to display in the warning message box.

    Returns:
        Callable: A decorator that wraps a check function.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_result = func(*args, **kwargs)
            status, msg_insert = func_result
            if status is False:
                if msg_insert is not None:
                    formatted_msg = message.format(*msg_insert)
                else:
                    formatted_msg = message
                msg_response = JailWarningBox(formatted_msg, title).exec()
                kwargs['msg_response'] = msg_response
                return func(*args, **kwargs)
            return func_result
        return wrapper
    return decorator


def required_check(title: str, message: str) -> Callable:
    """Wraps a check function and displays a message that stops user from proceeding if check fails.

    Args:
        title (str):
            The title of the message box.
        message (str):
            The message to display in the message box. Use '{number_position}' to
            indicate where to insert additional information if a tuple is returned by the wrapped
            function.

    Returns:
        Callable: A decorator that wraps a check function. The wrapped function returns the status
            of the original check function.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            func_result = func(*args, **kwargs)
            if isinstance(func_result, tuple):
                status, msg_insert = func_result
            else:
                status = func_result
                msg_insert = None
            if status is False:
                if msg_insert is not None:
                    formatted_msg = message.format(*msg_insert)
                else:
                    formatted_msg = message
                RequiredBox(formatted_msg, title).exec()
            return status
        return wrapper
    return decorator


def required_condition_check(func):
    """Wraps a check and hard stops the user with a detailed message for the hard stop."""
    @wraps(func)
    def wrapper(*args, **kwargs) -> bool:
        func_result = func(*args, **kwargs)
        status, condition_name = func_result
        condition_name = condition_name[0]
        message = ADD_CONDITIONS_MSG.format(condition_name)
        if status is False:
            RequiredBox(message, ADD_CONDITIONS_TITLE).exec()
        return status
    return wrapper


def log_failed_checks(check_name: str) -> None:
    """Logs failed checks with warning."""
    logger.warning(f'{check_name} FAILED')


class BaseChecks(object):
    """Class for initializing Checks for Dialogs."""

    check_list: list = []

    def __init__(self, dialog) -> None:
        self.dialog = dialog
        self.today = QDate.currentDate()
        self.check_status = self.perform_check_list()

    def perform_check_list(self) -> bool:
        """Loops through a list of checks and logs checks that fail.

        The method is called prior to the entry creation process for a dialog. If any of the checks
        fail it will show a message and either abort the entry creation process returning False or
        show a message that allows the user to correct the failed check and return True.
        """
        check_results = self.run_checks()
        for check_name, check_result in check_results:
            if check_result is False:
                log_failed_checks(check_name)
                return False
        return True

    def run_checks(self) -> Generator[tuple[str, bool], None, None]:
        """Returns a Generator of bool (True or False) results for each check in the check_list."""
        return ((check_method, getattr(self, check_method)()) for check_method in self.check_list)
