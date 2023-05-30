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
        self.model.sealing_type = self.dialog.sealing_type_box.currentText()
        self.model.seal_decision = self.dialog.seal_decision_box.currentText()
        self.model.state_response = self.dialog.state_response_box.currentText()
        self.model.denial_reasons = self.dialog.denial_reasons_text_box.toPlainText()
        self.model.bci_number = self.dialog.bci_number_line_edit.text()
        self.model.fbi_number = self.dialog.fbi_number_line_edit.text()
        self.model.offense_seal_list = self.dialog.offense_line_edit.text()
        self.model.offense_date = self.dialog.offense_date.get_date_as_string()


class CompetencyDialogUpdater(BaseDialogUpdater):
    """Updater for Competency Dialog - no charge grid."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.update_case_information()
        self.update_entry_content()

    def update_case_information(self) -> CaseInformationUpdater:
        return CaseInformationUpdater(self.dialog)

    def update_entry_content(self):
        self.model.competency_decision = self.dialog.competency_determination_box.currentText()
        self.model.jury_trial.date = self.dialog.trial_date.get_date_as_string()
        self.model.final_pretrial.date = self.dialog.final_pretrial_date.get_date_as_string()
        self.model.final_pretrial.time = self.dialog.final_pretrial_time_box.currentText()
        self.model.jury_trial.location = self.dialog.hearing_location_box.currentText()
        self.model.treatment_type = self.dialog.treatment_type_box.currentText()
        self.model.defendant_in_jail = self.dialog.in_jail_box.currentText()

