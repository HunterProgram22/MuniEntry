"""The controller module for the LEAP plea dialog."""
import os
import pathlib
from datetime import date, timedelta
from loguru import logger
from docxtpl import DocxTemplate

from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QLabel, QPushButton, QMessageBox, QComboBox, QLineEdit
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

from views.custom_widgets import (
    PleaComboBox,
    FindingComboBox,
    FineLineEdit,
    FineSuspendedLineEdit,
    DeleteButton,
    AmendButton,
)
from views.leap_plea_long_dialog_ui import Ui_LeapPleaLongDialog
from models.template_types import TEMPLATE_DICT
from models.case_information import CaseInformation, CriminalCharge
from controllers.criminal_dialogs import BaseCriminalDialog
from resources.db.DatabaseCreation import create_offense_list, create_statute_list


PATH = str(pathlib.Path().absolute())
TEMPLATE_PATH = PATH + "\\resources\\templates\\"
SAVE_PATH = PATH + "\\resources\\saved\\"
DB_PATH = PATH + "\\resources\\db\\"
CHARGES_DATABASE = DB_PATH + "\\charges.sqlite"


class LeapPleaLongDialog(BaseCriminalDialog, Ui_LeapPleaLongDialog):
    """The dialog inherits from the BaseCriminalDialog (controller) and the
    Ui_LeapPleaLongDialog (view)."""

    @logger.catch
    def __init__(self, judicial_officer, parent=None):
        super().__init__(parent)
        self.case_information = CaseInformation(judicial_officer)
        self.modify_view()
        self.connect_signals_to_slots()
        self.dialog_name = "Leap Plea Dialog"
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.delete_button_list = []
        self.complete_program_date_dict = {
            "forthwith": 0,
            "120 days": 120,
        }
        self.set_sentencing_date("120 days")

    @logger.catch
    def create_entry(self):
        """The standard function used to create an entry when a create entry
        button is press/click/released.

        TODO: This needs to be refactored back to Criminal Dialogs with template
        and path information set to the template module."""
        self.doc = DocxTemplate(self.template.template_path)
        self.doc.render(self.case_information.get_case_information())
        self.set_document_name()
        self.doc.save(SAVE_PATH + self.docname)
        os.startfile(SAVE_PATH + self.docname)

    @logger.catch
    def modify_view(self):
        """The modify view method updates the view that is created on init from the
        Ui_MinorMisdemeanorDialog. Place items in this method that can't be added
        directly in QtDesigner so that they don't need to be changed in the view file
        each time pyuic5 is run."""
        statute_list = create_statute_list()
        self.statute_choice_box.addItems(statute_list)
        self.offense_choice_box.addItems(create_offense_list())
        self.plea_trial_date.setDate(QtCore.QDate.currentDate())
        #self.balance_due_date.setDate(QtCore.QDate.currentDate())
        self.statute_choice_box.setCurrentText("")
        self.offense_choice_box.setCurrentText("")

    @logger.catch
    def connect_signals_to_slots(self):
        """The method connects any signals to slots. Generally, connecting with
        pressed is preferred to clicked because a clicked event sends a bool
        argument to the function. However, clicked is used in some instances
        because it is a press and release of a button. Using pressed sometimes
        caused an event to be triggered twice."""
        self.cancel_Button.pressed.connect(self.close_event)
        self.clear_fields_case_Button.pressed.connect(self.clear_case_information_fields)
        self.create_entry_Button.pressed.connect(self.create_entry_process)
        self.add_charge_Button.clicked.connect(self.add_charge_process)
        self.clear_fields_charge_Button.pressed.connect(self.clear_charge_fields)
        self.statute_choice_box.currentTextChanged.connect(self.set_offense)
        self.offense_choice_box.currentTextChanged.connect(self.set_statute)
        self.guilty_all_Button.pressed.connect(self.guilty_all_plea_and_findings)
        self.time_to_complete_box.currentTextChanged.connect(self.set_sentencing_date)

    @logger.catch
    def update_case_information(self):
        """The method calls functions to update the case information model
        with the data for the case that is in the fields on the view. This does
        not update the model
        with information in the charge fields (offense, statute, plea, etc.)
        the charge information is transferred to the model upon press of the
        add charge button.

        Fields that are updated upon pressed() of createEntryButton = case
        number, first name, last name."""
        self.update_party_information()
        self.add_dispositions_and_fines()

    @logger.catch
    def update_party_information(self):
        """This is subclassed from Criminal Dialogs (TODO: it will be once i refactor)."""
        self.case_information.case_number = self.case_number_lineEdit.text()
        self.case_information.defendant.first_name = self.defendant_first_name_lineEdit.text()
        self.case_information.defendant.last_name = self.defendant_last_name_lineEdit.text()
        self.case_information.plea_trial_date = self.plea_trial_date.date().toString("MMMM dd, yyyy")
        self.case_information.sentencing_date = self.sentencing_date.date().toString("MMMM dd, yyyy")

    @logger.catch
    def add_dispositions_and_fines(self):
        """Row 3 - plea.

        Column count increases by 2 instead of one due to grid adding two
        columns when a charge is added (odd numbered column is empty)."""
        column = 2
        try:
            for index in range(len(self.case_information.charges_list)):
                self.case_information.charges_list[index].plea = self.charges_gridLayout.itemAtPosition(3,column).widget().currentText()
                index +=1
                column +=2
        except AttributeError:
            print("Attribute error allowed to pass for lack of widget")

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
        self.add_delete_button_to_view(row, column)

    def add_delete_button_to_view(self, row, column):
        delete_button = DeleteButton()
        self.delete_button_list.append(delete_button)
        delete_button.pressed.connect(self.delete_charge)
        self.charges_gridLayout.addWidget(delete_button, row, column)

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

    @logger.catch
    def set_sentencing_date(self, time_to_pay_text):
        """Sets the sentencing date. This function is similar to set pay date.

        TODO: Refactor into single subclassed function."""
        days_to_add = self.complete_program_date_dict[time_to_pay_text]
        future_date = date.today() + timedelta(days_to_add)
        today = date.today()

        def next_monday(future_date, weekday=0):
            """This function returns the number of days to add to today to set
            the payment due date out to the Tuesday after the number of days
            set in the set_pay_date function. The default of 0 for weekday is
            what sets it to a Monday. If it is 1 it would be Tuesday, 3 would
            be Wednesday, etc."""
            days_ahead = weekday - future_date.weekday()
            if days_ahead <= 0:  # Target day already happened this week
                days_ahead += 7
            return future_date + timedelta(days_ahead)

        future_date = next_monday(future_date, 0)
        total_days_to_add = (future_date - today).days
        self.sentencing_date.setDate(QDate.currentDate().addDays(total_days_to_add))


if __name__ == "__main__":
    print("LPD ran directly")
else:
    print("LPD ran when imported")
