"""The module that contains all controller classes that are commmon to criminal
cases (criminal includes traffic). """
import os
from docxtpl import DocxTemplate
from loguru import logger

from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QLabel, QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

from models.case_information import (
    CaseInformation,
    CriminalCharge,
    AmendOffenseDetails,
    LicenseSuspensionTerms,
    CommunityControlTerms,
    CommunityServiceTerms,
    OtherConditionsTerms,
)
from views.add_conditions_dialog_ui import Ui_AddConditionsDialog
from views.amend_offense_dialog_ui import Ui_AmendOffenseDialog
from views.custom_widgets import (
    PleaComboBox,
    FineLineEdit,
    DeleteButton,
    AmendButton,
    AlliedCheckbox,
)
from resources.db.create_data_lists import create_offense_list, create_statute_list
from settings import SAVE_PATH, CHARGES_DATABASE
from .helper_functions import create_entry


@logger.catch
def create_database_connections():
    """The databases for the application are created upon import of the module, which is done
    on application startup. The connections to the databases are created, but the opening and
    closing of the databases is handled by the appropriate class dialog."""
    offense_database_connection = QSqlDatabase.addDatabase("QSQLITE", "offenses")
    offense_database_connection.setDatabaseName(CHARGES_DATABASE)
    statute_database_connection = QSqlDatabase.addDatabase("QSQLITE", "statutes")
    statute_database_connection.setDatabaseName(CHARGES_DATABASE)
    return offense_database_connection, statute_database_connection


@logger.catch
def open_databases():
    """
    https://www.tutorialspoint.com/pyqt/pyqt_database_handling.htm
    https://doc.qt.io/qtforpython/overviews/sql-connecting.html
    NOTE: If running create_psql_table.py to update database, must delete
    the old charges.sqlite file to insure it is updated.
    """
    database_offenses.open()
    database_statutes.open()


@logger.catch
def close_databases():
    """Closes any databases that were opened at the start of the dialog."""
    database_offenses.close()
    database_offenses.removeDatabase(CHARGES_DATABASE)
    database_statutes.close()
    database_statutes.removeDatabase(CHARGES_DATABASE)


class BaseCriminalDialog(QDialog):
    """This class is a base class to provide methods that are used by some criminal controllers
     in the application. This class is never instantiated as its own dialog, but the init contains
     the setup for all inherited class controllers."""
    def __init__(self, judicial_officer, case=None, parent=None):
        """Databases must be opened first in order for them to be accessed
        when the UI is built so it can populate fields.The setupUI calls to
        the view to create the UI."""
        open_databases()
        super().__init__(parent)
        self.judicial_officer = judicial_officer
        self.case = case
        self.setupUi(self)
        self.modify_view()
        self.connect_signals_to_slots()
        self.doc = None
        self.docname = None

    @logger.catch
    def modify_view(self):
        """The modify view method updates the view that is created on init with
        self.setupUI. Place items in this method that can't be added
        directly in QtDesigner (or are more easily added later) so that they
        don't need to be changed in the view file each time pyuic5 is run."""
        self.plea_trial_date.setDate(QtCore.QDate.currentDate())

    @logger.catch
    def connect_signals_to_slots(self):
        """At present this includes buttons common to all criminal dialogs. Buttons that are
        specific to only a certain dialog are added in the subclassed version of the method."""
        self.cancel_Button.pressed.connect(self.close_event)
        self.clear_fields_case_Button.pressed.connect(self.clear_case_information_fields)
        self.create_entry_Button.pressed.connect(self.create_entry_process)

    @logger.catch
    def update_case_information(self):
        """"This method may be called in multiple places when a button is pressed to
        make sure all information is current. The subclass version of the method
        will call updates to specific portions of the view for that dialog."""
        self.update_party_information()

    @logger.catch
    def update_party_information(self):
        """Updates the party information from the GUI(view) and saves it to the model."""
        self.case_information.case_number = self.case_number_lineEdit.text()
        self.case_information.defendant.first_name = self.defendant_first_name_lineEdit.text()
        self.case_information.defendant.last_name = self.defendant_last_name_lineEdit.text()
        self.case_information.plea_trial_date = (
            self.plea_trial_date.date().toString("MMMM dd, yyyy")
        )

    @logger.catch
    def close_window(self):
        """Function connected to a button to close the window. Can be connected
        to any button press/click/release to close a window."""
        close_databases()
        self.close()

    @logger.catch
    def clear_case_information_fields(self):
        """Clears the text in the fields in the top case information frame and resets the cursor
        to the first text entry box."""
        self.defendant_first_name_lineEdit.clear()
        self.defendant_last_name_lineEdit.clear()
        self.case_number_lineEdit.clear()
        self.defendant_first_name_lineEdit.setFocus()

    @logger.catch
    def create_entry_process(self):
        """The order of functions that are called when the create_entry_Button is pressed()
        on a criminal dialog. The order is important to make sure the information is
        updated before the entry is created."""
        self.update_case_information()
        create_entry(self)
        self.close_event()

    @logger.catch
    def close_event(self):
        """Place any cleanup items (i.e. close_databases) here that should be
        called when the entry is created and the dialog closed."""
        close_databases()
        self.close_window()

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


class CriminalPleaDialog(BaseCriminalDialog):
    """This class subclasses the BaseCriminalDialog for methods that are specific to
    dialogs/entries that require entering a plea and finding in a case."""
    def __init__(self, judicial_officer, case=None, parent=None):
        super().__init__(judicial_officer, case, parent)
        self.case_information = CaseInformation(self.judicial_officer)
        self.delete_button_list = []
        self.amend_button_list = []
        self.criminal_charge = None
        self.load_arraignment_data()

    @logger.catch
    def load_arraignment_data(self):
        if self.case.case_number != None:
            self.case_number_lineEdit.setText(self.case.case_number)
            self.defendant_first_name_lineEdit.setText(self.case.defendant_first_name)
            self.defendant_last_name_lineEdit.setText(self.case.defendant_last_name)
            self.add_charge_from_caseloaddata()

    def add_charge_from_caseloaddata(self):
        for index, charge in enumerate(self.case.charges_list):
            self.criminal_charge = CriminalCharge()
            (self.criminal_charge.offense, self.criminal_charge.statute, self.criminal_charge.degree) = \
            self.case.charges_list[index]
            # self.criminal_charge.type = self.set_offense_type() FIGURE OUT FOR COSTS
            self.case_information.add_charge_to_list(self.criminal_charge)
            self.add_charge_to_view()
            self.statute_choice_box.setFocus()

    def modify_view(self):
        super().modify_view()
        self.statute_choice_box.addItems(create_statute_list())
        self.offense_choice_box.addItems(create_offense_list())
        self.statute_choice_box.setCurrentText("")
        self.offense_choice_box.setCurrentText("")

    def connect_signals_to_slots(self):
        super().connect_signals_to_slots()
        self.add_charge_Button.clicked.connect(self.add_charge_process)
        self.clear_fields_charge_Button.pressed.connect(self.clear_charge_fields)
        self.statute_choice_box.currentTextChanged.connect(self.set_offense)
        self.offense_choice_box.currentTextChanged.connect(self.set_statute)
        self.guilty_all_Button.pressed.connect(self.set_all_plea_and_findings)

    def update_case_information(self):
        super().update_case_information()
        self.add_dispositions_and_fines()
        self.update_costs_and_fines_information()
        self.check_add_conditions()
        self.calculate_costs_and_fines()

    def add_dispositions_and_fines(self):
        """This method is specfic to each subclass."""

    @logger.catch
    def update_costs_and_fines_information(self):
        """Updates the costs and fines from the GUI(view) and saves it to the model."""
        self.case_information.court_costs_ordered = self.court_costs_box.currentText()
        self.case_information.ability_to_pay_time = self.ability_to_pay_box.currentText()
        self.case_information.balance_due_date = (
            self.balance_due_date.date().toString("MMMM dd, yyyy")
        )

    @logger.catch
    def check_add_conditions(self):
        """Checks to see what conditions in the Add Conditions box are checked and then
        transfers the information from the conditions to case_information model if the
        box is checked.
        FIX: Resolved AttributeError with try and except, but perhaps refactor
        to create a license suspension details object at init for CaseInformation
        (and for other conditions as well).

        TODO:
        in future refactor this to have it loop through the different conditions so code
        doesn't need to be added each time a condition is added."""
        add_conditions_dict = {
            self.license_suspension_checkBox: self.case_information.license_suspension_details.license_suspension_ordered,
            self.community_control_checkBox: self.case_information.community_control_terms.community_control_required,
            self.community_service_checkBox: self.case_information.community_service_terms.community_service_ordered,
            self.other_conditions_checkBox: self.case_information.other_conditions_details.other_conditions_ordered,
        }
        for key, value in add_conditions_dict.items():
            if key.isChecked():
                value = True
        # try:
        #     if self.license_suspension_checkBox.isChecked():
        #         self.case_information.license_suspension_details.license_suspension_ordered = (
        #             True
        #         )
        #     if self.community_control_checkBox.isChecked():
        #         self.case_information.community_control_terms.community_control_required = (
        #             True
        #         )
        #     if self.community_service_checkBox.isChecked():
        #         self.case_information.community_service_terms.community_service_ordered = (
        #             True
        #         )
        #     if self.other_conditions_checkBox.isChecked():
        #         self.case_information.other_conditions_details.other_conditions_ordered = (
        #             True
        #         )
        # except AttributeError:
        #     pass

    @logger.catch
    def calculate_costs_and_fines(self):
        """Calculates costs and fines based on the case type (moving, non-moving, criminal) and
        then adds it to any fines that are in the fines_amount box and substracts fines in the
        fines_suspended box. The loop stops when a case of the highest fine is found because
        court costs are always for the highest charge. The _index is underscored because it is
        not used but is required to unpack enumerate()."""
        self.case_information.court_costs = 0
        if self.court_costs_box.currentText() == "Yes":
            for _index, charge in enumerate(self.case_information.charges_list):
                if self.case_information.court_costs == 124:
                    break
                if charge.type == "Moving Traffic":
                    self.case_information.court_costs = max(self.case_information.court_costs, 124)
                elif charge.type == "Criminal":
                    self.case_information.court_costs = max(self.case_information.court_costs, 114)
                elif charge.type == "Non-moving Traffic":
                    self.case_information.court_costs = max(self.case_information.court_costs, 95)
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

    @logger.catch
    def add_charge_process(self, _bool):
        """The order of functions that are called when the add_charge_Button is
        clicked(). The order is important to make sure the information is
        updated before the charge is added and the data cleared from the fields.

        The _bool is passed as an argument through clicked() but not used."""
        self.criminal_charge = CriminalCharge()
        self.add_charge()
        self.clear_charge_fields()

    @logger.catch
    def add_charge(self):
        """The add_charge_process, from which this is called, creates a criminal
        charge object and adds the data in the view to the object. The criminal
        charge (offense, statute, degree and type) is then added to the case
        information model (by appending the charge object to the criminal
        charges list).

        The offense, statute and degree are added to the view by the method
        add_charge_to_view, not this method. This method is triggered on
        clicked() of the Add Charge button."""
        self.criminal_charge.offense = self.offense_choice_box.currentText()
        self.criminal_charge.statute = self.statute_choice_box.currentText()
        self.criminal_charge.degree = self.degree_choice_box.currentText()
        self.criminal_charge.type = self.set_offense_type()
        self.case_information.add_charge_to_list(self.criminal_charge)
        self.add_charge_to_view()
        self.statute_choice_box.setFocus()

    @logger.catch
    def add_charge_to_view(self):
        """Adds the charge that was added through add_charge method to the
        view/GUI. The first row=0 because of python zero-based indexing. The
        column is set at one more than the current number of columns because
        it is the column to which the charge will be added.

        :added_charge_index: - The added charge index is one less than the
        total charges in charges_list because of zero-based indexing. Thus, if
        there is one charge, the index of the charge to be added to the
        charge_dict from the charges_list is 0.

        The python builtin vars function returns the __dict__ attribute of
        the object.

        The self.criminal_charge.offense added as a parameter for FineLineEdit
        is the current one added when "Add Charge" is pressed.

        TODO: Refactor so that there isn't a need for a if branch to skip the
        attribute for charge type."""
        row = 0
        column = self.charges_gridLayout.columnCount() + 1
        added_charge_index = len(self.case_information.charges_list) - 1
        charge = vars(self.case_information.charges_list[added_charge_index])
        for value in charge.values():
            if value is not None:
                if value in ["Moving Traffic", "Non-moving Traffic", "Criminal"]:
                    break
                self.charges_gridLayout.addWidget(QLabel(value), row, column)
                row += 1
        self.charges_gridLayout.addWidget(AlliedCheckbox(), row, column)
        row += 1
        self.charges_gridLayout.addWidget(PleaComboBox(), row, column)
        row += 1
        return row, column

    def clear_charge_fields(self):
        """Clears the fields that are used for adding a charge. The
        statute_choice_box and offense_choice_box use the clearEditText
        method because those boxes are editable."""
        self.statute_choice_box.clearEditText()
        self.offense_choice_box.clearEditText()

    def add_delete_button_to_view(self, row, column):
        """This method is called in the dialog subclass so that it is inserted in the
        correct row."""
        delete_button = DeleteButton()
        self.delete_button_list.append(delete_button)
        delete_button.pressed.connect(self.delete_charge)
        self.charges_gridLayout.addWidget(delete_button, row, column)

    def add_amend_button_to_view(self, row, column):
        """This method is called in the dialog subclass so that it is inserted in the
        correct row."""
        amend_button = AmendButton()
        self.amend_button_list.append(amend_button)
        amend_button.clicked.connect(self.start_amend_offense_dialog)
        self.charges_gridLayout.addWidget(amend_button, row, column)

    @logger.catch
    def delete_charge(self):
        """Deletes the offense from the case_information.charges list. Then
        decrements the total charges by one so that other functions using the
        total charges for indexing are correct."""
        index = self.delete_button_list.index(self.sender())
        del self.case_information.charges_list[index]
        del self.delete_button_list[index]
        self.delete_charge_from_view()
        self.statute_choice_box.setFocus()

    @logger.catch
    def delete_charge_from_view(self):
        """Uses the delete_button that is indexed to the column to delete the
        QLabels for the charge."""
        index = self.charges_gridLayout.indexOf(self.sender())
        column = self.charges_gridLayout.getItemPosition(index)[1]
        for row in range(self.charges_gridLayout.rowCount()):
            layout_item = self.charges_gridLayout.itemAtPosition(row, column)
            if layout_item is not None:
                layout_item.widget().deleteLater()
                self.charges_gridLayout.removeItem(layout_item)

    @logger.catch
    def set_all_plea_and_findings(self):
        """Sets the plea and findings boxes for all charges currently
        in the charges_gridLayout."""
        if self.sender() == self.guilty_all_Button:
            plea = "Guilty"
        elif self.sender() == self.no_contest_all_Button:
            plea = "No Contest"
        for column in range(self.charges_gridLayout.columnCount()):
            try:
                if isinstance(self.charges_gridLayout.itemAtPosition(
                        4, column).widget(), PleaComboBox):
                    self.charges_gridLayout.itemAtPosition(
                        4, column).widget().setCurrentText(plea)
                    if self.charges_gridLayout.itemAtPosition(
                            3, column).widget().isChecked():
                        self.charges_gridLayout.itemAtPosition(
                            5, column).widget().setCurrentText("Guilty - Allied Offense")
                    else:
                        self.charges_gridLayout.itemAtPosition(
                            5, column).widget().setCurrentText("Guilty")
                    column += 1
            except AttributeError:
                pass
        try:
            self.set_cursor_to_fine_line_edit()
        except AttributeError:
            pass

    @logger.catch
    def set_cursor_to_fine_line_edit(self):
        """Moves the cursor to the FineLineEdit box. Row is set to 7, but for different dialogs
        this could end up changing."""
        for column in range(self.charges_gridLayout.columnCount()):
            try:
                if isinstance(self.charges_gridLayout.itemAtPosition(
                        6, column).widget(), FineLineEdit):
                    self.charges_gridLayout.itemAtPosition(6, column).widget().setFocus()
                    break
            except AttributeError:
                pass

    @logger.catch
    def show_costs_and_fines(self, _bool):
        """The _bool is the toggle from the clicked() of the button pressed. No
        action is taken with respect to it."""
        self.update_case_information()
        message = QMessageBox()
        message.setIcon(QMessageBox.Information)
        message.setWindowTitle("Total Costs and Fines")
        message.setInformativeText("Costs: $" + str(self.case_information.court_costs) +
            "\nFines: $" + str(self.case_information.total_fines) +
            "\nFines Suspended: $" + str(self.case_information.total_fines_suspended) +
            "\n\n*Does not include possible bond forfeiture or other costs \n that " +
            "may be assesed as a result of prior actions in case. ")
        total_fines_and_costs = (self.case_information.court_costs +
            self.case_information.total_fines) - self.case_information.total_fines_suspended
        message.setText("Total Costs and Fines Due By Due Date: $" + str(total_fines_and_costs))
        message.setStandardButtons(QMessageBox.Ok)
        message.exec_()

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
        query = QSqlQuery(database_statutes)
        query.prepare("SELECT * FROM charges WHERE " "statute LIKE '%' || :key || '%'")
        query.bindValue(":key", key)
        query.exec()
        while query.next():
            statute = query.value(2)
            offense_type = query.value(4)
            if statute == key:
                query.finish()
                return offense_type

    @logger.catch
    def set_statute(self, key):
        """This method queries based on the offense and then sets the statute
        and degree based on the offense in the database.

        :key: is the string that is passed by the function each time the field
        is changed on the view. This is the offense."""
        if self.freeform_entry_checkBox.isChecked():
            return None
        query = QSqlQuery(database_offenses)
        query.prepare("SELECT * FROM charges WHERE " "offense LIKE '%' || :key || '%'")
        query.bindValue(":key", key)
        query.exec()
        while query.next():
            offense = query.value(1)
            statute = query.value(2)
            degree = query.value(3)
            if offense == key:
                self.statute_choice_box.setCurrentText(statute)
                self.degree_choice_box.setCurrentText(degree)
                query.finish()
                break

    @logger.catch
    def set_offense(self, key):
        """This method queries based on the statute and then sets the offense
        and degree based on the statute in the database.

        :key: is the string that is passed by the function each time the field
        is changed on the view. This is the statute."""
        if self.freeform_entry_checkBox.isChecked():
            return None
        query = QSqlQuery(database_statutes)
        query.prepare("SELECT * FROM charges WHERE " "statute LIKE '%' || :key || '%'")
        query.bindValue(":key", key)
        query.exec()
        while query.next():
            offense = query.value(1)
            statute = query.value(2)
            degree = query.value(3)
            if statute == key:
                self.offense_choice_box.setCurrentText(offense)
                self.degree_choice_box.setCurrentText(degree)
                query.finish()
                break


class AddConditionsDialog(BaseCriminalDialog, Ui_AddConditionsDialog):
    """The AddConditionsDialog is created when the addConditionsButton is clicked on
    the NoJailPleaDialog. The conditions that are available to enter information
    for are based on the checkboxes that are checked on the NJPD screen."""
    @logger.catch
    def __init__(self, main_dialog, parent=None):
        self.case_information = main_dialog.case_information
        super().__init__(parent)
        self.community_service = (
            main_dialog.community_service_checkBox.isChecked()
        )
        self.license_suspension = (
            main_dialog.license_suspension_checkBox.isChecked()
        )
        self.community_control = (
            main_dialog.community_control_checkBox.isChecked()
        )
        self.other_conditions = (
            main_dialog.other_conditions_checkBox.isChecked()
        )
        self.other_conditions = (
            main_dialog.other_conditions_checkBox.isChecked()
        )
        self.enable_condition_frames()

    @logger.catch
    def connect_signals_to_slots(self):
        self.cancel_Button.pressed.connect(self.close_event)
        self.add_conditions_Button.pressed.connect(self.add_conditions)
        self.add_conditions_Button.released.connect(self.close_window)
        self.community_service_days_to_complete_box.currentIndexChanged.connect(
            self.set_service_date)

    @logger.catch
    def modify_view(self):
        """Modifies the view of AddConditionsDialog that is created by the UI
        file.
        Gets the total number of charges from the charges in charges_list then
        loops through the charges_list and adds parts of each charge to the
        view. CLEAN UP?"""
        index_of_charge_to_add = 0
        column = self.charges_gridLayout.columnCount() + 1
        total_charges_to_add = len(self.case_information.charges_list)
        while index_of_charge_to_add < total_charges_to_add:
            charge = vars(self.case_information.charges_list[index_of_charge_to_add])
            if charge is not None:
                self.charges_gridLayout.addWidget(
                    QLabel(charge.get("offense")), 0, column
                )
                self.charges_gridLayout.addWidget(
                    QLabel(charge.get("statute")), 1, column
                )
                self.charges_gridLayout.addWidget(
                    QLabel(charge.get("finding")), 2, column
                )
                column += 1
                index_of_charge_to_add += 1

    @logger.catch
    def enable_condition_frames(self):
        """Enables the frames on the AddConditionsDialog dialog if the condition is checked
        on the NoJailPleaDialog screen. Also creates an instance of the object for
        each condition."""
        if self.other_conditions is True:
            self.other_conditions_frame.setEnabled(True)
            self.other_conditions_details = OtherConditionsTerms()
        if self.license_suspension is True:
            self.license_suspension_frame.setEnabled(True)
            self.license_suspension_details = LicenseSuspensionTerms()
            self.license_suspension_date_box.setDate(QtCore.QDate.currentDate())
        if self.community_service is True:
            self.community_service_frame.setEnabled(True)
            #self.community_service_terms = CommunityServiceTerms()
            self.community_service_date_to_complete_box.setDate(
                QtCore.QDate.currentDate()
            )
        if self.community_control is True:
            self.community_control_frame.setEnabled(True)
            self.community_control_terms = CommunityControlTerms()

    @logger.catch
    def add_conditions(self):
        """The method is connected to the pressed() signal of add_conditions_Button on the
        Add Conditions screen."""
        if self.community_service is True:
            self.add_community_service_terms()
        if self.community_control is True:
            self.add_community_control_terms()
        if self.license_suspension is True:
            self.add_license_suspension_details()
        if self.other_conditions is True:
            self.add_other_condition_details()

    @logger.catch
    def add_community_control_terms(self):
        """The method adds the data entered to the CommunityControlTerms object
        that is created when the dialog is initialized. Then the data is transferred
        to case_information."""
        self.community_control_terms.type_of_community_control = (
            self.type_of_community_control_box.currentText()
        )
        self.community_control_terms.term_of_community_control = (
            self.term_of_community_control_box.currentText()
        )
        self.case_information.community_control_terms = self.community_control_terms

    @logger.catch
    def add_community_service_terms(self):
        """The method adds the data entered to the CommunityServiceTerms object
        that is created when the dialog is initialized. Then the data is transferred
        to case_information."""
        self.case_information.community_service_terms.hours_of_service = (
            self.community_service_hours_ordered_box.value()
        )
        self.case_information.community_service_terms.days_to_complete_service = (
            self.community_service_days_to_complete_box.currentText()
        )
        self.case_information.community_service_terms.due_date_for_service = (
            self.community_service_date_to_complete_box.date().toString("MMMM dd, yyyy")
        )
        self.case_information.community_service_terms.community_service_ordered = True
        print(self.case_information.community_service_terms.hours_of_service)


    @logger.catch
    def add_license_suspension_details(self):
        """The method adds the data entered to the LicenseSuspensionTerms object
        that is created when the dialog is initialized. Then the data is transferred
        to case_information."""
        self.license_suspension_details.license_type = (
            self.license_type_box.currentText()
        )
        self.license_suspension_details.license_suspended_date = (
            self.license_suspension_date_box.date().toString("MMMM dd, yyyy")
        )
        self.license_suspension_details.license_suspension_term = (
            self.term_of_suspension_box.currentText()
        )
        if self.remedial_driving_class_checkBox.isChecked():
            self.license_suspension_details.remedial_driving_class_required = True
        else:
            self.license_suspension_details.remedial_driving_class_required = False
        self.case_information.license_suspension_details = (
            self.license_suspension_details
        )

    @logger.catch
    def add_other_condition_details(self):
        """The method allows for adding other conditions based on free form text
        entry."""
        self.other_conditions_details.other_conditions_terms = (
            self.other_conditions_plainTextEdit.toPlainText()
        )
        self.case_information.other_conditions_details = (
            self.other_conditions_details
        )

    @logger.catch
    def set_service_date(self, days_to_complete):
        """Sets the community_service_date_to_complete_box based on the number
        of days chosen in the community_service_date_to_complete_box."""
        days_to_complete = int(
            self.community_service_days_to_complete_box.currentText()
        )
        self.community_service_date_to_complete_box.setDate(
            QDate.currentDate().addDays(days_to_complete)
        )

    @logger.catch
    def close_event(self):
        """This close event is called instead of the parent class close_event because the databases
        need to remain open and the parent class close_event closes the databases."""
        self.close_window()


class AmendOffenseDialog(BaseCriminalDialog, Ui_AmendOffenseDialog):
    """The AddOffenseDialog is created when the amend_button is pressed for a specific charge.
    The case information is passed in order to populate the case information banner. The
    button_index is to determine which charge the amend_button is amending."""
    @logger.catch
    def __init__(self, case_information, button_index, parent=None):
        self.button_index = button_index
        self.case_information = case_information
        self.amend_offense_details = AmendOffenseDetails()
        super().__init__(parent)
        self.set_case_information_banner()
        self.connect_signals_to_slots()

    @logger.catch
    def modify_view(self):
        """The modify view sets the original charge based on the item in the main dialog
        for which amend button was pressed."""
        self.original_charge_box.setCurrentText(self.case_information.charges_list[self.button_index].offense)
        self.amended_charge_box.addItems(create_offense_list())

    @logger.catch
    def connect_signals_to_slots(self):
        """TODO: the continue button signals/slots should be refactored into single ordered method
        like with other dialogs."""
        self.clear_fields_Button.pressed.connect(self.clear_amend_charge_fields)
        self.amend_offense_Button.pressed.connect(self.amend_offense)
        self.cancel_Button.pressed.connect(self.close_event)

    @logger.catch
    def clear_amend_charge_fields(self):
        self.original_charge_box.clearEditText()
        self.amended_charge_box.clearEditText()

    @logger.catch
    def amend_offense(self):
        """Adds the data entered for the amended offense to the AmendOffenseDetails
        object then points the case_information object to the AmendOffenseDetails
        object."""
        self.amend_offense_details.original_charge = (
            self.original_charge_box.currentText()
        )
        self.amend_offense_details.amended_charge = (
            self.amended_charge_box.currentText()
        )
        self.amend_offense_details.motion_disposition = (
            self.motion_decision_box.currentText()
        )
        self.case_information.amend_offense_details = self.amend_offense_details
        self.close_event()

    @logger.catch
    def close_event(self):
        """Uses subclass of close_event so that it doesn't close databases."""
        self.close_window()


if __name__ == "__main__":
    print("BCD ran directly")
else:
    print("BCD ran when imported")
    database_offenses, database_statutes = create_database_connections()
