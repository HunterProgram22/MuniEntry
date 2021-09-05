import pathlib

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

from views.minor_misdemeanor_dialog_ui import Ui_MinorMisdemeanorDialog
from models.CaseInformation import CaseInformation, CriminalCharge
from controllers.CriminalDialogs import BaseCriminalDialog, AmendOffenseDialog
from controllers.DatabaseCreation import create_offense_list

PATH = str(pathlib.Path().absolute())
TEMPLATE_PATH = PATH + "\\resources\\templates\\"
SAVE_PATH = PATH + "\\resources\\saved\\"
DB_PATH = PATH + "\\resources\\db\\"


class MinorMisdemeanorDialog(BaseCriminalDialog, Ui_MinorMisdemeanorDialog):
    def __init__(self, judicial_officer, parent=None):
        super().__init__(parent)
        self.case_information = CaseInformation(judicial_officer)
        self.offense_count = 0
        self.delete_button_index = 0 #This is used to index a delete button to the charge list
        self.delete_button_list = [] #This is used to map a delete button to a charge in charge list
        self.set_template()
        self.database = QSqlDatabase.addDatabase("QSQLITE")
        self.database.setDatabaseName(DB_PATH + "\\charges.sqlite")
        self.database.open()

        # View Setup
        self.offense_list, self.statute_list = create_offense_list()
        self.statute_choice_box.addItems(self.statute_list)
        self.offense_choice_box.addItems(self.offense_list)
        self.plea_trial_date.setDate(QtCore.QDate.currentDate())
        self.balance_due_date.setDate(QtCore.QDate.currentDate())

    def set_template(self):
        if self.case_information.judicial_officer == "Bunner":
            self.template = TEMPLATE_PATH + "Bunner_No_Jail_Traffic_Template.docx"
            self.template_name = "Traffic Judgment Entry"
        elif self.case_information.judicial_officer == "Pelanda":
            self.template = TEMPLATE_PATH + "Pelanda_No_Jail_Traffic_Template.docx"
            self.template_name = "Traffic Judgment Entry"
        elif self.case_information.judicial_officer == "Rohrer":
            self.template = TEMPLATE_PATH + "Rohrer_No_Jail_Traffic_Template.docx"
            self.template_name = "Traffic Judgment Entry"
        elif self.case_information.judicial_officer == "Hemmeter":
            self.template = TEMPLATE_PATH + "Hemmeter_No_Jail_Traffic_Template.docx"
            self.template_name = "Traffic Judgment Entry"


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
        self.add_offense_to_view()


    def add_offense_to_view(self):
        """Adds the offense that was added through add_offense method to the view/GUI."""
        row = 0
        grid_rows = 8 #This should maybe be obtained through rowCount() - not magic number
        column = self.charges_gridLayout.columnCount() + 1
        added_charge_index = len(self.case_information.charges_list)-1
        charge_dict = (vars(self.case_information.charges_list[added_charge_index]))
        for key, value in charge_dict.items():
            if value is not None:
                self.charges_gridLayout.addWidget(QLabel(value), row, column)
                row +=1
        delete_button = QPushButton("Delete")
        self.delete_button_list.append(delete_button)
        delete_button.setStyleSheet("background-color: rgb(160, 160, 160);")
        delete_button.clicked.connect(self.delete_offense)
        self.charges_gridLayout.addWidget(delete_button, row, column)
        self.case_information.total_charges = self.offense_count
        return None


    def delete_offense(self):
        """TEST: Make sure it is deleting the offense based on the button for that offense."""
        index = self.delete_button_list.index(self.sender())
        #print(self.sender())
        #print(index)
        del self.case_information.charges_list[index]
        del self.delete_button_list[index]
        self.case_information.total_charges -= 1
        self.offense_count -=1
        self.delete_offense_from_view()

    def delete_offense_from_view(self):
        index = self.charges_gridLayout.indexOf(self.sender())
        column = self.charges_gridLayout.getItemPosition(index)[1]
        for row in range(self.charges_gridLayout.rowCount()):
            layout_item = self.charges_gridLayout.itemAtPosition(row, column)
            if layout_item is not None:
                layout_item.widget().deleteLater()
                self.charges_gridLayout.removeItem(layout_item)

    def update_case_information(self):
        self.case_information.case_number = self.case_number_lineEdit.text()
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
