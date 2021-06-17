import sys, os
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docxtpl import DocxTemplate
from PyQt5.uic import loadUi

from PyQt5.QtCore import QDate, Qt, QDateTime
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox

from Dialogs.BaseDialogs import BaseDialog, PATH, TEMPLATE_PATH, SAVE_PATH

from pyuifiles.ovi_dialog_ui import Ui_OviDialog
from pyuifiles.sentencing_entry_dialog_ui import Ui_SentencingDialog
from pyuifiles.ability_to_pay_dialog_ui import Ui_AbilityToPayDialog
from pyuifiles.failure_to_appear_dialog_ui import Ui_FailureToAppearDialog
from pyuifiles.case_information_ui import Ui_CaseInformationDialog


class BaseCriminalDialog(BaseDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

    def proceed_to_sentencing(self):
        dialog = SentencingDialog(self.fields_dict)
        dialog.exec()

    def proceed_to_ability_to_pay(self):
        dialog = AbilityToPayDialog(self.fields_dict, self.sentencing_dict)
        dialog.exec()

    def close_window(self):
        self.close()


class CaseInformationDialog(BaseCriminalDialog, Ui_CaseInformationDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

    def set_dialog(self, bool):
        if self.sender().objectName() == "waived_counsel_checkbox":
            if bool == True:
                self.counsel_name.setEnabled(False)
            else:
                self.counsel_name.setEnabled(True)

    def continue_dialog(self):
        self.fields_dict = self.get_dialog_fields()
        if self.ovi_checkbox.isChecked():
            dialog = OviDialog(self.fields_dict)
            dialog.exec()
        else:
            self.proceed_to_sentencing()


class OviDialog(BaseCriminalDialog, Ui_OviDialog):
    def __init__(self, fields_dict, parent=None):
        super().__init__(parent)
        self.fields_dict = fields_dict
        self.defendant_name_label.setText(self.fields_dict.get("defendant_name"))
        self.case_number_label.setText(self.fields_dict.get("case_number"))
        self.counsel_name_label.setText(
            "Attorney: " + self.fields_dict.get("counsel_name")
        )

    def set_dialog(self, bool):
        if self.sender().objectName() == "refused_checkbox":
            if bool == True:
                self.ovi_in_20_years.setEnabled(True)
            else:
                self.ovi_in_20_years.setEnabled(False)


class AbilityToPayDialog(BaseCriminalDialog, Ui_AbilityToPayDialog):
    def __init__(self, fields_dict, sentencing_dict, parent=None):
        super().__init__(parent)
        self.fields_dict = fields_dict
        self.sentencing_dict = sentencing_dict
        self.defendant_name_label.setText(self.fields_dict.get("defendant_name"))
        self.case_number_label.setText(self.fields_dict.get("case_number"))
        self.counsel_name_label.setText(
            "Attorney: " + self.fields_dict.get("counsel_name")
        )
        self.entry_name_label.setText(SentencingDialog.template_name)
        self.offense_1.setText(self.sentencing_dict["offense_1"])


class SentencingDialog(BaseCriminalDialog, Ui_SentencingDialog):
    def __init__(self, fields_dict, parent=None):
        super().__init__(parent)
        self.fields_dict = fields_dict
        self.defendant_name_label.setText(self.fields_dict.get("defendant_name"))
        self.case_number_label.setText(self.fields_dict.get("case_number"))
        self.counsel_name_label.setText(
            "Attorney: " + self.fields_dict.get("counsel_name")
        )
        self.offense_count = 1
        self.sentencing_dict = {
            "offense_1": self.offense_1,
            "plea_1": self.plea_1,
            "finding_1": self.finding_1,
            "fines_1": self.fines_1,
            "fines_suspended_1": self.fines_suspended_1,
            "jail_days_1": self.jail_days_1,
            "jail_days_suspended_1": self.jail_days_suspended_1,
            "offense_2": self.offense_2,
            "plea_2": self.plea_2,
            "finding_2": self.finding_2,
            "fines_2": self.fines_2,
            "fines_suspended_2": self.fines_suspended_2,
            "jail_days_2": self.jail_days_2,
            "jail_days_suspended_2": self.jail_days_suspended_2,
            "offense_3": self.offense_3,
            "plea_3": self.plea_3,
            "finding_3": self.finding_3,
            "fines_3": self.fines_3,
            "fines_suspended_3": self.fines_suspended_3,
            "jail_days_3": self.jail_days_3,
            "jail_days_suspended_3": self.jail_days_suspended_3,
        }

    def add_offense(self):
        """Need to add an error message or address what happens when more than
        4 offenses are added in a case."""
        offense = "offense_" + str(self.offense_count)
        plea = "plea_" + str(self.offense_count)
        finding = "finding_" + str(self.offense_count)
        fines = "fines_" + str(self.offense_count)
        fines_suspended = "fines_suspended_" + str(self.offense_count)
        jail_days = "jail_days_" + str(self.offense_count)
        jail_days_suspended = "jail_days_suspended_" + str(self.offense_count)
        self.sentencing_dict[offense].setText(self.offense_choice_box.currentText())
        self.sentencing_dict[plea].setText(self.plea_choice_box.currentText())
        self.sentencing_dict[finding].setText(self.finding_choice_box.currentText())
        self.sentencing_dict[fines].setText(self.fine_amount.text())
        self.sentencing_dict[fines_suspended].setText(self.fines_suspended.text())
        self.sentencing_dict[jail_days].setText(self.jail_days.text())
        self.sentencing_dict[jail_days_suspended].setText(
            self.jail_days_suspended.text()
        )
        self.offense_count += 1


class FailureToAppearDialog(BaseCriminalDialog, Ui_FailureToAppearDialog):
    template = TEMPLATE_PATH + "Failure_To_Appear_Entry.docx"
    template_name = "Failure_To_Appear_Entry"

    def __init__(self, parent=None):
        super().__init__(parent)
