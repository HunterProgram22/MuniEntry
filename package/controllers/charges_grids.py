"""Module contains all versions of QGridLayout that are used as charges grids on dialogs."""
from PyQt5.QtWidgets import QGridLayout, QLabel

from package.views import custom_widgets as cw


def attribute_check(func, *args, **kwargs):
    """Wrapper to check if an attribute exists.

    Skips the check if the attribute does not exist.
    """
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except AttributeError:
            pass

    return wrapper


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

    def get_plea(self) -> str:
        """Returns copy of the label of the plea button after stripping ' All' from end.

        Ex. "Guilty All" button is returned as "Guilty" to be used as the plea.
        """
        return self.sender().text().replace(' All', '')

    def check_if_column_empty(self, column: int) -> bool:
        if self.itemAtPosition(0, column) is None:
            return True

    @attribute_check
    def check_if_charge_dismissed(self, column: int) -> bool:
        if self.itemAtPosition(self.row_dismissed_box, column).widget().isChecked():
            return True

    @attribute_check
    def check_if_allied_offense(self, column: int) -> bool:
        if self.itemAtPosition(self.row_allied_box, column).widget().isChecked():
            return True

    @attribute_check
    def set_cursor_to_first_fine_box(self) -> None:
        """Sets the cursor to the first non-dismissed charge's fine box.

        Column is immediately incremented because 1st column is grid labels.
        """
        for column in range(0, self.columnCount()):
            column += 1
            if self.check_if_column_empty(column):
                continue
            if self.check_if_charge_dismissed(column):
                continue
            self.itemAtPosition(self.row_fine, column).widget().setFocus()
            break

    def set_all_pleas(self):
        """Sets the plea for all charges based on the button pressed.

        Ex. Pressing 'No Contest All' sets all pleas to No Contest.
        """
        plea = self.get_plea()
        for column in range(0, self.columnCount()):
            column += 1
            if self.check_if_column_empty(column):
                continue
            plea_box = self.itemAtPosition(self.row_plea, column).widget()
            if self.check_if_charge_dismissed(column):
                continue
            plea_box.setCurrentText(plea)
        self.set_cursor_to_first_fine_box()

    def set_all_findings(self):
        """Sets the findings for all charges to either Guilty or Guilty - Allied Offense."""
        for column in range(0, self.columnCount()):
            column += 1
            if self.check_if_column_empty(column):
                continue
            finding_box = self.itemAtPosition(self.row_finding, column).widget()
            if self.check_if_charge_dismissed(column):
                continue
            if self.check_if_allied_offense(column):
                finding_box.setCurrentText('Guilty - Allied Offense')
            else:
                finding_box.setCurrentText('Guilty')

    def add_charge_to_grid(self, charge, column):
        """Adds three required charge fields - offense, statute and degree - to the charge grid."""
        self.addWidget(QLabel(charge.offense), self.row_offense, column)
        self.addWidget(cw.StatuteLineEdit(charge.statute), self.row_statute, column)
        self.addWidget(cw.DegreeComboBox(charge.degree), self.row_degree, column)

    def add_delete_button_to_grid(self, charge, column, dialog):
        self.addWidget(cw.ChargeGridDeleteButton(column, charge, dialog), self.row_delete_button,
                       column)

    def add_plea_box_to_grid(self, column, dialog):
        self.addWidget(cw.PleaComboBox(column, dialog), self.row_plea, column)


class NotGuiltyPleaGrid(ChargesGrid):
    """Charge Grid for NotGuiltyPleaBond Dialog.

    The dialog does not enter a finding, so the grid is only 5 rows total and the rows are
    renumbered accordingly for this class.
    """

    row_offense = 0
    row_statute = 1
    row_degree = 2
    row_plea = 3
    row_delete_button = 4

    def add_fields_to_charges_grid(self, dialog):
        """Adds the fields required for the NotGuiltyPleaGrid.

        Required fields: offense, statute, degree, plea, delete button.
        """
        column = self.columnCount() + 1
        charge = dialog.entry_case_information.charges_list[-1]
        self.add_charge_to_grid(charge, column)
        self.add_plea_box_to_grid(column, dialog)
        self.add_delete_button_to_grid(charge, column, dialog)


class LeapAdmissionPleaGrid(ChargesGrid):
    row_dismissed_box = 3
    row_plea = 4
    row_amend_button = 5
    row_delete_button = 6

    def add_fields_to_charges_grid(self, dialog):
        """The column is set to the one more than the current number of columns because
        a new charge is being added."""
        charge = dialog.entry_case_information.charges_list[-1]
        column = self.columnCount() + 1 # Add 1 because adding new column
        self.add_charge_to_grid(charge, column)
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

    def add_fields_to_charges_grid(self, dialog):
        charge = dialog.entry_case_information.charges_list[-1]
        column = self.columnCount() + 1 # Add 1 because adding new column
        self.add_charge_to_grid(charge, column)
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


class FineOnlyChargesGrid(ChargesGrid):
    row_dismissed_box = 3
    row_allied_box = 4
    row_plea = 5
    row_finding = 6
    row_fine = 7
    row_fine_suspended = 8
    row_amend_button = 9
    row_delete_button = 10

    def add_fields_to_charges_grid(self, dialog):
        charge = dialog.entry_case_information.charges_list[-1]
        column = self.columnCount() + 1 # Add 1 because adding new column
        self.add_charge_to_grid(charge, column)
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


class JailChargesGrid(FineOnlyChargesGrid):
    row_jail_days = 9
    row_jail_days_suspended = 10
    row_amend_button = 11
    row_delete_button = 12

    def add_fields_to_charges_grid(self, dialog):
        """The column is set to the one more than the current number of columns because
        a new charge is being added."""
        charge = dialog.entry_case_information.charges_list[-1]
        column = self.columnCount() + 1 # Add 1 because adding new column
        self.add_charge_to_grid(charge, column)
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
