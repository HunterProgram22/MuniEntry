"""Module that contains ViewModifier classes. ViewModifier classes are called for a dialog
after the setupUI is called. This class makes changes to the view that are outside the the specific
view file. Modifications to the view are placed in the ViewModifier class so that they don't need to
be updated each time a view file is recompiled through the pyuic5 command."""
from loguru import logger
from PyQt5 import QtCore
from PyQt5.QtCore import QDate

from package.controllers.helper_functions import set_future_date


class BaseDialogViewModifier(object):
    def __init__(self, dialog):
        dialog.plea_trial_date.setDate(QtCore.QDate.currentDate())
        if dialog.case_table == "final_pretrials":
            dialog.appearance_reason_box.setCurrentText("change of plea")


class FineOnlyDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        dialog.balance_due_date.setDate(QtCore.QDate.currentDate())


class JailCCDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        dialog.balance_due_date.setDate(QtCore.QDate.currentDate())


class DiversionDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        diversion_pay_days_to_add = set_future_date(97, None, 1)
        dialog.diversion_fine_pay_date_box.setDate(QDate.currentDate().addDays(diversion_pay_days_to_add))
        jail_report_days_to_add = set_future_date(97, None, 4)
        dialog.diversion_jail_report_date_box.setDate(QDate.currentDate().addDays(jail_report_days_to_add))
        dialog.show_jail_report_date_box()
        dialog.show_other_conditions_box()


class NotGuiltyBondDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
