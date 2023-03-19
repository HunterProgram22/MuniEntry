"""This module provides functions for working with user log files in the Munientry application."""
from os import path, startfile

from loguru import logger

from munientry.settings.paths import LOG_PATH
from munientry.logging_module import USER_LOG_NAME


def open_user_log_file() -> None:
    """Opens the user log file in the default system text editor.

    Keyboard shortcut is set to 'Ctrl-L' in mainwindow/shortcuts.py.
    """
    startfile(path.join(LOG_PATH, USER_LOG_NAME))
    logger.info('Current system log opened.')
