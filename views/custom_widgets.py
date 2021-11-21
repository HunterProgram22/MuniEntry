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
    def add_charge_to_grid(self, dialog):
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
        added_charge_index = len(dialog.case_information.charges_list) - 1
        charge = vars(dialog.case_information.charges_list[added_charge_index])
        self.addWidget(QLabel(charge['offense']), row, column)
        row += 1
        self.addWidget(QLabel(charge['statute']), row, column)
        row += 1
        self.addWidget(QLabel(charge['degree']), row, column)
        row += 1
        self.addWidget(AlliedCheckbox(), row, column)
        row += 1
        self.addWidget(PleaComboBox(), row, column)
        row += 1
        self.addWidget(FindingComboBox(), row, column)
        row += 1
        self.addWidget(FineLineEdit(dialog.criminal_charge.offense), row, column)
        row += 1
        self.addWidget(FineSuspendedLineEdit(), row, column)
        row += 1
        self.add_delete_button_to_view(dialog, row, column)
        row += 1
        self.add_amend_button_to_view(dialog, row, column)

    def add_delete_button_to_view(self, dialog, row, column):
        """This method is called in the dialog subclass so that it is inserted in the
        correct row."""
        delete_button = DeleteButton()
        dialog.delete_button_list.append(delete_button)
        delete_button.pressed.connect(dialog.delete_charge)
        self.addWidget(delete_button, row, column)

    def add_amend_button_to_view(self, dialog, row, column):
        """This method is called in the dialog subclass so that it is inserted in the
        correct row."""
        amend_button = AmendButton()
        dialog.amend_button_list.append(amend_button)
        amend_button.clicked.connect(dialog.start_amend_offense_dialog)
        self.addWidget(amend_button, row, column)
