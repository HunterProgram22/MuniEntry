

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



class JailChargesGrid(QGridLayout):
    def __init__(self, parent=None):
        super(QGridLayout, self).__init__(parent)
        self.row_offense = 0
        self.row_statute = 1
        self.row_degree = 2
        self.row_allied_box = 3
        self.row_plea = 4
        self.row_finding = 5
        self.row_fine = 6
        self.row_fine_suspended = 7
        self.row_jail_days = 8
        self.row_jail_days_suspended = 9
        self.row_amend_button = 10
        self.row_delete_button = 11

    @logger.catch
    def add_charge_only_to_grid(self, dialog):
        """Adds the charge that was added through add_charge method to the
        view/GUI. The first row=0 because of python zero-based indexing. The
        column is set at one more than the current number of columns because
        it is the column to which the charge will be added.

        :added_charge_index: - The added charge index is one less than the
        total charges in charges_list because of zero-based indexing. Thus, if
        there is one charge, the index of the charge to be added to the
        charge_dict from the charges_list is 0.

        The python builtin vars function returns the __dict__ attribute of
        the object."""
        column = self.columnCount() + 1
        added_charge_index = len(dialog.entry_case_information.charges_list) - 1
        charge = vars(dialog.entry_case_information.charges_list[added_charge_index])
        self.addWidget(QLabel(charge['offense']), self.row_offense, column)
        self.addWidget(QLabel(charge['statute']), self.row_statute, column)
        self.addWidget(QLabel(charge['degree']), self.row_degree, column)
        self.addWidget(AlliedCheckbox(), self.row_allied_box, column)
        self.addWidget(PleaComboBox(), self.row_plea, column)
        self.addWidget(FindingComboBox(), self.row_finding, column)
        self.addWidget(FineLineEdit(charge['offense']), self.row_fine, column)
        self.addWidget(FineSuspendedLineEdit(), self.row_fine_suspended, column)
        self.addWidget(JailLineEdit(charge['offense']), self.row_jail_days, column)
        self.addWidget(JailSuspendedLineEdit(), self.row_jail_days_suspended, column)
        self.add_amend_button_to_grid(dialog, self.row_amend_button, column)
        self.add_delete_button_to_grid(dialog, self.row_delete_button, column)

    def add_delete_button_to_grid(self, dialog, row, column):
        delete_button = DeleteButton()
        dialog.delete_button_list.append(delete_button)
        delete_button.pressed.connect(dialog.delete_charge)
        self.addWidget(delete_button, row, column)

    def add_amend_button_to_grid(self, dialog, row, column):
        amend_button = AmendButton()
        dialog.amend_button_list.append(amend_button)
        amend_button.clicked.connect(dialog.start_amend_offense_dialog)
        self.addWidget(amend_button, row, column)

    def check_plea_and_findings(self):
        """Shows warning if no plea or findings are entered. Checks one at a time so unless all
        fields have a plea and finding you will get the warning until they are filled in.

        MOVE: Should this be in CriminalBaseDialog or a decorator or standalone function???"""
        row_plea, row_finding = self.set_plea_and_finding_rows()
        column = 2
        loop_counter = 0
        while loop_counter < self.columnCount():
            try:
                if self.itemAtPosition(row_plea, column).widget().currentText() == "":
                    RequiredBox("You must enter a plea.")
                    return None
                if self.itemAtPosition(row_finding, column).widget().currentText() == "":
                    RequiredBox("You must enter a finding.")
                    return None
            except AttributeError:
                pass
            column += 2
            loop_counter += 1
        return "Pass"

    def set_plea_and_finding_rows(self):
        """The initial values of row_plea and row_finding are the common rows for plea and findings.
        They are set to allow this method to return both values even if there is no finding row
        (i.e. LEAP Dialog)."""
        row_plea = 4
        row_finding = 5
        for row in range(self.rowCount()):
            if self.itemAtPosition(row, 0).widget().text() == "Plea:":
                row_plea = row
            if self.itemAtPosition(row, 0).widget().text() == "Finding:":
                row_finding = row
        return row_plea, row_finding

    @logger.catch
    def delete_charge_from_grid(self):
        """Uses the delete_button that is indexed to the column to delete the
        QLabels for the charge."""
        index = self.indexOf(self.sender())
        column = self.getItemPosition(index)[1]
        for row in range(self.rowCount()):
            layout_item = self.itemAtPosition(row, column)
            if layout_item is not None:
                layout_item.widget().deleteLater()
                self.removeItem(layout_item)

    @logger.catch
    def set_all_plea_and_findings(self, dialog):
        """Sets the plea and findings boxes for all charges currently
        in the charges_gridLayout.
        TODO: Row-1 = should be allied-checkbox and row+1 = should be finding choice box.
        This can be refactored better."""
        button_dict = {}
        if hasattr(dialog, "guilty_all_Button"):
            button_dict[dialog.guilty_all_Button] = "Guilty"
        if hasattr(dialog, "no_contest_all_Button"):
            button_dict[dialog.no_contest_all_Button] = "No Contest"
        if hasattr(dialog, "not_guilty_all_Button"):
            button_dict[dialog.not_guilty_all_Button] = "Not Guilty"
        plea = button_dict.get(self.sender())
        for row in range(self.rowCount()):
            for column in range(self.columnCount()):
                if self.itemAtPosition(row, column) is not None:
                    if isinstance(self.itemAtPosition(
                            row, column).widget(), PleaComboBox):
                        self.itemAtPosition(
                            row, column).widget().setCurrentText(plea)
                        if isinstance(self.itemAtPosition(
                                row, column).widget(), AlliedCheckbox):
                            if self.itemAtPosition(
                                    row-1, column).widget().isChecked():
                                self.itemAtPosition(
                                    row+1, column).widget().setCurrentText("Guilty - Allied Offense")
                        else:
                            try:
                                if self.itemAtPosition(row+1, column) is not None:
                                    self.itemAtPosition(
                                        row+1, column).widget().setCurrentText("Guilty")
                            except AttributeError:
                                pass
                    column += 1
                else:
                    column += 1
        self.set_cursor_to_fine_line_edit()

    @logger.catch
    def set_cursor_to_fine_line_edit(self):
        """Moves the cursor to the FineLineEdit box. Row is set to 6, but
        for different dialogs this could end up changing, however, the check
        for the delete button may resolve this issue."""
        for column in range(1, self.columnCount()):
            if self.itemAtPosition(4, column) is not None:
                if isinstance(self.itemAtPosition(4, column).widget(), DeleteButton):
                    return None
                elif isinstance(self.itemAtPosition(
                        6, column).widget(), FineLineEdit):
                    self.itemAtPosition(6, column).widget().setFocus()
                    break
                column += 1
