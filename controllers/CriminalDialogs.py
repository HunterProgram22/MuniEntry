import sys, os, pathlib
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docxtpl import DocxTemplate
from PyQt5.uic import loadUi

from PyQt5.QtCore import QDate, Qt, QDateTime
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QLabel
from PyQt5.QtSql import QSqlDatabase

from views.case_information_dialog_ui import Ui_CaseInformationDialog
from views.amend_offense_dialog_ui import Ui_AmendOffenseDialog
from views.add_conditions_dialog_ui import Ui_AddConditionsDialog
from models.CaseInformation import (
    CaseInformation,
    CriminalCharge,
    AmendOffenseDetails,
)
from resources.db.DatabaseCreation import create_offense_list

PATH = str(pathlib.Path().absolute())
TEMPLATE_PATH = PATH + "\\resources\\Templates\\"
SAVE_PATH = PATH + "\\resources\\Saved\\"
DB_PATH = PATH + "\\resources\\db\\"
CHARGES_DATABASE = DB_PATH + "\\charges.sqlite"

"""TODO: Need to add maximize and minimize buttons for controllers."""


class BaseCriminalDialog(QDialog):
    """This class is a base class to provide methods that are used by some or all
    class controllers that are used in the application. This class is never instantiated
    as its own dialog, but the init contains the setup for all inherited class controllers."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def close_window(self):
        self.close()

    def create_entry(self):
        self.doc = DocxTemplate(self.template_path)
        self.doc.render(self.case_information.get_case_information())
        self.set_document_name()
        self.doc.save(SAVE_PATH + self.docname)
        os.startfile(SAVE_PATH + self.docname)

    def set_document_name(self):
        self.docname = (
            self.case_information.case_number + "_" + self.template_name + ".docx"
        )

    def set_case_information_banner(self):
        self.defendant_name_label.setText(
            "State of Ohio v. {defendant_first_name} {defendant_last_name}".format(
                defendant_first_name = self.case_information.defendant_first_name,
                defendant_last_name = self.case_information.defendant_last_name
                )
        )
        self.case_number_label.setText(self.case_information.case_number)
        if self.case_information.defendant_attorney_name is not None:
            self.defendant_attorney_name_label.setText(
                "Attorney: " + self.case_information.defendant_attorney_name
            )
        else:
            self.defendant_attorney_name_label.setText("Attorney: None")

    def set_charges_grid(self):
        """TODO: the criminal charge is a list in case information so need to
        account for that when setting charges grid to get it to work."""
        total_charges = self.case_information.total_charges
        for charge in range(total_charges):
            self.charges_gridLayout.addWidget(
                QLabel(self.case_information.criminal_charge.offense), 0, charge
            )
            self.charges_gridLayout.addWidget(
                QLabel(self.case_information.criminal_charge.plea), 1, charge
            )
            self.charges_gridLayout.addWidget(
                QLabel(self.case_information.criminal_charge.finding), 2, charge
            )
            self.charges_gridLayout.addWidget(
                QLabel(self.case_information.criminal_charge.fines_amount), 3, charge
            )
            self.charges_gridLayout.addWidget(
                QLabel(self.case_information.criminal_charge.fines_suspended), 4, charge
            )
            self.charges_gridLayout.addWidget(
                QLabel(self.case_information.criminal_charge.jail_days), 5, charge
            )
            self.charges_gridLayout.addWidget(
                QLabel(self.case_information.criminal_charge.jail_days_suspended),
                6,
                charge,
            )
            total_charges -= 1

    def update_case_information(self):
        pass



class AddConditionsDialog(BaseCriminalDialog, Ui_AddConditionsDialog):
    def __init__(self, case_information, parent=None):
        super().__init__(parent)
        self.case_information = case_information


class CaseInformationDialog(BaseCriminalDialog, Ui_CaseInformationDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.case_information = CaseInformation()

    def set_dialog(self, bool):
        if self.sender().objectName() == "waived_counsel_checkbox":
            if bool == True:
                self.defendant_attorney_name.setEnabled(False)
            else:
                self.defendant_attorney_name.setEnabled(True)

    def update_case_information(self):
        """This slot is tied to the signal 'pressed()', which has precedence over
        released() and clicked()."""
        self.case_information.case_number = self.case_number.text()
        self.case_information.defendant_name = self.defendant_name.text()
        self.case_information.defendant_attorney_name = (
            self.defendant_attorney_name.text()
        )
        self.case_information.plea_trial_date = self.plea_trial_date.date().toString(
            "MMMM dd, yyyy"
        )
        self.case_information.case_number = self.case_number.text()
        self.case_information.defendant_name = self.defendant_name.text()
        self.case_information.defendant_attorney_name = (
            self.defendant_attorney_name.text()
        )
        if self.is_citizen_checkbox.isChecked():
            self.case_information.is_citizen = True
        if self.citizen_deportation_checkbox.isChecked():
            self.case_information.citizen_deportation = True
        if self.waived_counsel_checkbox.isChecked():
            self.case_information.waived_counsel = True
        if self.understood_plea_checkbox.isChecked():
            self.case_information.understood_plea = True
        else:
            self.case_information.understood_plea = False


class AmendOffenseDialog(BaseCriminalDialog, Ui_AmendOffenseDialog):
    def __init__(self, case_information=None, parent=None):
        super().__init__(parent)
        self.case_information = case_information
        self.set_case_information_banner()
        self.set_database()
        self.modify_view()

    def modify_view(self):
        """The modify view method updates the view that is created on init.
        Place items in this method that can't be added directly in QtDesigner
        so that they don't need to be changed in the view file each time pyuic5
        is run."""
        self.offense_list, self.statute_list = create_offense_list()
        self.original_charge_box.addItems(self.offense_list)
        self.amended_charge_box.addItems(self.offense_list)

    def set_database(self):
        """
        https://www.tutorialspoint.com/pyqt/pyqt_database_handling.htm
        https://doc.qt.io/qtforpython/overviews/sql-connecting.html
        """
        self.database = QSqlDatabase.addDatabase("QSQLITE")
        self.database.setDatabaseName(CHARGES_DATABASE)
        self.database.open()

    def amend_offense(self):
        self.amend_offense_details = AmendOffenseDetails()
        self.amend_offense_details.original_charge = (
            self.original_charge_box.currentText()
        )
        self.amend_offense_details.amended_charge = (
            self.amended_charge_box.currentText()
        )
        self.amend_offense_details.amending_procedure = (
            self.pursuant_to_box.currentText()
        )
        self.amend_offense_details.motion_disposition = (
            self.motion_decision_box.currentText()
        )
        self.case_information.amend_offense_details = self.amend_offense_details
