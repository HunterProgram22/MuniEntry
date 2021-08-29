import pathlib

from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

from views.traffic_case_information_dialog_ui import Ui_TrafficCaseInformationDialog
from models.CaseInformation import CaseInformation, CriminalCharge
from controllers.CriminalDialogs import BaseCriminalDialog, AmendOffenseDialog
from controllers.DatabaseCreation import create_offense_list

PATH = str(pathlib.Path().absolute())
TEMPLATE_PATH = PATH + "\\resources\\templates\\"
SAVE_PATH = PATH + "\\resources\\saved\\"
DB_PATH = PATH + "\\resources\\db\\"


class TrafficCaseInformationDialog(BaseCriminalDialog, Ui_TrafficCaseInformationDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.case_information = CaseInformation()
        self.offense_count = 0
        self.offense_view_count_index = 0 #This is used to navigate the charges list
        self.template = TEMPLATE_PATH + "No_Jail_Traffic_Template.docx"
        self.template_name = "Traffic Judgment Entry"
        self.database = QSqlDatabase.addDatabase("QSQLITE")
        self.database.setDatabaseName(DB_PATH + "\\charges.sqlite")
        self.database.open()

        # View Setup
        self.offense_list, self.statute_list = create_offense_list()
        self.statute_choice_box.addItems(self.statute_list)
        self.offense_choice_box.addItems(self.offense_list)
        self.plea_trial_date.setDate(QtCore.QDate.currentDate())
        self.balance_due_date.setDate(QtCore.QDate.currentDate())

    def amend_offense(self):
        AmendOffenseDialog(self.case_information).exec()

    def closeEvent(self, event):
        self.database.close()

    def add_offense(self):
        """Creates a criminal charge object and adds the data in the fields
        in the view to the object. The criminal charge is then added to the case
        information model (the criminal charges list).
        The offense is added to the view by the method add_offense_to_view,
        not this method. This method is triggered on press of the Add Offense
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
        self.offense_count += 1
        """TODO: Add offense to view function here so its not a separate signal."""

    def delete_offense(self):
        """Deletes the last offense in the criminal_charges list (i.e. the one that
        was added most recently.) This method does not remove the offense from view,
        that is done by delete_offense_from_view. Triggered on press of Delete Offense
        button."""
        del self.case_information.charges_list[self.case_information.total_charges-1]
        self.case_information.total_charges -= 1
        self.offense_count -=1
        print(self.case_information.charges_list)
        print("Number of columns is: " + str(self.charges_gridLayout.columnCount()))

    def add_offense_to_view(self):
        """Adds the offense that was added through add_offense method to the view/GUI.
        This method is triggered on release of the Add Offense button."""
        column = len(self.case_information.charges_list) + 1
        added_charge_index = len(self.case_information.charges_list)-1
        self.charges_gridLayout.addWidget(
            QLabel(self.case_information.charges_list[added_charge_index].offense), 0, column
        )
        self.charges_gridLayout.addWidget(
            QLabel(self.case_information.charges_list[added_charge_index].statute), 1, column
        )
        self.charges_gridLayout.addWidget(
            QLabel(self.case_information.charges_list[added_charge_index].degree), 2, column
        )
        self.charges_gridLayout.addWidget(
            QLabel(self.case_information.charges_list[added_charge_index].plea), 3, column
        )
        self.charges_gridLayout.addWidget(
            QLabel(self.case_information.charges_list[added_charge_index].finding), 4, column
        )
        self.charges_gridLayout.addWidget(
            QLabel(self.case_information.charges_list[added_charge_index].fines_amount), 5, column
        )
        self.charges_gridLayout.addWidget(
            QLabel(self.case_information.charges_list[added_charge_index].fines_suspended), 6, column
        )
        self.charges_gridLayout.addWidget(
            QLabel(self.case_information.charges_list[added_charge_index].court_costs), 7, column
        )
        self.delete_button = QPushButton("Delete")
        self.delete_button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.delete_button.clicked.connect(self.delete_offense_from_view)
        self.charges_gridLayout.addWidget(
            self.delete_button, 8, column
        )
        self.case_information.total_charges = self.offense_count

    def delete_offense_from_view(self):
        """FIX: This works, but messes up the index if you add after you delete
        and add another and try to delete again - need to fix."""
        self.delete_offense()
        index = self.charges_gridLayout.indexOf(self.sender())
        column = self.charges_gridLayout.getItemPosition(index)[1]
        print("Column is: " + str(column))
        for row in range(self.charges_gridLayout.rowCount()):
            layout_item = self.charges_gridLayout.itemAtPosition(row, column)
            if layout_item is not None:
                layout_item.widget().deleteLater()
                self.charges_gridLayout.removeItem(layout_item)

    def update_case_information(self):
        self.case_information.case_number = self.case_number.text()
        self.case_information.defendant_name = self.defendant_name.text()
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
        key = self.offense_choice_box.currentText()
        query = QSqlQuery()
        query.prepare(
            "SELECT * FROM charges WHERE "
            "offense LIKE '%' || :key || '%'"
            )
        query.bindValue(":key", key)
        """FIX: When typing in editable box this calls the query for every keystroke"""
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
        key = self.statute_choice_box.currentText()
        query = QSqlQuery()
        query.prepare(
            "SELECT * FROM charges WHERE "
            "statute LIKE '%' || :key || '%'"
            )
        query.bindValue(":key", key)
        """FIX: When typing in editable box this calls the query for every keystroke"""
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
        """Function to set the pay date based on the amount of time given the defendant
        to pay his costs and fines."""
        if self.ability_to_pay_box.currentText() == "forthwith":
            self.balance_due_date.setDate(QDate.currentDate())
        elif self.ability_to_pay_box.currentText() == "within 30 days":
            self.balance_due_date.setDate(QDate.currentDate().addDays(30))
        elif self.ability_to_pay_box.currentText() == "within 60 days":
            self.balance_due_date.setDate(QDate.currentDate().addDays(60))
        elif self.ability_to_pay_box.currentText() == "within 90 days":
            self.balance_due_date.setDate(QDate.currentDate().addDays(90))
