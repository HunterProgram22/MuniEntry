"""Module contains all versions of QGridLayout that are used as charges grids on dialogs."""
from loguru import logger
from PyQt5.QtWidgets import QGridLayout, QLabel

from package.views import custom_widgets as cw


class ChargesGrid(QGridLayout):
    """The base format of the charges_gridLayout used for a main_entry_dialog.

    The ChargesGrid subclasses the QGridLayout and provides methods for manipulating the grid.
    Each main_entry_dialog that has a ChargesGrid (self.charges_gridLayout) has a specific
    subclassed version that is set by changing the class of the QGridLayout to the class of
    the specific subclassed ChargesGrid. This avoids having to initialize the grid during the
    setupUI method called by the main_entry_dialog classes modify_view method. The class is
    set prior to loading the case data during the main_entry_dialog load_cms_data_to_view method.
    """

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

    def get_add_column(self) -> int:
        """Returns one more than total columns so a new column is used to add items."""
        return self.columnCount() + 1

    def get_plea(self) -> str:
        """Returns copy of the label of the plea button after stripping " All" from end.

        Ex. "Guilty All" button is returned as "Guilty" to be used as the plea.
        """
        return self.sender().text().replace(' All', '')

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

    @logger.catch
    def set_all_pleas(self):
        """This method after setting all pleas calls the set_all_findings. In the Not
        Guilty Plea Grid the method is overriden to not call the set_all_findings
        because there are no findings to be set with a Not Guilty plea."""
        plea = self.get_plea()
        for column in range(1, self.columnCount()):
            if self.itemAtPosition(self.row_offense, column) is not None:
                if (
                    self.itemAtPosition(self.row_dismissed_box, column)
                    .widget()
                    .isChecked()
                ):
                    continue
                self.itemAtPosition(self.row_plea, column).widget().setCurrentText(plea)
                self.set_all_findings(column)
        self.set_cursor_to_fine_line_edit()

    @logger.catch
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
        charge = self.get_last_charge_in_charges_list(dialog)
        column = self.get_add_column()
        self.addWidget(QLabel(charge.offense), self.row_offense, column)
        self.addWidget(cw.StatuteLineEdit(charge.statute), self.row_statute, column)
        self.addWidget(cw.DegreeComboBox(charge.degree), self.row_degree, column)
        self.addWidget(cw.PleaComboBox(column, dialog), self.row_plea, column)
        self.addWidget(
            cw.ChargeGridDeleteButton(column, charge, dialog),
            self.row_delete_button,
            column,
        )

    def set_all_pleas(self):
        """This method overrides the ChargesGrid set_all_pleas because there are no
        findings to be added for a Not Guilty plea."""
        plea = self.get_plea()
        for column in range(1, self.columnCount()):
            if self.itemAtPosition(self.row_offense, column) is not None:
                self.itemAtPosition(self.row_plea, column).widget().setCurrentText(plea)


class LeapAdmissionPleaGrid(ChargesGrid):
    row_dismissed_box = 3
    row_plea = 4
    row_amend_button = 5
    row_delete_button = 6

    def add_charge_only_to_grid(self, dialog):
        """The column is set to the one more than the current number of columns because
        a new charge is being added."""
        charge = self.get_last_charge_in_charges_list(dialog)
        column = self.get_add_column()
        self.addWidget(QLabel(charge.offense), self.row_offense, column)
        self.addWidget(cw.StatuteLineEdit(charge.statute), self.row_statute, column)
        self.addWidget(cw.DegreeComboBox(charge.degree), self.row_degree, column)
        self.addWidget(
            cw.DismissedCheckbox(column, dialog), self.row_dismissed_box, column
        )
        self.addWidget(cw.PleaComboBox(column, dialog), self.row_plea, column)
        self.addWidget(
            cw.ChargeGridAmendButton(column, charge, dialog), self.row_amend_button, column
        )
        self.addWidget(
            cw.ChargeGridDeleteButton(column, charge, dialog),
            self.row_delete_button,
            column,
        )

    def set_all_pleas(self):
        """Overrides the base set_all_pleas because LEAP does not have findings set."""
        plea = self.get_plea()
        for column in range(1, self.columnCount()):
            if self.itemAtPosition(self.row_offense, column) is not None:
                if (
                    self.itemAtPosition(self.row_dismissed_box, column)
                    .widget()
                    .isChecked()
                ):
                    continue
                self.itemAtPosition(self.row_plea, column).widget().setCurrentText(plea)


class PleaOnlyGrid(ChargesGrid):
    row_dismissed_box = 3
    row_allied_box = 4
    row_plea = 5
    row_finding = 6
    row_amend_button = 7
    row_delete_button = 8

    def add_charge_only_to_grid(self, dialog):
        charge = self.get_last_charge_in_charges_list(dialog)
        column = self.get_add_column()
        self.addWidget(QLabel(charge.offense), self.row_offense, column)
        self.addWidget(cw.StatuteLineEdit(charge.statute), self.row_statute, column)
        self.addWidget(cw.DegreeComboBox(charge.degree), self.row_degree, column)
        self.addWidget(
            cw.DismissedCheckbox(column, dialog), self.row_dismissed_box, column
        )
        self.addWidget(cw.AlliedCheckbox(column, dialog), self.row_allied_box, column)
        self.addWidget(cw.PleaComboBox(column, dialog), self.row_plea, column)
        self.addWidget(cw.FindingComboBox(), self.row_finding, column)
        self.addWidget(
            cw.ChargeGridAmendButton(column, charge, dialog), self.row_amend_button, column
        )
        self.addWidget(
            cw.ChargeGridDeleteButton(column, charge, dialog),
            self.row_delete_button,
            column,
        )


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
        charge = self.get_last_charge_in_charges_list(dialog)
        column = self.get_add_column()
        self.addWidget(QLabel(charge.offense), self.row_offense, column)
        self.addWidget(cw.StatuteLineEdit(charge.statute), self.row_statute, column)
        self.addWidget(cw.DegreeComboBox(charge.degree), self.row_degree, column)
        self.addWidget(
            cw.DismissedCheckbox(column, dialog), self.row_dismissed_box, column
        )
        self.addWidget(cw.AlliedCheckbox(column, dialog), self.row_allied_box, column)
        self.addWidget(cw.PleaComboBox(column, dialog), self.row_plea, column)
        self.addWidget(cw.FindingComboBox(), self.row_finding, column)
        self.addWidget(cw.FineLineEdit(charge.offense), self.row_fine, column)
        self.addWidget(cw.FineSuspendedLineEdit(), self.row_fine_suspended, column)
        self.addWidget(
            cw.ChargeGridAmendButton(column, charge, dialog), self.row_amend_button, column
        )
        self.addWidget(
            cw.ChargeGridDeleteButton(column, charge, dialog),
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
        column = self.get_add_column()
        self.addWidget(QLabel(charge.offense), self.row_offense, column)
        self.addWidget(cw.StatuteLineEdit(charge.statute), self.row_statute, column)
        self.addWidget(cw.DegreeComboBox(charge.degree), self.row_degree, column)
        self.addWidget(
            cw.DismissedCheckbox(column, dialog), self.row_dismissed_box, column
        )
        self.addWidget(cw.AlliedCheckbox(column, dialog), self.row_allied_box, column)
        self.addWidget(cw.PleaComboBox(column, dialog), self.row_plea, column)
        self.addWidget(cw.FindingComboBox(), self.row_finding, column)
        self.addWidget(cw.FineLineEdit(charge.offense), self.row_fine, column)
        self.addWidget(cw.FineSuspendedLineEdit(), self.row_fine_suspended, column)
        self.addWidget(cw.JailLineEdit(charge.offense), self.row_jail_days, column)
        self.addWidget(cw.JailSuspendedLineEdit(), self.row_jail_days_suspended, column)
        self.addWidget(
            cw.ChargeGridAmendButton(column, charge, dialog), self.row_amend_button, column
        )
        self.addWidget(
            cw.ChargeGridDeleteButton(column, charge, dialog),
            self.row_delete_button,
            column,
        )

    def set_all_trial_findings(self):
        self.trial_finding = self.get_plea()
        for column in range(1, self.columnCount()):
            if self.itemAtPosition(self.row_offense, column) is not None:
                if (
                        self.itemAtPosition(self.row_dismissed_box, column)
                                .widget()
                                .isChecked()
                ):
                    continue
                if self.itemAtPosition(self.row_allied_box, column).widget().isChecked():
                    self.itemAtPosition(self.row_finding, column).widget().setCurrentText(
                        "Guilty - Allied Offense"
                    )
                else:
                    self.itemAtPosition(self.row_finding, column).widget().setCurrentText(
                       self.trial_finding
                )


class DiversionChargesGrid(JailChargesGrid):
    """The Diversion main_entry_dialog currently uses the same ChargesGrid as the
    JailChargesGrid. This class is created and the ChargesGrid for Diversion is
    assigned to to this class of grid for consistency and in case there is a need for
    specific changes in the fututre."""


if __name__ == "__main__":
    print("Charges Grids ran directly")
else:
    print("Charges Grids imported")
