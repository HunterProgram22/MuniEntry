"""Base Classes for CrimTraffic Entries."""
from __future__ import annotations

from os import startfile

from docxtpl import DocxTemplate
from loguru import logger
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QLabel
from munientry.builders.base_builders import BaseDialogSignalConnector, BaseDialogBuilder, \
    BaseDialogViewModifier, BaseDialogSlotFunctions

from munientry.controllers.helper_functions import set_future_date
from munientry.models.template_types import TEMPLATE_DICT
from munientry.settings import (
    SAVE_PATH,
    SPECIAL_DOCKETS_COSTS,
    TYPE_CHECKING,
    WIDGET_TYPE_SET_DICT, )
from munientry.widgets.message_boxes import InfoBox, RequiredBox

if TYPE_CHECKING:
    from munientry.models.cms_models import CmsCaseInformation
    from munientry.models.party_types import JudicialOfficer


class CrimTrafficDialogBuilder(BaseDialogBuilder):
    """The base class for all criminal and traffic main entry dialogs."""

    def __init__(
        self,
        judicial_officer: JudicialOfficer,
        cms_case: CmsCaseInformation = None,
        case_table: str = None,
        parent: BaseDialogBuilder = None,
    ) -> None:
        """Self.case_table must be set before the call to super().__init__.

        The init of BaseDialog, called by super().__init__ calls ModifyView which will use the
        case table.
        """
        self.case_table = case_table
        logger.info(f'Loading case from {self.case_table}')
        super().__init__(parent)
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.judicial_officer = judicial_officer
        self.cms_case = cms_case
        self.validator = QIntValidator(0, 1000, self)
        loaded_case = cms_case.case_number
        logger.info(f'Loaded Case {loaded_case}')
        self.load_entry_case_information_model()
        self.entry_case_information.judicial_officer = self.judicial_officer
        self.load_cms_data_to_view()
        try:
            self.defense_counsel_name_box.load_attorneys()
        except AttributeError as error:
            logger.warning(error)
        self.criminal_charge = None
        self.popup_dialog = None
        self.additional_setup()

    def additional_setup(self):
        """Abstract base method used in subclasses for additional setup after init."""


class CrimTrafficViewModifier(BaseDialogViewModifier):
    """Base View Builder for CrimTraffic Entries."""

    def set_appearance_reason(self):
        if self.dialog.case_table == 'final_pretrials':
            self.dialog.appearance_reason_box.setCurrentText('a change of plea')
        elif self.dialog.case_table == 'pleas':
            self.dialog.appearance_reason_box.setCurrentText('a change of plea')
        elif self.dialog.case_table == 'trials_to_court':
            self.dialog.appearance_reason_box.setCurrentText('a change of plea')

    def set_case_information_banner(self):
        defendant = self.dialog.main_dialog.entry_case_information.defendant
        defendant_name = f'{defendant.first_name} {defendant.last_name}'
        self.dialog.defendant_name_label.setText(f'State of Ohio v. {defendant_name}')
        self.dialog.case_number_label.setText(
            self.dialog.main_dialog.entry_case_information.case_number,
        )


class CrimTrafficSlotFunctions(BaseDialogSlotFunctions):
    """Base set of functions for CrimTraffic Entries."""

    def start_add_charge_dialog(self):
        from munientry.builders.charges.charges_dialogs import AddChargeDialog

        self.dialog.update_entry_case_information()
        self.dialog.popup_dialog = AddChargeDialog(self.dialog)
        self.dialog.popup_dialog.exec()

    def start_amend_offense_dialog(self):
        from munientry.builders.charges.charges_dialogs import AmendChargeDialog

        self.dialog.update_entry_case_information()
        self.dialog.popup_dialog = AmendChargeDialog(self.dialog)
        self.dialog.popup_dialog.exec()

    def close_window(self):
        """Closes window by calling closeEvent in BaseDialog.

        Event is logged in BaseDialog closeEvent.
        """
        self.dialog.close()

    def clear_case_information_fields(self):
        self.dialog.defendant_first_name_lineEdit.clear()
        self.dialog.defendant_last_name_lineEdit.clear()
        self.dialog.case_number_lineEdit.clear()
        self.dialog.defendant_first_name_lineEdit.setFocus()

    def create_entry(self) -> None:
        """Loads the proper template and creates the entry."""
        self.dialog.update_entry_case_information()
        doc = DocxTemplate(self.dialog.template.template_path)
        case_data = self.dialog.entry_case_information.get_case_information()
        doc.render(case_data)
        docname = self.set_document_name()
        logger.info(f'Entry Created: {docname}')
        try:
            doc.save(SAVE_PATH + docname)
        except PermissionError as error:
            logger.warning(error)
            self.dialog.message_box = RequiredBox(
                'An entry for this case is already open in Word.\n'
                + 'You must close the Word document first.',
            )
            self.dialog.message_box.exec()
        startfile(SAVE_PATH + docname)

    def create_entry_process(self) -> None:
        """Only creates the entry if the dialog passes all checks and returns 'Pass'."""
        if self.update_info_and_perform_checks() == 'Pass':
            self.create_entry()

    def set_document_name(self) -> str:
        """Returns a name for the document in the format CaseNumber_TemplateName.docx.

        Example: 21CRB1234_Crim_Traffic Judgment Entry.docx
        """
        case_number = self.dialog.entry_case_information.case_number
        template_name = self.dialog.template.template_name
        return f'{case_number}_{template_name}.docx'

    def set_fines_costs_pay_date(self, days_to_add_string):
        """Sets the fines/costs pay date.

        Date is set to the Tuesday after the number of days added, unless forthwith or a special
        docket is selected.
        """
        if days_to_add_string == 'forthwith':
            self.dialog.balance_due_date.setHidden(False)
            self.dialog.balance_due_date.setDate(QDate.currentDate())
        elif days_to_add_string in SPECIAL_DOCKETS_COSTS:
            self.dialog.balance_due_date.setHidden(True)
        else:
            self.dialog.balance_due_date.setHidden(False)
            days_to_add = self.get_days_to_add(days_to_add_string)
            total_days_to_add = set_future_date(days_to_add, 'Tuesday')
            self.dialog.balance_due_date.setDate(
                QDate.currentDate().addDays(total_days_to_add),
            )

    def get_days_to_add(self, days_to_add_string):
        pay_date_dict = {
            'within 30 days': 30,
            'within 60 days': 60,
            'within 90 days': 90,
        }
        return pay_date_dict.get(days_to_add_string)

    def update_info_and_perform_checks(self):
        """This method performs an update then calls to the main_entry_dialog's InfoChecker class.

        The InfoChecker check_status will return as 'Fail' if any of the checks are hard stops -
        meaning the warning message doesn't allow immediate correction.

        The dialog.update_entry_case_information is called a second time to update the model
        with any changes to information that was made by the InfoChecker checks.
        """
        self.dialog.update_entry_case_information()
        self.dialog.perform_info_checks()
        if self.dialog.dialog_checks.check_status == 'Fail':
            return 'Fail'
        self.dialog.update_entry_case_information()
        return 'Pass'

    def set_defense_counsel(self) -> None:
        if self.dialog.defense_counsel_waived_checkBox.isChecked():
            self.dialog.defense_counsel_name_box.setEnabled(False)
            self.dialog.defense_counsel_type_box.setEnabled(False)
        else:
            self.dialog.defense_counsel_name_box.setEnabled(True)
            self.dialog.defense_counsel_type_box.setEnabled(True)

    def set_fra_in_file(self, current_text: str) -> None:
        """Sets the FRA (proof of insurance) to true if the view indicates 'Yes'."""
        if current_text == 'Yes':
            self.dialog.entry_case_information.fra_in_file = True
            self.dialog.fra_in_court_box.setCurrentText('No')
        elif current_text == 'No':
            self.dialog.entry_case_information.fra_in_file = False
        else:
            self.dialog.entry_case_information.fra_in_file = None

    def set_fra_in_court(self, current_text: str) -> None:
        """Sets the FRA (proof of insurance) to true if the view indicates 'Yes'."""
        if current_text == 'Yes':
            self.dialog.entry_case_information.fra_in_court = True
        elif current_text == 'No':
            self.dialog.entry_case_information.fra_in_court = False
        else:
            self.dialog.entry_case_information.fra_in_court = None

    def show_costs_and_fines(self):
        self.dialog.update_entry_case_information()
        costs = str(self.dialog.entry_case_information.court_costs.amount)
        fines = str(self.dialog.entry_case_information.total_fines)
        fines_suspended = str(self.dialog.entry_case_information.total_fines_suspended)
        total_fines_and_costs = str(self.get_total_fines_and_costs())
        message_box = InfoBox(
            f'Total Costs and Fines Due By Due Date: $ {total_fines_and_costs}',
            'Total Costs and Fines',
        )
        message_box.setInformativeText(
            f'Costs: $ {costs}'
            + f'\nFines: $ {fines}'
            + f'\nFines Suspended: $ {fines_suspended}'
            + '\n\n*Does not include possible bond forfeiture or other costs that'
            + ' may be assessed as a result of prior actions in the case.',
        )
        message_box.exec_()

    def get_total_fines_and_costs(self) -> int:
        return (
            (
                self.dialog.entry_case_information.court_costs.amount
                + self.dialog.entry_case_information.total_fines
            )
            - self.dialog.entry_case_information.total_fines_suspended
        )

    def update_community_service_due_date(self, _index=None) -> None:
        days_to_complete = int(
            self.dialog.community_service_days_to_complete_box.currentText(),
        )
        self.dialog.community_service_date_to_complete_box.setDate(
            QDate.currentDate().addDays(days_to_complete),
        )

    def conditions_checkbox_toggle(self):
        """TODO: This needs to be refactored.

        It loops through all additional conditions to set a single one as true or false.

        TODO: Ultimately want to tie a checbox to the 'ordered' attribute of a conditions model.
        """
        for condition_items in self.dialog.additional_conditions_list:
            checkbox_name, condition = condition_items
            if self.dialog.sender().isChecked():
                if checkbox_name == self.dialog.sender().objectName():
                    setattr(condition, 'ordered', True)
            elif checkbox_name == self.dialog.sender().objectName():
                setattr(condition, 'ordered', False)

    def show_hide_checkbox_connected_fields(self):
        """Gets list of boxes tied to condition checkbox and sets to show or hidden."""
        checkbox = self.dialog.sender()
        boxes = self.dialog.condition_checkbox_dict.get(checkbox.objectName())
        for field in boxes:
            if checkbox.isChecked():
                getattr(self.dialog, field).setEnabled(True)
                getattr(self.dialog, field).setHidden(False)
                getattr(self.dialog, field).setFocus(True)
            else:
                getattr(self.dialog, field).setEnabled(False)
                getattr(self.dialog, field).setHidden(True)

    def show_bond_boxes(self, bond_mod_string):
        if bond_mod_string == 'request to modify bond is granted':
            self.dialog.bond_frame.setHidden(False)
            self.dialog.bond_conditions_frame.setHidden(False)
            self.dialog.special_bond_conditions_frame.setHidden(False)
        else:
            self.dialog.bond_frame.setHidden(True)
            self.dialog.bond_conditions_frame.setHidden(True)
            self.dialog.special_bond_conditions_frame.setHidden(True)


class CrimTrafficSignalConnector(BaseDialogSignalConnector):
    """Extends Base Dialog Signal Connector for CrimTraffic Entries."""

    def connect_fra_signals(self):
        self.dialog.fra_in_file_box.currentTextChanged.connect(
            self.dialog.functions.set_fra_in_file,
        )
        self.dialog.fra_in_court_box.currentTextChanged.connect(
            self.dialog.functions.set_fra_in_court,
        )

    def connect_plea_all_button_signals(self):
        self.dialog.add_charge_Button.released.connect(
            self.dialog.functions.start_add_charge_dialog,
        )
        self.dialog.guilty_all_Button.pressed.connect(
            self.dialog.charges_gridLayout.set_all_pleas,
        )
        self.dialog.guilty_all_Button.pressed.connect(
            self.dialog.charges_gridLayout.set_all_findings,
        )
        self.dialog.no_contest_all_Button.pressed.connect(
            self.dialog.charges_gridLayout.set_all_pleas,
        )
        self.dialog.no_contest_all_Button.pressed.connect(
            self.dialog.charges_gridLayout.set_all_findings,
        )

    def connect_not_guilty_all_button(self):
        self.dialog.not_guilty_all_Button.pressed.connect(
            self.dialog.charges_gridLayout.set_all_pleas,
        )

    def connect_add_charge_button(self):
        self.dialog.add_charge_Button.released.connect(
            self.dialog.functions.start_add_charge_dialog,
        )

    def connect_court_cost_signals(self):
        self.dialog.ability_to_pay_box.currentTextChanged.connect(
            self.dialog.functions.set_fines_costs_pay_date,
        )
        self.dialog.costs_and_fines_Button.released.connect(
            self.dialog.functions.show_costs_and_fines,
        )

    def connect_main_dialog_additional_condition_signals(self):
        self.dialog.license_suspension_checkBox.toggled.connect(
            self.dialog.functions.conditions_checkbox_toggle,
        )
        self.dialog.community_service_checkBox.toggled.connect(
            self.dialog.functions.conditions_checkbox_toggle,
        )
        self.dialog.other_conditions_checkBox.toggled.connect(
            self.dialog.functions.conditions_checkbox_toggle,
        )
        self.dialog.add_conditions_Button.pressed.connect(
            self.dialog.functions.start_add_conditions_dialog,
        )

    def connect_condition_dialog_main_signals(self):
        self.dialog.add_conditions_Button.pressed.connect(self.dialog.functions.add_conditions)
        self.dialog.add_conditions_Button.released.connect(self.dialog.functions.close_window)

    def connect_community_service_days_update(self):
        self.dialog.community_service_days_to_complete_box.currentIndexChanged.connect(
            self.dialog.functions.update_community_service_due_date
        )


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
