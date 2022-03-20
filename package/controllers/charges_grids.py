from PyQt5.QtWidgets import QGridLayout, QLabel

from package.views.custom_widgets import (
    PleaComboBox,
    AlliedCheckbox,
    FineLineEdit,
    StatuteLineEdit,
    DegreeComboBox,
    FindingComboBox,
    FineSuspendedLineEdit,
    JailLineEdit,
    JailSuspendedLineEdit,
    DismissedCheckbox,
    ChargeGridDeleteButton,
    ChargeGridAmendButton,
)


class ChargesGrid(QGridLayout):
    """The base format of the charges grid that is used when a main_entry_dialog needs
    to display and interact with charges in a case. The ChargesGrid subclasses the
    QGridLayout and provides methods for manipulating the grid. Each main_entry_dialog
    that has a ChargesGrid has a specific subclassed version that is set by changing
    the class of the QGridLayout to the class of the specific subclassed ChargesGrid.
    This avoids having to initialize the grid during the setupUI method called by the
    main_entry_dialog classes modify_view method. The class is set prior to
    loading the case data during the main_entry_dialog load_cms_data_to_view method."""

    row_offense = 0
    row_statute = 1
    row_degree = 2
    row_dismissed_box = 3
    row_allied_box = 4
    row_plea = 5
    row_finding = 6
    row_fine = 7
    row_fine_suspended = 8
    row_amend_button = 9
    row_delete_button = 10

    def get_last_charge_in_charges_list(self, dialog):
        return dialog.entry_case_information.charges_list[-1]

    def set_plea(self):
        """Returns a copy of the label of the specific plea all button (i.e. "Guilty
        All" is returned as "Guilty")."""
        return self.sender().text().strip(" All")

    def set_cursor_to_fine_line_edit(self):
        """Sets the cursor to the first non-dismissed charge's fine box."""
        for column in range(1, self.columnCount()):
            if self.itemAtPosition(ChargesGrid.row_fine, column) is not None:
                if (
                    self.itemAtPosition(ChargesGrid.row_dismissed_box, column)
                    .widget()
                    .isChecked()
                ):
                    column += 1
                    continue
                self.itemAtPosition(ChargesGrid.row_fine, column).widget().setFocus()
                break
            column += 1

    def set_all_pleas(self):
        """This method after setting all pleas calls the set_all_findings. In the Not
        Guilty Plea Grid the method is overriden to not call the set_all_findings
        because there are no findings to be set with a Not Guilty plea."""
        plea = self.set_plea()
        for column in range(1, self.columnCount()):
            if self.itemAtPosition(self.row_offense, column) is not None:
                if (
                    self.itemAtPosition(self.row_dismissed_box, column)
                    .widget()
                    .isChecked()
                ):
                    continue
                else:
                    self.itemAtPosition(self.row_plea, column).widget().setCurrentText(
                        plea
                    )
                    self.set_all_findings(column)
        self.set_cursor_to_fine_line_edit()

    def set_all_findings(self, column):
        if self.itemAtPosition(self.row_allied_box, column).widget().isChecked():
            self.itemAtPosition(self.row_finding, column).widget().setCurrentText(
                "Guilty - Allied Offense"
            )
        else:
            self.itemAtPosition(self.row_finding, column).widget().setCurrentText(
                "Guilty"
            )


class NotGuiltyPleaGrid(ChargesGrid):
    row_plea = 3
    row_delete_button = 4

    def add_charge_only_to_grid(self, dialog):
        """The column is set to the one more than the current number of columns because
        a new charge is being added."""
        charge = self.get_last_charge_in_charges_list(dialog)
        column = self.columnCount() + 1
        self.addWidget(QLabel(charge.offense), self.row_offense, column)
        self.addWidget(StatuteLineEdit(charge.statute), self.row_statute, column)
        self.addWidget(DegreeComboBox(charge.degree), self.row_degree, column)
        self.addWidget(PleaComboBox(column), self.row_plea, column)
        self.addWidget(
            ChargeGridDeleteButton(column, charge, dialog),
            self.row_delete_button,
            column,
        )

    def set_all_pleas(self):
        """This method overrides the ChargesGrid set_all_pleas because there are no
        findings to be added for a Not Guilty plea."""
        plea = self.set_plea()
        for column in range(1, self.columnCount()):
            if self.itemAtPosition(self.row_offense, column) is not None:
                self.itemAtPosition(self.row_plea, column).widget().setCurrentText(plea)


class NoJailChargesGrid(ChargesGrid):
    row_dismissed_box = 3
    row_allied_box = 4
    row_plea = 5
    row_finding = 6
    row_fine = 7
    row_fine_suspended = 8
    row_amend_button = 9
    row_delete_button = 10

    def add_charge_only_to_grid(self, dialog):
        """The column is set to the one more than the current number of columns because
        a new charge is being added."""
        charge = self.get_last_charge_in_charges_list(dialog)
        column = self.columnCount() + 1
        self.addWidget(QLabel(charge.offense), self.row_offense, column)
        self.addWidget(StatuteLineEdit(charge.statute), self.row_statute, column)
        self.addWidget(DegreeComboBox(charge.degree), self.row_degree, column)
        self.addWidget(
            DismissedCheckbox(column, dialog), self.row_dismissed_box, column
        )
        self.addWidget(AlliedCheckbox(column, dialog), self.row_allied_box, column)
        self.addWidget(PleaComboBox(column), self.row_plea, column)
        self.addWidget(FindingComboBox(), self.row_finding, column)
        self.addWidget(FineLineEdit(charge.offense), self.row_fine, column)
        self.addWidget(FineSuspendedLineEdit(), self.row_fine_suspended, column)
        self.addWidget(
            ChargeGridAmendButton(column, charge, dialog), self.row_amend_button, column
        )
        self.addWidget(
            ChargeGridDeleteButton(column, charge, dialog),
            self.row_delete_button,
            column,
        )


class JailChargesGrid(NoJailChargesGrid):
    row_jail_days = 9
    row_jail_days_suspended = 10
    row_amend_button = 11
    row_delete_button = 12

    def add_charge_only_to_grid(self, dialog):
        """The column is set to the one more than the current number of columns because
        a new charge is being added."""
        charge = self.get_last_charge_in_charges_list(dialog)
        column = self.columnCount() + 1
        self.addWidget(QLabel(charge.offense), self.row_offense, column)
        self.addWidget(StatuteLineEdit(charge.statute), self.row_statute, column)
        self.addWidget(DegreeComboBox(charge.degree), self.row_degree, column)
        self.addWidget(
            DismissedCheckbox(column, dialog), self.row_dismissed_box, column
        )
        self.addWidget(AlliedCheckbox(column, dialog), self.row_allied_box, column)
        self.addWidget(PleaComboBox(column), self.row_plea, column)
        self.addWidget(FindingComboBox(), self.row_finding, column)
        self.addWidget(FineLineEdit(charge.offense), self.row_fine, column)
        self.addWidget(FineSuspendedLineEdit(), self.row_fine_suspended, column)
        self.addWidget(JailLineEdit(charge.offense), self.row_jail_days, column)
        self.addWidget(JailSuspendedLineEdit(), self.row_jail_days_suspended, column)
        self.addWidget(
            ChargeGridAmendButton(column, charge, dialog), self.row_amend_button, column
        )
        self.addWidget(
            ChargeGridDeleteButton(column, charge, dialog),
            self.row_delete_button,
            column,
        )


class DiversionChargesGrid(JailChargesGrid):
    """The Diversion main_entry_dialog currently uses the same ChargesGrid as the
    JailChargesGrid. This class is created and the ChargesGrid for Diversion is
    assigned to to this class of grid for consistency and in case there is a need for
    specific changes in the fututre."""

    pass


def main():
    pass


if __name__ == "__main__":
    main()
