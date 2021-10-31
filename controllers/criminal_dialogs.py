"""The module that contains all controller classes that are commmon to criminal
cases (criminal includes traffic). """
import os
import pathlib
from docxtpl import DocxTemplate
from loguru import logger

from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QLabel, QPushButton, QMessageBox, QComboBox, QLineEdit
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
from resources.db.DatabaseCreation import create_offense_list, create_statute_list
from views.custom_widgets import (
    PleaComboBox,
    FindingComboBox,
    FineLineEdit,
    FineSuspendedLineEdit,
    DeleteButton,
    AmendButton,
)
from settings import TEMPLATE_PATH, SAVE_PATH, DB_PATH, CHARGES_DATABASE


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
    """This class is a base class to provide methods that are used by some or
    all class controllers that are used in the application. This class is never
    instantiated as its own dialog, but the init contains the setup for all
    inherited class controllers."""

    def __init__(self, judicial_officer, parent=None):
        """Databases must be opened first in order for them to be accessed
        when the UI is built so it can populate fields.The setupUI calls to
        the view to create the UI."""
        open_databases()
        super().__init__(parent)
        self.setupUi(self)
        self.modify_view()
        self.connect_signals_to_slots()
        self.delete_button_list = []
        self.doc = None
        self.docname = None

    @logger.catch
    def modify_view(self):
        """The modify view method updates the view that is created on init with
        self.setupUI. Place items in this method that can't be added
        directly in QtDesigner (or are more easily added later) so that they
        don't need to be changed in the view file each time pyuic5 is run."""
        statute_list = create_statute_list()
        self.statute_choice_box.addItems(statute_list)
        self.offense_choice_box.addItems(create_offense_list())
        self.plea_trial_date.setDate(QtCore.QDate.currentDate())
        self.statute_choice_box.setCurrentText("")
        self.offense_choice_box.setCurrentText("")

    @logger.catch
    def connect_signals_to_slots(self):
        """The method connects any signals to slots. Generally, connecting with
        pressed is preferred to clicked because a clicked event sends a bool
        argument to the function. However, clicked is used in some instances
        because it is a press and release of a button. Using pressed sometimes
        caused an event to be triggered twice.

        At present this includes buttons common to all criminal dialogs. Buttons
        that are specific to only a certain dialog are added in the subclassed
        version of the method."""
        self.cancel_Button.pressed.connect(self.close_event)
        self.clear_fields_case_Button.pressed.connect(self.clear_case_information_fields)
        self.create_entry_Button.pressed.connect(self.create_entry_process)
        self.add_charge_Button.clicked.connect(self.add_charge_process)
        self.clear_fields_charge_Button.pressed.connect(self.clear_charge_fields)
        self.statute_choice_box.currentTextChanged.connect(self.set_offense)
        self.offense_choice_box.currentTextChanged.connect(self.set_statute)
        self.guilty_all_Button.pressed.connect(self.guilty_all_plea_and_findings)

    @logger.catch
    def update_case_information(self):
        """"The method calls functions to update the case information model
        with the data for the case that is in the fields on the view. This
        method may be called in multiple places when a button is pressed to
        make sure all information is current."""
        self.update_party_information()
        self.add_dispositions_and_fines()
        self.update_costs_and_fines_information()
        self.check_add_conditions()
        self.calculate_costs_and_fines()

    @logger.catch
    def update_party_information(self):
        self.case_information.case_number = self.case_number_lineEdit.text()
        self.case_information.defendant.first_name = self.defendant_first_name_lineEdit.text()
        self.case_information.defendant.last_name = self.defendant_last_name_lineEdit.text()
        self.case_information.plea_trial_date = self.plea_trial_date.date().toString("MMMM dd, yyyy")

    def add_dispositions_and_fines(self):
        """This method is specfic to each subclass."""
        pass

    @logger.catch
    def update_costs_and_fines_information(self):
        self.case_information.court_costs_ordered = self.court_costs_box.currentText()
        self.case_information.ability_to_pay_time = self.ability_to_pay_box.currentText()
        self.case_information.balance_due_date = self.balance_due_date.date().toString("MMMM dd, yyyy")

    @logger.catch
    def check_add_conditions(self):
        """Checks to see what conditions in the Add Conditions box are checked and then
        transfers the information from the conditions to case_information model if the
        box is checked.
        FIX: This is showing a none on logger.catch when starting the AddConditionsDialog,
        but it is necessary to make sure the conditions are added to the entry. Refacotr.

        TODO:
        in future refactor this to have it loop through the different conditions so code
        doesn't need to be added each time a condition is added."""
        if self.license_suspension_checkBox.isChecked():
            self.case_information.license_suspension_details.license_suspension_ordered = (
                True
            )
        if self.community_control_checkBox.isChecked():
            self.case_information.community_control_terms.community_control_required = (
                True
            )
        if self.community_service_checkBox.isChecked():
            self.case_information.community_service_terms.community_service_ordered = (
                True
            )
        if self.other_conditions_checkBox.isChecked():
            self.case_information.other_conditions_details.other_conditions_ordered = (
                True
            )

    @logger.catch
    def calculate_costs_and_fines(self):
        self.case_information.court_costs = 0
        if self.court_costs_box.currentText() == "Yes":
            for index, charge in enumerate(self.case_information.charges_list):
                if self.case_information.court_costs == 124:
                    break
                else:
                    if charge.type == "Moving Traffic":
                        if self.case_information.court_costs < 124:
                            self.case_information.court_costs = 124
                    elif charge.type == "Criminal":
                        if self.case_information.court_costs < 114:
                            self.case_information.court_costs = 114
                    elif charge.type == "Non-moving Traffic":
                        if self.case_information.court_costs < 95:
                            self.case_information.court_costs = 95
        total_fines = 0
        try:
            for index, charge in enumerate(self.case_information.charges_list):
                if charge.fines_amount == '':
                    charge.fines_amount = 0
                total_fines = total_fines + int(charge.fines_amount)
            self.case_information.total_fines = total_fines
            total_fines_suspended = 0
            for index, charge in enumerate(self.case_information.charges_list):
                if charge.fines_suspended == '':
                    charge.fines_suspended = 0
                total_fines_suspended = total_fines_suspended + int(charge.fines_suspended)
            self.case_information.total_fines_suspended = total_fines_suspended
        except TypeError:
            print("A type error was allowed to pass - this is because of deleted charge.")

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
        self.charges_gridLayout.addWidget(PleaComboBox(), row, column)
        row +=1
        return row, column

    def add_delete_button_to_view(self, row, column):
        delete_button = DeleteButton()
        self.delete_button_list.append(delete_button)
        delete_button.pressed.connect(self.delete_charge)
        self.charges_gridLayout.addWidget(delete_button, row, column)

    def add_amend_button_to_view(self, row, column):
        amend_button = AmendButton()
        self.amend_button_list.append(amend_button)
        amend_button.pressed.connect(self.start_amend_offense_dialog)
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




    def close_window(self):
        """Function connected to a button to close the window. Can be connected
        to any button press/click/release to close a window."""
        self.close()

    def clear_case_information_fields(self):
        self.defendant_first_name_lineEdit.clear()
        self.defendant_last_name_lineEdit.clear()
        self.case_number_lineEdit.clear()
        self.defendant_first_name_lineEdit.setFocus()

    def clear_charge_fields(self):
        """Clears the fields that are used for adding a charge. The
        statute_choice_box and offense_choice_box use the clearEditText
        method because those boxes are editable."""
        self.statute_choice_box.clearEditText()
        self.offense_choice_box.clearEditText()

    @logger.catch
    def add_charge_process(self, bool):
        """The order of functions that are called when the add_charge_Button is
        clicked(). The order is important to make sure the informaiton is
        updated before the charge is added and the data cleared from the fields.

        The bool is passed as an argument through clicked() but not used."""
        self.criminal_charge = CriminalCharge()
        self.add_charge()
        self.clear_charge_fields()

    @logger.catch
    def create_entry_process(self):
        """The order of functions that are called when the create_entry_Button is pressed()
        on the MinorMisdemeanorDialog. The order is important to make sure the information is
        updated before the entry is created."""
        self.update_case_information()
        self.create_entry()
        self.close_event()

    @logger.catch
    def create_entry(self):
        """The standard function used to create an entry when a create entry
        button is press/click/released."""
        self.doc = DocxTemplate(self.template.template_path)
        self.doc.render(self.case_information.get_case_information())
        self.set_document_name()
        self.doc.save(SAVE_PATH + self.docname)
        os.startfile(SAVE_PATH + self.docname)

    def set_document_name(self):
        """Sets document name based on the case number and name of the template
        must include '.docx' to make it a Word document."""
        self.docname = (
            self.case_information.case_number + "_" + self.template.template_name + ".docx"
        )

    def set_case_information_banner(self):
        """Sets the banner on a view of the interface. It modifies label
        widgets on the view to text that was entered."""
        self.defendant_name_label.setText(
            "State of Ohio v. {defendant_first_name} {defendant_last_name}".format(
                defendant_first_name = self.case_information.defendant.first_name,
                defendant_last_name = self.case_information.defendant.last_name
                )
            )
        self.case_number_label.setText(self.case_information.case_number)
        if self.case_information.defendant_attorney_name is not None:
            self.defendant_attorney_name_label.setText(
                "Attorney: " + self.case_information.defendant_attorney_name
            )
        else:
            self.defendant_attorney_name_label.setText("Attorney: None")



    @logger.catch
    def close_event(self):
        """Place any cleanup items (i.e. close_databases) here that should be
        called when the entry is created and the dialog closed."""
        close_databases()
        self.close_window()

    def set_offense_type(self):
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
                break

    def guilty_all_plea_and_findings(self):
        """Sets the plea and findings boxes to guilty for all charges currently
        in the charges_gridLayout."""
        for column in range(self.charges_gridLayout.columnCount()):
            try:
                if isinstance(self.charges_gridLayout.itemAtPosition(3, column).widget(), PleaComboBox):
                    self.charges_gridLayout.itemAtPosition(3,column).widget().setCurrentText("Guilty")
                    self.charges_gridLayout.itemAtPosition(4,column).widget().setCurrentText("Guilty")
                    column +=1
            except AttributeError:
                pass
        try:
            self.set_cursor_to_FineLineEdit()
        except AttributeError:
            pass

    def no_contest_all_plea_and_findings(self):
        """Sets the plea box to no contest and findings boxes to guilty for all
        charges currently in the charges_gridLayout."""
        for column in range(self.charges_gridLayout.columnCount()):
            try:
                if isinstance(self.charges_gridLayout.itemAtPosition(3, column).widget(), PleaComboBox):
                    self.charges_gridLayout.itemAtPosition(3,column).widget().setCurrentText("No Contest")
                    self.charges_gridLayout.itemAtPosition(4,column).widget().setCurrentText("Guilty")
                    column +=1
            except AttributeError:
                pass
        self.set_cursor_to_FineLineEdit()

    def clear_case_information_fields(self):
        self.defendant_first_name_lineEdit.clear()
        self.defendant_last_name_lineEdit.clear()
        self.case_number_lineEdit.clear()
        self.defendant_first_name_lineEdit.setFocus()

    def clear_charge_fields(self):
        """Clears the fields that are used for adding a charge. The
        statute_choice_box and offense_choice_box use the clearEditText
        method because those boxes are editable."""
        self.statute_choice_box.clearEditText()
        self.offense_choice_box.clearEditText()

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


class AddConditionsDialog(BaseCriminalDialog, Ui_AddConditionsDialog):
    """The AddConditionsDialog is created when the addConditionsButton is clicked on
    the MinorMisdemeanorDialog. The conditions that are available to enter information
    for are based on the checkboxes that are checked on the MMD screen."""

    @logger.catch
    def __init__(self, minor_misdemeanor_dialog, parent=None):
        self.case_information = minor_misdemeanor_dialog.case_information
        super().__init__(parent)
        self.community_service = (
            minor_misdemeanor_dialog.community_service_checkBox.isChecked()
        )
        self.license_suspension = (
            minor_misdemeanor_dialog.license_suspension_checkBox.isChecked()
        )
        self.community_control = (
            minor_misdemeanor_dialog.community_control_checkBox.isChecked()
        )
        self.other_conditions = (
            minor_misdemeanor_dialog.other_conditions_checkBox.isChecked()
        )
        self.other_conditions = (
            minor_misdemeanor_dialog.other_conditions_checkBox.isChecked()
        )
        self.enable_condition_frames()

    @logger.catch
    def connect_signals_to_slots(self):
        self.cancel_Button.pressed.connect(self.close_event)
        self.continue_Button.pressed.connect(self.add_conditions)
        self.continue_Button.released.connect(self.close_window)
        self.community_service_days_to_complete_box.currentIndexChanged.connect(self.set_service_date)

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
        on the MinorMisdemeanorDialog screen. Also creates an instance of the object for
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
            self.community_service_terms = CommunityServiceTerms()
            self.community_service_date_to_complete_box.setDate(
                QtCore.QDate.currentDate()
            )
        if self.community_control is True:
            self.community_control_frame.setEnabled(True)
            self.community_control_terms = CommunityControlTerms()

    @logger.catch
    def add_conditions(self):
        """The method is connected to the pressed() signal of continue_Button on the
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
        self.community_service_terms.hours_of_service = (
            self.community_service_hours_ordered_box.value()
        )
        self.community_service_terms.days_to_complete_service = (
            self.community_service_days_to_complete_box.currentText()
        )
        self.community_service_terms.due_date_for_service = (
            self.community_service_date_to_complete_box.date().toString("MMMM dd, yyyy")
        )
        self.case_information.community_service_terms = self.community_service_terms

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


class AmendOffenseDialog(BaseCriminalDialog, Ui_AmendOffenseDialog):
    """The AddOffenseDialog is created when the amendOffenseButton is clicked on
    the MinorMisdemeanorDialog screen. The case information is passed in
    order to populate the case information banner.

    The set_case_information_banner is an inherited method from BaseCriminalDialog."""
    @logger.catch
    def __init__(self, case_information, parent=None):
        super().__init__(parent)
        self.case_information = case_information
        self.amend_offense_details = AmendOffenseDetails()
        self.set_case_information_banner()
        self.modify_view()

    @logger.catch
    def modify_view(self):
        """The modify view method updates the view that is created on init.
        Place items in this method that can't be added directly in QtDesigner
        so that they don't need to be changed in the view file each time pyuic5
        is run."""
        offense_list = create_offense_list()
        self.original_charge_box.addItems(offense_list)
        self.amended_charge_box.addItems(offense_list)

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


if __name__ == "__main__":
    print("BCD ran directly")
else:
    print("BCD ran when imported")
    database_offenses, database_statutes = create_database_connections()
