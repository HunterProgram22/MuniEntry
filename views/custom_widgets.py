from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QLabel, QPushButton, QMessageBox, QComboBox, QLineEdit, QCheckBox, QGridLayout

from loguru import logger

class PleaComboBox(QComboBox):
    def __init__(self, parent=None):
        super(QComboBox, self).__init__(parent)
        self.set_up_widget()

    def set_up_widget(self):
        self.setMinimumSize(QtCore.QSize(200, 0))
        self.setMaximumSize(QtCore.QSize(200, 50))
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setEditable(True)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setObjectName("plea_choice_box")
        self.addItem("")
        self.addItem("Guilty")
        self.addItem("No Contest")
        self.addItem("Not Guilty")
        self.addItem("Dismissed")


class FindingComboBox(QComboBox):
    def __init__(self, parent=None):
        super(QComboBox, self).__init__(parent)
        self.set_up_widget()

    def set_up_widget(self):
        self.setMinimumSize(QtCore.QSize(200, 0))
        self.setMaximumSize(QtCore.QSize(200, 50))
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setEditable(True)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setObjectName("finding_choice_box")
        self.addItem("")
        self.addItem("Guilty")
        self.addItem("Not Guilty")
        self.addItem("Dismissed")
        self.addItem("Guilty - Allied Offense")
        self.addItem("Not Guilty - Allied Offense")


class FineLineEdit(QLineEdit):
    def __init__(self, offense=None, parent=None):
        super(QLineEdit, self).__init__(parent)
        self.set_up_widget(offense)

    def set_up_widget(self, offense):
        self.setMinimumSize(QtCore.QSize(200, 0))
        self.setMaximumSize(QtCore.QSize(200, 50))
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setObjectName("fines_amount")
        if offense == "Seatbelt - Driver":
            self.setText("30")
        elif offense == "Seatbelt - Passenger":
            self.setText("20")
        elif offense == "Failure to Stop for School Bus":
            self.setText("500")
        else:
            self.setText("")


class FineSuspendedLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super(QLineEdit, self).__init__(parent)
        self.set_up_widget()

    def set_up_widget(self):
        self.setMinimumSize(QtCore.QSize(200, 0))
        self.setMaximumSize(QtCore.QSize(200, 50))
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setObjectName("fines_suspended")


class JailLineEdit(QLineEdit):
    def __init__(self, offense=None, parent=None):
        super(QLineEdit, self).__init__(parent)
        self.set_up_widget(offense)

    def set_up_widget(self, offense):
        self.setMinimumSize(QtCore.QSize(200, 0))
        self.setMaximumSize(QtCore.QSize(200, 50))
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setObjectName("jaild_days")


class JailSuspendedLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super(QLineEdit, self).__init__(parent)
        self.set_up_widget()

    def set_up_widget(self):
        self.setMinimumSize(QtCore.QSize(200, 0))
        self.setMaximumSize(QtCore.QSize(200, 50))
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setObjectName("jail_days_suspended")


class DeleteButton(QPushButton):
    def __init__(self, parent=None):
        super(QPushButton, self).__init__(parent)
        self.set_up_widget()

    def set_up_widget(self):
        self.setStyleSheet("background-color: rgb(170, 58, 63);")
        self.setText("Delete")
        self.setObjectName("delete_Button")
        self.setFocusPolicy(QtCore.Qt.NoFocus)


class AmendButton(QPushButton):
    def __init__(self, parent=None):
        super(QPushButton, self).__init__(parent)
        self.set_up_widget()

    def set_up_widget(self):
        self.setStyleSheet("background-color: rgb(62, 146, 255);")
        self.setText("Amend")
        self.setObjectName("amend_Button")
        self.setFocusPolicy(QtCore.Qt.NoFocus)


class AlliedCheckbox(QCheckBox):
    def __init__(self, parent=None):
        super(QCheckBox, self).__init__(parent)
        self.set_up_widget()

    def set_up_widget(self):
        self.setText("Allied Offense")
        self.setObjectName("allied_checkBox")
        self.setFocusPolicy(QtCore.Qt.NoFocus)


class RequiredBox(QMessageBox):
    def __init__(self, message, parent=None):
        super(QMessageBox, self).__init__(parent)
        self.message = message
        self.set_up_widget()

    def set_up_widget(self):
        self.setIcon(QMessageBox.Warning)
        self.setWindowTitle("Required")
        self.setText(self.message)
        self.setStandardButtons(QMessageBox.Ok)
        self.exec()


class ChargesGrid(QGridLayout):
    def __init__(self, parent=None):
        super(QGridLayout, self).__init__(parent)

    @logger.catch
    def add_charge_only_to_grid(self, dialog, add_allied_box=True, add_delete_button=False):
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
        row = 0
        column = self.columnCount() + 1
        added_charge_index = len(dialog.entry_case_information.charges_list) - 1
        charge = vars(dialog.entry_case_information.charges_list[added_charge_index])
        self.addWidget(QLabel(charge['offense']), row, column)
        row += 1
        self.addWidget(QLabel(charge['statute']), row, column)
        row += 1
        self.addWidget(QLabel(charge['degree']), row, column)
        row += 1
        if add_allied_box == True:
            self.addWidget(AlliedCheckbox(), row, column)
            row += 1
        self.addWidget(PleaComboBox(), row, column)
        row += 1
        if add_delete_button == True:
            self.add_delete_button_to_grid(dialog, row, column)
            row += 1
        return row, column, charge

    def no_jail_add_charge_finding_and_fines_to_grid(self, dialog):
        row, column, charge = self.add_charge_only_to_grid(dialog)
        self.addWidget(FindingComboBox(), row, column)
        row += 1
        self.addWidget(FineLineEdit(charge['offense']), row, column)
        row += 1
        self.addWidget(FineSuspendedLineEdit(), row, column)
        row += 1
        self.add_amend_button_to_grid(dialog, row, column)
        row += 1
        self.add_delete_button_to_grid(dialog, row, column)

    def jail_add_charge_finding_fines_and_jail_to_grid(self, dialog):
        row, column, charge = self.add_charge_only_to_grid(dialog)
        self.addWidget(FindingComboBox(), row, column)
        row += 1
        self.addWidget(FineLineEdit(charge['offense']), row, column)
        row += 1
        self.addWidget(FineSuspendedLineEdit(), row, column)
        row += 1
        self.addWidget(JailLineEdit(charge['offense']), row, column)
        row += 1
        self.addWidget(JailSuspendedLineEdit(), row, column)
        row += 1
        self.add_amend_button_to_grid(dialog, row, column)
        row += 1
        self.add_delete_button_to_grid(dialog, row, column)

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


def main():
    pass

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()
