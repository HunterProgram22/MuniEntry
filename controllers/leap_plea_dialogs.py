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
from settings import LEAP_COMPLETE_DATE_DICT


class LeapPleaLongDialog(BaseCriminalDialog, Ui_LeapPleaLongDialog):
    """The dialog inherits from the BaseCriminalDialog (controller) and the
    Ui_LeapPleaLongDialog (view)."""

    @logger.catch
    def __init__(self, judicial_officer, parent=None):
        super().__init__(parent)
        self.case_information = CaseInformation(judicial_officer)
        self.dialog_name = "Leap Plea Dialog"
        self.template = TEMPLATE_DICT.get(self.dialog_name)

    @logger.catch
    def modify_view(self):
        """The modify view method updates the view that is created on init."""
        super().modify_view()
        self.set_sentencing_date("120 days")

    @logger.catch
    def connect_signals_to_slots(self):
        """The method connects additional signals to slots. That are not
        included in the BaseCriminalDialog."""
        super().connect_signals_to_slots()
        self.time_to_complete_box.currentTextChanged.connect(self.set_sentencing_date)

    @logger.catch
    def update_case_information(self):
        """The method calls functions to update the case information model."""
        self.update_party_information()
        self.add_dispositions_and_fines()

    @logger.catch
    def update_party_information(self):
        super().update_party_information()
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
        row, column = super().add_charge_to_view()
        self.add_delete_button_to_view(row, column)




    @logger.catch
    def set_sentencing_date(self, time_to_pay_text):
        """Sets the sentencing date. This function is similar to set pay date.

        TODO: Refactor into single subclassed function."""
        days_to_add = LEAP_COMPLETE_DATE_DICT[time_to_pay_text]
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
