

class AddPlea:
    """Row 3 - plea when no allied checkbox added. Column starts at 1
    because column 0 is labels. The grid adds an empty column every time a
    charge is added, could increment by 2, but by incrementing by 1 and
    checking for None it ensures it will catch any weird add/delete.
    This method only adds the plea and is used in LEAP short and long and
    Not Guilty. No Jail Plea overrides this to include findings and fines.
    TODO: Rename and refactor out magic numbers.
    REFACTOR to CLASS and call class in subclass for dialog."""
    def __init__(self, dialog):
        self.dialog = dialog
        column = 1
        row = 3
        for index, charge in enumerate(self.dialog.entry_case_information.charges_list):
            while self.dialog.charges_gridLayout.itemAtPosition(row, column) is None:
                column += 1
            if isinstance(self.dialog.charges_gridLayout.itemAtPosition(
                    row, column).widget(), PleaComboBox):
                charge.plea = self.dialog.charges_gridLayout.itemAtPosition(
                    row, column).widget().currentText()
                column += 1
            column += 1



class AddPleaFindingsFines:
    """Row 3 - allied checkbox, Row 4 - plea, 5 - finding, 6 - fine,
    7 fine-suspended. Columns start at 1 because 0 is labels."""
    def __init__(self, dialog):
        self.dialog = dialog
        self.column = 1
        for index, charge in enumerate(self.dialog.entry_case_information.charges_list):
            while self.dialog.charges_gridLayout.itemAtPosition(3, self.column) is None:
                self.column += 1
            charge.plea = self.dialog.charges_gridLayout.itemAtPosition(
                4, self.column).widget().currentText()
            charge.finding = self.dialog.charges_gridLayout.itemAtPosition(
                5, self.column).widget().currentText()
            charge.fines_amount = self.dialog.charges_gridLayout.itemAtPosition(
                6, self.column).widget().text()
            if self.dialog.charges_gridLayout.itemAtPosition(7, self.column).widget().text() == "":
                charge.fines_suspended = "0"
            else:
                charge.fines_suspended = (
                    self.dialog.charges_gridLayout.itemAtPosition(
                        7, self.column).widget().text()
                )
            self.column += 1


class AddPleaFindingsFinesJail:
    def __init__(self, dialog):
        self.dialog = dialog
        self.column = 1
        for index, charge in enumerate(self.dialog.entry_case_information.charges_list):
            while self.dialog.charges_gridLayout.itemAtPosition(3, self.column) is None:
                self.column += 1
            charge.plea = self.dialog.charges_gridLayout.itemAtPosition(
                4, self.column).widget().currentText()
            charge.finding = self.dialog.charges_gridLayout.itemAtPosition(
                5, self.column).widget().currentText()
            charge.fines_amount = self.dialog.charges_gridLayout.itemAtPosition(
                6, self.column).widget().text()
            if self.dialog.charges_gridLayout.itemAtPosition(7, self.column).widget().text() == "":
                charge.fines_suspended = "0"
            else:
                charge.fines_suspended = (
                    self.dialog.charges_gridLayout.itemAtPosition(
                        7, self.column).widget().text()
                )
            if self.dialog.charges_gridLayout.itemAtPosition(8, self.column).widget().text() == "":
                charge.jail_days = "None"
            else:
                charge.jail_days = self.dialog.charges_gridLayout.itemAtPosition(
                    8, self.column).widget().text()
            if self.dialog.charges_gridLayout.itemAtPosition(9, self.column).widget().text() == "":
                charge.jail_days_suspended = "None"
            else:
                charge.jail_days_suspended = self.dialog.charges_gridLayout.itemAtPosition(
                    9, self.column).widget().text()
            self.column += 1
