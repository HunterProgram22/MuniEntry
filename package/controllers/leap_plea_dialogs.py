"""The controller module for the LEAP plea dialog."""
from package.controllers.base_dialogs import CriminalBaseDialog
from loguru import logger

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QLabel

from package.views.leap_plea_short_dialog_ui import Ui_LeapPleaShortDialog
from package.views.leap_plea_long_dialog_ui import Ui_LeapPleaLongDialog
from package.views.custom_widgets import PleaComboBox
from package.views.charges_grids import LeapPleaGrid
from package.models.template_types import TEMPLATE_DICT
from package.controllers.helper_functions import set_future_date
from settings import LEAP_COMPLETE_DATE_DICT


class LeapPleaLongDialog(CriminalBaseDialog, Ui_LeapPleaLongDialog):
    """The dialog inherits from the BaseDialog (controller) and the
    Ui_LeapPleaLongDialog (view)."""
    @logger.catch
    def __init__(self, judicial_officer, case=None, parent=None):
        super().__init__(judicial_officer, case, parent)
        self.charges_gridLayout.__class__ = LeapPleaGrid
        self.dialog_name = "Leap Plea Dialog"
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.load_cms_data_to_view()

    @logger.catch
    def modify_view(self):
        """Sets the sentencing date."""
        super().modify_view()
        self.set_sentencing_date("120 days")

    @logger.catch
    def connect_signals_to_slots(self):
        """The method connects additional signals to slots. That are not
        included in the BaseDialog."""
        super().connect_signals_to_slots()
        self.guilty_all_Button.pressed.connect(self.set_plea_and_findings_process)
        self.time_to_complete_box.currentTextChanged.connect(self.set_sentencing_date)

    @logger.catch
    def update_case_information(self):
        super().update_case_information()
        self.add_plea_to_entry_case_information()
        self.entry_case_information.sentencing_date = (
            self.sentencing_date.date().toString("MMMM dd, yyyy")
        )

    def add_charge_to_grid(self):
        self.charges_gridLayout.add_charge_only_to_grid(self)
        self.statute_choice_box.setFocus()

    @logger.catch
    def add_charge_to_view(self):
        """This add charge to view largely copies the base version in criminal_dialogs, could be
        refactored."""
        row = 0
        column = self.charges_gridLayout.columnCount() + 1
        added_charge_index = len(self.entry_case_information.charges_list) - 1
        charge = vars(self.entry_case_information.charges_list[added_charge_index])
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


class LeapPleaShortDialog(CriminalBaseDialog, Ui_LeapPleaShortDialog):
    """The dialog inherits from the CriminalBaseDialog(controller) and the
    Ui_LeapPleaShortDialog (view)."""
    @logger.catch
    def __init__(self, judicial_officer, case=None, parent=None):
        super().__init__(judicial_officer, case, parent)
        self.charges_gridLayout.__class__ = LeapPleaGrid
        self.dialog_name = "Leap Precourt Completion Dialog"
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.load_cms_data_to_view()

    @logger.catch
    def connect_signals_to_slots(self):
        """The method connects additional signals to slots. That are not
        included in the BaseDialog."""
        super().connect_signals_to_slots()
        self.guilty_all_Button.pressed.connect(self.set_plea_and_findings_process)

    def add_charge_to_grid(self):
        self.charges_gridLayout.add_charge_only_to_grid(self)
        self.statute_choice_box.setFocus()

    @logger.catch
    def update_case_information(self):
        super().update_case_information()
        self.add_plea_to_entry_case_information()


if __name__ == "__main__":
    print("LPD ran directly")
