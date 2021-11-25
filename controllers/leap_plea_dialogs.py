"""The controller module for the LEAP plea dialog."""
from loguru import logger

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QLabel

from views.leap_plea_short_dialog_ui import Ui_LeapPleaShortDialog
from views.leap_plea_long_dialog_ui import Ui_LeapPleaLongDialog
from views.custom_widgets import PleaComboBox
from models.template_types import TEMPLATE_DICT
from controllers.helper_functions import set_future_date
from controllers.criminal_dialogs import CriminalPleaDialog
from settings import LEAP_COMPLETE_DATE_DICT


class LeapPleaLongDialog(CriminalPleaDialog, Ui_LeapPleaLongDialog):
    """The dialog inherits from the BaseDialog (controller) and the
    Ui_LeapPleaLongDialog (view)."""
    @logger.catch
    def __init__(self, judicial_officer, case, parent=None):
        super().__init__(judicial_officer, case, parent)
        self.dialog_name = "Leap Plea Dialog"
        self.template = TEMPLATE_DICT.get(self.dialog_name)

    @logger.catch
    def modify_view(self):
        super().modify_view()
        self.set_sentencing_date("120 days")

    @logger.catch
    def connect_signals_to_slots(self):
        super().connect_signals_to_slots()
        self.time_to_complete_box.currentTextChanged.connect(self.set_sentencing_date)

    @logger.catch
    def update_case_information(self):
        self.update_party_information()
        self.add_dispositions_and_fines()

    @logger.catch
    def update_party_information(self):
        super().update_party_information()
        self.case_information.sentencing_date = (
            self.sentencing_date.date().toString("MMMM dd, yyyy")
        )

    def add_charge_to_grid(self):
        self.charges_gridLayout.add_charge_only_to_grid(
            self, add_allied_box=False, add_delete_button=True)
        self.statute_choice_box.setFocus()

    @logger.catch
    def add_dispositions_and_fines(self):
        """Row 3 - plea. Column count increases by 2 instead of one due to grid adding two
        columns when a charge is added (odd numbered column is empty). Column starts at 2
        because column 0 is labels."""
        column = 2
        for index, charge in enumerate(self.case_information.charges_list):
            charge.plea = self.charges_gridLayout.itemAtPosition(
                3, column).widget().currentText()
            column += 2

    @logger.catch
    def add_charge_to_view(self):
        """This add charge to view largely copies the base version in criminal_dialogs, could be
        refactored."""
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
        row += 1
        self.add_delete_button_to_view(row, column)

    @logger.catch
    def set_sentencing_date(self, days_to_add):
        "Sets the sentencing date to the Monday (0) after the days added."""
        total_days_to_add = set_future_date(days_to_add, LEAP_COMPLETE_DATE_DICT, 0)
        self.sentencing_date.setDate(QDate.currentDate().addDays(total_days_to_add))

    @logger.catch
    def set_all_plea_and_findings(self):
        """Sets the plea boxes to guilty for all charges currently
        in the charges_gridLayout.

        TODO: Refactor from criminal dialog version."""
        for column in range(self.charges_gridLayout.columnCount()):
            try:
                if isinstance(self.charges_gridLayout.itemAtPosition(
                        3, column).widget(), PleaComboBox):
                    self.charges_gridLayout.itemAtPosition(
                        3, column).widget().setCurrentText("Guilty")
                    column += 1
            except AttributeError:
                pass


class LeapPleaShortDialog(CriminalPleaDialog, Ui_LeapPleaShortDialog):
    """The dialog inherits from the LeapPleaLongDialog(controller) and the
    Ui_LeapPleaShortDialog (view)."""
    @logger.catch
    def __init__(self, judicial_officer, case, parent=None):
        super().__init__(judicial_officer, case, parent)
        self.dialog_name = "Leap Precourt Completion Dialog"
        self.template = TEMPLATE_DICT.get(self.dialog_name)

    def add_charge_to_grid(self):
        self.charges_gridLayout.add_charge_only_to_grid(
            self, add_allied_box=False, add_delete_button=True)  
        self.statute_choice_box.setFocus()

    @logger.catch
    def update_case_information(self):
        self.update_party_information()
        self.add_dispositions_and_fines()

    @logger.catch
    def add_dispositions_and_fines(self):
        """Row 3 - plea. Column count increases by 2 instead of one due to grid adding two
        columns when a charge is added (odd numbered column is empty). Column starts at 2
        because column 0 is labels."""
        column = 2
        for index, charge in enumerate(self.case_information.charges_list):
            charge.plea = self.charges_gridLayout.itemAtPosition(
                3, column).widget().currentText()
            column += 2


if __name__ == "__main__":
    print("LPD ran directly")
