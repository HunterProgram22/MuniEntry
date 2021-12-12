"""The module that contains all controller classes that are common to criminal
cases (criminal includes traffic). """
import os

from controllers.helper_functions import set_document_name
from docxtpl import DocxTemplate
from loguru import logger

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

from models.case_information import (
    CriminalCaseInformation,
    CriminalCharge,
    AmendOffenseDetails,
)
from views.amend_offense_dialog_ui import Ui_AmendOffenseDialog
from views.custom_widgets import (
    ChargesGrid,
    PleaComboBox,
)
from controllers.base_dialogs import BaseDialog
from resources.db.create_data_lists import create_offense_list, create_statute_list
from settings import CHARGES_DATABASE, SAVE_PATH


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


class CriminalPleaDialog(BaseDialog):
    """This class subclasses the BaseDialog for methods that are specific to
    dialogs/entries that require entering a plea and finding in a case.

    The self.charges_gridLayout class is changed so that the methods from the ChargesGrid
    custom widget can be used, but the design of a standard QtDesigner QGridLayout can be changed
    in QtDesigner and pyuic5 ran without needing to update the ui.py file each time."""
    def __init__(self, judicial_officer, case=None, parent=None):
        open_databases()
        super().__init__(parent)
        self.judicial_officer = judicial_officer
        self.case = case
        try:
            self.charges_gridLayout.__class__ = ChargesGrid
        except AttributeError:
            pass
        self.case_information = CriminalCaseInformation(self.judicial_officer)
        self.criminal_charge = None
        self.set_statute_and_offense_choice_boxes()
        self.plea_trial_date.setDate(QtCore.QDate.currentDate())
        self.delete_button_list = []
        self.amend_button_list = []
        self.load_arraignment_data()

    def modify_view(self):
        pass

    def connect_signals_to_slots(self):
        """This method extends the base_dialog method to add additional signals
        and slots to be connected."""
        super().connect_signals_to_slots()
        self.clear_fields_case_Button.pressed.connect(lambda dialog=self: clear_case_information_fields(dialog))
        self.create_entry_Button.pressed.connect(lambda dialog=self: create_entry_process(dialog))
        self.add_charge_Button.clicked.connect(self.add_charge_process)
        self.clear_fields_charge_Button.pressed.connect(self.clear_charge_fields)
        self.statute_choice_box.currentTextChanged.connect(self.set_statute_and_offense)
        self.offense_choice_box.currentTextChanged.connect(self.set_statute_and_offense)
        try:
            self.guilty_all_Button.pressed.connect(self.set_plea_and_findings_process)
        except AttributeError:
            pass



    # CMS Loader Functions
    @logger.catch
    def load_arraignment_data(self):
        """Uses the case number selected to get the case object from main and load case data."""
        if self.case.case_number is not None:
            self.case_number_lineEdit.setText(self.case.case_number)
            self.defendant_first_name_lineEdit.setText(self.case.defendant.first_name)
            self.defendant_last_name_lineEdit.setText(self.case.defendant.last_name)
            self.add_caseloaddata_to_case_information()

    def add_caseloaddata_to_case_information(self):
        """Loads the data from the case object that is created from the sql table.
        self.criminal_charge.type = self.set_offense_type() FIGURE OUT FOR COSTS"""
        for _index, charge in enumerate(self.case.charges_list):
            self.criminal_charge = CriminalCharge()
            (self.criminal_charge.offense, self.criminal_charge.statute,
                self.criminal_charge.degree) = charge
            self.case_information.add_charge_to_list(self.criminal_charge)
            self.add_charge_to_grid()



    # Criminal DialogCleanUp Functions
    def close_event(self):
        """This method closes the databases before calling the base dialog close_event."""
        close_databases()
        super().close_event()



    # Criminal CasePartyUpdater Functions

    def set_case_number_and_date(self):
        self.case_information.case_number = self.case_number_lineEdit.text()
        self.case_information.plea_trial_date = self.plea_trial_date.date().toString("MMMM dd, yyyy")

    @logger.catch
    def update_case_information(self):
        """"Docstring needs updating."""
        self.set_case_number_and_date()
        self.set_party_information()
        self.add_additional_case_information()

    @logger.catch
    def set_party_information(self):
        """Updates the party information from the GUI(view) and saves it to the model."""
        self.case_information.defendant.first_name = self.defendant_first_name_lineEdit.text()
        self.case_information.defendant.last_name = self.defendant_last_name_lineEdit.text()


    # Modify Case Information Functions
    def add_additional_case_information(self):
        self.add_dispositions_and_fines()
        self.update_costs_and_fines_information()
        self.check_add_conditions()
        self.calculate_costs_and_fines()

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
        for index, charge in enumerate(self.case_information.charges_list):
            while self.charges_gridLayout.itemAtPosition(row, column) is None:
                column += 1
            if isinstance(self.charges_gridLayout.itemAtPosition(
                          row, column).widget(), PleaComboBox):
                charge.plea = self.charges_gridLayout.itemAtPosition(
                              row, column).widget().currentText()
                column += 1
            column += 1

    @logger.catch
    def update_costs_and_fines_information(self):
        """Updates the costs and fines from the GUI(view) and saves it to the model."""
        self.case_information.court_costs.ordered = self.court_costs_box.currentText()
        self.case_information.court_costs.ability_to_pay_time = self.ability_to_pay_box.currentText()
        self.case_information.court_costs.balance_due_date = \
            self.balance_due_date.date().toString("MMMM dd, yyyy")

    @logger.catch
    def calculate_costs_and_fines(self):
        """Calculates costs and fines based on the case type (moving, non-moving, criminal) and
        then adds it to any fines that are in the fines_amount box and subtracts fines in the
        fines_suspended box. The loop stops when a case of the highest fine is found because
        court costs are always for the highest charge. The _index is underscored because it is
        not used but is required to unpack enumerate()."""
        self.case_information.court_costs.amount = 0
        if self.court_costs_box.currentText() == "Yes":
            for _index, charge in enumerate(self.case_information.charges_list):
                if self.case_information.court_costs.amount == 124:
                    break
                if charge.type == "Moving Traffic":
                    self.case_information.court_costs.amount = max(self.case_information.court_costs.amount, 124)
                elif charge.type == "Criminal":
                    self.case_information.court_costs.amount = max(self.case_information.court_costs.amount, 114)
                elif charge.type == "Non-moving Traffic":
                    self.case_information.court_costs.amount = max(self.case_information.court_costs.amount, 95)
        total_fines = 0
        try:
            for _index, charge in enumerate(self.case_information.charges_list):
                if charge.fines_amount == '':
                    charge.fines_amount = 0
                total_fines = total_fines + int(charge.fines_amount)
            self.case_information.total_fines = total_fines
            total_fines_suspended = 0
            for _index, charge in enumerate(self.case_information.charges_list):
                if charge.fines_suspended == '':
                    charge.fines_suspended = 0
                total_fines_suspended = total_fines_suspended + int(charge.fines_suspended)
            self.case_information.total_fines_suspended = total_fines_suspended
        except TypeError:
            print("A type error was allowed to pass - this is because of deleted charge.")



    # Slot Functions
    @logger.catch
    def add_charge_process(self, _bool):
        """The order of functions that are called when the add_charge_Button is
        clicked(). The order is important to make sure the information is
        updated before the charge is added and the data cleared from the fields.

        The _bool is passed as an argument through clicked() but not used."""
        self.add_charge_to_case_information()
        self.add_charge_to_grid()
        self.clear_charge_fields()

    @logger.catch
    def add_charge_to_case_information(self):
        """The offense, statute and degree are added to the view by the method
        add_charge_to_view, not this method. This method is triggered on
        clicked() of the Add Charge button."""
        self.criminal_charge = CriminalCharge()
        self.criminal_charge.offense = self.offense_choice_box.currentText()
        self.criminal_charge.statute = self.statute_choice_box.currentText()
        self.criminal_charge.degree = self.degree_choice_box.currentText()
        self.criminal_charge.type = self.set_offense_type()
        self.case_information.add_charge_to_list(self.criminal_charge)

    def add_charge_to_grid(self):
        self.charges_gridLayout.add_charge_finding_and_fines_to_grid(self)
        self.statute_choice_box.setFocus()

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
    def set_fra_in_file(self, current_text):
        """Sets the FRA (proof of insurance) to true if the view indicates 'yes'
        that the FRA was shown in the complaint of file."""
        if current_text == "Yes":
            self.case_information.fra_in_file = True
            self.fra_in_court_box.setCurrentText("No")
        elif current_text == "No":
            self.case_information.fra_in_file = False
        else:
            self.case_information.fra_in_file = None

    @logger.catch
    def set_fra_in_court(self, current_text):
        """Sets the FRA (proof of insurance) to true if the view indicates 'yes'
        that the FRA was shown in court."""
        if current_text == "Yes":
            self.case_information.fra_in_court = True
        elif current_text == "No":
            self.case_information.fra_in_court = False
        else:
            self.case_information.fra_in_court = None

    @logger.catch
    def set_offense_type(self):
        """This calls the database_statutes and behind the scenes sets the appropriate case type
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
        """This method is set in CriminalPleaDialog class but called in subclasses because
        NotGuiltyBondDialog doesn't currently have statute and offense choice boxes."""
        self.statute_choice_box.addItems(create_statute_list())
        self.offense_choice_box.addItems(create_offense_list())
        self.statute_choice_box.setCurrentText("")
        self.offense_choice_box.setCurrentText("")



    # Move to Charges Grid Widget Class (?)
    @logger.catch
    def delete_charge(self):
        """Deletes the offense from the case_information.charges list. Then
        decrements the total charges by one so that other functions using the
        total charges for indexing are correct."""
        index = self.delete_button_list.index(self.sender())
        del self.case_information.charges_list[index]
        del self.delete_button_list[index]
        self.charges_gridLayout.delete_charge_from_grid()
        self.statute_choice_box.setFocus()

    # CostsAndFines Class
    @logger.catch
    def show_costs_and_fines(self, _bool):
        """The _bool is the toggle from the clicked() of the button pressed. No
        action is taken with respect to it."""
        self.update_case_information()
        message = QMessageBox()
        message.setIcon(QMessageBox.Information)
        message.setWindowTitle("Total Costs and Fines")
        # noinspection PyUnresolvedReferences
        message.setInformativeText("Costs: $" + str(self.case_information.court_costs.amount) +
                                   "\nFines: $" + str(self.case_information.total_fines) +
                                   "\nFines Suspended: $" + str(self.case_information.total_fines_suspended) +
                                   "\n\n*Does not include possible bond forfeiture or other costs \n that " +
                                   "may be assessed as a result of prior actions in case. ")
        total_fines_and_costs = \
            (self.case_information.court_costs.amount + self.case_information.total_fines) - \
            self.case_information.total_fines_suspended
        message.setText("Total Costs and Fines Due By Due Date: $" + str(total_fines_and_costs))
        message.setStandardButtons(QMessageBox.Ok)
        message.exec_()


class AmendOffenseDialog(BaseDialog, Ui_AmendOffenseDialog):
    """The AddOffenseDialog is created when the amend_button is pressed for a specific charge.
    The case information is passed in order to populate the case information banner. The
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
        self.connect_signals_to_slots()

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
        object then points the case_information object to the AmendOffenseDetails
        object."""
        self.amend_offense_details.original_charge = self.original_charge_box.currentText()
        self.amend_offense_details.amended_charge = self.amended_charge_box.currentText()
        self.amend_offense_details.motion_disposition = self.motion_decision_box.currentText()
        self.case_information.amend_offense_details = self.amend_offense_details
        amended_charge = self.current_offense + " - AMENDED"
        self.case_information.charges_list[self.button_index].offense = amended_charge
        for columns in range(self.main_dialog.charges_gridLayout.columnCount()):
            if self.main_dialog.charges_gridLayout.itemAtPosition(0, columns) is not None:
                if self.main_dialog.charges_gridLayout.itemAtPosition(
                        0, columns).widget().text() == self.current_offense:
                    self.main_dialog.charges_gridLayout.itemAtPosition(0, columns).widget().setText(amended_charge)
        self.close_event()


if __name__ == "__main__":
    print("BCD ran directly")
else:
    print("BCD ran when imported")
    database_offenses = create_database_connections()


@logger.catch
def create_entry_process(dialog):
    """The order of the create entry process is important to make sure the
    information is updated before the entry is created."""
    dialog.update_case_information()
    if dialog.charges_gridLayout.check_plea_and_findings() is None:
        return None
    create_entry(dialog)
    dialog.close_event()


@logger.catch
def create_entry(dialog):
    """Loads the proper template and creates the entry."""
    doc = DocxTemplate(dialog.template.template_path)
    doc.render(dialog.case_information.get_case_information())
    docname = set_document_name(dialog)
    doc.save(SAVE_PATH + docname)
    os.startfile(SAVE_PATH + docname)


@logger.catch
def clear_case_information_fields(dialog):
    """Clears the text in the fields in the top case information frame and resets the cursor
    to the first text entry (defendant_first_name_lineEdit) box."""
    dialog.defendant_first_name_lineEdit.clear()
    dialog.defendant_last_name_lineEdit.clear()
    dialog.case_number_lineEdit.clear()
    dialog.defendant_first_name_lineEdit.setFocus()