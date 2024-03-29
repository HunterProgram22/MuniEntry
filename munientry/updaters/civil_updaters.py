"""Module that contains case updaters for civil dialogs."""
from munientry.updaters.base_updaters import BaseDialogUpdater


class CivCaseInformationUpdater(BaseDialogUpdater):
    """Updates the model data with the case information fram (top frame on dialogs)."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.model.case_number = self.dialog.case_number_lineEdit.text()
        self.model.entry_date = self.dialog.entry_date.get_date_as_string()
        self.model.appearance_reason = self.dialog.appearance_reason_box.currentText()
        self.update_plaintiff()
        self.update_defendant()

    def update_plaintiff(self) -> None:
        self.model.plaintiff.party_name = self.dialog.plaintiff_lineEdit.text()

    def update_defendant(self) -> None:
        self.model.defendant.party_name = self.dialog.defendant_lineEdit.text()


class CivFreeformDialogUpdater(BaseDialogUpdater):

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.update_case_information()
        self.update_entry_content()

    def update_case_information(self) -> CivCaseInformationUpdater:
        return CivCaseInformationUpdater(self.dialog)

    def update_entry_content(self):
        self.model.entry_content_text = self.dialog.entry_content_textEdit.toPlainText()
