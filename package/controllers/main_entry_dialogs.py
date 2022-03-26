"""The module that contains the main classes for creating an entry dialog."""
from PyQt5.QtGui import QIntValidator
from PyQt5.QtSql import QSqlQuery

from db.databases import open_charges_db_connection
from package.controllers.base_dialogs import BaseDialog
from package.controllers.cms_case_loaders import CmsNoChargeLoader, CmsChargeLoader, CmsFraLoader
from package.controllers.case_updaters import (
    JailCCDialogCaseModelUpdater,
    FineOnlyDialogCaseModelUpdater,
    NotGuiltyBondDialogCaseModelUpdater,
    DiversionDialogCaseModelUpdater,
    ProbationViolationBondDialogCaseModelUpdater,
)
from package.controllers.conditions_dialogs import AddJailOnlyDialog
from package.controllers.signal_connectors import (
    DiversionDialogSignalConnector,
    JailCCDialogSignalConnector,
    FineOnlyDialogSignalConnector,
    NotGuiltyBondDialogSignalConnector,
    ProbationViolationBondDialogSignalConnector,
)
from package.controllers.slot_functions import (
    DiversionDialogSlotFunctions,
    JailCCDialogSlotFunctions,
    FineOnlyDialogSlotFunctions,
    NotGuiltyBondDialogSlotFunctions,
    ProbationViolationBondDialogSlotFunctions,
)
from package.controllers.view_modifiers import (
    DiversionDialogViewModifier,
    JailCCDialogViewModifier,
    FineOnlyDialogViewModifier,
    NotGuiltyBondDialogViewModifier,
    ProbationViolationBondDialogViewModifier,
    FailureToAppearDialogViewModifier,
)
from package.models.case_information import (
    BondConditions,
    CriminalCaseInformation,
    CommunityControlViolationBondConditions,
)
from package.models.template_types import TEMPLATE_DICT
from package.controllers.charges_grids import (
    JailChargesGrid,
    NoJailChargesGrid,
    NotGuiltyPleaGrid,
    DiversionChargesGrid,
)
from package.views.custom_widgets import DefenseCounselComboBox, NoScrollComboBox
from package.views.diversion_plea_dialog_ui import Ui_DiversionPleaDialog
from package.views.fine_only_plea_dialog_ui import Ui_FineOnlyPleaDialog
from package.views.jail_cc_plea_dialog_ui import Ui_JailCCPleaDialog
from package.views.not_guilty_bond_dialog_ui import Ui_NotGuiltyBondDialog
from package.views.probation_violation_bond_dialog_ui import Ui_ProbationViolationBondDialog
from package.views.failure_to_appear_dialog_ui import Ui_FailureToAppearDialog
from package.controllers.information_checkers import (
    FineOnlyDialogInfoChecker,
    NotGuiltyBondDialogInfoChecker,
    DiversionDialogInfoChecker,
    JailCCPleaDialogInfoChecker,
    ProbationViolationBondDialogInfoChecker,
)


class CriminalBaseDialog(BaseDialog):
    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
        self.case_table = case_table
        super().__init__(parent)
        self.judicial_officer = judicial_officer
        self.cms_case = cms_case
        self.entry_case_information = CriminalCaseInformation(self.judicial_officer)
        self.load_cms_data_to_view()
        self.defense_counsel_name_box.__class__ = DefenseCounselComboBox
        self.defense_counsel_name_box.load_attorneys()
        self.appearance_reason_box.__class__ = NoScrollComboBox
        self.defense_counsel_type_box.__class__ = NoScrollComboBox
        self.criminal_charge = None

    def load_cms_data_to_view(self):
        raise NotImplementedError

    def update_entry_case_information(self):
        raise NotImplementedError

    def perform_info_checks(self):
        raise NotImplementedError

    # TO BE REFACTORED #
    def add_charge_to_grid(self):
        self.charges_gridLayout.add_charge_only_to_grid(self)
        self.defense_counsel_name_box.setFocus()

    def start_jail_only_dialog(self):
        self.update_entry_case_information()
        AddJailOnlyDialog(self).exec()


class DiversionPleaDialog(CriminalBaseDialog, Ui_DiversionPleaDialog):
    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.dialog_name = "Diversion Plea Dialog"
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.entry_case_information.diversion.ordered = True

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
        return DiversionDialogCaseModelUpdater(self)

    def perform_info_checks(self):
        self.dialog_checks = DiversionDialogInfoChecker(self)


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

    def connect_signals_to_slots(self):
        return JailCCDialogSignalConnector(self)

    def load_cms_data_to_view(self):
        self.charges_gridLayout.__class__ = JailChargesGrid
        return CmsFraLoader(self)

    def update_entry_case_information(self):
        return JailCCDialogCaseModelUpdater(self)

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
        return FineOnlyDialogCaseModelUpdater(self)

    def perform_info_checks(self):
        self.dialog_checks = FineOnlyDialogInfoChecker(self)


class NotGuiltyBondDialog(CriminalBaseDialog, Ui_NotGuiltyBondDialog):
    condition_checkbox_list = [
        ("monitoring_checkBox", "monitoring_type_box"),
        ("specialized_docket_checkBox", "specialized_docket_type_box"),
    ]

    def __init__(self, judicial_officer, case=None, parent=None):
        super().__init__(judicial_officer, case, parent)
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

    def modify_view(self):
        return NotGuiltyBondDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = NotGuiltyBondDialogSlotFunctions(self)
        self.functions.hide_boxes()

    def connect_signals_to_slots(self):
        return NotGuiltyBondDialogSignalConnector(self)

    def load_cms_data_to_view(self):
        self.charges_gridLayout.__class__ = NotGuiltyPleaGrid
        return CmsChargeLoader(self)

    def update_entry_case_information(self):
        """Calls the dialog specific CaseModelUpdater in the case_updaters.py module."""
        return NotGuiltyBondDialogCaseModelUpdater(self)

    def add_charge_to_grid(self):
        self.charges_gridLayout.add_charge_only_to_grid(self)
        self.defense_counsel_name_box.setFocus()

    def perform_info_checks(self):
        self.dialog_checks = NotGuiltyBondDialogInfoChecker(self)


class ProbationViolationBondDialog(CriminalBaseDialog, Ui_ProbationViolationBondDialog):
    def __init__(self, judicial_officer, case=None, parent=None):
        super().__init__(judicial_officer, case, parent)
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
        return ProbationViolationBondDialogCaseModelUpdater(self)

    def perform_info_checks(self):
        self.dialog_checks = ProbationViolationBondDialogInfoChecker(self)


class FailureToAppearDialog(CriminalBaseDialog, Ui_FailureToAppearDialog):
    def __init__(self, judicial_officer, case=None, parent=None):
        super().__init__(judicial_officer, case, parent)
        self.dialog_name = "Failure To Appear Dialog"
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        # self.entry_case_information.bond_conditions = BondConditions()

    def modify_view(self):
        return FailureToAppearDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        pass

    #     self.functions = FailureToAppearDialogSlotFunctions(self)
    #     self.functions.hide_boxes()
    #
    def connect_signals_to_slots(self):
        pass

    #     return FailureToAppearDialogSignalConnector(self)
    #
    def load_cms_data_to_view(self):
        pass

    #     return CmsLoader(self)
    #
    def update_entry_case_information(self):
        pass

    #     return FailureToAppearDialogCaseUpdater(self)

    def perform_info_checks(self):
        pass

    #     self.dialog_checks = FailureToAppearDialogInfoChecker(self)


if __name__ == "__main__":
    charges_database = open_charges_db_connection()
else:
    charges_database = open_charges_db_connection()
