"""The module that contains all controller classes that are common to criminal
cases (criminal includes traffic). """
from loguru import logger

from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QLabel, QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

from models.case_information import (
    CaseInformation,
    CriminalCharge,
    AmendOffenseDetails,
    LicenseSuspension,
    CommunityService,
    OtherConditions,
)
from views.add_conditions_dialog_ui import Ui_AddConditionsDialog
from views.add_special_bond_conditions_dialog_ui import Ui_AddSpecialBondConditionsDialog
from views.amend_offense_dialog_ui import Ui_AmendOffenseDialog
from views.custom_widgets import (
    ChargesGrid,
    PleaComboBox,
)
from controllers.base_dialogs import BaseDialog
from resources.db.create_data_lists import create_offense_list, create_statute_list
from settings import CHARGES_DATABASE


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
        super().__init__(judicial_officer, case, parent)
        try:
            self.charges_gridLayout.__class__ = ChargesGrid
        except AttributeError:
            pass
        self.case_information = CaseInformation(self.judicial_officer)
        self.criminal_charge = None
        self.add_conditions_dict = {
            self.license_suspension_checkBox: self.case_information.license_suspension.ordered,
            self.community_service_checkBox: self.case_information.community_service.ordered,
            self.other_conditions_checkBox: self.case_information.other_conditions.ordered,
        }
        self.set_statute_and_offense_choice_boxes()
        self.delete_button_list = []
        self.amend_button_list = []
        self.load_arraignment_data()

    @logger.catch
    def load_arraignment_data(self):
        """Uses the case number selected to get the case object from main and load case data."""
        if self.case.case_number is not None:
            self.case_number_lineEdit.setText(self.case.case_number)
            self.defendant_first_name_lineEdit.setText(self.case.defendant_first_name)
            self.defendant_last_name_lineEdit.setText(self.case.defendant_last_name)
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

    def close_event(self):
        close_databases()
        super().close_event()

    def set_statute_and_offense_choice_boxes(self):
        """This method is set in CriminalPleaDialog class but called in subclasses because
        NotGuiltyBondDialog doesn't currently have statute and offense choice boxes."""
        self.statute_choice_box.addItems(create_statute_list())
        self.offense_choice_box.addItems(create_offense_list())
        self.statute_choice_box.setCurrentText("")
        self.offense_choice_box.setCurrentText("")

    def connect_signals_to_slots(self):
        super().connect_signals_to_slots()
        self.add_charge_Button.clicked.connect(self.add_charge_process)
        self.clear_fields_charge_Button.pressed.connect(self.clear_charge_fields)
        self.statute_choice_box.currentTextChanged.connect(self.set_statute_and_offense)
        self.offense_choice_box.currentTextChanged.connect(self.set_statute_and_offense)
        try:
            self.guilty_all_Button.pressed.connect(self.set_plea_and_findings_process)
        except AttributeError:
            pass

    def set_plea_and_findings_process(self):
        self.charges_gridLayout.set_all_plea_and_findings(self)

    def update_case_information(self):
        super().update_case_information()
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
        self.case_information.court_costs.balance_due_date = (
            self.balance_due_date.date().toString("MMMM dd, yyyy")
        )

    @logger.catch
    def check_add_conditions(self):
        """TODO: Bug exists where if you uncheck boxes after adding conditions they are still added. This is probably
        because of a dictionary being used. Refactor back away from dictionary?"""
        for key, value in self.add_conditions_dict.items():
            if key.isChecked():
                self.add_conditions_dict[key] = True
            else:
                self.add_conditions_dict[key] = False


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
                                   "may be assessed as a result of prior actions in case. ")
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


class AddConditionsDialog(BaseDialog, Ui_AddConditionsDialog):
    """The AddConditionsDialog is created when the addConditionsButton is clicked on
    the NoJailPleaDialog. The conditions that are available to enter information
    for are based on the checkboxes that are checked on the NJPD screen."""
    @logger.catch
    def __init__(self, main_dialog, parent=None):
        self.charges_list = main_dialog.case_information.charges_list  # Show charges on banner
        super().__init__(self, parent)
        self.case_information = main_dialog.case_information
        self.community_service = main_dialog.community_service_checkBox.isChecked()
        self.license_suspension = main_dialog.license_suspension_checkBox.isChecked()
        self.other_conditions = main_dialog.other_conditions_checkBox.isChecked()
        self.other_conditions = main_dialog.other_conditions_checkBox.isChecked()
        self.enable_condition_frames()

    @logger.catch
    def connect_signals_to_slots(self):
        self.cancel_Button.pressed.connect(self.close_event)
        self.add_conditions_Button.pressed.connect(self.add_conditions)
        self.add_conditions_Button.released.connect(self.close_window)
        self.community_service_days_to_complete_box.currentIndexChanged.connect(
            self.set_community_service_date
        )

    @logger.catch
    def modify_view(self):
        """Modifies the view of AddConditionsDialog that is created by the UI
        file. Gets the total number of charges from the charges in charges_list then
        loops through the charges_list and adds parts of each charge to the
        view."""
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint |
                            QtCore.Qt.WindowMaximizeButtonHint)
        column = self.charges_gridLayout.columnCount() + 1
        for _index, charge in enumerate(self.charges_list):
            charge = vars(charge)
            if charge is not None:
                self.charges_gridLayout.addWidget(QLabel(charge.get("offense")), 0, column)
                self.charges_gridLayout.addWidget(QLabel(charge.get("statute")), 1, column)
                self.charges_gridLayout.addWidget(QLabel(charge.get("finding")), 2, column)
                column += 1

    @logger.catch
    def enable_condition_frames(self):
        """Enables the frames on the AddConditionsDialog dialog if the condition is checked
        on the NoJailPleaDialog screen."""
        if self.other_conditions is True:
            self.other_conditions_frame.setEnabled(True)
        if self.license_suspension is True:
            self.license_suspension_frame.setEnabled(True)
            self.license_suspension_date_box.setDate(QtCore.QDate.currentDate())
        if self.community_service is True:
            self.community_service_frame.setEnabled(True)
            self.community_service_date_to_complete_box.setDate(QtCore.QDate.currentDate())

    @logger.catch
    def add_conditions(self):
        """The method is connected to the pressed() signal of add_conditions_Button on the
        Add Conditions screen."""
        if self.community_service is True:
            self.case_information.community_service = CommunityService()
            self.add_community_service_terms()
        if self.license_suspension is True:
            self.case_information.license_suspension = LicenseSuspension()
            self.add_license_suspension_details()
        if self.other_conditions is True:
            self.case_information.other_conditions = OtherConditions()
            self.add_other_condition_details()

    @logger.catch
    def add_community_service_terms(self):
        """The method adds the data entered to the CommunityService object
        that is created when the dialog is initialized."""
        self.case_information.community_service.hours_of_service = (
            self.community_service_hours_ordered_box.value()
        )
        self.case_information.community_service.days_to_complete_service = (
            self.community_service_days_to_complete_box.currentText()
        )
        self.case_information.community_service.due_date_for_service = (
            self.community_service_date_to_complete_box.date().toString("MMMM dd, yyyy")
        )
        self.case_information.community_service.ordered = True

    @logger.catch
    def add_license_suspension_details(self):
        """The method adds the data entered to the LicenseSuspension object
        that is created when the dialog is initialized."""
        self.case_information.license_suspension.license_type = (
            self.license_type_box.currentText()
        )
        self.case_information.license_suspension.suspended_date = (
            self.license_suspension_date_box.date().toString("MMMM dd, yyyy")
        )
        self.case_information.license_suspension.suspension_term = (
            self.term_of_suspension_box.currentText()
        )
        if self.remedial_driving_class_checkBox.isChecked():
            self.case_information.license_suspension.remedial_driving_class_required = True
        else:
            self.case_information.license_suspension.remedial_driving_class_required = False
        self.case_information.license_suspension.ordered = True

    @logger.catch
    def add_other_condition_details(self):
        """The method allows for adding other conditions based on free form text
        entry."""
        self.case_information.other_conditions.terms = (
            self.other_conditions_plainTextEdit.toPlainText()
        )
        self.case_information.other_conditions.ordered = True

    @logger.catch
    def set_community_service_date(self, _index):
        """Sets the community_service_date_to_complete_box based on the number
        of days chosen in the community_service_date_to_complete_box. The _index is passed from the
        signal but not used."""
        days_to_complete = int(self.community_service_days_to_complete_box.currentText())
        self.community_service_date_to_complete_box.setDate(
            QDate.currentDate().addDays(days_to_complete)
        )

    @logger.catch
    def close_event(self):
        """This close event is called instead of the parent class close_event because the databases
        need to remain open and the parent class close_event closes the databases."""
        self.close_window()


class AddSpecialBondConditionsDialog(BaseDialog, Ui_AddSpecialBondConditionsDialog):
    """The AddSpecialBondConditionsDialog is for Bond Conditions for NGBond and FTABond Dialogs."""
    @logger.catch
    def __init__(self, main_dialog, parent=None):
        self.charges_list = main_dialog.case_information.charges_list  # Show charges on banner
        super().__init__(self, parent)
        self.case_information = main_dialog.case_information
        self.domestic_violence = main_dialog.domestic_violence_checkBox.isChecked()
        self.admin_license_suspension = main_dialog.admin_license_suspension_checkBox.isChecked()
        self.vehicle_seizure = main_dialog.vehicle_seizure_checkBox.isChecked()
        self.no_contact = main_dialog.no_contact_checkBox.isChecked()
        self.custodial_supervision = main_dialog.custodial_supervision_checkBox.isChecked()
        self.other_conditions = main_dialog.other_conditions_checkBox.isChecked()
        self.enable_condition_frames()

    @logger.catch
    def connect_signals_to_slots(self):
        self.cancel_Button.pressed.connect(self.close_event)
        self.add_special_conditions_Button.pressed.connect(self.add_special_conditions)
        self.add_special_conditions_Button.released.connect(self.close_window)

    @logger.catch
    def enable_condition_frames(self):
        if self.domestic_violence is True:
            self.domestic_violence_frame.setEnabled(True)
        if self.admin_license_suspension is True:
            self.admin_license_suspension_frame.setEnabled(True)
        if self.vehicle_seizure is True:
            self.vehicle_seizure_frame.setEnabled(True)
        if self.no_contact is True:
            self.no_contact_frame.setEnabled(True)
        if self.custodial_supervision is True:
            self.custodial_supervision_frame.setEnabled(True)
        if self.other_conditions is True:
            self.other_conditions_frame.setEnabled(True)

    @logger.catch
    def add_special_conditions(self):
        """The method is connected to the pressed() signal of add_special_conditions_Button on the
        Add Special Conditions screen."""
        if self.domestic_violence is True:
            self.add_domestic_violence_terms()
        if self.admin_license_suspension is True:
            self.add_admin_license_suspension_terms()

    @logger.catch
    def add_domestic_violence_terms(self):
        self.case_information.special_bond_conditions.domestic_violence_vacate = (
            self.domestic_violence_vacate_checkBox.isChecked()
        )

    @logger.catch
    def add_admin_license_suspension_terms(self):
        self.case_information.admin_license_suspension.ordered = (
            self.admin_license_suspension
        )
        self.case_information.admin_license_suspension.objection = (
            self.admin_license_suspension_objection_box.currentText()
        )
        self.case_information.admin_license_suspension.disposition = (
            self.admin_license_suspension_disposition_box.currentText()
        )
        self.case_information.admin_license_suspension.explanation = (
            self.admin_license_suspension_explanation_box.text()
        )

    @logger.catch
    def modify_view(self):
        """Modifies the view that is created by the UI file. Gets the total number of charges
        from the charges in charges_list then loops through the charges_list and adds parts of
        each charge to the view."""
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint |
                            QtCore.Qt.WindowMaximizeButtonHint)
        column = self.charges_gridLayout.columnCount() + 1
        for _index, charge in enumerate(self.charges_list):
            charge = vars(charge)
            if charge is not None:
                self.charges_gridLayout.addWidget(QLabel(charge.get("offense")), 0, column)
                self.charges_gridLayout.addWidget(QLabel(charge.get("statute")), 1, column)
                column += 1


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
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint |
                            QtCore.Qt.WindowMaximizeButtonHint)
        self.original_charge_box.setCurrentText(self.current_offense)
        self.amended_charge_box.addItems(create_offense_list())

    @logger.catch
    def connect_signals_to_slots(self):
        self.clear_fields_Button.pressed.connect(self.clear_amend_charge_fields)
        self.amend_offense_Button.pressed.connect(self.amend_offense)
        self.cancel_Button.pressed.connect(self.close_event)

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

    @logger.catch
    def close_event(self):
        """Uses subclass of close_event so that it doesn't close databases."""
        self.close_window()


if __name__ == "__main__":
    print("BCD ran directly")
else:
    print("BCD ran when imported")
    database_offenses = create_database_connections()
