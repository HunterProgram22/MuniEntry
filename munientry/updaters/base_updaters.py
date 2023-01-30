"""Base module that contains the base dialog updater."""
from loguru import logger


class BaseDialogUpdater(object):
    """Updater base class from which all Dialog Updaters inherit for setup."""

    def __init__(self, dialog) -> None:
        self.dialog = dialog
        self.model = dialog.entry_case_information


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
