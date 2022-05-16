"""Module that contains case updaters for dialogs that do not have a charge grid."""

from package.updaters.base_updaters import CBD, BaseDialogUpdater
from package.updaters.general_updaters import CaseInformationUpdater


class NoPleaBondDialogUpdater(BaseDialogUpdater):
    """Updater for No Plea Bond Dialog - no charge grid."""

    def __init__(self, dialog: CBD) -> None:
        super().__init__(dialog)
        self.update_case_information()
        self.update_bond_conditions()

    def update_case_information(self) -> CaseInformationUpdater:
        return CaseInformationUpdater(self.dialog)

    def update_bond_conditions(self) -> None:
        self.dialog.transfer_view_data_to_model(self.model.bond_conditions)


class BondHearingDialogUpdater(BaseDialogUpdater):
    """Updater for Bond Hearing Dialog - no charge grid."""

    def __init__(self, dialog: CBD) -> None:
        super().__init__(dialog)
        self.update_case_information()
        self.update_bond_conditions()

    def update_case_information(self) -> CaseInformationUpdater:
        return CaseInformationUpdater(self.dialog)

    def update_bond_conditions(self) -> None:
        self.dialog.transfer_view_data_to_model(self.model.bond_conditions)


class FailureToAppearDialogUpdater(BaseDialogUpdater):
    """Updater for Failure To Appear Dialog - no charge grid."""

    def __init__(self, dialog: CBD) -> None:
        super().__init__(dialog)
        self.update_case_information()
        self.update_fta_conditions()

    def update_case_information(self) -> CaseInformationUpdater:
        return CaseInformationUpdater(self.dialog)

    def update_fta_conditions(self) -> None:
        self.dialog.transfer_view_data_to_model(self.model.fta_conditions)


class ProbationViolationBondDialogUpdater(BaseDialogUpdater):
    """Updater for Probation Violation Dialog - no charge grid."""

    def __init__(self, dialog: CBD) -> None:
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
