"""The BaseDialogs modules contains common base classes from which other dialogs inherit."""
import os

from PyQt5 import QtCore
from PyQt5.QtSql import QSqlQuery, QSqlDatabase
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtGui
from controllers.helper_functions import set_document_name
from docxtpl import DocxTemplate
from loguru import logger
from models.case_information import CriminalCaseInformation, CriminalCharge
from resources.db.create_data_lists import create_statute_list, create_offense_list
from settings import CHARGES_DATABASE, SAVE_PATH
from views.custom_widgets import ChargesGrid, PleaComboBox


@logger.catch
def create_entry(dialog):
    """Loads the proper template and creates the entry."""
    doc = DocxTemplate(dialog.template.template_path)
    doc.render(dialog.entry_case_information.get_case_information())
    docname = set_document_name(dialog)
    doc.save(SAVE_PATH + docname)
    os.startfile(SAVE_PATH + docname)


class BaseDialog(QDialog):
    """This class is a base class to provide methods that are used by some criminal controllers
     in the application. This class is never instantiated as its own dialog, but the init contains
     the setup for all inherited class controllers."""
    def __init__(self, parent=None):
        """Databases must be opened first in order for them to be accessed
        when the UI is built so it can populate fields.The setupUI calls to
        the view to create the UI."""
        super().__init__(parent)
        self.setWindowIcon(QtGui.QIcon('./resources/icons/gavel.jpg'))
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
        specific to only a certain dialog are added in the subclassed version of the method.

        The create entry process is connected with a lambda function because it needs the dialog to be
        passed as an argument (dialog = self) and if it is connected without lambda it would be called on
        dialog creation instead of upon button pressed."""
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


class CriminalBaseDialog(BaseDialog):
    """This class subclasses the BaseDialog for methods that are specific to
    dialogs/entries that require entering a plea and finding in a cms_case.

    The self.charges_gridLayout class is changed so that the methods from the ChargesGrid
    custom widget can be used, but the design of a standard QtDesigner QGridLayout can be changed
    in QtDesigner and pyuic5 ran without needing to update the ui.py file each time."""
    # INIT Functions
    def __init__(self, judicial_officer, cms_case=None, parent=None):
        open_databases()
        super().__init__(parent)
        self.judicial_officer = judicial_officer
        self.cms_case = cms_case
        try:
            self.charges_gridLayout.__class__ = ChargesGrid
        except AttributeError:
            pass
        self.entry_case_information = CriminalCaseInformation(self.judicial_officer)
        self.criminal_charge = None
        self.delete_button_list = []
        self.amend_button_list = []
        self.load_cms_data_to_view()

    def modify_view(self):
        self.plea_trial_date.setDate(QtCore.QDate.currentDate())
        self.set_statute_and_offense_choice_boxes()

    def connect_signals_to_slots(self):
        """This method extends the base_dialog method to add additional signals
        and slots to be connected."""
        super().connect_signals_to_slots()
        self.clear_fields_case_Button.pressed.connect(self.clear_case_information_fields)
        self.create_entry_Button.pressed.connect(self.create_entry_process)
        self.add_charge_Button.clicked.connect(self.add_charge_process)
        self.clear_fields_charge_Button.pressed.connect(self.clear_charge_fields)
        self.statute_choice_box.currentTextChanged.connect(self.set_statute_and_offense)
        self.offense_choice_box.currentTextChanged.connect(self.set_statute_and_offense)

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
        """"Docstring needs updating."""
        return CasePartyUpdater(self)

    # Modify Case Information Functions
    @logger.catch
    def add_dispositions_and_fines(self):
        """Row 3 - plea when no allied checkbox added. Column starts at 1
        because column 0 is labels. The grid adds an empty column every time a
        charge is added, could increment by 2, but by incrementing by 1 and
        checking for None it ensures it will catch any weird add/delete.
        This method only adds the plea and is used in LEAP short and long and
        Not Guilty. No Jail Plea overrides this to include findings and fines.
        TODO: Rename and refactor out magic numbers."""
        column = 1
        row = 3
        for index, charge in enumerate(self.entry_case_information.charges_list):
            while self.charges_gridLayout.itemAtPosition(row, column) is None:
                column += 1
            if isinstance(self.charges_gridLayout.itemAtPosition(
                          row, column).widget(), PleaComboBox):
                charge.plea = self.charges_gridLayout.itemAtPosition(
                              row, column).widget().currentText()
                column += 1
            column += 1

    # Slot Functions
    @logger.catch
    def clear_case_information_fields(self):
        """Clears the text in the fields in the top cms_case information frame and resets the cursor
        to the first text entry (defendant_first_name_lineEdit) box."""
        self.defendant_first_name_lineEdit.clear()
        self.defendant_last_name_lineEdit.clear()
        self.case_number_lineEdit.clear()
        self.defendant_first_name_lineEdit.setFocus()

    @logger.catch
    def add_charge_process(self, _bool):
        """The order of functions that are called when the add_charge_Button is
        clicked(). The order is important to make sure the information is
        updated before the charge is added and the data cleared from the fields.

        The _bool is passed as an argument through clicked() but not used."""
        self.add_charge_to_entry_case_information()
        self.add_charge_to_grid()
        self.clear_charge_fields()

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

    def add_charge_to_grid(self):
        self.charges_gridLayout.add_charge_finding_and_fines_to_grid(self)
        self.statute_choice_box.setFocus()

    @logger.catch
    def create_entry_process(self):
        """The order of the create entry process is important to make sure the
        information is updated before the entry is created."""
        self.update_case_information()
        if self.charges_gridLayout.check_plea_and_findings() is None:
            return None
        create_entry(self)
        self.close_event()

    def clear_charge_fields(self):
        """Clears the fields that are used for adding a charge. The
        statute_choice_box and offense_choice_box use the clearEditText
        method because those boxes are editable."""
        self.statute_choice_box.clearEditText()
        self.offense_choice_box.clearEditText()

    # Setter Functions
    @logger.catch
    def set_statute_and_offense(self, key):
        """:key: is the string that is passed by the function each time the field
        is changed on the view."""
        field = None
        if self.freeform_entry_checkBox.isChecked():
            return None
        if self.sender() == self.statute_choice_box:
            field = 'statute'
        elif self.sender() == self.offense_choice_box:
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
                    self.statute_choice_box.setCurrentText(statute)
            elif field == 'statute':
                if statute == key:
                    self.offense_choice_box.setCurrentText(offense)
            self.degree_choice_box.setCurrentText(degree)
            query.finish()
            break

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

    def set_statute_and_offense_choice_boxes(self):
        """REFACTOR to two methods?"""
        self.statute_choice_box.addItems(create_statute_list())
        self.offense_choice_box.addItems(create_offense_list())
        self.statute_choice_box.setCurrentText("")
        self.offense_choice_box.setCurrentText("")

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
def create_database_connections():
    """The databases for the application are created upon import of the module, which is done
    on application startup. The connections to the databases are created, but the opening and
    closing of the databases is handled by the appropriate class dialog."""
    offense_database_connection = QSqlDatabase.addDatabase("QSQLITE", "offenses")
    offense_database_connection.setDatabaseName(CHARGES_DATABASE)
    return offense_database_connection


@logger.catch
def open_databases():
    database_offenses.open()


@logger.catch
def close_databases():
    """Closes any databases that were opened at the start of the dialog."""
    database_offenses.close()
    database_offenses.removeDatabase(CHARGES_DATABASE)


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

    def set_case_number_and_date(self, dialog):
        dialog.entry_case_information.case_number = self.case_number
        dialog.entry_case_information.plea_trial_date = self.plea_trial_date

    def set_party_information(self, dialog):
        """Updates the party information from the GUI(view) and saves it to the model."""
        dialog.entry_case_information.defendant.first_name = self.defendant_first_name
        dialog.entry_case_information.defendant.last_name = self.defendant_last_name


class CMSLoader:
    """Uses the cms_case number selected to get the cms_case object from main and load cms_case data."""
    def __init__(self, dialog):
        self.cms_case = dialog.cms_case
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
        for _index, charge in enumerate(self.cms_case.charges_list):
            self.criminal_charge = CriminalCharge()
            (self.criminal_charge.offense, self.criminal_charge.statute,
             self.criminal_charge.degree) = charge
            dialog.entry_case_information.add_charge_to_list(self.criminal_charge)
            dialog.add_charge_to_grid()


if __name__ == "__main__":
    print("BCD ran directly")
else:
    print("BCD ran when imported")
    database_offenses = create_database_connections()
