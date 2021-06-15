import sys, os
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docxtpl import DocxTemplate
from PyQt5.uic import loadUi

from PyQt5.QtCore import QDate, Qt, QDateTime
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox

from Dialogs.BaseDialogs import BaseDialog, PATH, TEMPLATE_PATH, SAVE_PATH

from pyuifiles.ovi_entry_dialog_ui import Ui_OviDialog
from pyuifiles.sentencing_entry_dialog_ui import Ui_SentencingDialog
from pyuifiles.ability_to_pay_dialog_ui import Ui_AbilityToPayDialog
from pyuifiles.failure_to_appear_dialog_ui import Ui_FailureToAppearDialog
from pyuifiles.case_information_ui import Ui_CaseInformationDialog


class BaseCriminalDialog(BaseDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

    def proceed_to_sentencing(self):
        self.fields_dict = self.get_dialog_fields()
        dialog = SentencingDialog(self.fields_dict)
        dialog.exec()

    def proceed_to_ability_to_pay(self):
        dialog = AbilityToPayDialog(self.fields_dict)
        dialog.exec()

    def close_window(self):
        self.close()


class CaseInformationDialog(BaseCriminalDialog, Ui_CaseInformationDialog):
    template = None
    template_name = None

    def __init__(self, parent=None):
        super().__init__(parent)

    def continue_dialog(self):
        self.fields_dict = self.get_dialog_fields()
        if self.ovi_checkbox.isChecked():
            dialog = OviEntryDialog(self.fields_dict)
            dialog.exec()


class OviEntryDialog(BaseCriminalDialog, Ui_OviDialog):
    template = TEMPLATE_PATH + "Ovi_Entry.docx"
    template_name = "Ovi_Entry"

    def __init__(self, fields_dict, parent=None):
        super().__init__(parent)
        self.fields_dict = fields_dict
        self.defendant_name_label.setText(self.fields_dict.get("defendant_name"))
        self.case_number_label.setText(self.fields_dict.get("case_number"))
        self.counsel_name_label.setText(
            "Attorney: " + self.fields_dict.get("counsel_name")
        )

    def set_dialog(self, bool):
        if self.sender().objectName() == "waived_counsel_checkbox":
            if bool == True:
                self.counsel_name.setEnabled(False)
                self.ovi_in_20_years.setEnabled(True)
            else:
                self.counsel_name.setEnabled(True)
        if self.sender().objectName() == "refused_checkbox":
            if bool == True:
                self.ovi_in_20_years.setEnabled(True)
            else:
                self.ovi_in_20_years.setEnabled(False)


class AbilityToPayDialog(BaseCriminalDialog, Ui_AbilityToPayDialog):
    template = None
    template_name = None

    def __init__(self, fields_dict, parent=None):
        super().__init__(parent)
        self.fields_dict = fields_dict
        self.defendant_name_label.setText(self.fields_dict.get("defendant_name"))
        self.case_number_label.setText(self.fields_dict.get("case_number"))
        self.counsel_name_label.setText(
            "Attorney: " + self.fields_dict.get("counsel_name")
        )
        self.entry_name_label.setText(SentencingDialog.template_name)


class SentencingDialog(BaseCriminalDialog, Ui_SentencingDialog):
    template = TEMPLATE_PATH + "Sentencing_Entry.docx"
    template_name = "Sentencing_Entry"

    def __init__(self, fields_dict, parent=None):
        super().__init__(parent)
        self.fields_dict = fields_dict
        self.defendant_name_label.setText(self.fields_dict.get("defendant_name"))
        self.case_number_label.setText(self.fields_dict.get("case_number"))
        self.counsel_name_label.setText(
            "Attorney: " + self.fields_dict.get("counsel_name")
        )

    def add_offense(self):
        self.offense_label_1.setText(self.offense_choice_box.currentText())
        self.plea_label_1.setText(self.plea_choice_box.currentText())
        self.finding_label_1.setText(self.finding_choice_box.currentText())


class FailureToAppearDialog(BaseCriminalDialog, Ui_FailureToAppearDialog):
    template = TEMPLATE_PATH + "Failure_To_Appear_Entry.docx"
    template_name = "Failure_To_Appear_Entry"

    def __init__(self, parent=None):
        super().__init__(parent)
