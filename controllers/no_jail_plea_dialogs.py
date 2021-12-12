"""The controller module for the no jail plea dialog - it is not limited
to minor misdemeanors, but does not contain functions to account for jail time.
Loads all charges - including non-minor-misdemeanors from a database."""
from loguru import logger

from PyQt5 import QtCore
from PyQt5.QtCore import QDate

from views.no_jail_plea_dialog_ui import Ui_NoJailPleaDialog
from models.template_types import TEMPLATE_DICT
from controllers.helper_functions import set_future_date
from controllers.criminal_dialogs import (
    AmendOffenseDialog,
)
from controllers.conditions_dialogs import AddConditionsDialog
from .criminal_dialogs import CriminalPleaDialog
from settings import PAY_DATE_DICT


class NoJailPleaDialog(CriminalPleaDialog, Ui_NoJailPleaDialog):
    """The dialog inherits from the CriminalPleaDialog (controller) and the
    Ui_NoJailPleaDialog (view)."""
    @logger.catch
    def __init__(self, judicial_officer, case=None, parent=None):
        super().__init__(judicial_officer, case, parent)
        self.add_conditions_dict = {
            self.license_suspension_checkBox: self.entry_case_information.license_suspension.ordered,
            self.community_service_checkBox: self.entry_case_information.community_service.ordered,
            self.other_conditions_checkBox: self.entry_case_information.other_conditions.ordered,
        }
        self.dialog_name = 'No Jail Plea Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)

    @logger.catch
    def load_cms_data_to_view(self):
        super().load_cms_data_to_view()
        fra_value_dict = {"Y": "Yes", "N": "No", "U": "N/A"}
        if self.case.fra_in_file in fra_value_dict:
            self.fra_in_file_box.setCurrentText(fra_value_dict[self.case.fra_in_file])
        else:
            self.fra_in_file_box.setCurrentText("N/A")
        self.set_fra_in_file(self.fra_in_file_box.currentText())
        self.set_fra_in_court(self.fra_in_court_box.currentText())

    @logger.catch
    def modify_view(self):
        """Sets the balance due date in the view to today."""
        super().modify_view()
        self.balance_due_date.setDate(QtCore.QDate.currentDate())

    @logger.catch
    def connect_signals_to_slots(self):
        """The method connects additional signals to slots. That are not
        included in the BaseDialog."""
        super().connect_signals_to_slots()
        self.add_conditions_Button.pressed.connect(self.start_add_conditions_dialog)
        self.fra_in_file_box.currentTextChanged.connect(self.set_fra_in_file)
        self.fra_in_court_box.currentTextChanged.connect(self.set_fra_in_court)
        self.ability_to_pay_box.currentTextChanged.connect(self.set_pay_date)
        self.no_contest_all_Button.pressed.connect(self.set_plea_and_findings_process)
        self.costs_and_fines_Button.clicked.connect(self.show_costs_and_fines)

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
    def add_dispositions_and_fines(self):
        """Row 3 - allied checkbox, Row 4 - plea, 5 - finding, 6 - fine,
        7 fine-suspended. Columns start at 1 because 0 is labels."""
        column = 1
        for index, charge in enumerate(self.entry_case_information.charges_list):
            while self.charges_gridLayout.itemAtPosition(3, column) is None:
                column += 1
            charge.plea = self.charges_gridLayout.itemAtPosition(
                4, column).widget().currentText()
            charge.finding = self.charges_gridLayout.itemAtPosition(
                5, column).widget().currentText()
            charge.fines_amount = self.charges_gridLayout.itemAtPosition(
                6, column).widget().text()
            if self.charges_gridLayout.itemAtPosition(7, column).widget().text() == "":
                charge.fines_suspended = "0"
            else:
                charge.fines_suspended = (
                    self.charges_gridLayout.itemAtPosition(
                        7, column).widget().text()
                )
            column += 1

    @logger.catch
    def set_pay_date(self, days_to_add):
        "Sets the sentencing date to the Tuesday (1) after the days added."""
        total_days_to_add = set_future_date(days_to_add, PAY_DATE_DICT, 1)
        self.balance_due_date.setDate(QDate.currentDate().addDays(total_days_to_add))

    @logger.catch
    def start_amend_offense_dialog(self, _bool):
        """Opens the amend offense dialog as a modal window. The
        entry_case_information is passed to the dialog class in order to populate
        the case information banner. The _bool is from clicked and not used."""
        self.update_case_information()
        button_index = self.amend_button_list.index(self.sender())
        AmendOffenseDialog(self, self.entry_case_information, button_index).exec()

    @logger.catch
    def start_add_conditions_dialog(self):
        """Opens the add conditions dialog as a modal window. It passes the
        instance of the NoJailPleaDialog class (self) as an argument
        so that the AddConditionsDialog can access all data from the
        NoJailPleaDialog when working in the AddConditionsDialog."""
        self.update_case_information()
        AddConditionsDialog(self).exec()


if __name__ == "__main__":
    print("NJPD ran directly")
