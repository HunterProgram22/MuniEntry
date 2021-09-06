"""The controller module for the minor misdemeanor dialog - it is not limited
to minor misdemeanors, but does not contain functions to account for jail time.
Loads all charges - including non-minor-misdemeanors from a databse."""

import pathlib

from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

from views.minor_misdemeanor_dialog_ui import Ui_MinorMisdemeanorDialog
from models.CaseInformation import CaseInformation, CriminalCharge
from models.Templates import TEMPLATE_DICT
from controllers.CriminalDialogs import BaseCriminalDialog, AmendOffenseDialog
from resources.db.DatabaseCreation import create_offense_list


PATH = str(pathlib.Path().absolute())
TEMPLATE_PATH = PATH + "\\resources\\templates\\"
SAVE_PATH = PATH + "\\resources\\saved\\"
DB_PATH = PATH + "\\resources\\db\\"
CHARGES_DATABASE = DB_PATH + "\\charges.sqlite"


class MinorMisdemeanorDialog(BaseCriminalDialog, Ui_MinorMisdemeanorDialog):
    """This dialog is used when there will not be any jail time imposed. It does
    not inherently limit cases to minor misdemeanors or unclassified
    misdemeanors, however, it does not include fields to enter jail time.

    FIX: Pylint says too many attributes 11/7. Possibly reduce/refactor."""

    def __init__(self, judicial_officer, parent=None):
        super().__init__(parent)
        self.case_information = CaseInformation(judicial_officer)
        self.modify_view()
        self.set_counters()
        self.set_database()
        self.set_template()
        self.criminal_charge = None
        self.pay_date_dict = {
            "forthwith": 0,
            "within 30 days": 30,
            "within 60 days": 60,
            "within 90 days": 90,
        }

    def modify_view(self):
        """The modify view method updates the view that is created on init.
        Place items in this method that can't be added directly in QtDesigner
        so that they don't need to be changed in the view file each time pyuic5
        is run."""
        self.offense_list, self.statute_list = create_offense_list()
        self.statute_choice_box.addItems(self.statute_list)
        self.offense_choice_box.addItems(self.offense_list)
        self.plea_trial_date.setDate(QtCore.QDate.currentDate())
        self.balance_due_date.setDate(QtCore.QDate.currentDate())

    def set_counters(self):
        """The counters track whether an item is added to the model/view. The
        delete button index is used to specify which delete button in the
        delete button list needs to be deleted when a charge is deleted."""
        self.charge_count = 0
        self.delete_button_index = 0
        self.delete_button_list = []

    def set_database(self):
        """
        https://www.tutorialspoint.com/pyqt/pyqt_database_handling.htm
        https://doc.qt.io/qtforpython/overviews/sql-connecting.html
        """
        self.database = QSqlDatabase.addDatabase("QSQLITE")
        self.database.setDatabaseName(CHARGES_DATABASE)
        self.database.open()

    def set_template(self):
        """The TEMPLATE_DICT stores a template for each judicial officer. In
        the future this should be connected to set the template from a database
        with the information to make updating easier."""
        template = TEMPLATE_DICT.get(self.case_information.judicial_officer)
        self.template_path = template.template_path
        self.template_name = template.template_name

    def amend_offense(self):
        """Opens the amend offense dialog as a modal window.

        TODO: The self.case_information is not currently transferring."""
        AmendOffenseDialog(self.case_information).exec()

    def close_event(self):
        """TODO: This does not appear to close the database. It is currently
        tied to clicked() on createEntryButton."""
        self.database.close()

    def add_charge(self):
        """Creates a criminal charge object and adds the data in the view to
        the object. The criminal charge is then added to the case information
        model (by appending the charge object to the criminal charges list).
        The offense is added to the view by the method add_charge_to_view,
        not this method. This method is triggered on press of the Add Charge
        button."""
        self.criminal_charge = CriminalCharge()
        self.criminal_charge.offense = self.offense_choice_box.currentText()
        self.criminal_charge.statute = self.statute_choice_box.currentText()
        self.criminal_charge.degree = self.degree_choice_box.currentText()
        self.criminal_charge.plea = self.plea_choice_box.currentText()
        self.criminal_charge.finding = self.finding_choice_box.currentText()
        self.criminal_charge.fines_amount = self.fines_amount.text()
        self.criminal_charge.fines_suspended = self.fines_suspended.text()
        self.criminal_charge.court_costs = self.court_costs_box.currentText()
        self.case_information.add_charge(self.criminal_charge)
        self.charge_count += 1
        self.add_charge_to_view()

    def add_charge_to_view(self):
        """Adds the charge that was added through add_charge method to the
        view/GUI. The first row=0 because of python zero-based indexing. The
        column is set at one more than the current number of columns because
        it is the column to which the charge will be added.

        :added_charge_index: - The added charge index is one less than the
        total charges in charges_list because of zero-based indexing. Thus, if
        there is one charge, the index of the charge to be added to the
        charge_dict from the charges_list is 0.

        TODO: Is the charges_dict really necessary because it is a local
        variable so each time the function is called only the new charge to be
        added is in the charge_dict. Can it be done with just the list?
        """
        row = 0
        column = self.charges_gridLayout.columnCount() + 1
        added_charge_index = len(self.case_information.charges_list) - 1
        charge_dict = vars(self.case_information.charges_list[added_charge_index])
        for value in charge_dict.values():
            if value is not None:
                self.charges_gridLayout.addWidget(QLabel(value), row, column)
                row += 1
        delete_button = QPushButton("Delete")
        self.delete_button_list.append(delete_button)
        delete_button.setStyleSheet("background-color: rgb(160, 160, 160);")
        delete_button.clicked.connect(self.delete_charge)
        self.charges_gridLayout.addWidget(delete_button, row, column)
        self.case_information.total_charges = self.charge_count

    def delete_charge(self):
        """Deletes the offense from the case_information.charges list. Then
        decrements the total charges by one so that other functions using the
        total charges for indexing are correct.

        TODO: It is duplicative to have self.case_information.total_charges and
        self.charge_count, can code be refactored to just use
        self.case_information.total_charges. Issue is the timing of adding to
        the view and the model. Perhaps add to view first??

        TEST: Make sure it is deleting the offense based on the button
        for that offense."""
        index = self.delete_button_list.index(self.sender())
        del self.case_information.charges_list[index]
        del self.delete_button_list[index]
        self.case_information.total_charges -= 1
        self.charge_count -= 1
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

    """PAUSE REFACTORING"""

    def update_case_information(self):
        self.case_information.case_number = self.case_number_lineEdit.text()
        self.case_information.defendant_last_name = (
            self.defendant_last_name_lineEdit.text()
        )
        self.case_information.plea_trial_date = self.plea_trial_date.date().toString(
            "MMMM dd, yyyy"
        )
        self.case_information.ability_to_pay_time = (
            self.ability_to_pay_box.currentText()
        )
        self.case_information.balance_due_date = self.balance_due_date.date().toString(
            "MMMM dd, yyyy"
        )

    def set_statute(self):
        """FIX: When typing in editable box this calls the query for every
        keystroke"""
        key = self.offense_choice_box.currentText()
        query = QSqlQuery()
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
        """FIX: When typing in editable box this calls the query for every
        keystroke"""
        key = self.statute_choice_box.currentText()
        query = QSqlQuery()
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
        """TODO: Need to update the addDays to account for the tuesday after
        the 30, 60, 90 days."""
        days = self.pay_date_dict[self.ability_to_pay_box.currentText()]
        self.balance_due_date.setDate(QDate.currentDate().addDays(days))
