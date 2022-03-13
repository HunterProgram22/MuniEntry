from PyQt5.QtGui import QIntValidator
from PyQt5.QtSql import QSqlQuery
from loguru import logger
from package.controllers.base_dialogs import CMS_FRALoader, CMSLoader, BaseDialog, close_databases, \
    charges_database
from package.controllers.case_updaters import DiversionDialogCaseUpdater, JailCCDialogCaseUpdater, \
    FineOnlyDialogCaseUpdater, NotGuiltyBondDialogCaseUpdater
from package.controllers.conditions_dialogs import AddJailOnlyDialog
from package.controllers.plea_finding_controllers import NoJailPleaFindingFines, JailAddPleaFindingsFinesJail, \
    NotGuiltyAddPlea
from package.controllers.signal_connectors import DiversionDialogSignalConnector, JailCCDialogSignalConnector, \
    FineOnlyDialogSignalConnector, NotGuiltyBondDialogSignalConnector
from package.controllers.slot_functions import DiversionDialogSlotFunctions, JailCCDialogSlotFunctions, \
    FineOnlyDialogSlotFunctions, NotGuiltyBondDialogSlotFunctions
from package.controllers.view_modifiers import DiversionDialogViewModifier, JailCCDialogViewModifier, \
    FineOnlyDialogViewModifier, NotGuiltyBondDialogViewModifier
from package.controllers.case_updaters import DiversionDialogCaseUpdater
from package.models.case_information import BondConditions, CriminalCaseInformation
from package.models.template_types import TEMPLATE_DICT
from package.views.charges_grids import JailChargesGrid, NoJailChargesGrid, NotGuiltyPleaGrid
from package.views.custom_widgets import DefenseCounselComboBox
from package.views.diversion_plea_dialog_ui import Ui_DiversionPleaDialog
from package.views.fine_only_plea_dialog_ui import Ui_FineOnlyPleaDialog
from package.views.jail_cc_plea_dialog_ui import Ui_JailCCPleaDialog
from package.views.not_guilty_bond_dialog_ui import Ui_NotGuiltyBondDialog


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
        self.criminal_charge = None

    def load_cms_data_to_view(self):
        raise NotImplementedError

    def add_plea_to_entry_case_information(self):
        raise NotImplementedError

    def update_entry_case_information(self):
        raise NotImplementedError


    # TO BE REFACTORED #
    def set_offense_type(self):
        """This calls the database_statutes and behind the scenes sets the appropriate cms_case type
        for each charge. It does not show up in the view, but is used for calculating costs."""
        key = self.statute_choice_box.currentText()
        if self.freeform_entry_checkBox.isChecked():
            return None
        query = QSqlQuery(charges_database)
        query.prepare("SELECT * FROM charges WHERE statute LIKE '%' || :key || '%'")
        query.bindValue(":key", key)
        query.exec()
        while query.next():
            statute = query.value(2)
            offense_type = query.value(4)
            if statute == key:
                query.finish()
                return offense_type

    def add_charge_to_grid(self):
        self.charges_gridLayout.add_charge_only_to_grid(self)
        self.defense_counsel_name_box.setFocus()

    def calculate_costs_and_fines(self):
        """Calculates costs and fines based on the cms_case type (moving, non-moving, criminal) and
        then adds it to any fines that are in the fines_amount box and subtracts fines in the
        fines_suspended box. The loop stops when a cms_case of the highest fine is found because
        court costs are always for the highest charge. The _index is underscored because it is
        not used but is required to unpack enumerate().

        TODO: This needs to be refactored and fixed - code in the AddPlea functions for each dialog have code
        that exists just to deal with this function setting the charge fines/fines_suspended to 0."""
        self.entry_case_information.court_costs.amount = self.calculate_court_costs()
        total_fines = 0
        try:
            for charge in self.entry_case_information.charges_list:
                try:
                    local_charge_fines_amount = int(charge.fines_amount[2:])
                except ValueError:
                    local_charge_fines_amount = 0
                if local_charge_fines_amount == '':
                    local_charge_fines_amount = 0
                try:
                    total_fines = total_fines + int(local_charge_fines_amount)
                except ValueError: # This error catches the " " (space) that is placed if a charge is dismissed.
                    pass
            self.entry_case_information.total_fines = total_fines
            total_fines_suspended = 0
            for _index, charge in enumerate(self.entry_case_information.charges_list):
                try:
                    local_charge_fines_suspended = int(charge.fines_suspended[2:])
                except ValueError:
                    local_charge_fines_suspended = 0
                if local_charge_fines_suspended == '':
                    local_charge_fines_suspended = 0
                try:
                    total_fines_suspended = total_fines_suspended + int(local_charge_fines_suspended)
                except ValueError: # This error catches the " " (space) that is placed if a charge is dismissed.
                    pass
            self.entry_case_information.total_fines_suspended = total_fines_suspended
        except TypeError:
            print("A type error was allowed to pass - this is because of deleted charge.")

    def calculate_court_costs(self):
        self.entry_case_information.court_costs.amount = 0
        if self.court_costs_box.currentText() == "Yes":
            for charge in self.entry_case_information.charges_list:
                if self.entry_case_information.court_costs.amount == 124:
                    break
                if charge.type == "Moving":
                    self.entry_case_information.court_costs.amount = max(
                        self.entry_case_information.court_costs.amount, 124)
                elif charge.type == "Criminal":
                    self.entry_case_information.court_costs.amount = max(
                        self.entry_case_information.court_costs.amount, 114)
                elif charge.type == "Non-moving":
                    self.entry_case_information.court_costs.amount = max(
                        self.entry_case_information.court_costs.amount, 95)
        return self.entry_case_information.court_costs.amount

    def start_jail_only_dialog(self):
        self.update_entry_case_information()
        AddJailOnlyDialog(self).exec()


class DiversionPleaDialog(CriminalBaseDialog, Ui_DiversionPleaDialog):
    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.dialog_name = 'Diversion Plea Dialog'
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
        self.charges_gridLayout.__class__ = JailChargesGrid # Use JailChargesGrid because same setup for Diversion
        return CMS_FRALoader(self)

    def update_entry_case_information(self):
        return DiversionDialogCaseUpdater(self)

    def add_plea_findings_and_fines_to_entry_case_information(self):
        return JailAddPleaFindingsFinesJail.add(self) # self is dialog


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
        self.dialog_name = 'Jail CC Plea Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        if self.case_table == 'slated':
            self.in_jail_box.setCurrentText('Yes')

    def modify_view(self):
        return JailCCDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = JailCCDialogSlotFunctions(self)

    def connect_signals_to_slots(self):
        return JailCCDialogSignalConnector(self)

    def load_cms_data_to_view(self):
        self.charges_gridLayout.__class__ = JailChargesGrid
        return CMS_FRALoader(self)

    def update_entry_case_information(self):
        return JailCCDialogCaseUpdater(self)

    def add_plea_findings_and_fines_to_entry_case_information(self):
        return JailAddPleaFindingsFinesJail.add(self) # self is dialog


class FineOnlyPleaDialog(CriminalBaseDialog, Ui_FineOnlyPleaDialog):
    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.additional_conditions_list = [
            ("license_suspension_checkBox", self.entry_case_information.license_suspension),
            ("community_service_checkBox", self.entry_case_information.community_service),
            ("other_conditions_checkBox", self.entry_case_information.other_conditions),
        ]
        self.dialog_name = 'Fine Only Plea Dialog'
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
        return CMS_FRALoader(self)

    def update_entry_case_information(self):
        return FineOnlyDialogCaseUpdater(self)

    def add_plea_findings_and_fines_to_entry_case_information(self):
        return NoJailPleaFindingFines.add(self) # self is the dialog


class NotGuiltyBondDialog(CriminalBaseDialog, Ui_NotGuiltyBondDialog):
    condition_checkbox_list = [
        ("monitoring_checkBox", "monitoring_type_box"),
        ("specialized_docket_checkBox", "specialized_docket_type_box"),
    ]

    def __init__(self, judicial_officer, case=None, parent=None):
        super().__init__(judicial_officer, case, parent)
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

    def modify_view(self):
        return NotGuiltyBondDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = NotGuiltyBondDialogSlotFunctions(self)
        self.functions.hide_boxes()

    def connect_signals_to_slots(self):
        return NotGuiltyBondDialogSignalConnector(self)

    def load_cms_data_to_view(self):
        self.charges_gridLayout.__class__ = NotGuiltyPleaGrid
        return CMSLoader(self)

    def update_entry_case_information(self):
        return NotGuiltyBondDialogCaseUpdater(self)

    def add_charge_to_grid(self):
        self.charges_gridLayout.add_charge_only_to_grid(self)
        self.defense_counsel_name_box.setFocus()

    def add_plea_to_entry_case_information(self):
        return NotGuiltyAddPlea.add(self) # self is the dialog
