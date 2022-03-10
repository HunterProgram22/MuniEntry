"""The BaseDialogs modules contains common base classes from which other dialogs inherit."""

from loguru import logger
from PyQt5.QtCore import QDate
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QDialog, QComboBox, QCheckBox, QLineEdit, QTextEdit, QDateEdit, QTimeEdit, QRadioButton

from db.databases import open_charges_db_connection, create_offense_list, create_statute_list
from package.controllers.helper_functions import set_future_date
from package.models.case_information import CriminalCaseInformation, CriminalCharge, AmendOffenseDetails
from package.views.add_charge_dialog_ui import Ui_AddChargeDialog
from package.views.amend_charge_dialog_ui import Ui_AmendChargeDialog
from package.controllers.view_modifiers import AddChargeDialogViewModifier, AmendChargeDialogViewModifier
from package.controllers.signal_connectors import AddChargeDialogSignalConnector, AmendChargeDialogSignalConnector
from package.views.custom_widgets import DefenseCounselComboBox
from settings import PAY_DATE_DICT


def close_databases():
    charges_database.close()
    charges_database.removeDatabase("QSQLITE")


class BaseDialog(QDialog):
    """This class is a base class to provide methods that are used by some criminal controllers
     in the application. This class is never instantiated as its own dialog, but the init contains
     the setup for all inherited class controllers."""
    def __init__(self, case_table=None, parent=None):
        """Databases must be opened first in order for them to be accessed
        when the UI is built so it can populate fields.The setupUI calls to
        the view to create the UI."""
        super().__init__(parent)
        self.case_table = case_table
        self.modify_view()
        self.connect_signals_to_slots()

    def modify_view(self):
        """The modify view method updates the view that is created on init with self.setupUI.
        Place items in this method that can't be added directly in QtDesigner (or are more easily added later)
        so that they don't need to be changed in the view file each time pyuic5 is run."""
        raise NotImplementedError

    def connect_signals_to_slots(self):
        """This method includes buttons common to all dialogs. Buttons that are
        specific to only a certain dialog are added in the subclassed version of the method."""
        raise NotImplementedError


    @logger.catch
    def close_event(self):
        """This is a generic close event function tied to certain buttons. Used if you don't want to override the
        base dialog. TODO: This should be refactored to a single closeEvent method."""
        self.close_window()

    @logger.catch
    def closeEvent(self, event):
        """This is the QDialog base version of the method that is being overriden here.
        Place any cleanup items (i.e. close_databases) here that should be
        called when the entry is created and the dialog closed."""
        self.close_window()

    def close_window(self):
        """Function connected to a button to close the window. Can be connected
        to any button press/click/release to close a window. This can also be called
        at the end of the close_event process to close the dialog."""
        self.close()

    def transfer_field_data_to_model(self, terms_object):
        """Function that loops through a list of fields and transfers the data in the field
        to the appropriate model attribute. The function uses the appropriate pyqt method for the field type.
        Format of item in terms_list is a list of tuples (item[0] = model data,
        item[1] = view field that contains the data)

        The try/except block accounts for dialogs that may not have an attribute from a terms_list."""
        terms_list = getattr(terms_object, "terms_list")
        for item in terms_list:
            (model_attribute, view_field) = item
            try:
                if isinstance(getattr(self, view_field), QComboBox):
                    setattr(terms_object, model_attribute, getattr(self, view_field).currentText())
                elif isinstance(getattr(self, view_field), QCheckBox):
                    setattr(terms_object, model_attribute, getattr(self, view_field).isChecked())
                elif isinstance(getattr(self, view_field), QRadioButton):
                    setattr(terms_object, model_attribute, getattr(self, view_field).isChecked())
                elif isinstance(getattr(self, view_field), QLineEdit):
                    setattr(terms_object, model_attribute, getattr(self, view_field).text())
                elif isinstance(getattr(self, view_field), QTextEdit):
                    plain_text = getattr(self, view_field).toPlainText()
                    try:
                        if plain_text[-1] == '.':
                            plain_text = plain_text[:-1]
                    except IndexError:
                        pass
                    setattr(terms_object, model_attribute, plain_text)
                elif isinstance(getattr(self, view_field), QDateEdit):
                    setattr(terms_object, model_attribute, getattr(self, view_field).date().toString("MMMM dd, yyyy"))
                elif isinstance(getattr(self, view_field), QTimeEdit):
                    setattr(terms_object, model_attribute, getattr(self, view_field).time().toString("hh:mm A"))
            except AttributeError:
                pass


class CriminalBaseDialog(BaseDialog):
    """This class subclasses the BaseDialog for methods that are specific to
    dialogs/entries that require entering a plea and finding in a cms_case.

    The self.charges_gridLayout class is changed so that the methods from the ChargesGrid
    custom widget can be used, but the design of a standard QtDesigner QGridLayout can be changed
    in QtDesigner and pyuic5 ran without needing to update the ui.py file each time."""
    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
        # open_databases() # This only seems necessary for testing as the connection is already opened when run as main.
        super().__init__(case_table, parent)
        self.judicial_officer = judicial_officer
        self.cms_case = cms_case
        self.entry_case_information = CriminalCaseInformation(self.judicial_officer)
        self.defense_counsel_name_box.__class__ = DefenseCounselComboBox
        self.defense_counsel_name_box.load_attorneys()
        self.criminal_charge = None

    def set_defense_counsel(self):
        if self.defense_counsel_waived_checkBox.isChecked():
            self.defense_counsel_name_box.setEnabled(False)
            self.defense_counsel_type_box.setEnabled(False)
        else:
            self.defense_counsel_name_box.setEnabled(True)
            self.defense_counsel_type_box.setEnabled(True)

    @logger.catch
    def load_cms_data_to_view(self):
        return CMSLoader(self)

    def close_event(self):
        """This method closes the databases before calling the base dialog close_event."""
        close_databases()
        super().close_event()

    @logger.catch
    def update_case_information(self):
        """Calls the class responsible for updating party and counsel information and plea date. The
        'self' that is passed is the dialog. It loads the information in those fields into the CriminalCaseInformation
        model attributes. PyCharm highlights potential error because that attributes are part of the
        CriminalCaseInformation model which is passed as self.entry_case_information."""
        return CasePartyUpdater(self)

    @logger.catch
    def add_plea_to_entry_case_information(self):
        """This method is never used directly. AddPlea is a pass-through for this case dialog. In the specific dialogs
        it will call to a subclassed version of AddPlea that is specific to the charges grid for that dialog."""
        return AddPlea(self)

    def set_plea_and_findings_process(self):
        self.charges_gridLayout.set_all_plea_and_findings(self)

    @logger.catch
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

    @logger.catch
    def start_amend_offense_dialog(self):
        self.update_case_information()
        AmendChargeDialog(self).exec()

    @logger.catch
    def start_add_charge_dialog(self):
        self.update_case_information()
        AddChargeDialog(self).exec()

    @logger.catch
    def set_pay_date(self, days_to_add):
        "Sets the sentencing date to the Tuesday (1) after the days added."""
        if days_to_add == "forthwith":
            self.balance_due_date.setDate(QDate.currentDate())
        else:
            total_days_to_add = set_future_date(days_to_add, PAY_DATE_DICT, 1)
            self.balance_due_date.setDate(QDate.currentDate().addDays(total_days_to_add))


class BaseChargeDialog(BaseDialog):
    @logger.catch
    def __init__(self, main_dialog, button_index=None, parent=None):
        self.main_dialog = main_dialog
        self.button_index = button_index
        charges_database.open()
        super().__init__(parent)
        self.set_statute_and_offense_choice_boxes()

    def set_statute_and_offense_choice_boxes(self):
        self.statute_choice_box.addItems(create_statute_list())
        self.offense_choice_box.addItems(create_offense_list())
        self.statute_choice_box.setCurrentText("")
        self.offense_choice_box.setCurrentText("")


class AddChargeDialog(BaseChargeDialog, Ui_AddChargeDialog):
    def __init__(self, main_dialog, parent=None):
        super().__init__(main_dialog, parent)

    def modify_view(self):
        return AddChargeDialogViewModifier(self)

    @logger.catch
    def connect_signals_to_slots(self):
        return AddChargeDialogSignalConnector(self)

    @logger.catch
    def add_charge_process(self):
        """The order of functions that are called when the add_charge_Button is
        clicked(). The order is important to make sure the information is
        updated before the charge is added and the data cleared from the fields."""
        self.add_charge_to_entry_case_information()
        self.main_dialog.add_charge_to_grid()
        self.close_event()

    @logger.catch
    def add_charge_to_entry_case_information(self):
        """TODO: self.criminal_charge_type needs to be fixed to add back in to get costs calculator to work
        again eventually."""
        self.criminal_charge = CriminalCharge()
        self.criminal_charge.offense = self.offense_choice_box.currentText()
        self.criminal_charge.statute = self.statute_choice_box.currentText()
        self.criminal_charge.degree = self.degree_choice_box.currentText()
        # self.criminal_charge.type = self.set_offense_type()
        self.main_dialog.entry_case_information.add_charge_to_list(self.criminal_charge)

    @logger.catch
    def clear_add_charge_fields(self):
        self.statute_choice_box.clearEditText()
        self.offense_choice_box.clearEditText()


class AmendChargeDialog(BaseChargeDialog, Ui_AmendChargeDialog):
    def __init__(self, main_dialog, parent=None):
        super().__init__(main_dialog, parent)
        self.amend_offense_details = AmendOffenseDetails()
        self.charge = self.sender().charge
        self.current_offense_name = self.sender().charge.offense
        self.original_charge_label.setText(self.current_offense_name)

    def modify_view(self):
        return AmendChargeDialogViewModifier(self)

    @logger.catch
    def connect_signals_to_slots(self):
        return AmendChargeDialogSignalConnector(self)

    @logger.catch
    def clear_amend_charge_fields(self):
        """Clears the fields in the view."""
        self.statute_choice_box.clearEditText()
        self.offense_choice_box.clearEditText()

    @logger.catch
    def amend_offense(self):
        """Adds the data entered for the amended offense to the AmendOffenseDetails
        object then points the entry_case_information object to the AmendOffenseDetails
        object."""
        self.amend_offense_details.original_charge = self.current_offense_name
        self.amend_offense_details.amended_charge = self.offense_choice_box.currentText()
        self.amend_offense_details.motion_disposition = self.motion_decision_box.currentText()
        self.main_dialog.entry_case_information.amend_offense_details = self.amend_offense_details
        if self.motion_decision_box.currentText() == "Granted":
            amended_charge = f"{self.current_offense_name} - AMENDED to {self.amend_offense_details.amended_charge}"
            setattr(self.charge, 'offense', amended_charge)
            self.main_dialog.entry_case_information.amended_charges_list.append(
                (self.amend_offense_details.original_charge, self.amend_offense_details.amended_charge)
            )
            for columns in range(self.main_dialog.charges_gridLayout.columnCount()):
                if (
                    self.main_dialog.charges_gridLayout.itemAtPosition(0, columns) is not None
                    and self.main_dialog.charges_gridLayout.itemAtPosition(
                        0, columns).widget().text() == self.current_offense_name
                ):
                    self.main_dialog.charges_gridLayout.itemAtPosition(0, columns).widget().setText(amended_charge)
                    self.main_dialog.charges_gridLayout.itemAtPosition(1, columns).widget().setText(self.statute_choice_box.currentText())
                    self.main_dialog.charges_gridLayout.itemAtPosition(2, columns).widget().setCurrentText(self.degree_choice_box.currentText())
        self.close_event()


class CasePartyUpdater:
    """Class responsible for updating case number, date, appearance reasons and party information. Top frame
    on primary dialogs."""
    def __init__(self, dialog):
        self.set_case_number_and_date(dialog)
        self.set_party_information(dialog)
        self.set_defense_counsel_information(dialog)
        self.set_appearance_reason(dialog)

    def set_case_number_and_date(self, dialog):
        dialog.entry_case_information.case_number = dialog.case_number_lineEdit.text()
        dialog.entry_case_information.plea_trial_date = dialog.plea_trial_date.date().toString("MMMM dd, yyyy")

    def set_party_information(self, dialog):
        dialog.entry_case_information.defendant.first_name = dialog.defendant_first_name_lineEdit.text()
        dialog.entry_case_information.defendant.last_name = dialog.defendant_last_name_lineEdit.text()

    def set_defense_counsel_information(self, dialog):
        dialog.entry_case_information.defense_counsel = dialog.defense_counsel_name_box.currentText()
        dialog.entry_case_information.defense_counsel_type = dialog.defense_counsel_type_box.currentText()
        dialog.entry_case_information.defense_counsel_waived = dialog.defense_counsel_waived_checkBox.isChecked()

    def set_appearance_reason(self, dialog):
        dialog.entry_case_information.appearance_reason = dialog.appearance_reason_box.currentText()


class CMSLoader:
    """Uses the cms_case number selected to get the cms_case object from main and load cms_case data."""
    def __init__(self, dialog):
        self.cms_case = dialog.cms_case
        self.criminal_charge = None
        self.load_cms_data(dialog)

    def load_cms_data(self, dialog):
        if self.cms_case.case_number is not None:
            dialog.case_number_lineEdit.setText(self.cms_case.case_number)
            dialog.defendant_first_name_lineEdit.setText(self.cms_case.defendant.first_name)
            dialog.defendant_last_name_lineEdit.setText(self.cms_case.defendant.last_name)
            self.add_cms_criminal_charges_to_entry_case_information(dialog)
        else:
            return None

    def add_cms_criminal_charges_to_entry_case_information(self, dialog):
        """Loads the data from the cms_case object that is created from the sql table.
        self.criminal_charge.type = self.set_offense_type() FIGURE OUT FOR COSTS"""
        for charge in self.cms_case.charges_list:
            self.criminal_charge = CriminalCharge()
            (self.criminal_charge.offense, self.criminal_charge.statute,
             self.criminal_charge.degree, self.criminal_charge.type) = charge
            dialog.entry_case_information.add_charge_to_list(self.criminal_charge)
            dialog.add_charge_to_grid()


class CMS_FRALoader(CMSLoader):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.add_fra_data(dialog)

    def add_fra_data(self, dialog):
        fra_value_dict = {"Y": "Yes", "N": "No", "U": "N/A"}
        if self.cms_case.case_number is None:
            dialog.fra_in_file_box.setCurrentText("N/A")
        elif self.cms_case.case_number[2:5] == "CRB":
            dialog.fra_frame.setHidden(True)
        elif self.cms_case.fra_in_file in fra_value_dict:
            dialog.fra_in_file_box.setCurrentText(fra_value_dict[self.cms_case.fra_in_file])
        else:
            dialog.fra_in_file_box.setCurrentText("N/A")
        dialog.set_fra_in_file(dialog.fra_in_file_box.currentText())
        dialog.set_fra_in_court(dialog.fra_in_court_box.currentText())


class AddPlea:
    """This class is specifically implemented for each main dialog with a more specific name."""
    pass


if __name__ == "__main__":
    print("BCD ran directly")
else:
    print("BCD ran when imported")
    charges_database = open_charges_db_connection()
