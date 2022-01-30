from PyQt5.QtWidgets import QGridLayout, QLabel
from loguru import logger
from package.views.custom_widgets import DeleteButton, AmendButton, PleaComboBox, AlliedCheckbox, FineLineEdit, \
    StatuteLineEdit, DegreeComboBox, FindingComboBox, FineSuspendedLineEdit, JailLineEdit, JailSuspendedLineEdit, \
    DismissedCheckbox


class ChargesGrid(QGridLayout):
    row_offense = 0
    row_statute = 1
    row_degree = 2

    def __init__(self, parent=None):
        super().__init__(parent)

    def add_charge_only_to_grid(self, dialog):
        pass

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

    def create_button_dict(self, dialog):
        button_dict = {}
        if hasattr(dialog, "guilty_all_Button"):
            button_dict[dialog.guilty_all_Button] = "Guilty"
        if hasattr(dialog, "no_contest_all_Button"):
            button_dict[dialog.no_contest_all_Button] = "No Contest"
        if hasattr(dialog, "not_guilty_all_Button"):
            button_dict[dialog.not_guilty_all_Button] = "Not Guilty"
        return button_dict

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


class LeapPleaGrid(ChargesGrid):
    row_dismissed_box = 3
    row_plea = 4
    row_delete_button = 5

    @logger.catch
    def add_charge_only_to_grid(self, dialog):
        column = self.columnCount() + 1
        added_charge_index = len(dialog.entry_case_information.charges_list) - 1
        charge = vars(dialog.entry_case_information.charges_list[added_charge_index])
        self.addWidget(QLabel(charge['offense']), LeapPleaGrid.row_offense, column)
        self.addWidget(StatuteLineEdit(charge['statute']), LeapPleaGrid.row_statute, column)
        self.addWidget(DegreeComboBox(charge['degree']), LeapPleaGrid.row_degree, column)
        self.addWidget(DismissedCheckbox(column, dialog), LeapPleaGrid.row_dismissed_box, column)
        self.addWidget(PleaComboBox(column), LeapPleaGrid.row_plea, column)
        self.add_delete_button_to_grid(dialog, LeapPleaGrid.row_delete_button, column)

    @logger.catch
    def set_all_plea_and_findings(self, dialog):
        button_dict = self.create_button_dict(dialog)
        plea = button_dict.get(self.sender())
        for column in range(1, self.columnCount()):
            if self.itemAtPosition(LeapPleaGrid.row_offense, column) is not None:
                if self.itemAtPosition(LeapPleaGrid.row_dismissed_box, column).widget().isChecked():
                    continue
                else:
                    self.itemAtPosition(LeapPleaGrid.row_plea, column).widget().setCurrentText(plea)


class NotGuiltyPleaGrid(ChargesGrid):
    row_plea = 3
    row_delete_button = 4

    @logger.catch
    def add_charge_only_to_grid(self, dialog):
        column = self.columnCount() + 1
        added_charge_index = len(dialog.entry_case_information.charges_list) - 1
        charge = vars(dialog.entry_case_information.charges_list[added_charge_index])
        self.addWidget(QLabel(charge['offense']), NotGuiltyPleaGrid.row_offense, column)
        self.addWidget(StatuteLineEdit(charge['statute']), LeapPleaGrid.row_statute, column)
        self.addWidget(DegreeComboBox(charge['degree']), LeapPleaGrid.row_degree, column)
        self.addWidget(PleaComboBox(column), NotGuiltyPleaGrid.row_plea, column)
        self.add_delete_button_to_grid(dialog, NotGuiltyPleaGrid.row_delete_button, column)

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

    def __init__(self, parent=None):
        super().__init__(parent)

    @logger.catch
    def add_charge_only_to_grid(self, dialog):
        column = self.columnCount() + 1
        added_charge_index = len(dialog.entry_case_information.charges_list) - 1
        charge = vars(dialog.entry_case_information.charges_list[added_charge_index])
        self.addWidget(QLabel(charge['offense']), NoJailChargesGrid.row_offense, column)
        self.addWidget(StatuteLineEdit(charge['statute']), NoJailChargesGrid.row_statute, column)
        self.addWidget(DegreeComboBox(charge['degree']), NoJailChargesGrid.row_degree, column)
        self.addWidget(DismissedCheckbox(column, dialog), NoJailChargesGrid.row_dismissed_box, column)
        self.addWidget(AlliedCheckbox(), NoJailChargesGrid.row_allied_box, column)
        self.addWidget(PleaComboBox(column), NoJailChargesGrid.row_plea, column)
        self.addWidget(FindingComboBox(), NoJailChargesGrid.row_finding, column)
        self.addWidget(FineLineEdit(charge['offense']), NoJailChargesGrid.row_fine, column)
        self.addWidget(FineSuspendedLineEdit(), NoJailChargesGrid.row_fine_suspended, column)
        self.add_amend_button_to_grid(dialog, NoJailChargesGrid.row_amend_button, column)
        self.add_delete_button_to_grid(dialog, NoJailChargesGrid.row_delete_button, column)

    @logger.catch
    def set_all_plea_and_findings(self, dialog):
        button_dict = self.create_button_dict(dialog)
        plea = button_dict.get(self.sender())
        for column in range(1, self.columnCount()):
            if self.itemAtPosition(NoJailChargesGrid.row_offense, column) is not None:
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

    def __init__(self, parent=None):
        super().__init__(parent)

    @logger.catch
    def add_charge_only_to_grid(self, dialog):
        column = self.columnCount() + 1
        added_charge_index = len(dialog.entry_case_information.charges_list) - 1
        charge = vars(dialog.entry_case_information.charges_list[added_charge_index])
        self.addWidget(QLabel(charge['offense']), JailChargesGrid.row_offense, column)
        self.addWidget(StatuteLineEdit(charge['statute']), JailChargesGrid.row_statute, column)
        self.addWidget(DegreeComboBox(charge['degree']), JailChargesGrid.row_degree, column)
        self.addWidget(DismissedCheckbox(column, dialog), JailChargesGrid.row_dismissed_box, column)
        self.addWidget(AlliedCheckbox(), JailChargesGrid.row_allied_box, column)
        self.addWidget(PleaComboBox(column), JailChargesGrid.row_plea, column)
        self.addWidget(FindingComboBox(), JailChargesGrid.row_finding, column)
        self.addWidget(FineLineEdit(charge['offense']), JailChargesGrid.row_fine, column)
        self.addWidget(FineSuspendedLineEdit(), JailChargesGrid.row_fine_suspended, column)
        self.addWidget(JailLineEdit(charge['offense']), JailChargesGrid.row_jail_days, column)
        self.addWidget(JailSuspendedLineEdit(), JailChargesGrid.row_jail_days_suspended, column)
        self.add_amend_button_to_grid(dialog, JailChargesGrid.row_amend_button, column)
        self.add_delete_button_to_grid(dialog, JailChargesGrid.row_delete_button, column)

    @logger.catch
    def set_all_plea_and_findings(self, dialog):
        button_dict = self.create_button_dict(dialog)
        plea = button_dict.get(self.sender())
        for column in range(1, self.columnCount()):
            if self.itemAtPosition(JailChargesGrid.row_offense, column) is not None:
                self.itemAtPosition(JailChargesGrid.row_plea, column).widget().setCurrentText(plea)
                if self.itemAtPosition(JailChargesGrid.row_allied_box, column).widget().isChecked():
                    self.itemAtPosition(JailChargesGrid.row_finding, column).widget().setCurrentText("Guilty - Allied Offense")
                else:
                    self.itemAtPosition(JailChargesGrid.row_finding, column).widget().setCurrentText("Guilty")
        self.set_cursor_to_fine_line_edit()

def main():
    pass

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()