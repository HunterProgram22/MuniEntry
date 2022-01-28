import pathlib

from PyQt5 import QtCore
from PyQt5.QtCore import QSortFilterProxyModel, Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QMessageBox, QComboBox, QLineEdit, QCheckBox, QGridLayout, QApplication, QCompleter
from PyQt5 import QtGui

from loguru import logger

from settings import ICON_PATH


class ExtendedComboBox(QComboBox):
    def __init__(self, parent=None):
        """Code is from the user Joachim Bonfert 8/2/21 answer at https://stackoverflow.com/questions/4827207/
        how-do-i-filter-the-pyqt-qcombobox-items-based-on-the-text-input"""
        super(ExtendedComboBox, self).__init__(parent)
        self.setFocusPolicy(Qt.StrongFocus)
        self.setEditable(True)

        # add a filter model to filter matching items
        self.pFilterModel = QSortFilterProxyModel(self)
        self.pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.pFilterModel.setSourceModel(self.model())

        # add a completer, which uses the filter model
        self.completer = QCompleter(self.pFilterModel, self)
        # always show all (filtered) completions
        self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.setCompleter(self.completer)

        # connect signals
        self.lineEdit().textEdited[str].connect(self.pFilterModel.setFilterFixedString)
        self.completer.activated.connect(self.on_completer_activated)

    # on selection of an item from the completer, select the corresponding item from combobox
    def on_completer_activated(self, text):
        if text:
            index = self.findText(text)
            self.setCurrentIndex(index)
            self.activated[str].emit(self.itemText(index))

    # on model change, update the models of the filter and completer as well
    def setModel(self, model):
        super(ExtendedComboBox, self).setModel(model)
        self.pFilterModel.setSourceModel(model)
        self.completer.setModel(self.pFilterModel)

    # on model column change, update the model column of the filter and completer as well
    def setModelColumn(self, column):
        self.completer.setCompletionColumn(column)
        self.pFilterModel.setFilterKeyColumn(column)
        super(ExtendedComboBox, self).setModelColumn(column)


class StatuteLineEdit(QLineEdit):
    def __init__(self, statute=None, parent=None):
        super(QLineEdit, self).__init__(parent)
        self.set_up_widget(statute)

    def set_up_widget(self, statute):
        self.setMinimumSize(QtCore.QSize(200, 0))
        self.setMaximumSize(QtCore.QSize(200, 50))
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setObjectName("statute_lineEdit")
        self.setText(statute)


class DegreeComboBox(QComboBox):
    def __init__(self, degree, parent=None):
        super(QComboBox, self).__init__(parent)
        self.set_up_widget(degree)

    def set_up_widget(self, degree):
        self.setMinimumSize(QtCore.QSize(200, 0))
        self.setMaximumSize(QtCore.QSize(200, 50))
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setEditable(True)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setObjectName("degree_choice_box")
        self.addItem("")
        self.addItem("M1")
        self.addItem("M2")
        self.addItem("M3")
        self.addItem("M4")
        self.addItem("MM")
        self.addItem("UCM")
        self.setCurrentText(degree)


class PleaComboBox(QComboBox):
    def __init__(self, column, parent=None):
        super(QComboBox, self).__init__(parent)
        self.column = column
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
        # self.currentTextChanged.connect(
        #   lambda plea, column=self.column: ChargesGrid.update_if_dismissed(plea, column))


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
        self.addItem("Lesser Included")
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
        self.setObjectName("jail_days")


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
        self.setWindowIcon(QtGui.QIcon(ICON_PATH + 'gavel.ico'))
        self.setIcon(QMessageBox.Critical)
        self.setWindowTitle("Required")
        self.setText(self.message)
        self.setStandardButtons(QMessageBox.Ok)


class WarningBox(QMessageBox):
    def __init__(self, message, parent=None):
        super(QMessageBox, self).__init__(parent)
        self.message = message
        self.set_up_widget()

    def set_up_widget(self):
        self.setWindowIcon(QtGui.QIcon(ICON_PATH + 'gavel.ico'))
        self.setIcon(QMessageBox.Warning)
        self.setWindowTitle("Warning")
        self.setText(self.message)
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)


class ChargesGrid(QGridLayout):
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
                    message = RequiredBox("You must enter a plea.")
                    message.exec()
                    return None
                elif self.itemAtPosition(row_plea, column).widget().currentText() == "Dismissed":
                    column += 2
                    loop_counter += 1
                    continue
                elif self.itemAtPosition(row_finding, column).widget().currentText() == "":
                    offense = self.itemAtPosition(0, column).widget().text()
                    message = RequiredBox(f"You must enter a finding for {offense}.")
                    message.exec()
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
                    if isinstance(self.itemAtPosition(row, column).widget(), PleaComboBox):
                        self.itemAtPosition(row, column).widget().setCurrentText(plea)
                        if isinstance(self.itemAtPosition(row-1, column).widget(), AlliedCheckbox):
                            if self.itemAtPosition(row-1, column).widget().isChecked():
                                self.itemAtPosition(row+1, column).widget().setCurrentText("Guilty - Allied Offense")
                            else:
                                try:
                                    if self.itemAtPosition(row+1, column) is not None:
                                        self.itemAtPosition(row+1, column).widget().setCurrentText("Guilty")
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


class LeapPleaGrid(ChargesGrid):
    row_offense = 0
    row_statute = 1
    row_degree = 2
    row_plea = 3
    row_delete_button = 4

    @logger.catch
    def add_charge_only_to_grid(self, dialog):
        column = self.columnCount() + 1
        added_charge_index = len(dialog.entry_case_information.charges_list) - 1
        charge = vars(dialog.entry_case_information.charges_list[added_charge_index])
        self.addWidget(QLabel(charge['offense']), LeapPleaGrid.row_offense, column)
        self.addWidget(StatuteLineEdit(charge['statute']), LeapPleaGrid.row_statute, column)
        self.addWidget(DegreeComboBox(charge['degree']), LeapPleaGrid.row_degree, column)
        self.addWidget(PleaComboBox(column), LeapPleaGrid.row_plea, column)
        self.add_delete_button_to_grid(dialog, LeapPleaGrid.row_delete_button, column)


class NotGuiltyPleaGrid(ChargesGrid):
    """This grid keeps the statute and degree as labels that are not editable."""
    row_offense = 0
    row_statute = 1
    row_degree = 2
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


class NoJailChargesGrid(ChargesGrid):
    row_offense = 0
    row_statute = 1
    row_degree = 2
    row_allied_box = 3
    row_plea = 4
    row_finding = 5
    row_fine = 6
    row_fine_suspended = 7
    row_amend_button = 8
    row_delete_button = 9

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
        self.addWidget(AlliedCheckbox(), NoJailChargesGrid.row_allied_box, column)
        self.addWidget(PleaComboBox(column), NoJailChargesGrid.row_plea, column)
        self.addWidget(FindingComboBox(), NoJailChargesGrid.row_finding, column)
        self.addWidget(FineLineEdit(charge['offense']), NoJailChargesGrid.row_fine, column)
        self.addWidget(FineSuspendedLineEdit(), NoJailChargesGrid.row_fine_suspended, column)
        self.add_amend_button_to_grid(dialog, NoJailChargesGrid.row_amend_button, column)
        self.add_delete_button_to_grid(dialog, NoJailChargesGrid.row_delete_button, column)


class JailChargesGrid(ChargesGrid):
    row_offense = 0
    row_statute = 1
    row_degree = 2
    row_allied_box = 3
    row_plea = 4
    row_finding = 5
    row_fine = 6
    row_fine_suspended = 7
    row_jail_days = 8
    row_jail_days_suspended = 9
    row_amend_button = 10
    row_delete_button = 11

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
        self.addWidget(AlliedCheckbox(), JailChargesGrid.row_allied_box, column)
        self.addWidget(PleaComboBox(column), JailChargesGrid.row_plea, column)
        self.addWidget(FindingComboBox(), JailChargesGrid.row_finding, column)
        self.addWidget(FineLineEdit(charge['offense']), JailChargesGrid.row_fine, column)
        self.addWidget(FineSuspendedLineEdit(), JailChargesGrid.row_fine_suspended, column)
        self.addWidget(JailLineEdit(charge['offense']), JailChargesGrid.row_jail_days, column)
        self.addWidget(JailSuspendedLineEdit(), JailChargesGrid.row_jail_days_suspended, column)
        self.add_amend_button_to_grid(dialog, JailChargesGrid.row_amend_button, column)
        self.add_delete_button_to_grid(dialog, JailChargesGrid.row_delete_button, column)


def main():
    pass

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()
