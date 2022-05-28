"""The module that contains the main classes for creating an entry dialog."""
from PyQt5.QtGui import QIntValidator

from package.controllers.base_dialogs import CriminalBaseDialog
from package.controllers.cms_case_loaders import CmsNoChargeLoader, CmsChargeLoader, CmsFraLoader
from package.updaters.grid_case_updaters import (
    JailCCDialogUpdater,
    FineOnlyDialogUpdater,
    NotGuiltyBondDialogUpdater,
    DiversionDialogUpdater,
    PleaOnlyDialogUpdater,
    LeapAdmissionPleaDialogUpdater,
)
from package.updaters.no_grid_case_updaters import NoPleaBondDialogUpdater, \
    BondHearingDialogUpdater, FailureToAppearDialogUpdater, \
    ProbationViolationBondDialogUpdater
from package.controllers.signal_connectors import (
    DiversionDialogSignalConnector,
    JailCCDialogSignalConnector,
    FineOnlyDialogSignalConnector,
    NotGuiltyBondDialogSignalConnector,
    NoPleaBondDialogSignalConnector,
    ProbationViolationBondDialogSignalConnector,
    FailureToAppearDialogSignalConnector,
    BondHearingDialogSignalConnector,
    PleaOnlyDialogSignalConnector,
    LeapAdmissionPleaDialogSignalConnector,
)
from package.controllers.slot_functions import (
    DiversionDialogSlotFunctions,
    JailCCDialogSlotFunctions,
    FineOnlyDialogSlotFunctions,
    NotGuiltyBondDialogSlotFunctions,
    NoPleaBondDialogSlotFunctions,
    ProbationViolationBondDialogSlotFunctions,
    FailureToAppearDialogSlotFunctions,
    BondHearingDialogSlotFunctions,
    PleaOnlyDialogSlotFunctions,
    LeapAdmissionPleaDialogSlotFunctions,
)
from package.controllers.view_modifiers import (
    DiversionDialogViewModifier,
    JailCCDialogViewModifier,
    FineOnlyDialogViewModifier,
    NotGuiltyBondDialogViewModifier,
    NoPleaBondDialogViewModifier,
    ProbationViolationBondDialogViewModifier,
    FailureToAppearDialogViewModifier,
    BondHearingDialogViewModifier,
    PleaOnlyDialogViewModifier,
    LeapAdmissionPleaDialogViewModifier,
    LeapSentencingDialogViewModifier,
)
from package.controllers.information_checkers import (
    FineOnlyDialogInfoChecker,
    NotGuiltyBondDialogInfoChecker,
    NoPleaBondDialogInfoChecker,
    DiversionDialogInfoChecker,
    JailCCPleaDialogInfoChecker,
    ProbationViolationBondDialogInfoChecker,
    FailureToAppearDialogInfoChecker,
    BondHearingDialogInfoChecker,
    PleaOnlyDialogInfoChecker,
    LeapAdmissionPleaDialogInfoChecker,
)
from package.models.case_information import (
    BondConditions,
    BondModificationConditions,
    CommunityControlViolationBondConditions,
    FailureToAppearConditions,
)
from package.models.template_types import TEMPLATE_DICT
from package.controllers.charges_grids import (
    JailChargesGrid,
    PleaOnlyGrid,
    LeapAdmissionPleaGrid,
    NoJailChargesGrid,
    NotGuiltyPleaGrid,
    DiversionChargesGrid,
)
from package.views.diversion_plea_dialog_ui import Ui_DiversionPleaDialog
from package.views.fine_only_plea_dialog_ui import Ui_FineOnlyPleaDialog
from package.views.jail_cc_plea_dialog_ui import Ui_JailCCPleaDialog
from package.views.not_guilty_bond_dialog_ui import Ui_NotGuiltyBondDialog
from package.views.no_plea_bond_dialog_ui import Ui_NoPleaBondDialog
from package.views.probation_violation_bond_dialog_ui import Ui_ProbationViolationBondDialog
from package.views.failure_to_appear_dialog_ui import Ui_FailureToAppearDialog
from package.views.plea_only_dialog_ui import Ui_PleaOnlyDialog
from package.views.bond_hearing_dialog_ui import Ui_BondHearingDialog
from package.views.leap_admission_plea_dialog_ui import Ui_LeapAdmissionPleaDialog
from package.views.leap_sentencing_dialog_ui import Ui_LeapSentencingDialog


class DiversionPleaDialog(CriminalBaseDialog, Ui_DiversionPleaDialog):
    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.dialog_name = "Diversion Plea Dialog"
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.entry_case_information.diversion.ordered = True
        self.functions.show_restitution_boxes()

    def modify_view(self):
        return DiversionDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = DiversionDialogSlotFunctions(self)
        self.functions.show_jail_report_date_box()
        self.functions.show_other_conditions_box()

    def connect_signals_to_slots(self):
        return DiversionDialogSignalConnector(self)

    def load_cms_data_to_view(self):
        self.charges_gridLayout.__class__ = DiversionChargesGrid
        return CmsFraLoader(self)

    def update_entry_case_information(self):
        return DiversionDialogUpdater(self)

    def perform_info_checks(self):
        self.dialog_checks = DiversionDialogInfoChecker(self)


class PleaOnlyDialog(CriminalBaseDialog, Ui_PleaOnlyDialog):
    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.dialog_name = "Plea Only Dialog"
        self.template = TEMPLATE_DICT.get(self.dialog_name)

    def modify_view(self):
        return PleaOnlyDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = PleaOnlyDialogSlotFunctions(self)

    def connect_signals_to_slots(self):
        return PleaOnlyDialogSignalConnector(self)

    def load_cms_data_to_view(self):
        self.charges_gridLayout.__class__ = PleaOnlyGrid
        return CmsChargeLoader(self)

    def update_entry_case_information(self):
        return PleaOnlyDialogUpdater(self)

    def perform_info_checks(self):
        self.dialog_checks = PleaOnlyDialogInfoChecker(self)


class JailCCPleaDialog(CriminalBaseDialog, Ui_JailCCPleaDialog):
    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.validator = QIntValidator(0, 1000, self)
        self.jail_time_credit_box.setValidator(self.validator)
        self.additional_conditions_list = [
            ("community_control_checkBox", self.entry_case_information.community_control),
            ("license_suspension_checkBox", self.entry_case_information.license_suspension),
            ("community_service_checkBox", self.entry_case_information.community_service),
            ("other_conditions_checkBox", self.entry_case_information.other_conditions),
            ("jail_checkBox", self.entry_case_information.jail_terms),
            ("impoundment_checkBox", self.entry_case_information.impoundment),
            ("victim_notification_checkBox", self.entry_case_information.victim_notification),
        ]
        self.dialog_name = "Jail CC Plea Dialog"
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        if self.case_table == "slated":
            self.in_jail_box.setCurrentText("Yes")

    def modify_view(self):
        return JailCCDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = JailCCDialogSlotFunctions(self)
        self.functions.show_companion_case_fields()

    def connect_signals_to_slots(self):
        return JailCCDialogSignalConnector(self)

    def load_cms_data_to_view(self):
        self.charges_gridLayout.__class__ = JailChargesGrid
        return CmsFraLoader(self)

    def update_entry_case_information(self):
        return JailCCDialogUpdater(self)

    def perform_info_checks(self):
        self.dialog_checks = JailCCPleaDialogInfoChecker(self)


class FineOnlyPleaDialog(CriminalBaseDialog, Ui_FineOnlyPleaDialog):
    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.additional_conditions_list = [
            ("license_suspension_checkBox", self.entry_case_information.license_suspension),
            ("community_service_checkBox", self.entry_case_information.community_service),
            ("other_conditions_checkBox", self.entry_case_information.other_conditions),
        ]
        self.dialog_name = "Fine Only Plea Dialog"
        self.template = TEMPLATE_DICT.get(self.dialog_name)

    def modify_view(self):
        return FineOnlyDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = FineOnlyDialogSlotFunctions(self)
        self.functions.set_fines_credit_for_jail_field()

    def connect_signals_to_slots(self):
        return FineOnlyDialogSignalConnector(self)

    def load_cms_data_to_view(self):
        self.charges_gridLayout.__class__ = NoJailChargesGrid
        return CmsFraLoader(self)

    def update_entry_case_information(self):
        return FineOnlyDialogUpdater(self)

    def perform_info_checks(self):
        self.dialog_checks = FineOnlyDialogInfoChecker(self)


class LeapSentencingDialog(CriminalBaseDialog, Ui_LeapSentencingDialog):
    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.additional_conditions_list = [
            ("license_suspension_checkBox", self.entry_case_information.license_suspension),
            ("community_service_checkBox", self.entry_case_information.community_service),
            ("other_conditions_checkBox", self.entry_case_information.other_conditions),
        ]
        self.dialog_name = "Leap Sentencing Dialog"
        self.template = TEMPLATE_DICT.get(self.dialog_name)

    def modify_view(self):
        return LeapSentencingDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = FineOnlyDialogSlotFunctions(self)
        self.functions.set_fines_credit_for_jail_field()

    def connect_signals_to_slots(self):
        return FineOnlyDialogSignalConnector(self)

    def load_cms_data_to_view(self):
        self.charges_gridLayout.__class__ = NoJailChargesGrid
        return CmsFraLoader(self)

    def update_entry_case_information(self):
        return FineOnlyDialogUpdater(self)

    def perform_info_checks(self):
        self.dialog_checks = FineOnlyDialogInfoChecker(self)


class NotGuiltyBondDialog(CriminalBaseDialog, Ui_NotGuiltyBondDialog):
    condition_checkbox_dict = {
        "monitoring_checkBox": ["monitoring_type_box"],
        "specialized_docket_checkBox": ["specialized_docket_type_box"],
    }

    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
        super().__init__(judicial_officer, cms_case, parent)
        self.additional_conditions_list = [
            (
                "admin_license_suspension_checkBox",
                self.entry_case_information.admin_license_suspension,
            ),
            (
                "domestic_violence_checkBox",
                self.entry_case_information.domestic_violence_conditions,
            ),
            ("no_contact_checkBox", self.entry_case_information.no_contact),
            ("custodial_supervision_checkBox", self.entry_case_information.custodial_supervision),
            ("other_conditions_checkBox", self.entry_case_information.other_conditions),
            ("vehicle_seizure_checkBox", self.entry_case_information.vehicle_seizure),
        ]
        self.dialog_name = "Not Guilty Bond Dialog"
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.entry_case_information.bond_conditions = BondConditions()
        self.set_all_pleas_to_not_guilty()

    def set_all_pleas_to_not_guilty(self):
        """Sets all pleas to not guilty at load just like hitting not guilty all button."""
        for column in range(1, self.charges_gridLayout.columnCount()):
            if (
                self.charges_gridLayout.itemAtPosition(self.charges_gridLayout.row_offense, column)
                is not None
            ):
                self.charges_gridLayout.itemAtPosition(
                    self.charges_gridLayout.row_plea, column
                ).widget().setCurrentText("Not Guilty")

    def modify_view(self):
        return NotGuiltyBondDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = NotGuiltyBondDialogSlotFunctions(self)

    def connect_signals_to_slots(self):
        return NotGuiltyBondDialogSignalConnector(self)

    def load_cms_data_to_view(self):
        self.charges_gridLayout.__class__ = NotGuiltyPleaGrid
        return CmsChargeLoader(self)

    def update_entry_case_information(self):
        """Calls the dialog specific CaseModelUpdater in the grid_case_updaters.py module."""
        return NotGuiltyBondDialogUpdater(self)

    def add_charge_to_grid(self):
        self.charges_gridLayout.add_charge_only_to_grid(self)
        self.defense_counsel_name_box.setFocus()

    def perform_info_checks(self):
        self.dialog_checks = NotGuiltyBondDialogInfoChecker(self)


class NoPleaBondDialog(CriminalBaseDialog, Ui_NoPleaBondDialog):
    condition_checkbox_dict = {
        "monitoring_checkBox": ["monitoring_type_box"],
        "specialized_docket_checkBox": ["specialized_docket_type_box"],
    }

    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
        super().__init__(judicial_officer, cms_case, parent)
        self.additional_conditions_list = [
            (
                "admin_license_suspension_checkBox",
                self.entry_case_information.admin_license_suspension,
            ),
            (
                "domestic_violence_checkBox",
                self.entry_case_information.domestic_violence_conditions,
            ),
            ("no_contact_checkBox", self.entry_case_information.no_contact),
            ("custodial_supervision_checkBox", self.entry_case_information.custodial_supervision),
            ("other_conditions_checkBox", self.entry_case_information.other_conditions),
            ("vehicle_seizure_checkBox", self.entry_case_information.vehicle_seizure),
        ]
        self.dialog_name = "No Plea Bond Dialog"
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.entry_case_information.bond_conditions = BondConditions()

    def modify_view(self):
        return NoPleaBondDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = NoPleaBondDialogSlotFunctions(self)

    def connect_signals_to_slots(self):
        return NoPleaBondDialogSignalConnector(self)

    def update_entry_case_information(self):
        """Calls the dialog specific CaseModelUpdater in the grid_case_updaters.py module."""
        return NoPleaBondDialogUpdater(self)

    def load_cms_data_to_view(self):
        return CmsNoChargeLoader(self)

    def perform_info_checks(self):
        self.dialog_checks = NoPleaBondDialogInfoChecker(self)


class ProbationViolationBondDialog(CriminalBaseDialog, Ui_ProbationViolationBondDialog):
    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
        super().__init__(judicial_officer, cms_case, parent)
        self.dialog_name = "Probation Violation Bond Dialog"
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.entry_case_information.bond_conditions = CommunityControlViolationBondConditions()

    def modify_view(self):
        return ProbationViolationBondDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = ProbationViolationBondDialogSlotFunctions(self)
        self.functions.hide_bond_conditions()

    def connect_signals_to_slots(self):
        return ProbationViolationBondDialogSignalConnector(self)

    def load_cms_data_to_view(self):
        return CmsNoChargeLoader(self)

    def update_entry_case_information(self):
        return ProbationViolationBondDialogUpdater(self)

    def perform_info_checks(self):
        self.dialog_checks = ProbationViolationBondDialogInfoChecker(self)


class FailureToAppearDialog(CriminalBaseDialog, Ui_FailureToAppearDialog):
    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
        super().__init__(judicial_officer, cms_case, parent)
        self.dialog_name = "Failure To Appear Dialog"
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.entry_case_information.fta_conditions = FailureToAppearConditions()
        if (
            self.case_table == "final_pretrials"
        ):  # Ovverides the set_appearance_reason in ViewModifier
            self.appearance_reason_box.setCurrentText("final pre-trial")

    def modify_view(self):
        return FailureToAppearDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = FailureToAppearDialogSlotFunctions(self)
        self.functions.hide_warrant_radius()
        self.functions.hide_bond_boxes()

    def connect_signals_to_slots(self):
        return FailureToAppearDialogSignalConnector(self)

    def load_cms_data_to_view(self):
        return CmsNoChargeLoader(self)

    def update_entry_case_information(self):
        return FailureToAppearDialogUpdater(self)

    def perform_info_checks(self):
        self.dialog_checks = FailureToAppearDialogInfoChecker(self)


class BondHearingDialog(CriminalBaseDialog, Ui_BondHearingDialog):
    condition_checkbox_dict = {
        "monitoring_checkBox": ["monitoring_type_box"],
        "specialized_docket_checkBox": ["specialized_docket_type_box"],
    }

    def __init__(
        self,
        judicial_officer: object,
        cms_case: str = None,
        case_table: str = None,
        parent: object = None,
    ) -> None:
        super().__init__(judicial_officer, cms_case, parent)
        self.additional_conditions_list = [
            (
                "admin_license_suspension_checkBox",
                self.entry_case_information.admin_license_suspension,
            ),
            (
                "domestic_violence_checkBox",
                self.entry_case_information.domestic_violence_conditions,
            ),
            ("no_contact_checkBox", self.entry_case_information.no_contact),
            ("custodial_supervision_checkBox", self.entry_case_information.custodial_supervision),
            ("other_conditions_checkBox", self.entry_case_information.other_conditions),
            ("vehicle_seizure_checkBox", self.entry_case_information.vehicle_seizure),
        ]
        self.dialog_name = "Bond Hearing Dialog"
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.entry_case_information.bond_conditions = BondModificationConditions()

    def modify_view(self) -> BondHearingDialogViewModifier:
        return BondHearingDialogViewModifier(self)

    def create_dialog_slot_functions(self) -> None:
        self.functions = BondHearingDialogSlotFunctions(self)

    def connect_signals_to_slots(self) -> BondHearingDialogSignalConnector:
        return BondHearingDialogSignalConnector(self)

    def load_cms_data_to_view(self) -> CmsNoChargeLoader:
        return CmsNoChargeLoader(self)

    def update_entry_case_information(self) -> BondHearingDialogUpdater:
        """Calls the dialog specific CaseModelUpdater in the grid_case_updaters.py module."""
        return BondHearingDialogUpdater(self)

    def perform_info_checks(self) -> None:
        self.dialog_checks = BondHearingDialogInfoChecker(self)


class LeapAdmissionPleaDialog(CriminalBaseDialog, Ui_LeapAdmissionPleaDialog):
    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.dialog_name = "Leap Admission Plea Dialog"
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.functions.set_leap_sentencing_date("120 days")

    def modify_view(self) -> LeapAdmissionPleaDialogViewModifier:
        return LeapAdmissionPleaDialogViewModifier(self)

    def create_dialog_slot_functions(self) -> None:
        self.functions = LeapAdmissionPleaDialogSlotFunctions(self)

    def connect_signals_to_slots(self) -> LeapAdmissionPleaDialogSignalConnector:
        return LeapAdmissionPleaDialogSignalConnector(self)

    def load_cms_data_to_view(self) -> CmsChargeLoader:
        self.charges_gridLayout.__class__ = LeapAdmissionPleaGrid
        return CmsChargeLoader(self)

    def update_entry_case_information(self) -> LeapAdmissionPleaDialogUpdater:
        return LeapAdmissionPleaDialogUpdater(self)

    def perform_info_checks(self) -> LeapAdmissionPleaDialogInfoChecker:
        self.dialog_checks = LeapAdmissionPleaDialogInfoChecker(self)


if __name__ == "__main__":
    # charges_database = open_charges_db_connection()
    pass
else:
    # charges_database = open_charges_db_connection()
    pass
