from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIntValidator
from loguru import logger
from package.controllers.base_dialogs import CriminalSlotFunctions
from package.controllers.helper_functions import set_future_date


class BaseDialogViewModifier(object):
    def __init__(self, dialog):
        dialog.plea_trial_date.setDate(QtCore.QDate.currentDate())
        if dialog.case_table == "final_pretrials":
            dialog.appearance_reason_box.setCurrentText("change of plea")


class DiversionDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        diversion_pay_days_to_add = set_future_date(97, None, 1)
        dialog.diversion_fine_pay_date_box.setDate(QDate.currentDate().addDays(diversion_pay_days_to_add))
        jail_report_days_to_add = set_future_date(97, None, 4)
        dialog.diversion_jail_report_date_box.setDate(QDate.currentDate().addDays(jail_report_days_to_add))
        dialog.show_jail_report_date_box()
        dialog.show_other_conditions_box()