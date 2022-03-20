from PyQt5.QtWidgets import QGridLayout, QLabel
from loguru import logger
from package.views.custom_widgets import PleaComboBox, AlliedCheckbox, FineLineEdit, \
    StatuteLineEdit, DegreeComboBox, FindingComboBox, FineSuspendedLineEdit, JailLineEdit, JailSuspendedLineEdit, \
    DismissedCheckbox, ChargeGridDeleteButton, ChargeGridAmendButton


class ChargesGrid(QGridLayout):
    """The base format of the charges grid that is used when a main_entry_dialog needs to display and interact
    with charges in a case. The ChargesGrid subclasses the QGridLayout and provides methods for manipulating the
    grid. Each main_entry_dialog that has a ChargesGrid has a specific subclassed version that is set by changing
    the class of the QGridLayout to the class of the specific subclassed ChargesGrid. This avoids having to
    initialize the grid during the setupUI method called by the main_entry_dialog classes modify_view method.
    The class is set prior to loading the case data during the main_entry_dialog load_cms_data_to_view method."""
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

    def create_button_dict(self, dialog):
        button_dict = {}
        if hasattr(dialog, "guilty_all_Button"):
            button_dict[dialog.guilty_all_Button] = "Guilty"
        if hasattr(dialog, "no_contest_all_Button"):
            button_dict[dialog.no_contest_all_Button] = "No Contest"
        if hasattr(dialog, "not_guilty_all_Button"):
            button_dict[dialog.not_guilty_all_Button] = "Not Guilty"
        return button_dict

    def set_cursor_to_fine_line_edit(self):
        for column in range(1, self.columnCount()):
            if self.itemAtPosition(ChargesGrid.row_fine, column) is not None:
                if self.itemAtPosition(ChargesGrid.row_dismissed_box, column).widget().isChecked():
                    column += 1
                    continue
                self.itemAtPosition(ChargesGrid.row_fine, column).widget().setFocus()
                break
            column += 1


class NotGuiltyPleaGrid(ChargesGrid):
    row_plea = 3
    row_delete_button = 4

    @logger.catch
    def add_charge_only_to_grid(self, dialog):
        """The column is set to the one more than the current number of columns because a new charge is being
        added."""
        charge = self.get_last_charge_in_charges_list(dialog)
        column = self.columnCount() + 1
        self.addWidget(QLabel(charge.offense), NotGuiltyPleaGrid.row_offense, column)
        self.addWidget(StatuteLineEdit(charge.statute), NotGuiltyPleaGrid.row_statute, column)
        self.addWidget(DegreeComboBox(charge.degree), NotGuiltyPleaGrid.row_degree, column)
        self.addWidget(PleaComboBox(column), NotGuiltyPleaGrid.row_plea, column)
        self.addWidget(ChargeGridDeleteButton(column, charge, dialog), NotGuiltyPleaGrid.row_delete_button,
                       column)

    @logger.catch
    def set_all_plea_and_findings(self, dialog):
        button_dict = self.create_button_dict(dialog)
        plea = button_dict.get(self.sender())
        for column in range(1, self.columnCount()):
            if self.itemAtPosition(NotGuiltyPleaGrid.row_offense, column) is not None:
                self.itemAtPosition(NotGuiltyPleaGrid.row_plea, column).widget().setCurrentText(plea)


class NoJailChargesGrid(ChargesGrid):
    row_dismissed_box = 3
    row_allied_box = 4
    row_plea = 5
    row_finding = 6
    row_fine = 7
    row_fine_suspended = 8
    row_amend_button = 9
    row_delete_button = 10

    @logger.catch
    def add_charge_only_to_grid(self, dialog):
        """The column is set to the one more than the current number of columns because a new charge is being
        added."""
        charge = self.get_last_charge_in_charges_list(dialog)
        column = self.columnCount() + 1
        self.addWidget(QLabel(charge.offense), NoJailChargesGrid.row_offense, column)
        self.addWidget(StatuteLineEdit(charge.statute), NoJailChargesGrid.row_statute, column)
        self.addWidget(DegreeComboBox(charge.degree), NoJailChargesGrid.row_degree, column)
        self.addWidget(DismissedCheckbox(column, dialog), NoJailChargesGrid.row_dismissed_box, column)
        self.addWidget(AlliedCheckbox(column, dialog), NoJailChargesGrid.row_allied_box, column)
        self.addWidget(PleaComboBox(column), NoJailChargesGrid.row_plea, column)
        self.addWidget(FindingComboBox(), NoJailChargesGrid.row_finding, column)
        self.addWidget(FineLineEdit(charge.offense), NoJailChargesGrid.row_fine, column)
        self.addWidget(FineSuspendedLineEdit(), NoJailChargesGrid.row_fine_suspended, column)
        self.addWidget(ChargeGridAmendButton(column, charge, dialog), NoJailChargesGrid.row_amend_button, column)
        self.addWidget(ChargeGridDeleteButton(column, charge, dialog), NoJailChargesGrid.row_delete_button, column)

    @logger.catch
    def set_all_plea_and_findings(self, dialog):
        button_dict = self.create_button_dict(dialog)
        plea = button_dict.get(self.sender())
        for column in range(1, self.columnCount()):
            if self.itemAtPosition(NoJailChargesGrid.row_offense, column) is not None:
                if self.itemAtPosition(NoJailChargesGrid.row_dismissed_box, column).widget().isChecked():
                    continue
                else:
                    self.itemAtPosition(NoJailChargesGrid.row_plea, column).widget().setCurrentText(plea)
                    if self.itemAtPosition(NoJailChargesGrid.row_allied_box, column).widget().isChecked():
                        self.itemAtPosition(NoJailChargesGrid.row_finding, column).widget().setCurrentText("Guilty - Allied Offense")
                    else:
                        self.itemAtPosition(NoJailChargesGrid.row_finding, column).widget().setCurrentText("Guilty")
        self.set_cursor_to_fine_line_edit()


class JailChargesGrid(NoJailChargesGrid):
    row_jail_days = 9
    row_jail_days_suspended = 10
    row_amend_button = 11
    row_delete_button = 12

    @logger.catch
    def add_charge_only_to_grid(self, dialog):
        """The column is set to the one more than the current number of columns because a new charge is being
        added."""
        charge = self.get_last_charge_in_charges_list(dialog)
        column = self.columnCount() + 1
        self.addWidget(QLabel(charge.offense), JailChargesGrid.row_offense, column)
        self.addWidget(StatuteLineEdit(charge.statute), JailChargesGrid.row_statute, column)
        self.addWidget(DegreeComboBox(charge.degree), JailChargesGrid.row_degree, column)
        self.addWidget(DismissedCheckbox(column, dialog), JailChargesGrid.row_dismissed_box, column)
        self.addWidget(AlliedCheckbox(column, dialog), JailChargesGrid.row_allied_box, column)
        self.addWidget(PleaComboBox(column), JailChargesGrid.row_plea, column)
        self.addWidget(FindingComboBox(), JailChargesGrid.row_finding, column)
        self.addWidget(FineLineEdit(charge.offense), JailChargesGrid.row_fine, column)
        self.addWidget(FineSuspendedLineEdit(), JailChargesGrid.row_fine_suspended, column)
        self.addWidget(JailLineEdit(charge.offense), JailChargesGrid.row_jail_days, column)
        self.addWidget(JailSuspendedLineEdit(), JailChargesGrid.row_jail_days_suspended, column)
        self.addWidget(ChargeGridAmendButton(column, charge, dialog), JailChargesGrid.row_amend_button, column)
        self.addWidget(ChargeGridDeleteButton(column, charge, dialog), JailChargesGrid.row_delete_button, column)

    @logger.catch
    def set_all_plea_and_findings(self, dialog):
        button_dict = self.create_button_dict(dialog)
        plea = button_dict.get(self.sender())
        for column in range(1, self.columnCount()):
            if self.itemAtPosition(JailChargesGrid.row_offense, column) is not None:
                if self.itemAtPosition(JailChargesGrid.row_dismissed_box, column).widget().isChecked():
                    continue
                else:
                    self.itemAtPosition(JailChargesGrid.row_plea, column).widget().setCurrentText(plea)
                    if self.itemAtPosition(JailChargesGrid.row_allied_box, column).widget().isChecked():
                        self.itemAtPosition(JailChargesGrid.row_finding, column).widget().setCurrentText("Guilty - Allied Offense")
                    else:
                        self.itemAtPosition(JailChargesGrid.row_finding, column).widget().setCurrentText("Guilty")
        self.set_cursor_to_fine_line_edit()


class DiversionChargesGrid(JailChargesGrid):
    """The Diversion main_entry_dialog currently uses the same ChargesGrid as the JailChargesGrid. This class is
    created and the ChargesGrid for Diversion is assigned to to this class of grid for consistency and in case
    there is a need for specific changes in the fututre."""
    pass


def main():
    pass

if __name__ == "__main__":
   main()