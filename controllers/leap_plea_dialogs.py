"""The controller module for the LEAP plea dialog."""
from loguru import logger

from PyQt5.QtCore import QDate

from views.leap_plea_long_dialog_ui import Ui_LeapPleaLongDialog
from views.leap_precompletion_dialog_ui import Ui_LeapPleaShortDialog
from models.template_types import TEMPLATE_DICT
from models.case_information import CaseInformation
from controllers.helper_functions import set_future_date
from controllers.criminal_dialogs import BaseCriminalDialog
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

    @logger.catch
    def add_dispositions_and_fines(self):
        """Row 3 - plea. Column count increases by 2 instead of one due to grid adding two
        columns when a charge is added (odd numbered column is empty)."""
        column = 2
        try:
            for index in range(len(self.case_information.charges_list)):
                self.case_information.charges_list[index].plea = (
                    self.charges_gridLayout.itemAtPosition(3, column).widget().currentText()
                )
                index += 1
                column += 2
        except AttributeError:
            print("Attribute error allowed to pass for lack of widget")

    @logger.catch
    def add_charge_to_view(self):
        row, column = super().add_charge_to_view()
        self.add_delete_button_to_view(row, column)

    @logger.catch
    def set_sentencing_date(self, days_to_add):
        "Sets the sentencing date to the Monday (0) after the days added."""
        total_days_to_add = set_future_date(days_to_add, LEAP_COMPLETE_DATE_DICT, 0)
        self.sentencing_date.setDate(QDate.currentDate().addDays(total_days_to_add))


class LeapPleaShortDialog(BaseCriminalDialog, Ui_LeapPleaShortDialog):
    """The dialog inherits from the BaseCriminalDialog (controller) and the
    Ui_LeapPleaShortDialog (view)."""
    @logger.catch
    def __init__(self, judicial_officer, parent=None):
        super().__init__(parent)
        self.case_information = CaseInformation(judicial_officer)
        self.dialog_name = "Leap Precourt Completion Dialog"
        self.template = TEMPLATE_DICT.get(self.dialog_name)

    @logger.catch
    def modify_view(self):
        super().modify_view()

    @logger.catch
    def connect_signals_to_slots(self):
        super().connect_signals_to_slots()

    @logger.catch
    def update_case_information(self):
        self.update_party_information()
        self.add_dispositions_and_fines()

    @logger.catch
    def update_party_information(self):
        super().update_party_information()

    @logger.catch
    def add_dispositions_and_fines(self):
        """Row 3 - plea. Column count increases by 2 instead of one due to grid adding two
        columns when a charge is added (odd numbered column is empty)."""
        column = 2
        try:
            for index in range(len(self.case_information.charges_list)):
                self.case_information.charges_list[index].plea = (
                    self.charges_gridLayout.itemAtPosition(3, column).widget().currentText()
                )
                index += 1
                column += 2
        except AttributeError:
            print("Attribute error allowed to pass for lack of widget")

    @logger.catch
    def add_charge_to_view(self):
        row, column = super().add_charge_to_view()
        self.add_delete_button_to_view(row, column)


if __name__ == "__main__":
    print("LPD ran directly")
