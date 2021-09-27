"""The module that contains all controller classes that are commmon to criminal
cases (criminal includes traffic). """
import sys
import os
import pathlib
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docxtpl import DocxTemplate
from loguru import logger

from PyQt5.uic import loadUi
from PyQt5.QtCore import QDate, Qt, QDateTime
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QLabel, QLineEdit
    )
from PyQt5.QtSql import QSqlDatabase

from views.case_information_dialog_ui import Ui_CaseInformationDialog
from views.amend_offense_dialog_ui import Ui_AmendOffenseDialog
from views.add_conditions_dialog_ui import Ui_AddConditionsDialog
from models.CaseInformation import (
    CaseInformation,
    CriminalCharge,
    AmendOffenseDetails,
    LicenseSuspension,
    CommunityControlTerms,
    CommunityServiceTerms
)
from resources.db.DatabaseCreation import create_offense_list

PATH = str(pathlib.Path().absolute())
TEMPLATE_PATH = PATH + "\\resources\\Templates\\"
SAVE_PATH = PATH + "\\resources\\Saved\\"
DB_PATH = PATH + "\\resources\\db\\"
CHARGES_DATABASE = DB_PATH + "\\charges.sqlite"


class BaseCriminalDialog(QDialog):
    """This class is a base class to provide methods that are used by some or
    all class controllers that are used in the application. This class is never
    instantiated as its own dialog, but the init contains the setup for all
    inherited class controllers."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def close_window(self):
        """Function connected to a button to close the window. Can be connected
        to any button press/click/release to close a window."""
        self.close()

    def create_entry(self):
        """The standard function used to create an entry when a create entry
        button is press/click/released."""
        self.doc = DocxTemplate(self.template_path)
        self.doc.render(self.case_information.get_case_information())
        self.set_document_name()
        self.doc.save(SAVE_PATH + self.docname)
        os.startfile(SAVE_PATH + self.docname)

    def set_document_name(self):
        """Sets document name based on the case number and name of the template
        must include '.docx' to make it a Word document."""
        self.docname = (
            self.case_information.case_number + "_" + \
            self.template_name + ".docx"
        )

    def set_case_information_banner(self):
        """Sets the banner on a view of the interface. It modifies label
        widgets on the view to text that was entered."""
        self.defendant_name_label.setText(
            "State of Ohio v. {defendant_first_name} " \
            "{defendant_last_name}".format(
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

    def update_case_information(self):
        pass



class AddConditionsDialog(BaseCriminalDialog, Ui_AddConditionsDialog):
    def __init__(self, case_information=None, parent=None):
        super().__init__(parent)
        self.case_information = case_information
        self.license_suspension_details = LicenseSuspension()
        self.community_control_terms = CommunityControlTerms()
        self.community_service_terms = CommunityServiceTerms()

    @logger.catch
    def add_conditions(self, case_information=None):
        """FIX/DEBUG: This function is only being called if two positional
        arguments are set as parameters. Not sure why, but it works if it is
        set up to allow self and case_information even though case_information
        is not used directly as far as I can tell. This is likely the bool that
        is being fired when the button is pressed and I'm only seeing this when
        I wrap a function in a logger.

        TODO: This is not tied to the additional conditions checkbox grid on
        the MMD yet. It was tied to the Comm Service checkbox initially but
        it would revert status of case_information.community_service to the
        bool state of that box - either change variable name or remove Yes/No
        from dialog on add conditions CS box because it can create a conflict.

        The dialog should only enable boxes that were checked prior to add
        conditions. Then the values for enabled box should default to the most
        common condition terms.
        """
        if self.community_service_ordered_box.currentText() == "Yes":
            self.community_service_terms.hours_of_service = (
                self.community_service_hours_ordered_box.value()
            )
            self.community_service_terms.days_to_complete_service = (
                self.community_service_days_to_complete_box.currentText()
            )
            self.community_service_terms.due_date_for_service = (
                self.community_service_date_to_complete_box.date().toString(
                "MMMM dd, yyyy")
            )
            self.case_information.community_service_terms = (
                self.community_service_terms
            )
        else:
            self.case_information.community_service_terms = None
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
            self.remedial_driving_class_required = False
        if self.type_of_community_control_box.currentText() != "None":
            self.community_control_terms.type_of_community_control = (
                self.type_of_community_control_box.currentText()
            )
            self.community_control_terms.term_of_community_control = (
                self.term_of_community_control_box.currentText()
            )
            self.case_information.community_control_terms = (
                self.community_control_terms
            )
        self.case_information.license_suspension_details = (
            self.license_suspension_details
        )


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
        self.amend_offense_details.motion_disposition = (
            self.motion_decision_box.currentText()
        )
        self.case_information.amend_offense_details = self.amend_offense_details
