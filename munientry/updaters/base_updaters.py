"""Base module that contains the base dialog updater."""


class BaseDialogUpdater(object):
    """Updater base class from which all Dialog Updaters inherit for setup."""

    def __init__(self, dialog) -> None:
        self.dialog = dialog
        self.model = dialog.entry_case_information


class BaseModelUpdater(object):
    """Base class for updating model data with data from the Dialog."""

    def __init__(self, dialog) -> None:
        self.dialog = dialog
        self.model = dialog.entry_case_information
        self.model.case_number = self.dialog.case_number_lineEdit.text()
        self.model.entry_date = self.dialog.entry_date.date().toString('MMMM dd, yyyy')

    def set_party_information(self) -> None:
        self.model.defendant.first_name = self.dialog.defendant_first_name_lineEdit.text()
        self.model.defendant.last_name = self.dialog.defendant_last_name_lineEdit.text()
