"""The BaseDialogs modules contains common base classes from which other dialogs inherit."""
from __future__ import annotations

from os import startfile
from typing import Any

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtSql import QSqlQuery
from docxtpl import DocxTemplate
from loguru import logger
from PyQt5.QtGui import QCloseEvent, QIntValidator
from PyQt5.QtWidgets import QDialog, QLabel
from munientry.controllers.helper_functions import set_future_date

from munientry.models.scheduling_information import SchedulingCaseInformation
from munientry.settings import TYPE_CHECKING, WIDGET_TYPE_ACCESS_DICT, ICON_PATH, \
    WIDGET_TYPE_SET_DICT, SAVE_PATH, SPECIAL_DOCKETS_COSTS
from munientry.models.template_types import TEMPLATE_DICT
from munientry.widgets.message_boxes import RequiredBox, InfoBox

if TYPE_CHECKING:
    from munientry.models.cms_models import CmsCaseInformation
    from munientry.models.party_types import JudicialOfficer


class BaseDialogBuilder(QDialog):
    """This class is a base class for all dialog windows."""

    def __init__(self, parent: QDialog = None) -> None:
        super().__init__(parent)
        self.build_attrs = self._get_dialog_attributes()
        self._modify_view()
        self._connect_signals_to_slots()
        self.dialog_name = self.build_attrs.get('dialog_name', None)
        self.template = TEMPLATE_DICT.get(self.dialog_name)

    def _get_dialog_attributes(self) -> dict:
        return self.build_dict

    def _modify_view(self) -> None:
        self.build_attrs.get('view')(self)

    def _connect_signals_to_slots(self) -> None:
        self.functions = self.build_attrs.get('slots')(self)
        self.build_attrs.get('signals')(self)

    def load_entry_case_information_model(self):
        self.entry_case_information = self.build_attrs.get('case_information_model')()

    def load_cms_data_to_view(self) -> None:
        self.build_attrs.get('loader')(self)

    def update_entry_case_information(self) -> None:
        self.build_attrs.get('updater')(self)

    def perform_info_checks(self) -> None:
        self.dialog_checks = self.build_attrs.get('info_checker')(self)

    def transfer_view_data_to_model(self, model_class: type[Any]) -> None:
        """Takes data in the view fields and transfers to appropriate model class attribute.

        Method loops through all items in terms list which are maps of a model attribute to
        a view field. The appropriate transfer method is obtained from the WIDGET_TYPE_ACCESS_DICT

        Args:
            model_class: A dataclass object that has a terms_list attribute mapping
                view fields to model attributes.
        """
        for (model_attribute, view_field) in model_class.terms_list:
            widget_type = getattr(self, view_field).__class__.__name__
            view = getattr(self, view_field)
            view_field_data = getattr(view, WIDGET_TYPE_ACCESS_DICT.get(widget_type, 'None'))()
            class_name = model_class.__class__.__name__
            setattr(model_class, model_attribute, view_field_data)
            logger.info(f'{class_name} {model_attribute} set to: {view_field_data}.')

    def closeEvent(self, event: QCloseEvent) -> None:
        """Extends pyqt close event method in order to log when a dialog closes."""
        logger.dialog(f'{self.objectName()} Closed by {event}')


class CriminalDialogBuilder(BaseDialogBuilder):
    """The base class for all criminal and traffic main entry dialogs."""

    def __init__(
        self,
        judicial_officer: JudicialOfficer,
        cms_case: CmsCaseInformation = None,
        case_table: str = None,
        parent: BaseDialog = None,
    ) -> None:
        """Self.case_table must be set before the call to super().__init__.

        The init of BaseDialog, called by super().__init__ calls ModifyView which will use the
        case table.
        """
        self.case_table = case_table
        logger.info(f'Loading case from {self.case_table}')
        super().__init__(parent)
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
        pass

    # TO BE REFACTORED #
    def add_charge_to_grid(self):
        self.charges_gridLayout.add_fields_to_charges_grid(self)
        self.defense_counsel_name_box.setFocus()


class BaseDialog(QDialog):
    """This class is a base class for all dialog windows."""

    def __init__(self, parent: QDialog = None) -> None:
        super().__init__(parent)
        self._modify_view()
        self._connect_signals_to_slots()

    def _modify_view(self) -> None:
        """Abstract method that calls setupUI and creates the view.

        Raises:
            NotImplementedError: if the dialog does not implement the method.
        """
        raise NotImplementedError

    def _connect_signals_to_slots(self) -> None:
        """Abstract method that connects signals to dialog slot functions.

        Raises:
            NotImplementedError: if the dialog does not implement the method.
        """
        raise NotImplementedError

    def transfer_view_data_to_model(self, model_class: type[Any]) -> None:
        """Takes data in the view fields and transfers to appropriate model class attribute.

        Method loops through all items in terms list which are maps of a model attribute to
        a view field. The appropriate transfer method is obtained from the WIDGET_TYPE_ACCESS_DICT

        Args:
            model_class: A dataclass object that has a terms_list attribute mapping
                view fields to model attributes.
        """
        for (model_attribute, view_field) in model_class.terms_list:
            widget_type = getattr(self, view_field).__class__.__name__
            view = getattr(self, view_field)
            view_field_data = getattr(view, WIDGET_TYPE_ACCESS_DICT.get(widget_type, 'None'))()
            class_name = model_class.__class__.__name__
            setattr(model_class, model_attribute, view_field_data)
            logger.info(f'{class_name} {model_attribute} set to: {view_field_data}.')

    def closeEvent(self, event: QCloseEvent) -> None:
        """Extends pyqt close event method in order to log when a dialog closes."""
        logger.dialog(f'{self.objectName()} Closed by {event}')


class CriminalBaseDialog(BaseDialog):
    """The base class for all criminal and traffic main entry dialogs."""

    def __init__(
        self,
        judicial_officer: JudicialOfficer,
        cms_case: CmsCaseInformation = None,
        case_table: str = None,
        parent: BaseDialog = None,
    ) -> None:
        """Self.case_table must be set before the call to super().__init__.

        The init of BaseDialog, called by super().__init__ calls ModifyView which will use the
        case table.
        """
        self.case_table = case_table
        logger.info(f'Loading case from {self.case_table}')
        super().__init__(parent)
        self.judicial_officer = judicial_officer
        self.cms_case = cms_case
        self.validator = QIntValidator(0, 1000, self)
        loaded_case = cms_case.case_number
        logger.info(f'Loaded Case {loaded_case}')
        self.load_entry_case_information_model()
        self.load_cms_data_to_view()
        try:
            self.defense_counsel_name_box.load_attorneys()
        except AttributeError as error:
            logger.warning(error)
        self.criminal_charge = None
        self.popup_dialog = None

    def load_entry_case_information_model(self):
        raise NotImplementedError

    def load_cms_data_to_view(self) -> None:
        raise NotImplementedError

    def update_entry_case_information(self) -> None:
        raise NotImplementedError

    def perform_info_checks(self) -> None:
        raise NotImplementedError

    # TO BE REFACTORED #
    def add_charge_to_grid(self):
        self.charges_gridLayout.add_fields_to_charges_grid(self)
        self.defense_counsel_name_box.setFocus()


class SchedulingBaseDialog(BaseDialog):
    """The base class for all scheduling entries."""

    def __init__(self, judicial_officer=None, cms_case=None, case_table=None, parent=None):
        super().__init__(parent)
        self.case_table = case_table
        self.judicial_officer = judicial_officer
        self.entry_case_information = SchedulingCaseInformation()
        self.cms_case = cms_case
        case_number = cms_case.case_number
        logger.info(f'Loading {case_number} from {self.case_table}')
        self.load_cms_data_to_view()


class BaseDialogViewModifier:
    def __init__(self, dialog):
        self.dialog = dialog
        self.dialog.setWindowIcon(QtGui.QIcon(f'{ICON_PATH}gavel.ico'))
        self.dialog.setWindowFlags(self.dialog.windowFlags() |
                            QtCore.Qt.CustomizeWindowHint |
                            QtCore.Qt.WindowMaximizeButtonHint |
                            QtCore.Qt.WindowCloseButtonHint)
        self.dialog.setupUi(self.dialog)

    def set_appearance_reason(self):
        if self.dialog.case_table == "final_pretrials":
            self.dialog.appearance_reason_box.setCurrentText("a change of plea")
        elif self.dialog.case_table == "pleas":
            self.dialog.appearance_reason_box.setCurrentText("a change of plea")
        elif self.dialog.case_table == "trials_to_court":
            self.dialog.appearance_reason_box.setCurrentText("a change of plea")

    def set_case_information_banner(self):
        self.dialog.defendant_name_label.setText(
            "State of Ohio v. {defendant_first_name} {defendant_last_name}".format(
                defendant_first_name=self.dialog.main_dialog.entry_case_information.defendant.first_name,
                defendant_last_name=self.dialog.main_dialog.entry_case_information.defendant.last_name
            )
        )
        self.dialog.case_number_label.setText(self.dialog.main_dialog.entry_case_information.case_number)

    ###Additional Condition/Jail Dialog Setup Methods###
    def set_conditions_case_information_banner(self):
        column = self.dialog.charges_gridLayout.columnCount() + 1
        for _index, charge in enumerate(self.dialog.charges_list):
            charge = vars(charge)
            if charge is not None:
                self.dialog.charges_gridLayout.addWidget(QLabel(charge.get("offense")), 0, column)
                self.dialog.charges_gridLayout.addWidget(QLabel(charge.get("statute")), 1, column)
                self.dialog.charges_gridLayout.addWidget(QLabel(charge.get("finding")), 2, column)
                column += 1

    def set_report_date_view(self):
        if self.dialog.report_type_box.currentText() == "date set by Office of Community Control":
            self.dialog.report_date_box.setDisabled(True)
            self.dialog.report_date_box.setHidden(True)
            self.dialog.report_time_box.setDisabled(True)
            self.dialog.report_time_box.setHidden(True)
            self.dialog.report_date_label.setHidden(True)
            self.dialog.report_time_label.setHidden(True)
        elif self.dialog.report_type_box.currentText() == "forthwith":
            self.dialog.report_date_box.setDisabled(True)
            self.dialog.report_date_box.setHidden(True)
            self.dialog.report_time_box.setDisabled(True)
            self.dialog.report_time_box.setHidden(True)
            self.dialog.report_date_label.setHidden(True)
            self.dialog.report_time_label.setHidden(True)
        else:
            self.dialog.report_date_box.setEnabled(True)
            self.dialog.report_date_box.setHidden(False)
            self.dialog.report_time_box.setEnabled(True)
            self.dialog.report_time_box.setHidden(False)
            self.dialog.report_date_label.setHidden(False)
            self.dialog.report_time_label.setHidden(False)

    def set_report_days_notes_box(self):
        if self.dialog.jail_sentence_execution_type_box.currentText() == "consecutive days":
            self.dialog.jail_report_days_notes_box.setDisabled(True)
            self.dialog.jail_report_days_notes_box.setHidden(True)
        else:
            self.dialog.jail_report_days_notes_box.setDisabled(False)
            self.dialog.jail_report_days_notes_box.setHidden(False)

    @classmethod
    def hide_boxes(cls, dialog):
        for item in cls.condition_checkbox_list:
            (condition_checkbox, condition_field) = item
            if hasattr(dialog, condition_checkbox):
                if getattr(dialog, condition_checkbox).isChecked():
                    getattr(dialog, condition_field).setEnabled(True)
                    getattr(dialog, condition_field).setHidden(False)
                else:
                    getattr(dialog, condition_field).setEnabled(False)
                    getattr(dialog, condition_field).setHidden(True)

    def transfer_model_data_to_view(self, model_class):
        """Loops through the terms_list for a model and loads data into the view of the dialog on
        load. This is to allow for previously entered data to be shown if a user comes back to
        the dialog after having previously entered data."""
        for (model_attribute, view_field) in model_class.terms_list:
            key = getattr(self.dialog, view_field).__class__.__name__
            view = getattr(self.dialog, view_field)
            getattr(view, WIDGET_TYPE_SET_DICT.get(key))(getattr(model_class, model_attribute))


class BaseDialogSlotFunctions(object):
    def __init__(self, dialog):
        self.dialog = dialog

    def start_add_charge_dialog(self):
        from munientry.builders.charges_dialogs import AddChargeDialog

        self.dialog.update_entry_case_information()
        self.dialog.popup_dialog = AddChargeDialog(self.dialog)
        self.dialog.popup_dialog.exec()

    def start_amend_offense_dialog(self):
        from munientry.builders.charges_dialogs import AmendChargeDialog

        self.dialog.update_entry_case_information()
        self.dialog.popup_dialog = AmendChargeDialog(self.dialog)
        self.dialog.popup_dialog.exec()

    def close_window(self):
        """Closes window by calling closeEvent in BaseDialog.

        Event is logged in BaseDialog closeEvent.

        Function connected to a button to close the window. Can be connected
        to any button press/click/release to close a window. This can also be called
        at the end of the close_event process to close the dialog.
        """
        self.dialog.close()

    def clear_case_information_fields(self):
        self.dialog.defendant_first_name_lineEdit.clear()
        self.dialog.defendant_last_name_lineEdit.clear()
        self.dialog.case_number_lineEdit.clear()
        self.dialog.defendant_first_name_lineEdit.setFocus()

    def create_entry(self):
        """Loads the proper template and creates the entry."""
        self.dialog.update_entry_case_information()
        doc = DocxTemplate(self.dialog.template.template_path)
        case_data = self.dialog.entry_case_information.get_case_information()
        # extract_data(case_data)
        doc.render(case_data)
        docname = self.set_document_name()
        logger.info(f'Entry Created: {docname}')
        try:
            doc.save(SAVE_PATH + docname)
            startfile(SAVE_PATH + docname)
        except PermissionError as error:
            logger.warning(error)
            self.dialog.message_box = RequiredBox(
                "An entry for this case is already open in Word."
                " You must close the Word document first."
            )
            self.dialog.message_box.exec()

    def create_entry_process(self):
        """The info_checks variable is either "Pass" or "Fail" based on the checks performed by the
        update_info_and_perform_checks method."""
        if self.update_info_and_perform_checks() == "Pass":
            self.create_entry()

    def set_document_name(self):
        """Returns a name for the document in the format CaseNumber_TemplateName.docx
        (i.e. 21CRB1234_Crim_Traffic Judgment Entry.docx"""
        return (
            f"{self.dialog.entry_case_information.case_number}"
            f"_{self.dialog.template.template_name}.docx"
        )

    def set_fines_costs_pay_date(self, days_to_add_string):
        """Sets the sentencing date to the Tuesday after the number of days added."""
        if days_to_add_string == "forthwith":
            self.dialog.balance_due_date.setHidden(False)
            self.dialog.balance_due_date.setDate(QDate.currentDate())
        elif days_to_add_string in SPECIAL_DOCKETS_COSTS:
            self.dialog.balance_due_date.setHidden(True)
        else:
            self.dialog.balance_due_date.setHidden(False)
            days_to_add = self.get_days_to_add(days_to_add_string)
            total_days_to_add = set_future_date(days_to_add, "Tuesday")
            self.dialog.balance_due_date.setDate(
                QDate.currentDate().addDays(total_days_to_add)
            )

    def get_days_to_add(self, days_to_add_string):
        pay_date_dict = {
            "within 30 days": 30,
            "within 60 days": 60,
            "within 90 days": 90,
        }
        return pay_date_dict.get(days_to_add_string)

    @logger.catch
    def update_info_and_perform_checks(self):
        """This method performs an update then calls to the main_entry_dialog's InfoChecker class to run
        the checks for that dialog. The InfoChecker check_status will return as "Fail" if any of the
        checks are hard stops - meaning the warning message doesn't allow immediate correction.

        The dialog.update_entry_case_information is called a second time to update the model with any changes
        to information that was made by the InfoChecker checks."""
        self.dialog.update_entry_case_information()
        self.dialog.perform_info_checks()
        if self.dialog.dialog_checks.check_status == "Fail":
            return "Fail"
        self.dialog.update_entry_case_information()
        return "Pass"

    def set_defense_counsel(self):
        if self.dialog.defense_counsel_waived_checkBox.isChecked():
            self.dialog.defense_counsel_name_box.setEnabled(False)
            self.dialog.defense_counsel_type_box.setEnabled(False)
        else:
            self.dialog.defense_counsel_name_box.setEnabled(True)
            self.dialog.defense_counsel_type_box.setEnabled(True)

    def set_fra_in_file(self, current_text):
        """Sets the FRA (proof of insurance) to true if the view indicates 'yes'
        that the FRA was shown in the complaint of file."""
        if current_text == "Yes":
            self.dialog.entry_case_information.fra_in_file = True
            self.dialog.fra_in_court_box.setCurrentText("No")
        elif current_text == "No":
            self.dialog.entry_case_information.fra_in_file = False
        else:
            self.dialog.entry_case_information.fra_in_file = None

    def set_fra_in_court(self, current_text):
        """Sets the FRA (proof of insurance) to true if the view indicates 'yes'
        that the FRA was shown in court."""
        if current_text == "Yes":
            self.dialog.entry_case_information.fra_in_court = True
        elif current_text == "No":
            self.dialog.entry_case_information.fra_in_court = False
        else:
            self.dialog.entry_case_information.fra_in_court = None

    @logger.catch
    def show_costs_and_fines(self):
        self.dialog.update_entry_case_information()
        message = InfoBox()
        message.setWindowTitle("Total Costs and Fines")
        message.setInformativeText(
            f"Costs: $ {str(self.dialog.entry_case_information.court_costs.amount)}"
            f"\nFines: $ {str(self.dialog.entry_case_information.total_fines)}"
            f"\nFines Suspended: $ {str(self.dialog.entry_case_information.total_fines_suspended)}"
            f"\n\n*Does not include possible bond forfeiture or other costs \n that "
            f"may be assessed as a result of prior actions in the case. "
        )
        total_fines_and_costs = (
            self.dialog.entry_case_information.court_costs.amount
            + self.dialog.entry_case_information.total_fines
        ) - self.dialog.entry_case_information.total_fines_suspended
        message.setText(
            f"Total Costs and Fines Due By Due Date: $ {str(total_fines_and_costs)}"
        )
        message.exec_()

    def update_community_service_due_date(self, _index=None):
        days_to_complete = int(
            self.dialog.community_service_days_to_complete_box.currentText()
        )
        self.dialog.community_service_date_to_complete_box.setDate(
            QDate.currentDate().addDays(days_to_complete)
        )

    def set_offense(self, key):
        if self.dialog.freeform_entry_checkBox.isChecked():
            return None
        field = 'statute'
        offense, statute, degree = self.query_charges_database(key, field)
        if statute == key:
            self.dialog.offense_choice_box.setCurrentText(offense)
        self.dialog.degree_choice_box.setCurrentText(degree)

    def set_statute(self, key):
        if self.dialog.freeform_entry_checkBox.isChecked():
            return None
        field = 'offense'
        offense, statute, degree = self.query_charges_database(key, field)
        if offense == key:
            self.dialog.statute_choice_box.setCurrentText(statute)
        self.dialog.degree_choice_box.setCurrentText(degree)

    def query_charges_database(self, key, field):
        query_string = f"SELECT * FROM charges WHERE {field} LIKE '%' || :key || '%'"
        query = QSqlQuery(self.dialog.db_connection)
        query.prepare(query_string)
        query.bindValue(":key", key)
        query.bindValue(field, field)
        query.exec()
        query.next()
        offense = query.value(1)
        statute = query.value(2)
        degree = query.value(3)
        query.finish()
        return offense, statute, degree

    def conditions_checkbox_toggle(self):
        logger.button(f'{self.dialog.sender().text()} Checkbox Set: {self.dialog.sender().isChecked()}')
        if self.dialog.sender().isChecked():
            for items in self.dialog.additional_conditions_list:
                if items[0] == self.dialog.sender().objectName():
                    setattr(items[1], "ordered", True)
        else:
            for items in self.dialog.additional_conditions_list:
                if items[0] == self.dialog.sender().objectName():
                    setattr(items[1], "ordered", False)

    def set_report_date(self):
        if (
            self.dialog.report_type_box.currentText()
            == "date set by Office of Community Control"
        ):
            self.dialog.report_date_box.setDisabled(True)
            self.dialog.report_date_box.setHidden(True)
            self.dialog.report_time_box.setDisabled(True)
            self.dialog.report_time_box.setHidden(True)
            self.dialog.report_date_label.setHidden(True)
            self.dialog.report_time_label.setHidden(True)
        elif self.dialog.report_type_box.currentText() == "forthwith":
            self.dialog.report_date_box.setDisabled(True)
            self.dialog.report_date_box.setHidden(True)
            self.dialog.report_time_box.setDisabled(True)
            self.dialog.report_time_box.setHidden(True)
            self.dialog.report_date_label.setHidden(True)
            self.dialog.report_time_label.setHidden(True)
        else:
            self.dialog.report_date_box.setEnabled(True)
            self.dialog.report_date_box.setHidden(False)
            self.dialog.report_time_box.setEnabled(True)
            self.dialog.report_time_box.setHidden(False)
            self.dialog.report_date_label.setHidden(False)
            self.dialog.report_time_label.setHidden(False)

    def show_report_days_notes_box(self):
        if (
            self.dialog.jail_sentence_execution_type_box.currentText()
            == "consecutive days"
        ):
            self.dialog.jail_report_days_notes_box.setDisabled(True)
            self.dialog.jail_report_days_notes_box.setHidden(True)
        else:
            self.dialog.jail_report_days_notes_box.setDisabled(False)
            self.dialog.jail_report_days_notes_box.setHidden(False)

    def show_hide_checkbox_connected_fields(self):
        """Gets list of boxes tied to condition checkbox and sets to show or hidden based on
        whether the box is checked or not."""
        checkbox = self.dialog.sender()
        boxes = self.dialog.condition_checkbox_dict.get(checkbox.objectName())
        for item in boxes:
            if checkbox.isChecked():
                getattr(self.dialog, item).setEnabled(True)
                getattr(self.dialog, item).setHidden(False)
                getattr(self.dialog, item).setFocus(True)
            else:
                getattr(self.dialog, item).setEnabled(False)
                getattr(self.dialog, item).setHidden(True)

    def set_freeform_entry(self):
        if self.dialog.freeform_entry_checkBox.isChecked():
            self.dialog.statute_choice_box.setEditable(True)
            self.dialog.offense_choice_box.setEditable(True)
            self.dialog.statute_choice_box.clearEditText()
            self.dialog.offense_choice_box.clearEditText()
            self.dialog.degree_choice_box.setCurrentText("")
        else:
            self.dialog.statute_choice_box.setEditable(False)
            self.dialog.offense_choice_box.setEditable(False)
            self.dialog.statute_choice_box.setCurrentText("")
            self.dialog.offense_choice_box.setCurrentText("")
            self.dialog.degree_choice_box.setCurrentText("")

    def show_bond_boxes(self, bond_mod_string):
        if bond_mod_string == "request to modify bond is granted":
            self.dialog.bond_frame.setHidden(False)
            self.dialog.bond_conditions_frame.setHidden(False)
            self.dialog.special_bond_conditions_frame.setHidden(False)
        else:
            self.dialog.bond_frame.setHidden(True)
            self.dialog.bond_conditions_frame.setHidden(True)
            self.dialog.special_bond_conditions_frame.setHidden(True)


class BaseDialogSignalConnector_Refactor:
    """Refactor class for temp use only."""

    def __init__(self, dialog):
        self.dialog = dialog

    def connect_main_dialog_common_signals(self):
        self.dialog.cancel_Button.released.connect(self.dialog.functions.close_window)
        self.dialog.clear_fields_case_Button.released.connect(self.dialog.functions.clear_case_information_fields)
        self.dialog.create_entry_Button.released.connect(self.dialog.functions.create_entry_process)
        self.dialog.close_dialog_Button.released.connect(self.dialog.functions.close_window)
        self.dialog.defense_counsel_waived_checkBox.toggled.connect(self.dialog.functions.set_defense_counsel)

    def connect_not_guilty_all_button(self):
        self.dialog.not_guilty_all_Button.pressed.connect(self.dialog.charges_gridLayout.set_all_pleas)

    def connect_add_charge_button(self):
        self.dialog.add_charge_Button.released.connect(self.dialog.functions.start_add_charge_dialog)


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
