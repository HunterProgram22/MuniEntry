"""The controller module for the minor misdemeanor dialog - it is not limited
to minor misdemeanors, but does not contain functions to account for jail time.
Loads all charges - including non-minor-misdemeanors from a database."""
from loguru import logger

from PyQt5 import QtCore
from PyQt5.QtCore import QDate

from views.custom_widgets import (
    FindingComboBox,
    FineLineEdit,
    FineSuspendedLineEdit,
)
from views.minor_misdemeanor_dialog_ui import Ui_MinorMisdemeanorDialog
from models.template_types import TEMPLATE_DICT
from models.case_information import CaseInformation
from controllers.helper_functions import set_future_date
from controllers.criminal_dialogs import (
    BaseCriminalDialog,
    AddConditionsDialog,
    AmendOffenseDialog,
)
from settings import PAY_DATE_DICT


class MinorMisdemeanorDialog(BaseCriminalDialog, Ui_MinorMisdemeanorDialog):
    """The dialog inherits from the BaseCriminalDialog (controller) and the
    Ui_MinorMisdemeanorDialog (view).

    This dialog is used when there will not be any jail time imposed. It does
    not inherently limit cases to minor misdemeanors or unclassified
    misdemeanors, however, it does not include fields to enter jail time."""
    @logger.catch
    def __init__(self, judicial_officer, parent=None):
        super().__init__(judicial_officer, parent)
        self.case_information = CaseInformation(self.judicial_officer)
        self.dialog_name = "Minor Misdemeanor Dialog"
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.amend_button_list = []

    @logger.catch
    def modify_view(self):
        """The modify view method updates the view that is created on init."""
        super().modify_view()
        self.balance_due_date.setDate(QtCore.QDate.currentDate())

    @logger.catch
    def connect_signals_to_slots(self):
        """The method connects additional signals to slots. That are not
        included in the BaseCriminalDialog."""
        super().connect_signals_to_slots()
        self.add_conditions_Button.pressed.connect(self.start_add_conditions_dialog)
        self.fra_in_file_box.currentTextChanged.connect(self.set_fra_in_file)
        self.fra_in_court_box.currentTextChanged.connect(self.set_fra_in_court)
        self.ability_to_pay_box.currentTextChanged.connect(self.set_pay_date)
        self.no_contest_all_Button.pressed.connect(self.no_contest_all_plea_and_findings)
        self.costs_and_fines_Button.clicked.connect(self.show_costs_and_fines)

    @logger.catch
    def add_dispositions_and_fines(self):
        """Row 3 - allied checkbox, Row 4 - plea, 5 - finding, 6 - fine, 7 fine-suspended.
        Columns start at 0 for labels and 2 for first entry then 4 etc.

        Column count increases by 2 instead of one due to grid adding two
        columns when a charge is added (odd numbered column is empty)."""
        column = 2
        try:
            for index in range(len(self.case_information.charges_list)):
                self.case_information.charges_list[index].plea = (
                    self.charges_gridLayout.itemAtPosition(
                        4, column).widget().currentText()
                )
                self.case_information.charges_list[index].finding = (
                    self.charges_gridLayout.itemAtPosition(
                        5, column).widget().currentText()
                )
                self.case_information.charges_list[index].fines_amount = (
                    self.charges_gridLayout.itemAtPosition(
                        6, column).widget().text()
                )
                if self.charges_gridLayout.itemAtPosition(7, column).widget().text() == "":
                    self.case_information.charges_list[index].fines_suspended = "0"
                else:
                    self.case_information.charges_list[index].fines_suspended = (
                        self.charges_gridLayout.itemAtPosition(7, column).widget().text()
                    )
                index += 1
                column += 2
        except AttributeError:
            print("Attribute error allowed to pass for lack of widget")

    @logger.catch
    def add_charge_to_view(self):
        """Adds the charge that was added through add_charge method to the
        view/GUI."""
        row, column = super().add_charge_to_view()
        self.charges_gridLayout.addWidget(FindingComboBox(), row, column)
        row += 1
        self.charges_gridLayout.addWidget(FineLineEdit(self.criminal_charge.offense), row, column)
        row += 1
        self.charges_gridLayout.addWidget(FineSuspendedLineEdit(), row, column)
        row += 1
        self.add_delete_button_to_view(row, column)
        row += 1
        self.add_amend_button_to_view(row, column)

    @logger.catch
    def set_pay_date(self, days_to_add):
        "Sets the sentencing date to the Tuesday (1) after the days added."""
        total_days_to_add = set_future_date(days_to_add, PAY_DATE_DICT, 1)
        self.balance_due_date.setDate(QDate.currentDate().addDays(total_days_to_add))

    @logger.catch
    def start_amend_offense_dialog(self, _bool):
        """Opens the amend offense dialog as a modal window. The
        case_information is passed to the dialog class in order to populate
        the case information banner. The _bool is from clicked and not used."""
        self.update_case_information()
        button_index = self.amend_button_list.index(self.sender())
        AmendOffenseDialog(self.case_information, button_index).exec()

    @logger.catch
    def start_add_conditions_dialog(self):
        """Opens the add conditions dialog as a modal window. It passes the
        instance of the MinorMisdemeanorDialog class (self) as an argument
        so that the AddConditionsDialog can access all data from the
        MinorMisdemeanorDialog when working in the AddConditionsDialog."""
        self.update_case_information()
        AddConditionsDialog(self).exec()


if __name__ == "__main__":
    print("MMD ran directly")
