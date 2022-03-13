from PyQt5.QtGui import QIntValidator
from loguru import logger
from package.controllers.base_dialogs import CasePartyUpdater, CriminalBaseDialog
from package.controllers.not_guilty_bond_dialogs import NotGuiltyAddPlea
from package.controllers.sentencing_dialogs import CriminalSentencingDialog, JailAddPleaFindingsFinesJail, \
    NoJailPleaFindingFines
from package.controllers.signal_connectors import DiversionDialogSignalConnector, JailCCDialogSignalConnector, \
    FineOnlyDialogSignalConnector, NotGuiltyBondDialogSignalConnector
from package.controllers.slot_functions import DiversionDialogSlotFunctions, JailCCDialogSlotFunctions, \
    FineOnlyDialogSlotFunctions, NotGuiltyBondDialogSlotFunctions
from package.controllers.view_modifiers import DiversionDialogViewModifier, JailCCDialogViewModifier, \
    FineOnlyDialogViewModifier, NotGuiltyBondDialogViewModifier
from package.models.case_information import BondConditions
from package.models.template_types import TEMPLATE_DICT
from package.views.charges_grids import JailChargesGrid, NoJailChargesGrid, NotGuiltyPleaGrid
from package.views.diversion_plea_dialog_ui import Ui_DiversionPleaDialog
from package.views.fine_only_plea_dialog_ui import Ui_FineOnlyPleaDialog
from package.views.jail_cc_plea_dialog_ui import Ui_JailCCPleaDialog
from package.views.not_guilty_bond_dialog_ui import Ui_NotGuiltyBondDialog


class DiversionPleaDialog(CriminalSentencingDialog, Ui_DiversionPleaDialog):
    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.charges_gridLayout.__class__ = JailChargesGrid # Use JailChargesGrid because same setup for Diversion
        self.dialog_name = 'Diversion Plea Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.entry_case_information.diversion.ordered = True
        self.load_cms_data_to_view()

    def modify_view(self):
        return DiversionDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = DiversionDialogSlotFunctions(self)
        self.functions.show_jail_report_date_box()
        self.functions.show_other_conditions_box()

    def connect_signals_to_slots(self):
        return DiversionDialogSignalConnector(self)

    @logger.catch
    def add_plea_findings_and_fines_to_entry_case_information(self):
        return JailAddPleaFindingsFinesJail.add(self) # self is dialog

    @logger.catch
    def update_case_information(self):
        """"Ovverrides CriminalSentencingDialog update so add_additional_conditions method is not called."""
        self.add_plea_findings_and_fines_to_entry_case_information()
        self.transfer_field_data_to_model(self.entry_case_information.diversion)
        self.entry_case_information.diversion.program_name = self.entry_case_information.diversion.get_program_name()
        self.transfer_field_data_to_model(self.entry_case_information.other_conditions)
        return CasePartyUpdater(self)


class JailCCPleaDialog(CriminalSentencingDialog, Ui_JailCCPleaDialog):
    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.charges_gridLayout.__class__ = JailChargesGrid
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
        self.dialog_name = 'Jail CC Plea Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.load_cms_data_to_view()
        if self.case_table == 'slated':
            self.in_jail_box.setCurrentText('Yes')

    def modify_view(self):
        return JailCCDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = JailCCDialogSlotFunctions(self)

    def connect_signals_to_slots(self):
        return JailCCDialogSignalConnector(self)

    def update_jail_time_credit(self):
        self.entry_case_information.currently_in_jail = self.in_jail_box.currentText()
        self.entry_case_information.days_in_jail = self.jail_time_credit_box.text()
        self.entry_case_information.apply_jtc = self.jail_time_credit_apply_box.currentText()

    @logger.catch
    def add_plea_findings_and_fines_to_entry_case_information(self):
        return JailAddPleaFindingsFinesJail.add(self) # self is dialog


class FineOnlyPleaDialog(CriminalSentencingDialog, Ui_FineOnlyPleaDialog):
    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.charges_gridLayout.__class__ = NoJailChargesGrid
        self.additional_conditions_list = [
            ("license_suspension_checkBox", self.entry_case_information.license_suspension),
            ("community_service_checkBox", self.entry_case_information.community_service),
            ("other_conditions_checkBox", self.entry_case_information.other_conditions),
        ]
        self.dialog_name = 'Fine Only Plea Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.load_cms_data_to_view()

    def modify_view(self):
        return FineOnlyDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = FineOnlyDialogSlotFunctions(self)
        self.functions.set_fines_credit_for_jail_field()

    def connect_signals_to_slots(self):
        return FineOnlyDialogSignalConnector(self)

    def update_jail_time_credit(self):
        self.entry_case_information.fines_and_costs_jail_credit = self.credit_for_jail_checkBox.isChecked()
        self.entry_case_information.days_in_jail = self.jail_time_credit_box.text()

    def add_plea_findings_and_fines_to_entry_case_information(self):
        return NoJailPleaFindingFines.add(self) # self is the dialog


class NotGuiltyBondDialog(CriminalBaseDialog, Ui_NotGuiltyBondDialog):
    condition_checkbox_list = [
        ("monitoring_checkBox", "monitoring_type_box"),
        ("specialized_docket_checkBox", "specialized_docket_type_box"),
    ]

    @logger.catch
    def __init__(self, judicial_officer, case=None, parent=None):
        super().__init__(judicial_officer, case, parent)
        self.charges_gridLayout.__class__ = NotGuiltyPleaGrid
        self.additional_conditions_list = [
            ("admin_license_suspension_checkBox", self.entry_case_information.admin_license_suspension),
            ("domestic_violence_checkBox", self.entry_case_information.domestic_violence_conditions),
            ("no_contact_checkBox", self.entry_case_information.no_contact),
            ("custodial_supervision_checkBox", self.entry_case_information.custodial_supervision),
            ("other_conditions_checkBox", self.entry_case_information.other_conditions),
            ("vehicle_seizure_checkBox", self.entry_case_information.vehicle_seizure),
        ]
        self.dialog_name = "Not Guilty Bond Dialog"
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.entry_case_information.bond_conditions = BondConditions()
        self.load_cms_data_to_view()

    def modify_view(self):
        return NotGuiltyBondDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = NotGuiltyBondDialogSlotFunctions(self)
        self.functions.hide_boxes()

    def connect_signals_to_slots(self):
        return NotGuiltyBondDialogSignalConnector(self)

    @logger.catch
    def add_charge_to_grid(self):
        self.charges_gridLayout.add_charge_only_to_grid(self)
        self.defense_counsel_name_box.setFocus()

    @logger.catch
    def add_plea_to_entry_case_information(self):
        return NotGuiltyAddPlea.add(self) # self is the dialog

    @logger.catch
    def update_case_information(self):
        super().update_case_information()
        self.update_not_guilty_conditions()
        self.update_bond_conditions()

    @logger.catch
    def update_not_guilty_conditions(self):
        self.entry_case_information.appearance_reason = self.appearance_reason_box.currentText()
        self.add_plea_to_entry_case_information()

    @logger.catch
    def update_bond_conditions(self):
        """Updates the bond conditions from the GUI(view) and saves it to the model."""
        self.transfer_field_data_to_model(self.entry_case_information.bond_conditions)