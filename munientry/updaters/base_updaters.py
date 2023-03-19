"""Base module that contains the base dialog updater."""


class BaseDialogUpdater(object):
    """Updater base class for Crim from which all Dialog Updaters inherit for setup."""

    def __init__(self, dialog) -> None:
        self.dialog = dialog
        self.model = dialog.entry_case_information
