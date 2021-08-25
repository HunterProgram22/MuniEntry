import pathlib

from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QDialog, QLabel
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
        self.offense_count_index = 0 #This is used to navigate the charges list
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

    def delete_offense(self):
        del self.case_information.charges_list[self.case_information.total_charges-1]
        self.case_information.total_charges -= 1
        print(self.case_information.charges_list)

    def delete_offense_from_view(self):
        self.charges_gridLayout.removeWidget(QLabel(), 0, self.offense_count-1)


    def add_offense_to_view(self):
        self.charges_gridLayout.addWidget(
            QLabel(self.case_information.charges_list[self.offense_count_index].offense),
            0,
            self.offense_count
        )
        self.charges_gridLayout.addWidget(
            QLabel(self.case_information.charges_list[self.offense_count_index].statute), 1, self.offense_count
        )
        self.charges_gridLayout.addWidget(
            QLabel(self.case_information.charges_list[self.offense_count_index].degree), 2, self.offense_count
        )
        self.charges_gridLayout.addWidget(
            QLabel(self.case_information.charges_list[self.offense_count_index].plea), 3, self.offense_count
        )
        self.charges_gridLayout.addWidget(
            QLabel(self.case_information.charges_list[self.offense_count_index].finding), 4, self.offense_count
        )
        self.charges_gridLayout.addWidget(
            QLabel(self.case_information.charges_list[self.offense_count_index].fines_amount), 5, self.offense_count
        )
        self.charges_gridLayout.addWidget(
            QLabel(self.case_information.charges_list[self.offense_count_index].fines_suspended), 6, self.offense_count
        )
        self.charges_gridLayout.addWidget(
            QLabel(self.case_information.charges_list[self.offense_count_index].court_costs), 7, self.offense_count
        )
        self.case_information.total_charges = self.offense_count
        self.offense_count_index += 1

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
