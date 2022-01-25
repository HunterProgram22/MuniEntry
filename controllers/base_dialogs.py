"""The BaseDialogs modules contains common base classes from which other dialogs inherit."""
import os
import time
from win32com import client

from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtSql import QSqlQuery, QSqlDatabase
from PyQt5.QtWidgets import QDialog, QMessageBox, QComboBox, QCheckBox, QLineEdit, QTextEdit, QDateEdit
from PyQt5 import QtGui
from controllers.helper_functions import set_document_name
from docxtpl import DocxTemplate
from loguru import logger
from models.case_information import CriminalCaseInformation, CriminalCharge, AmendOffenseDetails
from resources.db.create_data_lists import create_statute_list, create_offense_list
from settings import CHARGES_DATABASE, SAVE_PATH
from views.amend_offense_dialog_ui import Ui_AmendOffenseDialog
from views.custom_widgets import PleaComboBox, WarningBox, RequiredBox
from settings import PAY_DATE_DICT
from controllers.helper_functions import set_future_date


@logger.catch
def create_database_connections():
    """The databases for the application are created upon import of the module, which is done
    on application startup. The connections to the databases are created, but the opening and
    closing of the databases is handled by the appropriate class dialog."""
    offense_database_connection = QSqlDatabase.addDatabase("QSQLITE", "offenses")
    offense_database_connection.setDatabaseName(CHARGES_DATABASE)
    return offense_database_connection


def open_databases():
    database_offenses.open()


def close_databases():
    """Closes any databases that were opened at the start of the dialog."""
    database_offenses.close()
    database_offenses.removeDatabase(CHARGES_DATABASE)


def print_document(docname):
    word = client.Dispatch("Word.Application")
    word.Documents.Open(SAVE_PATH + docname)
    word.ActiveDocument.PrintOut()
    time.sleep(1)
    word.ActiveDocument.Close()
    word.Quit()


@logger.catch
def print_entry(dialog):
    """Loads the proper template and creates the entry.
    TODO: This is duplicative of create_entry need to refactor."""
    doc = DocxTemplate(dialog.template.template_path)
    doc.render(dialog.entry_case_information.get_case_information())
    docname = set_document_name(dialog)
    try:
        doc.save(SAVE_PATH + docname)
        print_document(docname)
        os.startfile(SAVE_PATH + docname)
    except PermissionError:
        message = RequiredBox("An entry for this case is already open in Word."
                              " You must close the Word document first.")
        message.exec()


@logger.catch
def create_entry(dialog):
    """Loads the proper template and creates the entry."""
    doc = DocxTemplate(dialog.template.template_path)
    doc.render(dialog.entry_case_information.get_case_information())
    docname = set_document_name(dialog)
    try:
        doc.save(SAVE_PATH + docname)
        os.startfile(SAVE_PATH + docname)
    except PermissionError:
        message = RequiredBox("An entry for this case is already open in Word."
                              " You must close the Word document first.")
        message.exec()


class BaseDialog(QDialog):
    """This class is a base class to provide methods that are used by some criminal controllers
     in the application. This class is never instantiated as its own dialog, but the init contains
     the setup for all inherited class controllers."""
    def __init__(self, parent=None):
        """Databases must be opened first in order for them to be accessed
        when the UI is built so it can populate fields.The setupUI calls to
        the view to create the UI."""
        super().__init__(parent)
        self.setWindowIcon(QtGui.QIcon('./resources/icons/gavel.ico'))
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint |
                            QtCore.Qt.WindowMaximizeButtonHint)
        self.setupUi(self)
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

    def close_event(self):
        """Place any cleanup items (i.e. close_databases) here that should be
        called when the entry is created and the dialog closed."""
        self.close_window()

    def close_window(self):
        """Function connected to a button to close the window. Can be connected
        to any button press/click/release to close a window. This can also be called
        at the end of the close_event process to close the dialog."""
        self.close()

    def widget_type_check_set(self, terms_object, terms_list):
        """Function that loops through a list of fields and transfers the data in the field
        to the appropriate object. Format of terms_list is a list of tuples (item[0] = model data,
        item[1] = view field)"""
        for item in terms_list:
            if isinstance(getattr(self, item[1]), QComboBox):
                setattr(terms_object, item[0], getattr(self, item[1]).currentText())
            elif isinstance(getattr(self, item[1]), QCheckBox):
                setattr(terms_object, item[0], getattr(self, item[1]).isChecked())
            elif isinstance(getattr(self, item[1]), QLineEdit):
                setattr(terms_object, item[0], getattr(self, item[1]).text())
            elif isinstance(getattr(self, item[1]), QTextEdit):
                setattr(terms_object, item[0], getattr(self, item[1]).toPlainText())
            elif isinstance(getattr(self, item[1]), QDateEdit):
                setattr(terms_object, item[0], getattr(self, item[1]).date().toString("MMMM dd, yyyy"))


class CasePartyUpdater:
    """Class responsible for updating case number, date and party information. Top frame
    on primary dialogs."""
    def __init__(self, dialog):
        self.case_number = dialog.case_number_lineEdit.text()
        self.plea_trial_date = dialog.plea_trial_date.date().toString("MMMM dd, yyyy")
        self.defendant_first_name = dialog.defendant_first_name_lineEdit.text()
        self.defendant_last_name = dialog.defendant_last_name_lineEdit.text()
        self.set_case_number_and_date(dialog)
        self.set_party_information(dialog)
        try:
            self.set_defense_counsel_information(dialog)
        except AttributeError:
            pass

    def set_case_number_and_date(self, dialog):
        dialog.entry_case_information.case_number = self.case_number
        dialog.entry_case_information.plea_trial_date = self.plea_trial_date

    def set_party_information(self, dialog):
        """Updates the party information from the GUI(view) and saves it to the model."""
        dialog.entry_case_information.defendant.first_name = self.defendant_first_name
        dialog.entry_case_information.defendant.last_name = self.defendant_last_name

    def set_defense_counsel_information(self, dialog):
        dialog.entry_case_information.defense_counsel = dialog.defense_counsel_name.text()
        dialog.entry_case_information.defense_counsel_type = dialog.defense_counsel_type_box.currentText()
        dialog.entry_case_information.defense_counsel_waived = dialog.defense_counsel_waived_checkBox.isChecked()


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
             self.criminal_charge.degree) = charge
            dialog.entry_case_information.add_charge_to_list(self.criminal_charge)
            dialog.add_charge_to_grid()


class CMS_FRALoader(CMSLoader):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.add_fra_data(dialog)

    def add_fra_data(self, dialog):
        fra_value_dict = {"Y": "Yes", "N": "No", "U": "N/A"}
        if self.cms_case.fra_in_file in fra_value_dict:
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
        """The order of the create entry process is important to make sure the
        information is updated before the entry is created."""
        dialog.update_case_information()
        if dialog.charges_gridLayout.check_plea_and_findings() is None:
            return None
        if (
            hasattr(dialog, 'fra_in_file_box')
            and dialog.fra_in_file_box.currentText() == "No"
            and dialog.fra_in_court_box.currentText() == "N/A"
        ):
            message = WarningBox("The information provided currently "
                                 "indicates insurance was not shown in the file. "
                                 "There is no information on whether "
                                 "defendant showed proof of insurance "
                                 "in court. \n\nDo you wish to create an entry "
                                 "without indicating whether insurance was "
                                 "shown in court?")
            return_value = message.exec()
            if return_value == QMessageBox.No:
                return None
        create_entry(dialog)

    @classmethod
    @logger.catch
    def close_dialog(cls, dialog):
        dialog.close_event()

    @classmethod
    @logger.catch
    def print_entry_process(cls, dialog):
        """The order of the create entry process is important to make sure the
        information is updated before the entry is created.
        TODO: This is duplicate of create_entry_process need to refactor."""
        dialog.update_case_information()
        if dialog.charges_gridLayout.check_plea_and_findings() is None:
            return None
        if (
            hasattr(dialog, 'fra_in_file_box')
            and dialog.fra_in_file_box.currentText() == "No"
            and dialog.fra_in_court_box.currentText() == "N/A"
        ):
            message = WarningBox("The information provided currently "
                                 "indicates insurance was not shown in the file. "
                                 "There is no information on whether "
                                 "defendant showed proof of insurance "
                                 "in court. \n\nDo you wish to create an entry "
                                 "without indicating whether insurance was "
                                 "shown in court?")
            return_value = message.exec()
            if return_value == QMessageBox.No:
                return None
        print_entry(dialog)

    @classmethod
    def clear_charge_fields(cls, dialog):
        """Clears the fields that are used for adding a charge. The statute_choice_box and
        offense_choice_box use the clearEditText method because those boxes are editable."""
        dialog.statute_choice_box.clearEditText()
        dialog.offense_choice_box.clearEditText()

    @classmethod
    @logger.catch
    def add_charge_process(cls, dialog):
        """The order of functions that are called when the add_charge_Button is
        clicked(). The order is important to make sure the information is
        updated before the charge is added and the data cleared from the fields."""
        dialog.add_charge_to_entry_case_information()
        dialog.add_charge_to_grid()
        CriminalSlotFunctions.clear_charge_fields(dialog)

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
        query = QSqlQuery(database_offenses)
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
    """Row 3 - plea when no allied checkbox added. Column starts at 1
    because column 0 is labels. The grid adds an empty column every time a
    charge is added, could increment by 2, but by incrementing by 1 and
    checking for None it ensures it will catch any weird add/delete.
    This method only adds the plea and is used in LEAP short and long and
    Not Guilty. No Jail Plea and Jail CC Plea overrides this to include findings and fines.
    TODO: Rename and refactor out magic numbers. REFACTOR to CLASS and call class in subclass for dialog."""
    def __init__(self, dialog):
        self.dialog = dialog
        self.column = 1
        self.row = 3
        for charge in self.dialog.entry_case_information.charges_list:
            while self.dialog.charges_gridLayout.itemAtPosition(self.row, self.column) is None:
                self.column += 1
            charge.statute = self.dialog.charges_gridLayout.itemAtPosition(
                1, self.column).widget().text()
            charge.degree = self.dialog.charges_gridLayout.itemAtPosition(
                2, self.column).widget().currentText()
            if isinstance(self.dialog.charges_gridLayout.itemAtPosition(
                    self.row, self.column).widget(), PleaComboBox):
                charge.plea = self.dialog.charges_gridLayout.itemAtPosition(
                    self.row, self.column).widget().currentText()
                self.column += 1
            self.column += 1


class CriminalBaseDialog(BaseDialog):
    """This class subclasses the BaseDialog for methods that are specific to
    dialogs/entries that require entering a plea and finding in a cms_case.

    The self.charges_gridLayout class is changed so that the methods from the ChargesGrid
    custom widget can be used, but the design of a standard QtDesigner QGridLayout can be changed
    in QtDesigner and pyuic5 ran without needing to update the ui.py file each time."""
    def __init__(self, judicial_officer, cms_case=None, parent=None):
        open_databases()
        super().__init__(parent)
        self.judicial_officer = judicial_officer
        self.cms_case = cms_case
        self.entry_case_information = CriminalCaseInformation(self.judicial_officer)
        self.criminal_charge = None
        self.delete_button_list = []
        self.amend_button_list = []

    def modify_view(self):
        self.plea_trial_date.setDate(QtCore.QDate.currentDate())
        self.set_statute_and_offense_choice_boxes()

    def set_statute_and_offense_choice_boxes(self):
        self.statute_choice_box.addItems(create_statute_list())
        self.offense_choice_box.addItems(create_offense_list())
        self.statute_choice_box.setCurrentText("")
        self.offense_choice_box.setCurrentText("")

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
        self.add_charge_Button.pressed.connect(
            lambda dialog=self: CriminalSlotFunctions.add_charge_process(dialog))
        self.clear_fields_charge_Button.pressed.connect(
            lambda dialog=self: CriminalSlotFunctions.clear_charge_fields(dialog))
        self.statute_choice_box.currentTextChanged.connect(
            lambda key, dialog=self: CriminalSlotFunctions.set_statute_and_offense(key, dialog))
        self.offense_choice_box.currentTextChanged.connect(
            lambda key, dialog=self: CriminalSlotFunctions.set_statute_and_offense(key, dialog))

    # CMS Loader Functions - REFACTORED and WORKING
    @logger.catch
    def load_cms_data_to_view(self):
        return CMSLoader(self)

    # Criminal DialogCleanUp Functions
    def close_event(self):
        """This method closes the databases before calling the base dialog close_event."""
        close_databases()
        super().close_event()

    # Criminal CasePartyUpdater Functions - REFACTORED and WORKING
    @logger.catch
    def update_case_information(self):
        """TODO: This needs to be fixed it might update case information with blanks."""
        """"Docstring needs updating."""
        return CasePartyUpdater(self)

    # Modify Entry Case Information Functions - REFACTORED and WORKING
    @logger.catch
    def add_plea_to_entry_case_information(self):
        return AddPlea(self)

    # Slot Functions
    @logger.catch
    def add_charge_to_entry_case_information(self):
        """The offense, statute and degree are added to the view by the method
        add_charge_to_view, not this method. This method is triggered on
        clicked() of the Add Charge button."""
        self.criminal_charge = CriminalCharge()
        self.criminal_charge.offense = self.offense_choice_box.currentText()
        self.criminal_charge.statute = self.statute_choice_box.currentText()
        self.criminal_charge.degree = self.degree_choice_box.currentText()
        self.criminal_charge.type = self.set_offense_type()
        self.entry_case_information.add_charge_to_list(self.criminal_charge)

    # Setter Functions
    def set_plea_and_findings_process(self):
        self.charges_gridLayout.set_all_plea_and_findings(self)

    @logger.catch
    def set_offense_type(self):
        """This calls the database_statutes and behind the scenes sets the appropriate cms_case type
        for each charge. It does not show up in the view, but is used for calculating costs."""
        key = self.statute_choice_box.currentText()
        if self.freeform_entry_checkBox.isChecked():
            return None
        query = QSqlQuery(database_offenses)
        query.prepare("SELECT * FROM charges WHERE statute LIKE '%' || :key || '%'")
        query.bindValue(":key", key)
        query.exec()
        while query.next():
            statute = query.value(2)
            offense_type = query.value(4)
            if statute == key:
                query.finish()
                return offense_type

    # Move to Charges Grid Widget Class (?)
    @logger.catch
    def delete_charge(self):
        """Deletes the offense from the entry_case_information.charges list. Then
        decrements the total charges by one so that other functions using the
        total charges for indexing are correct."""
        index = self.delete_button_list.index(self.sender())
        del self.entry_case_information.charges_list[index]
        del self.delete_button_list[index]
        self.charges_gridLayout.delete_charge_from_grid()
        self.statute_choice_box.setFocus()

    @logger.catch
    def start_amend_offense_dialog(self, _bool):
        """Opens the amend offense dialog as a modal window. The
        entry_case_information is passed to the dialog class in order to populate
        the cms_case information banner. The _bool is from clicked and not used."""
        self.update_case_information()
        button_index = self.amend_button_list.index(self.sender())
        AmendOffenseDialog(self, self.entry_case_information, button_index).exec()

    @logger.catch
    def set_pay_date(self, days_to_add):
        "Sets the sentencing date to the Tuesday (1) after the days added."""
        total_days_to_add = set_future_date(days_to_add, PAY_DATE_DICT, 1)
        self.balance_due_date.setDate(QDate.currentDate().addDays(total_days_to_add))


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
            amended_charge = self.current_offense + " - AMENDED"
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
    database_offenses = create_database_connections()
