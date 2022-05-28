"""Module that contains case updaters for dialogs that have a charge grid."""

from package.updaters.base_updaters import CBD, BaseDialogUpdater
from package.updaters.charge_grid_updaters import (
    DiversionGridModelUpdater,
    FineOnlyGridModelUpdater,
    JailCCGridModelUpdater,
    NotGuiltyGridModelUpdater,
    PleaOnlyGridModelUpdater,
    LeapAdmissionPleaGridModelUpdater,
)
from package.updaters.general_updaters import (
    CaseInformationUpdater,
    CourtCostsUpdater,
    FinesUpdater,
    JailDataUpdater,
)


class DiversionDialogUpdater(BaseDialogUpdater):
    """Updater for Diversion Dialog - contains a charge grid."""

    def __init__(self, dialog: CBD) -> None:
        super().__init__(dialog)
        self.update_case_information()
        self.update_diversion_information()
        self.update_model_with_charge_grid_data()

    def update_case_information(self) -> CaseInformationUpdater:
        return CaseInformationUpdater(self.dialog)

    def update_diversion_information(self) -> None:
        self.dialog.transfer_view_data_to_model(self.model.diversion)
        self.model.diversion.program_name = self.model.diversion.get_program_name()
        self.dialog.transfer_view_data_to_model(self.model.other_conditions)

    def update_model_with_charge_grid_data(self) -> DiversionGridModelUpdater:
        return DiversionGridModelUpdater(self.dialog)


class JailCCDialogUpdater(BaseDialogUpdater):
    """Updater for Jail and Comm. Control Dialog - contains a charge grid."""

    def __init__(self, dialog: CBD) -> None:
        super().__init__(dialog)
        self.update_case_information()
        self.update_model_with_charge_grid_data()
        self.update_court_costs()
        self.update_fines()
        self.update_jail_data()

    def update_case_information(self) -> CaseInformationUpdater:
        self.model.victim_statements = self.dialog.victim_statements_checkBox.isChecked()
        self.model.offense_of_violence = self.dialog.offense_of_violence_checkBox.isChecked()
        return CaseInformationUpdater(self.dialog)

    def update_model_with_charge_grid_data(self) -> JailCCGridModelUpdater:
        return JailCCGridModelUpdater(self.dialog)

    def update_court_costs(self) -> CourtCostsUpdater:
        return CourtCostsUpdater(self.dialog)

    def update_fines(self) -> FinesUpdater:
        return FinesUpdater(self.dialog)

    def update_jail_data(self) -> JailDataUpdater:
        return JailDataUpdater(self.dialog)


class FineOnlyDialogUpdater(BaseDialogUpdater):
    """Updater for Fine Only Dialog - contains a charge grid."""

    def __init__(self, dialog: CBD) -> None:
        super().__init__(dialog)
        self.update_case_information()
        self.update_model_with_charge_grid_data()
        self.update_court_costs()
        self.update_fines()
        self.update_jail_time_credit_for_fines()

    def update_case_information(self) -> CaseInformationUpdater:
        return CaseInformationUpdater(self.dialog)

    def update_model_with_charge_grid_data(self) -> FineOnlyGridModelUpdater:
        return FineOnlyGridModelUpdater(self.dialog)

    def update_court_costs(self) -> CourtCostsUpdater:
        return CourtCostsUpdater(self.dialog)

    def update_fines(self) -> FinesUpdater:
        return FinesUpdater(self.dialog)

    def update_jail_time_credit_for_fines(self) -> None:
        self.model.fines_and_costs_jail_credit = self.dialog.credit_for_jail_checkBox.isChecked()
        self.model.fine_jail_days = self.dialog.jail_time_credit_box.text()


class LeapSentencingDialogUpdater(BaseDialogUpdater):
    """Updater for Leap Sentencing Dialog - contains a charge grid."""

    def __init__(self, dialog: CBD) -> None:
        super().__init__(dialog)
        self.update_case_information()
        self.update_model_with_charge_grid_data()
        self.update_court_costs()
        self.update_fines()
        self.update_jail_time_credit_for_fines()
        self.update_leap_plea_date()

    def update_case_information(self) -> CaseInformationUpdater:
        return CaseInformationUpdater(self.dialog)

    def update_model_with_charge_grid_data(self) -> FineOnlyGridModelUpdater:
        return FineOnlyGridModelUpdater(self.dialog)

    def update_court_costs(self) -> CourtCostsUpdater:
        return CourtCostsUpdater(self.dialog)

    def update_fines(self) -> FinesUpdater:
        return FinesUpdater(self.dialog)

    def update_jail_time_credit_for_fines(self) -> None:
        self.model.fines_and_costs_jail_credit = self.dialog.credit_for_jail_checkBox.isChecked()
        self.model.fine_jail_days = self.dialog.jail_time_credit_box.text()

    def update_leap_plea_date(self):
        self.model.leap_plea_date = self.dialog.leap_plea_date.get_date()


class LeapAdmissionPleaDialogUpdater(BaseDialogUpdater):
    """Updater for LEAP Admission Plea Dialog - contains a charge grid."""

    def __init__(self, dialog: CBD) -> None:
        super().__init__(dialog)
        self.update_case_information()
        self.update_model_with_charge_grid_data()
        self.model.leap_sentencing_date = self.dialog.sentencing_date.get_date()

    def update_case_information(self) -> CaseInformationUpdater:
        return CaseInformationUpdater(self.dialog)

    def update_model_with_charge_grid_data(self) -> LeapAdmissionPleaGridModelUpdater:
        return LeapAdmissionPleaGridModelUpdater(self.dialog)


class PleaOnlyDialogUpdater(BaseDialogUpdater):
    """Updater for Plea Only Dialog - contains a charge grid."""

    def __init__(self, dialog: CBD) -> None:
        super().__init__(dialog)
        self.update_case_information()
        self.update_model_with_charge_grid_data()
        self.update_model_with_future_sentencing_and_bond()

    def update_case_information(self) -> CaseInformationUpdater:
        return CaseInformationUpdater(self.dialog)

    def update_model_with_charge_grid_data(self) -> PleaOnlyGridModelUpdater:
        return PleaOnlyGridModelUpdater(self.dialog)

    def update_model_with_future_sentencing_and_bond(self) -> None:
        self.dialog.transfer_view_data_to_model(self.model.future_sentencing)


class NotGuiltyBondDialogUpdater(BaseDialogUpdater):
    """Updater for Not Guilty Bond Dialog - contains a charge grid."""

    def __init__(self, dialog: CBD) -> None:
        super().__init__(dialog)
        self.update_case_information()
        self.update_model_with_charge_grid_data()
        self.update_bond_conditions()

    def update_case_information(self) -> CaseInformationUpdater:
        return CaseInformationUpdater(self.dialog)

    def update_model_with_charge_grid_data(self) -> NotGuiltyGridModelUpdater:
        return NotGuiltyGridModelUpdater(self.dialog)

    def update_bond_conditions(self) -> None:
        self.dialog.transfer_view_data_to_model(self.model.bond_conditions)
