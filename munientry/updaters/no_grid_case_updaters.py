"""Module that contains case updaters for dialogs that do not have a charge grid."""
from loguru import logger

from munientry.updaters.base_updaters import BaseDialogUpdater
from munientry.updaters.general_updaters import CaseInformationUpdater


class NoPleaBondDialogUpdater(BaseDialogUpdater):
    """Updater for No Plea Bond Dialog - no charge grid."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.update_case_information()
        self.update_bond_conditions()

    def update_case_information(self) -> CaseInformationUpdater:
        return CaseInformationUpdater(self.dialog)

    def update_bond_conditions(self) -> None:
        self.dialog.transfer_view_data_to_model(self.model.bond_conditions)


class BondHearingDialogUpdater(BaseDialogUpdater):
    """Updater for Bond Hearing Dialog - no charge grid."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.update_case_information()
        self.update_bond_conditions()

    def update_case_information(self) -> CaseInformationUpdater:
        return CaseInformationUpdater(self.dialog)

    def update_bond_conditions(self) -> None:
        self.dialog.transfer_view_data_to_model(self.model.bond_conditions)


class FailureToAppearDialogUpdater(BaseDialogUpdater):
    """Updater for Failure To Appear Dialog - no charge grid."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.update_case_information()
        self.update_fta_conditions()

    def update_case_information(self) -> CaseInformationUpdater:
        return CaseInformationUpdater(self.dialog)

    def update_fta_conditions(self) -> None:
        self.dialog.transfer_view_data_to_model(self.model.fta_conditions)


class ArraignmentContinueDialogUpdater(BaseDialogUpdater):
    """Updater for Arraignment Continue Dialog - no charge grid."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.update_case_information()
        self.update_continuance_information()

    def update_case_information(self) -> CaseInformationUpdater:
        return CaseInformationUpdater(self.dialog)

    def update_continuance_information(self) -> None:
        self.dialog.transfer_view_data_to_model(self.model.continuance_conditions)


class ProbationViolationBondDialogUpdater(BaseDialogUpdater):
    """Updater for Probation Violation Dialog - no charge grid."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.update_case_information()
        self.update_model_with_probable_cause_information()
        self.update_bond_conditions()

    def update_case_information(self) -> CaseInformationUpdater:
        return CaseInformationUpdater(self.dialog)

    def update_model_with_probable_cause_information(self) -> None:
        self.model.cc_violation_probable_cause = (
            self.dialog.probable_cause_finding_box.currentText()
        )

    def update_bond_conditions(self) -> None:
        self.dialog.transfer_view_data_to_model(self.model.cc_bond_conditions)


class FreeformDialogUpdater(BaseDialogUpdater):
    """Updater for Freeform Dialog - no charge grid."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.update_case_information()
        self.update_entry_content()

    def update_case_information(self) -> CaseInformationUpdater:
        return CaseInformationUpdater(self.dialog)

    def update_entry_content(self):
        self.model.entry_content_text = self.dialog.entry_content_textEdit.toPlainText()


class CriminalSealingDialogUpdater(BaseDialogUpdater):
    """Updater for Criminal Sealing Dialog - no charge grid."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.update_case_information()
        self.update_entry_content()

    def update_case_information(self) -> CaseInformationUpdater:
        return CaseInformationUpdater(self.dialog)

    def update_entry_content(self):
        self.model.seal_decision = self.dialog.seal_decision_box.currentText()
        self.model.state_response = self.dialog.state_response_box.currentText()
        self.model.entry_content_text = self.dialog.entry_content_textEdit.toPlainText()
