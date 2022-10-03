"""Base module that contains the base dialog updater and base TypeVar for mypy checks."""
from loguru import logger
from typing import TypeVar


class BaseDialogUpdater(object):
    """Updater base class from which all Dialog Updaters inherit for setup."""

    def __init__(self, dialog) -> None:
        self.dialog = dialog
        self.model = dialog.entry_case_information


if __name__ == "__main__":
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
