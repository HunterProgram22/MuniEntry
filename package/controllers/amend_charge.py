class AmendOffenseDialog(AddChargeDialog, Ui_AmendOffenseDialog):
    """The AddOffenseDialog is created when the amend_button is pressed for a specific charge.
    The cms_case information is passed in order to populate the cms_case information banner. The
    button_index is to determine which charge the amend_button is amending."""
    @logger.catch
    def __init__(self, main_dialog, case_information, button_index, parent=None):
        self.amend_offense_details = AmendOffenseDetails()
        self.current_offense = self.case_information.charges_list[self.button_index].offense
        super().__init__(main_dialog, case_information, button_index, parent=None)

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
        if self.motion_decision_box.currentText() == "Granted":
            amended_charge = f"{self.current_offense} - AMENDED to {self.amend_offense_details.amended_charge}"
            self.case_information.charges_list[self.button_index].offense = amended_charge
            self.case_information.amended_charges_list.append(
                (self.original_charge_box.currentText(), self.amended_charge_box.currentText())
            )
            for columns in range(self.main_dialog.charges_gridLayout.columnCount()):
                if (
                    self.main_dialog.charges_gridLayout.itemAtPosition(0, columns) is not None
                    and self.main_dialog.charges_gridLayout.itemAtPosition(
                        0, columns).widget().text() == self.current_offense
                ):
                    self.main_dialog.charges_gridLayout.itemAtPosition(0, columns).widget().setText(amended_charge)
        self.close_event()