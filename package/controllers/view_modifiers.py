"""Module that contains ViewModifier classes. ViewModifier classes are called for a dialog
after the setupUI is called. This class makes changes to the view that are outside the the specific
view file. Modifications to the view are placed in the ViewModifier class so that they don't need to
be updated each time a view file is recompiled through the pyuic5 command."""
from loguru import logger
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import QDate
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QDialog, QLabel, QComboBox, QCheckBox, QLineEdit, QTextEdit, QDateEdit, QTimeEdit

from package.controllers.helper_functions import set_future_date


class BaseDialogViewModifier(object):
    def __init__(self, dialog):
        dialog.setWindowIcon(QtGui.QIcon('./icons/gavel.ico'))
        dialog.setWindowFlags(dialog.windowFlags() |
                            QtCore.Qt.CustomizeWindowHint |
                            QtCore.Qt.WindowMaximizeButtonHint |
                            QtCore.Qt.WindowCloseButtonHint)
        dialog.setupUi(dialog)


    ###Main Dialog Setup Methods###
    def set_plea_trial_date(self, dialog):
        dialog.plea_trial_date.setDate(QtCore.QDate.currentDate())

    def set_appearance_reason(self, dialog):
        if dialog.case_table == "final_pretrials":
            dialog.appearance_reason_box.setCurrentText("change of plea")

    def set_balance_due_date(self, dialog):
        dialog.balance_due_date.setDate(QtCore.QDate.currentDate())


    ###Additional Condition Dialog Setup Methods###
    def set_conditions_case_information_banner(self, dialog):
        column = dialog.charges_gridLayout.columnCount() + 1
        for _index, charge in enumerate(dialog.charges_list):
            charge = vars(charge)
            if charge is not None:
                dialog.charges_gridLayout.addWidget(QLabel(charge.get("offense")), 0, column)
                dialog.charges_gridLayout.addWidget(QLabel(charge.get("statute")), 1, column)
                dialog.charges_gridLayout.addWidget(QLabel(charge.get("finding")), 2, column)
                column += 1

    def set_license_suspension_default_date(self, dialog):
        dialog.license_suspension_date_box.setDate(QtCore.QDate.currentDate())

    def set_community_service_default_date(self, dialog):
        dialog.community_service_date_to_complete_box.setDate(QtCore.QDate.currentDate())

    def set_community_service_due_date(self, dialog, _index=None):
        days_to_complete = int(dialog.community_service_days_to_complete_box.currentText())
        dialog.community_service_date_to_complete_box.setDate(QDate.currentDate().addDays(days_to_complete))


class FineOnlyDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_plea_trial_date(dialog)
        self.set_appearance_reason(dialog)
        self.set_balance_due_date(dialog)


class JailCCDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_plea_trial_date(dialog)
        self.set_appearance_reason(dialog)
        self.set_balance_due_date(dialog)


class DiversionDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_plea_trial_date(dialog)
        self.set_appearance_reason(dialog)
        diversion_pay_days_to_add = set_future_date(97, None, 1)
        dialog.diversion_fine_pay_date_box.setDate(QDate.currentDate().addDays(diversion_pay_days_to_add))
        jail_report_days_to_add = set_future_date(97, None, 4)
        dialog.diversion_jail_report_date_box.setDate(QDate.currentDate().addDays(jail_report_days_to_add))
        dialog.show_jail_report_date_box()
        dialog.show_other_conditions_box()


class NotGuiltyBondDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_plea_trial_date(dialog)
        self.set_appearance_reason(dialog)


class AddConditionsDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_conditions_case_information_banner(dialog)
        self.set_license_suspension_default_date(dialog)
        self.set_community_service_default_date(dialog)
        self.set_community_service_due_date(dialog)
