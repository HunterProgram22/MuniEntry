"""The module that contains all controller classes that are common to criminal
cases (criminal includes traffic). """

from loguru import logger

from models.case_information import (
    AmendOffenseDetails,
)
from views.amend_offense_dialog_ui import Ui_AmendOffenseDialog
from controllers.base_dialogs import BaseDialog
from resources.db.create_data_lists import create_offense_list


class AmendOffenseDialog(BaseDialog, Ui_AmendOffenseDialog):
    """The AddOffenseDialog is created when the amend_button is pressed for a specific charge.
    The cms_case information is passed in order to populate the cms_case information banner. The
    button_index is to determine which charge the amend_button is amending."""
    @logger.catch
    def __init__(self, main_dialog, case_information, button_index, parent=None):
        self.button_index = button_index
        self.main_dialog = main_dialog
        self.case_information = case_information
        self.amend_offense_details = AmendOffenseDetails()
        self.current_offense = self.case_information.charges_list[self.button_index].offense
        super().__init__(parent)
        self.set_case_information_banner()
        self.connect_signals_to_slots()

    @logger.catch
    def modify_view(self):
        """The modify view sets the original charge based on the item in the main dialog
        for which amend button was pressed."""
        self.original_charge_box.setCurrentText(self.current_offense)
        self.amended_charge_box.addItems(create_offense_list())

    @logger.catch
    def connect_signals_to_slots(self):
        """This method overrides the base_dialog method to connect signals and
        slots specific to the amend_offense dialog."""
        self.clear_fields_Button.pressed.connect(self.clear_amend_charge_fields)
        self.amend_offense_Button.pressed.connect(self.amend_offense)
        self.cancel_Button.pressed.connect(self.close_event)

    @logger.catch
    def set_case_information_banner(self):
        """Sets the banner on a view of the interface. It modifies label
        widgets on the view to text that was entered."""
        self.defendant_name_label.setText(
            "State of Ohio v. {defendant_first_name} {defendant_last_name}".format(
                defendant_first_name=self.case_information.defendant.first_name,
                defendant_last_name=self.case_information.defendant.last_name
            )
        )
        self.case_number_label.setText(self.case_information.case_number)

    @logger.catch
    def clear_amend_charge_fields(self):
        """Clears the fields in the view."""
        self.original_charge_box.clearEditText()
        self.amended_charge_box.clearEditText()

    @logger.catch
    def amend_offense(self):
        """Adds the data entered for the amended offense to the AmendOffenseDetails
        object then points the entry_case_information object to the AmendOffenseDetails
        object."""
        self.amend_offense_details.original_charge = self.original_charge_box.currentText()
        self.amend_offense_details.amended_charge = self.amended_charge_box.currentText()
        self.amend_offense_details.motion_disposition = self.motion_decision_box.currentText()
        self.case_information.amend_offense_details = self.amend_offense_details
        amended_charge = self.current_offense + " - AMENDED"
        self.case_information.charges_list[self.button_index].offense = amended_charge
        for columns in range(self.main_dialog.charges_gridLayout.columnCount()):
            if self.main_dialog.charges_gridLayout.itemAtPosition(0, columns) is not None:
                if self.main_dialog.charges_gridLayout.itemAtPosition(
                        0, columns).widget().text() == self.current_offense:
                    self.main_dialog.charges_gridLayout.itemAtPosition(0, columns).widget().setText(amended_charge)
        self.close_event()


if __name__ == "__main__":
    print("BCD ran directly")
else:
    print("BCD ran when imported")
