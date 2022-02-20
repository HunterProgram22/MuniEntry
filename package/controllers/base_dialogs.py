"""The BaseDialogs modules contains common base classes from which other dialogs inherit."""
import os
import time

from docxtpl import DocxTemplate
from loguru import logger
from win32com import client
from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QDialog, QComboBox, QCheckBox, QLineEdit, QTextEdit, QDateEdit, QTimeEdit
from PyQt5 import QtGui

from db.databases import open_charges_db_connection, extract_data, create_offense_list, create_statute_list
from package.controllers.helper_functions import set_document_name, set_future_date, InfoChecker
from package.models.case_information import CriminalCaseInformation, CriminalCharge, AmendOffenseDetails
from package.views.add_charge_dialog_ui import Ui_AddChargeDialog
from package.views.amend_offense_dialog_ui import Ui_AmendOffenseDialog
from package.views.custom_widgets import RequiredBox, DefenseCounselComboBox
from settings import PAY_DATE_DICT, SAVE_PATH


def close_databases():
    charges_database.close()
    charges_database.removeDatabase("QSQLITE")


def print_document(docname):
    word = client.Dispatch("Word.Application")
    word.Documents.Open(SAVE_PATH + docname)
    word.ActiveDocument.PrintOut()
    time.sleep(1)
    word.ActiveDocument.Close()
    word.Quit()


@logger.catch
def create_entry(dialog, print_doc=False):
    """Loads the proper template and creates the entry."""
    doc = DocxTemplate(dialog.template.template_path)
    case_data = dialog.entry_case_information.get_case_information()
    extract_data(case_data)
    doc.render(case_data)
    docname = set_document_name(dialog)
    try:
        doc.save(SAVE_PATH + docname)
        if print_doc is True:
            print_document(docname)
        os.startfile(SAVE_PATH + docname)
    except PermissionError:
        message = RequiredBox("An entry for this case is already open in Word."
                              " You must close the Word document first.")
        message.exec()


class BaseDialog(QDialog):
    """This class is a base class to provide methods that are used by some criminal controllers
     in the application. This class is never instantiated as its own dialog, but the init contains
     the setup for all inherited class controllers."""
    def __init__(self, case_table=None, parent=None):
        """Databases must be opened first in order for them to be accessed
        when the UI is built so it can populate fields.The setupUI calls to
        the view to create the UI."""
        super().__init__(parent)
        self.setWindowIcon(QtGui.QIcon('./icons/gavel.ico'))
        self.setWindowFlags(self.windowFlags() |
                            QtCore.Qt.CustomizeWindowHint |
                            QtCore.Qt.WindowMaximizeButtonHint |
                            QtCore.Qt.WindowCloseButtonHint)
        self.setupUi(self)
        self.case_table = case_table
        self.modify_view()
        self.connect_signals_to_slots()

    def modify_view(self):
        """The modify view method updates the view that is created on init with self.setupUI.
        Place items in this method that can't be added directly in QtDesigner (or are more easily added later)
        so that they don't need to be changed in the view file each time pyuic5 is run."""
        pass

    def connect_signals_to_slots(self):
        """This method includes buttons common to all dialogs. Buttons that are
        specific to only a certain dialog are added in the subclassed version of the method."""
        self.cancel_Button.pressed.connect(self.close_event)

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
        item[1] = view field that contains the data)"""
        terms_list = getattr(terms_object, "terms_list")
        for item in terms_list:
            (model_attribute, view_field) = item
            if isinstance(getattr(self, view_field), QComboBox):
                setattr(terms_object, model_attribute, getattr(self, view_field).currentText())
            elif isinstance(getattr(self, view_field), QCheckBox):
                setattr(terms_object, model_attribute, getattr(self, view_field).isChecked())
            elif isinstance(getattr(self, view_field), QLineEdit):
                setattr(terms_object, model_attribute, getattr(self, view_field).text())
            elif isinstance(getattr(self, view_field), QTextEdit):
                setattr(terms_object, model_attribute, getattr(self, view_field).toPlainText())
            elif isinstance(getattr(self, view_field), QDateEdit):
                setattr(terms_object, model_attribute, getattr(self, view_field).date().toString("MMMM dd, yyyy"))
            elif isinstance(getattr(self, view_field), QTimeEdit):
                setattr(terms_object, model_attribute, getattr(self, view_field).time().toString("hh:mm A"))


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
        self.delete_button_list = []
        self.amend_button_list = []

    def modify_view(self):
        self.plea_trial_date.setDate(QtCore.QDate.currentDate())
        if self.case_table == "final_pretrials":
            self.appearance_reason_box.setCurrentText("change of plea")

    def connect_signals_to_slots(self):
        """This method extends the base_dialog method to add additional signals
        and slots to be connected. The lambda function is used because it needs the dialog to be
        passed as an argument (dialog = self) and if it is connected without lambda it would be called on
        dialog creation instead of upon button pressed."""
        super().connect_signals_to_slots()
        self.clear_fields_case_Button.pressed.connect(
            lambda dialog=self: CriminalSlotFunctions.clear_case_information_fields(dialog))
        self.create_entry_Button.pressed.connect(
            lambda dialog=self: CriminalSlotFunctions.create_entry_process(dialog))
        try:
            """This is part of a try/except because the JailCC Dialog doesnt currently have a print button, but might
            eventually."""
            self.print_entry_Button.pressed.connect(
                lambda dialog=self: CriminalSlotFunctions.print_entry_process(dialog))
        except AttributeError:
            pass
        self.close_dialog_Button.pressed.connect(
            lambda dialog=self: CriminalSlotFunctions.close_dialog(dialog))
        self.add_charge_Button.clicked.connect(self.start_add_charge_dialog)
        self.defense_counsel_waived_checkBox.toggled.connect(self.set_defense_counsel)

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
    def delete_charge(self):
        """Deletes the offense from the entry_case_information.charges list. Then
        decrements the total charges by one so that other functions using the
        total charges for indexing are correct."""
        index = self.delete_button_list.index(self.sender())
        del self.entry_case_information.charges_list[index]
        del self.delete_button_list[index]
        self.charges_gridLayout.delete_charge_from_grid()
        try: # This try/except is to account for not guilty button on Not Guilty dialog
            self.guilty_all_Button.setFocus()
        except AttributeError:
            self.not_guilty_all_Button.setFocus()

    @logger.catch
    def start_amend_offense_dialog(self, _bool):
        """Opens the amend offense dialog as a modal window. The
        entry_case_information is passed to the dialog class in order to populate
        the cms_case information banner. The _bool is from clicked and not used."""
        self.update_case_information()
        button_index = self.amend_button_list.index(self.sender())
        AmendOffenseDialog(self, self.entry_case_information, button_index).exec()

    @logger.catch
    def start_add_charge_dialog(self, _bool):
        """Opens the amend offense dialog as a modal window. The
        entry_case_information is passed to the dialog class in order to populate
        the cms_case information banner. The _bool is from clicked and not used."""
        self.update_case_information()
        AddChargeDialog(self, self.entry_case_information).exec()

    @logger.catch
    def set_pay_date(self, days_to_add):
        "Sets the sentencing date to the Tuesday (1) after the days added."""
        total_days_to_add = set_future_date(days_to_add, PAY_DATE_DICT, 1)
        self.balance_due_date.setDate(QDate.currentDate().addDays(total_days_to_add))


class AddChargeDialog(BaseDialog, Ui_AddChargeDialog):
    """The AddOffenseDialog is created when the amend_button is pressed for a specific charge.
    The cms_case information is passed in order to populate the cms_case information banner. The
    button_index is to determine which charge the amend_button is amending."""
    @logger.catch
    def __init__(self, main_dialog, case_information, parent=None):
        self.main_dialog = main_dialog
        self.case_information = case_information
        charges_database.open()
        super().__init__(parent)
        self.set_case_information_banner()
        self.set_statute_and_offense_choice_boxes()

    @logger.catch
    def modify_view(self):
        """The modify view sets the original charge based on the item in the main dialog
        for which amend button was pressed."""
        pass

    def set_statute_and_offense_choice_boxes(self):
        self.statute_choice_box.addItems(create_statute_list())
        self.offense_choice_box.addItems(create_offense_list())
        self.statute_choice_box.setCurrentText("")
        self.offense_choice_box.setCurrentText("")

    @logger.catch
    def connect_signals_to_slots(self):
        """TODO: The statute/offense connections can probably be moved to this dialog directly."""
        self.statute_choice_box.currentTextChanged.connect(
            lambda key, dialog=self: CriminalSlotFunctions.set_statute_and_offense(key, dialog))
        self.offense_choice_box.currentTextChanged.connect(
            lambda key, dialog=self: CriminalSlotFunctions.set_statute_and_offense(key, dialog))
        self.clear_fields_Button.pressed.connect(self.clear_add_charge_fields)
        self.add_charge_Button.pressed.connect(self.add_charge_process)
        self.cancel_Button.pressed.connect(self.close_event)

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
        self.case_information.add_charge_to_list(self.criminal_charge)

    @logger.catch
    def set_case_information_banner(self):
        """Sets the banner on a view of the interface. It modifies label
        widgets on the view to text that was entered."""
        self.defendant_name_label.setText(
            "State of Ohio v. {defendant_first_name} {defendant_last_name}".format(
                defendant_first_name=self.case_information.defendant.first_name,
                defendant_last_name=self.case_information.defendant.last_name
            )
        )
        self.case_number_label.setText(self.case_information.case_number)

    @logger.catch
    def clear_add_charge_fields(self):
        self.statute_choice_box.clearEditText()
        self.offense_choice_box.clearEditText()


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
            dialog.fra_in_file_box.setCurrentText("N/A")
        elif self.cms_case.fra_in_file in fra_value_dict:
            dialog.fra_in_file_box.setCurrentText(fra_value_dict[self.cms_case.fra_in_file])
        else:
            dialog.fra_in_file_box.setCurrentText("N/A")
        dialog.set_fra_in_file(dialog.fra_in_file_box.currentText())
        dialog.set_fra_in_court(dialog.fra_in_court_box.currentText())


class CriminalSlotFunctions:
    """Class for common criminal functions that are connected to slots/buttons in a dialog."""
    @classmethod
    @logger.catch
    def clear_case_information_fields(cls, dialog):
        """Clears the text in the fields in the top cms_case information frame and resets the cursor
        to the first text entry (defendant_first_name_lineEdit) box."""
        dialog.defendant_first_name_lineEdit.clear()
        dialog.defendant_last_name_lineEdit.clear()
        dialog.case_number_lineEdit.clear()
        dialog.defendant_first_name_lineEdit.setFocus()

    @classmethod
    @logger.catch
    def create_entry_process(cls, dialog):
        """The info_checks variable is either "Pass" or "Fail" based on the checks performed by the
        update_info_and_perform_checks method (found in helper_functions.py)."""
        info_checks = cls.update_info_and_perform_checks(dialog)
        if info_checks == "Pass":
            create_entry(dialog)

    @classmethod
    @logger.catch
    def print_entry_process(cls, dialog):
        info_checks = cls.update_info_and_perform_checks(dialog)
        if info_checks == "Pass":
            create_entry(dialog, print_doc=True)

    @classmethod
    @logger.catch
    def update_info_and_perform_checks(cls, dialog):
        dialog.update_case_information()
        if InfoChecker.check_defense_counsel(dialog) == "Fail":
            return "Fail"
        if InfoChecker.check_plea_and_findings(dialog) == "Fail":
            return "Fail"
        if InfoChecker.check_insurance(dialog) == "Fail":
            return "Fail"
        if InfoChecker.check_bond_amount(dialog) == "Fail":
            return "Fail"
        if InfoChecker.check_license_suspension(dialog) == "Fail":
            return "Fail"
        dialog.update_case_information()
        return "Pass"

    @classmethod
    @logger.catch
    def close_dialog(cls, dialog):
        dialog.close_event()


    @classmethod
    @logger.catch
    def set_statute_and_offense(cls, key, dialog):
        """:key: is the string that is passed by the function each time the field
        is changed on the view."""
        field = None
        if dialog.freeform_entry_checkBox.isChecked():
            return None
        if dialog.sender() == dialog.statute_choice_box:
            field = 'statute'
        elif dialog.sender() == dialog.offense_choice_box:
            field = 'offense'
        query = QSqlQuery(charges_database)
        query_string = f"SELECT * FROM charges WHERE {field} LIKE '%' || :key || '%'"
        query.prepare(query_string)
        query.bindValue(":key", key)
        query.bindValue(field, field)
        query.exec()
        while query.next():
            offense = query.value(1)
            statute = query.value(2)
            degree = query.value(3)
            if field == 'offense':
                if offense == key:
                    dialog.statute_choice_box.setCurrentText(statute)
            elif field == 'statute':
                if statute == key:
                    dialog.offense_choice_box.setCurrentText(offense)
            dialog.degree_choice_box.setCurrentText(degree)
            query.finish()
            break


class AddPlea:
    """This class is specifically implemented for each main dialog with a more specific name."""
    pass


class AmendOffenseDialog(BaseDialog, Ui_AmendOffenseDialog):
    """The AddOffenseDialog is created when the amend_button is pressed for a specific charge.
    The cms_case information is passed in order to populate the cms_case information banner. The
    button_index is to determine which charge the amend_button is amending."""
    @logger.catch
    def __init__(self, main_dialog, case_information, button_index, parent=None):
        self.button_index = button_index
        self.main_dialog = main_dialog
        self.case_information = case_information
        self.amend_offense_details = AmendOffenseDetails()
        self.current_offense = self.case_information.charges_list[self.button_index].offense
        super().__init__(parent)
        self.set_case_information_banner()

    @logger.catch
    def modify_view(self):
        """The modify view sets the original charge based on the item in the main dialog
        for which amend button was pressed."""
        self.original_charge_box.setCurrentText(self.current_offense)
        self.amended_charge_box.addItems(create_offense_list())

    @logger.catch
    def connect_signals_to_slots(self):
        """This method overrides the base_dialog method to connect signals and
        slots specific to the amend_offense dialog."""
        self.clear_fields_Button.pressed.connect(self.clear_amend_charge_fields)
        self.amend_offense_Button.pressed.connect(self.amend_offense)
        self.cancel_Button.pressed.connect(self.close_event)

    @logger.catch
    def set_case_information_banner(self):
        """Sets the banner on a view of the interface. It modifies label
        widgets on the view to text that was entered."""
        self.defendant_name_label.setText(
            "State of Ohio v. {defendant_first_name} {defendant_last_name}".format(
                defendant_first_name=self.case_information.defendant.first_name,
                defendant_last_name=self.case_information.defendant.last_name
            )
        )
        self.case_number_label.setText(self.case_information.case_number)

    @logger.catch
    def clear_amend_charge_fields(self):
        """Clears the fields in the view."""
        self.original_charge_box.clearEditText()
        self.amended_charge_box.clearEditText()

    @logger.catch
    def amend_offense(self):
        """Adds the data entered for the amended offense to the AmendOffenseDetails
        object then points the entry_case_information object to the AmendOffenseDetails
        object."""
        self.amend_offense_details.original_charge = self.original_charge_box.currentText()
        self.amend_offense_details.amended_charge = self.amended_charge_box.currentText()
        self.amend_offense_details.motion_disposition = self.motion_decision_box.currentText()
        self.case_information.amend_offense_details = self.amend_offense_details
        if self.motion_decision_box.currentText() == "Granted":
            amended_charge = f"{self.current_offense} - AMENDED to {self.amend_offense_details.amended_charge}"
            self.case_information.charges_list[self.button_index].offense = amended_charge
            self.case_information.amended_charges_list.append(
                (self.original_charge_box.currentText(), self.amended_charge_box.currentText())
            )
            for columns in range(self.main_dialog.charges_gridLayout.columnCount()):
                if (
                    self.main_dialog.charges_gridLayout.itemAtPosition(0, columns) is not None
                    and self.main_dialog.charges_gridLayout.itemAtPosition(
                        0, columns).widget().text() == self.current_offense
                ):
                    self.main_dialog.charges_gridLayout.itemAtPosition(0, columns).widget().setText(amended_charge)
        self.close_event()


if __name__ == "__main__":
    print("BCD ran directly")
else:
    print("BCD ran when imported")
    charges_database = open_charges_db_connection()
