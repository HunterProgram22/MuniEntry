"""The controller module for the minor misdemeanor dialog - it is not limited
to minor misdemeanors, but does not contain functions to account for jail time.
Loads all charges - including non-minor-misdemeanors from a database."""
import pathlib
from datetime import date, timedelta
from loguru import logger

from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

from views.minor_misdemeanor_dialog_ui import Ui_MinorMisdemeanorDialog
from views.add_conditions_dialog_ui import Ui_AddConditionsDialog
from views.amend_offense_dialog_ui import Ui_AmendOffenseDialog
from models.template_types import TEMPLATE_DICT
from models.case_information import (
    CaseInformation,
    CriminalCharge,
    AmendOffenseDetails,
    LicenseSuspension,
    CommunityControlTerms,
    CommunityServiceTerms
)
from controllers.criminal_dialogs import BaseCriminalDialog
from resources.db.DatabaseCreation import create_offense_list


PATH = str(pathlib.Path().absolute())
TEMPLATE_PATH = PATH + "\\resources\\templates\\"
SAVE_PATH = PATH + "\\resources\\saved\\"
DB_PATH = PATH + "\\resources\\db\\"
CHARGES_DATABASE = DB_PATH + "\\charges.sqlite"


def create_database_connections():
    """The databases for the applicaiton are created upon import of the module, which is done
    on application startup. The connections to the databases are created, but the opening and
    closing of the databases is handled by the appropriate class dialog."""
    offense_database_connection = QSqlDatabase.addDatabase("QSQLITE", "offenses")
    offense_database_connection.setDatabaseName(CHARGES_DATABASE)
    statute_database_connection = QSqlDatabase.addDatabase("QSQLITE", "statutes")
    statute_database_connection.setDatabaseName(CHARGES_DATABASE)
    return offense_database_connection , statute_database_connection

def open_databases():
    """
    https://www.tutorialspoint.com/pyqt/pyqt_database_handling.htm
    https://doc.qt.io/qtforpython/overviews/sql-connecting.html
    NOTE: If running create_psql_table.py to update database, must delete
    the old charges.sqlite file to insure it is updated.
    """
    database_offenses.open()
    database_statutes.open()

def close_databases():
    """Closes any databases that were opened at the start of the dialog."""
    database_offenses.close()
    database_offenses.removeDatabase(CHARGES_DATABASE)
    database_statutes.close()
    database_statutes.removeDatabase(CHARGES_DATABASE)


class MinorMisdemeanorDialog(BaseCriminalDialog, Ui_MinorMisdemeanorDialog):
    """The dialog inherits from the BaseCriminalDialog (controller) and the
    Ui_MinorMisdemeanorDialog (view).

    This dialog is used when there will not be any jail time imposed. It does
    not inherently limit cases to minor misdemeanors or unclassified
    misdemeanors, however, it does not include fields to enter jail time."""
    def __init__(self, judicial_officer, parent=None):
        open_databases()
        super().__init__(parent)
        self.case_information = CaseInformation(judicial_officer)
        self.modify_view()
        self.connect_signals_to_slots()
        self.set_template()
        self.criminal_charge = CriminalCharge()
        self.delete_button_list = []
        self.pay_date_dict = {
            "forthwith": 0,
            "within 30 days": 30,
            "within 60 days": 60,
            "within 90 days": 90,
        }

    def modify_view(self):
        """The modify view method updates the view that is created on init from the
        Ui_MinorMisdemeanorDialog. Place items in this method that can't be added
        directly in QtDesigner so that they don't need to be changed in the view file
        each time pyuic5 is run."""
        offense_list, statute_list = create_offense_list()
        self.statute_choice_box.addItems(statute_list)
        self.offense_choice_box.addItems(offense_list)
        self.plea_trial_date.setDate(QtCore.QDate.currentDate())
        self.balance_due_date.setDate(QtCore.QDate.currentDate())

    def connect_signals_to_slots(self):
        """The method that connects any signals to slots that are not standard
        functions in QtDesigner. Signals tied to clear() or clearEditText() and a
        few others native to QtDesigner are connected in the view.

        Have not yet moved: set_offense(), set_statute(), set_fra_in_file(),
        set_fra_in_court(), set_pay_date()."""
        self.create_entry_Button.pressed.connect(self.create_entry_process)
        self.add_conditions_Button.pressed.connect(self.start_add_conditions_dialog)
        self.amend_offense_Button.pressed.connect(self.start_amend_offense_dialog)
        self.add_charge_Button.pressed.connect(self.add_charge_process)
        self.add_charge_Button.released.connect(self.clear_charge_fields)

    def create_entry_process(self):
        """The order of functions that are called when the create_entry_Button is pressed()
        on the MinorMisdemeanorDialog. The order is important to make sure the information is
        updated before the entry is created."""
        self.update_case_information()
        self.create_entry()
        self.close_event()

    def add_charge_process(self):
        """The order of functions that are called when the add_charge_Button is pressed()
        on the MinorMisdemeanorDialog. The order is important to make sure the informaiton is
        updated before the charge is added and the data cleared from the fields."""
        self.criminal_charge = CriminalCharge()
        self.add_charge()

    def clear_charge_fields(self):
        """Does as it says and clears the fields that are used for adding a charge."""
        self.finding_choice_box.clearEditText()
        self.offense_choice_box.clearEditText()
        self.plea_choice_box.clearEditText()
        self.statute_choice_box.clearEditText()
        self.fines_suspended.clear()
        self.fines_amount.clear()

    def set_template(self):
        """The TEMPLATE_DICT stores the templates that are assigned to each judicial officer
        in the Templates.py model module."""
        self.template = TEMPLATE_DICT.get(self.case_information.judicial_officer.last_name)

    def start_amend_offense_dialog(self):
        """Opens the amend offense dialog as a modal window. The case_information is passed
        to the dialog class in order to populate the case information banner."""
        self.update_case_information()
        AmendOffenseDialog(self.case_information).exec()

    def start_add_conditions_dialog(self):
        """Opens the add conditions dialog as a modal window. It passes the
        instance of the MinorMisdemeanorDialog class (self) as an argument
        so that the AddConditionsDialog can access all data from the
        MinorMisdemeanorDialog when working in the AddConditionsDialog."""
        AddConditionsDialog(self).exec()

    def close_event(self):
        """Place any cleanup items (i.e. close_databases) here that should be
        called when the entry is created and the dialog closed."""
        close_databases()
        self.close_window()

    def add_charge(self):
        """Creates a criminal charge object and adds the data in the view to
        the object. The criminal charge is then added to the case information
        model (by appending the charge object to the criminal charges list).

        The offense is added to the view by the method add_charge_to_view,
        not this method. This method is triggered on press of the Add Charge
        button."""
        self.criminal_charge.offense = self.offense_choice_box.currentText()
        self.criminal_charge.statute = self.statute_choice_box.currentText()
        self.criminal_charge.degree = self.degree_choice_box.currentText()
        self.criminal_charge.plea = self.plea_choice_box.currentText()
        self.criminal_charge.finding = self.finding_choice_box.currentText()
        self.criminal_charge.fines_amount = self.fines_amount.text()
        self.criminal_charge.fines_suspended = self.fines_suspended.text()
        self.criminal_charge.court_costs = self.court_costs_box.currentText()
        self.case_information.add_charge_to_list(self.criminal_charge)
        self.add_charge_to_view()
        self.court_costs_box.setCurrentText("No")
        self.offense_choice_box.setFocus()

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
        the object."""
        row = 0
        column = self.charges_gridLayout.columnCount() + 1
        added_charge_index = len(self.case_information.charges_list) - 1
        charge = vars(self.case_information.charges_list[added_charge_index])
        for value in charge.values():
            if value is not None:
                self.charges_gridLayout.addWidget(QLabel(value), row, column)
                row += 1
        delete_button = QPushButton("Delete")
        self.delete_button_list.append(delete_button)
        delete_button.setStyleSheet("background-color: rgb(160, 160, 160);")
        delete_button.clicked.connect(self.delete_charge)
        self.charges_gridLayout.addWidget(delete_button, row, column)

    def delete_charge(self):
        """Deletes the offense from the case_information.charges list. Then
        decrements the total charges by one so that other functions using the
        total charges for indexing are correct."""
        index = self.delete_button_list.index(self.sender())
        del self.case_information.charges_list[index]
        del self.delete_button_list[index]
        self.delete_charge_from_view()

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
    def update_case_information(self):
        """The method updates the case information model with the data for the
        case that is in the fields on the view. This does not update the model
        with information in the charge fields (offense, statute, plea, etc.)
        the charge information is transferred to the model upon press of the
        add charge button.

        Fields that are updated upon pressed() of createEntryButton = case
        number, first name, last name, ability to pay time, balance due date,
        date of plea/trial,operator license number, date of birth, FRA (proof
        of insurance) in complaint, FRA in court."""
        self.case_information.case_number = self.case_number_lineEdit.text()
        self.case_information.defendant.first_name = self.defendant_first_name_lineEdit.text()
        self.case_information.defendant.last_name = self.defendant_last_name_lineEdit.text()
        self.case_information.plea_trial_date = (
            self.plea_trial_date.date().toString("MMMM dd, yyyy")
        )
        self.case_information.operator_license_number = self.operator_license_number_lineEdit.text()
        self.case_information.defendant_date_of_birth = (
            self.defendant_birth_date.date().toString("MMMM dd, yyyy")
        )
        self.case_information.ability_to_pay_time = self.ability_to_pay_box.currentText()
        self.case_information.balance_due_date = (
            self.balance_due_date.date().toString("MMMM dd, yyyy")
        )
        self.check_add_conditions()

    def check_add_conditions(self):
        """Checks to see what conditions in the Add Conditions box are checked and then
        transfers the information from the conditions to case_information model if the
        box is checked.

        TODO: At present you can't just check the box and use default conditions, you need
        to press the addConditionsButton to create the object/dialog and load the data. Also,
        in future refactor this to have it loop through the different conditions so code
        doesn't need to be added each time a condition is added."""
        if self.license_suspension_checkBox.isChecked():
            self.case_information.license_suspension_details.license_suspension_ordered = True
        if self.community_control_checkBox.isChecked():
            self.case_information.community_control_terms.community_control_required = True
        if self.community_service_checkBox.isChecked():
            self.case_information.community_service_terms.community_service_ordered = True

    def set_fra_in_file(self):
        """Sets the FRA (proof of insurance) to true if the view indicates 'yes'
        that the FRA was shown in the complaint of file."""
        if self.fra_in_file_box.currentText() == "Yes":
            self.case_information.fra_in_file = True
            self.fra_in_court_box.setCurrentText("No")
        elif self.fra_in_file_box.currentText() == "No":
            self.case_information.fra_in_file = False
        else:
            self.case_information.fra_in_file = None

    def set_fra_in_court(self):
        """Sets the FRA (proof of insurance) to true if the view indicates 'yes'
        that the FRA was shown in court."""
        if self.fra_in_court_box.currentText() == "Yes":
            self.case_information.fra_in_court = True
        elif self.fra_in_court_box.currentText() == "No":
            self.case_information.fra_in_court = False
        else:
            self.case_information.fra_in_court = None

    def set_statute(self):
        """This method queries based on the offense and then sets the statute
        and degree based on the offense in the database."""
        if self.freeform_entry_checkBox.isChecked():
            return None
        key = self.offense_choice_box.currentText()
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

    def set_offense(self):
        """This method queries based on the statute and then sets the offense
        and degree based on the statute in the database."""
        if self.freeform_entry_checkBox.isChecked():
            return None
        key = self.statute_choice_box.currentText()
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

    def set_pay_date(self):
        """Sets the balance of fines and costs to a future date (or today)
        depending on the selection of ability_to_pay_box. The inner function
        will move the actual date to the next tuesday per court procedure for
        show cause hearings being on Tuesday. Would need to be modified if the
        policy changed."""
        days_to_add = self.pay_date_dict[self.ability_to_pay_box.currentText()]
        future_date = date.today() + timedelta(days_to_add)
        today = date.today()

        def next_tuesday(future_date, weekday=1):
            """This function returns the number of days to add to today to set
            the payment due date out to the Tuesday after the number of days
            set in the set_pay_date function. The default of 1 for weekday is
            what sets it to a Tuesday. If it is 0 it would be Monday, 3 would
            be Wednesday, etc."""
            days_ahead = weekday - future_date.weekday()
            if days_ahead <= 0:  # Target day already happened this week
                days_ahead += 7
            return future_date + timedelta(days_ahead)

        future_date = next_tuesday(future_date, 1)
        total_days_to_add = (future_date - today).days
        self.balance_due_date.setDate(QDate.currentDate().addDays(total_days_to_add))


class AddConditionsDialog(BaseCriminalDialog, Ui_AddConditionsDialog):
    """The AddConditionsDialog is created when the addConditionsButton is clicked on
    the MinorMisdemeanorDialog. The conditions that are available to enter information
    for are based on the checkboxes that are checked on the MMD screen."""
    def __init__(self, minor_misdemeanor_dialog, parent=None):
        super().__init__(parent)
        self.case_information = minor_misdemeanor_dialog.case_information
        self.community_service = minor_misdemeanor_dialog.community_service_checkBox.isChecked()
        self.community_control = minor_misdemeanor_dialog.community_control_checkBox.isChecked()
        self.license_suspension = minor_misdemeanor_dialog.license_suspension_checkBox.isChecked()
        self.enable_condition_frames()

    def enable_condition_frames(self):
        """Enables the frames on the AddConditionsDialog dialog if the condition is checked
        on the MinorMisdemeanorDialog screen. Also creates an instance of the object for
        each condition."""
        if self.license_suspension is True:
            self.license_suspension_frame.setEnabled(True)
            self.license_suspension_details = LicenseSuspension()
            self.license_suspension_date_box.setDate(QtCore.QDate.currentDate().addDays(-30))
        if self.community_control is True:
            self.community_control_frame.setEnabled(True)
            self.community_control_terms = CommunityControlTerms()
        if self.community_service:
            self.community_service_frame.setEnabled(True)
            self.community_service_terms = CommunityServiceTerms()
            self.community_service_date_to_complete_box.setDate(QtCore.QDate.currentDate())

    def add_conditions(self):
        """The method is connected to the pressed() signal of continue_Button on the
        Add Conditions screen."""
        if self.community_service is True:
            self.add_community_service_terms()
        if self.community_control is True:
            self.add_community_control_terms()
        if self.license_suspension is True:
            self.add_license_suspension_details()

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

    def add_license_suspension_details(self):
        """The method adds the data entered to the LicenseSuspension object
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
        self.license_suspension_details.driving_privileges = (
            self.driving_privileges_type_box.currentText()
        )
        self.license_suspension_details.driving_privileges_term = (
            self.term_of_privileges_box.currentText()
        )
        if self.remedial_driving_class_checkBox.isChecked():
            self.license_suspension_details.remedial_driving_class_required = True
        else:
            self.license_suspension_details.remedial_driving_class_required = False
        self.case_information.license_suspension_details = self.license_suspension_details

    def set_service_date(self):
        """Sets the community_service_date_to_complete_box based on the number
        of days chosen in the community_service_date_to_complete_box."""
        days_added = int(self.community_service_days_to_complete_box.currentText())
        self.community_service_date_to_complete_box.setDate(QDate.currentDate().addDays(days_added))


class AmendOffenseDialog(BaseCriminalDialog, Ui_AmendOffenseDialog):
    """The AddOffenseDialog is created when the amendOffenseButton is clicked on
    the MinorMisdemeanorDialog screen. The case information is passed in
    order to populate the case information banner.

    The set_case_information_banner is an inherited method from BaseCriminalDialog."""
    def __init__(self, case_information, parent=None):
        super().__init__(parent)
        self.case_information = case_information
        self.amend_offense_details = AmendOffenseDetails()
        self.set_case_information_banner()
        self.modify_view()

    def modify_view(self):
        """The modify view method updates the view that is created on init.
        Place items in this method that can't be added directly in QtDesigner
        so that they don't need to be changed in the view file each time pyuic5
        is run."""
        offense_list = create_offense_list()[0]
        self.original_charge_box.addItems(offense_list)
        self.amended_charge_box.addItems(offense_list)

    def amend_offense(self):
        """Adds the data entered for the amended offense to the AmendOffenseDetails
        object then points the case_information object to the AmendOffenseDetails
        object."""
        self.amend_offense_details.original_charge = self.original_charge_box.currentText()
        self.amend_offense_details.amended_charge = self.amended_charge_box.currentText()
        self.amend_offense_details.motion_disposition = self.motion_decision_box.currentText()
        self.case_information.amend_offense_details = self.amend_offense_details


if __name__ == "__main__":
    print("MMD ran directly")
else:
    print("MMD ran when imported")
    database_offenses, database_statutes = create_database_connections()
