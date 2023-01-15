"""Module for menu log processes."""
from os import startfile

from loguru import logger

from munientry.appsettings.paths import LOG_PATH
from munientry.logging_module import USER_LOG_NAME


def open_current_log(_signal=None) -> None:
    """Menu function that opens the user logs directly or with keyboard shortcut."""
    startfile(f'{LOG_PATH}{USER_LOG_NAME}')
    logger.info(f'Current system log opened.')
