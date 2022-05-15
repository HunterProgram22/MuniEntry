"""Base module that contains the base dialog updater and base TypeVar for mypy checks."""

from typing import TypeVar

from package.controllers.base_dialogs import CriminalBaseDialog

CBD = TypeVar('CBD', bound=CriminalBaseDialog)


class BaseDialogUpdater(object):
    """Updater base class from which all Dialog Updaters inherit for setup."""

    def __init__(self, dialog: CBD) -> None:
        self.dialog = dialog
        self.model = dialog.entry_case_information
