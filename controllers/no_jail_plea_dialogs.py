"""The controller module for the no jail plea dialog - it is not limited
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
from views.no_jail_plea_dialog_ui import Ui_NoJailPleaDialog
from models.template_types import TEMPLATE_DICT
from models.case_information import CaseInformation
from controllers.helper_functions import set_future_date
from controllers.criminal_dialogs import (
    AddConditionsDialog,
    AmendOffenseDialog,
)
from .criminal_dialogs import CriminalPleaDialog
from settings import PAY_DATE_DICT


class NoJailPleaDialog(CriminalPleaDialog, Ui_NoJailPleaDialog):
    """The dialog inherits from the CriminalPleaDialog (controller) and the
    Ui_NoJailPleaDialog (view)."""
    @logger.catch
    def __init__(self, judicial_officer, case, parent=None):
        super().__init__(judicial_officer, case, parent)
        self.dialog_name = 'No Jail Plea Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        


    @logger.catch
    def load_arraignment_data(self):
        super().load_arraignment_data()
        fra_value_dict = {"Y": "Yes", "N": "No", "U": "N/A"}
        if self.case.fra_in_file in fra_value_dict:
            self.fra_in_file_box.setCurrentText(fra_value_dict[self.case.fra_in_file])
        else:
            self.fra_in_file_box.setCurrentText("N/A")
        self.set_fra_in_file(self.fra_in_file_box.currentText())
        self.set_fra_in_court(self.fra_in_court_box.currentText())

    @logger.catch
    def modify_view(self):
        """The modify view method updates the view that is created on init and loads
        case data from the arraignment case that is selected."""
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
    def add_dispositions_and_fines(self):
        """Row 3 - allied checkbox, Row 4 - plea, 5 - finding, 6 - fine, 7 fine-suspended.
        Columns start at 0 for labels and 2 for first entry then 4 etc.

        Column count increases by 2 instead of one due to grid adding two
        columns when a charge is added (odd numbered column is empty)."""
        column = 2
        loop_counter = 0
        charge_index = 0
        while loop_counter < self.charges_gridLayout.columnCount():
            try:
                self.case_information.charges_list[charge_index].plea = (
                    self.charges_gridLayout.itemAtPosition(
                        4, column).widget().currentText()
                )
                self.case_information.charges_list[charge_index].finding = (
                    self.charges_gridLayout.itemAtPosition(
                        5, column).widget().currentText()
                )
                self.case_information.charges_list[charge_index].fines_amount = (
                    self.charges_gridLayout.itemAtPosition(6, column).widget().text()
                )
                if self.charges_gridLayout.itemAtPosition(7, column).widget().text() == "":
                    self.case_information.charges_list[charge_index].fines_suspended = "0"
                else:
                    self.case_information.charges_list[charge_index].fines_suspended = (
                        self.charges_gridLayout.itemAtPosition(7, column).widget().text()
                    )
                charge_index += 1
            except AttributeError:
                pass
            column += 2
            loop_counter += 1

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
        AmendOffenseDialog(self, self.case_information, button_index).exec()

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
