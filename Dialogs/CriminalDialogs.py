import sys, os, pathlib
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docxtpl import DocxTemplate
from PyQt5.uic import loadUi

from PyQt5.QtCore import QDate, Qt, QDateTime
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox

from pyuifiles.ovi_dialog_ui import Ui_OviDialog
from pyuifiles.sentencing_dialog_ui import Ui_SentencingDialog
from pyuifiles.ability_to_pay_dialog_ui import Ui_AbilityToPayDialog
from pyuifiles.case_information_ui import Ui_CaseInformationDialog
from Dialogs.CaseInformation import CaseInformation, CriminalCharge

from HelperFunctions import getText

PATH = str(pathlib.Path().absolute())
TEMPLATE_PATH = PATH + "\\Templates\\"
SAVE_PATH = PATH + "\\Saved\\"


class BaseCriminalDialog(QDialog):
    """This class is a base class to provide methods that are used by some or all
    class dialogs that are used in the application. This class is never instantiated
    as its own dialog, but the init contains the setup for all inherited class dialogs."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def close_window(self):
        self.close()

    def get_dialog_fields(self):
        self.fields_dict = {
            "defendant_name": self.defendant_name.text(),
            "case_number": self.case_number.text(),
            "defendant_attorney_name": self.defendant_attorney_name.text(),
        }
        return self.fields_dict

    def proceed_to_sentencing(self):
        dialog = SentencingDialog(self.case_information)
        dialog.exec()

    def proceed_to_ability_to_pay(self):
        dialog = AbilityToPayDialog(self.case_information)
        dialog.exec()

    def set_case_information_banner(self):
        self.defendant_name_label.setText(self.case_information.defendant_name)
        self.case_number_label.setText(self.case_information.case_number)
        self.defendant_attorney_name_label.setText(
            "Attorney: " + self.case_information.defendant_attorney_name
        )


class CaseInformationDialog(BaseCriminalDialog, Ui_CaseInformationDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.case_information = CaseInformation()

    def set_dialog(self, bool):
        if self.sender().objectName() == "waived_counsel_checkbox":
            if bool == True:
                self.defendant_attorney_name.setEnabled(False)
            else:
                self.defendant_attorney_name.setEnabled(True)

    def update_case_information(self):
        self.fields_dict = self.get_dialog_fields()
        self.case_information.case_number = self.fields_dict.get("case_number")
        self.case_information.defendant_name = self.fields_dict.get("defendant_name")
        self.case_information.defendant_attorney_name = self.fields_dict.get(
            "defendant_attorney_name"
        )

    def continue_dialog(self):
        if self.ovi_checkbox.isChecked():
            dialog = OviDialog(self.case_information)
            dialog.exec()
        else:
            self.proceed_to_sentencing()


class OviDialog(BaseCriminalDialog, Ui_OviDialog):
    def __init__(self, case_information, parent=None):
        super().__init__(parent)
        self.case_information = case_information
        self.set_case_information_banner()

    def set_dialog(self, bool):
        if self.sender().objectName() == "refused_checkbox":
            if bool == True:
                self.ovi_in_20_years.setEnabled(True)
            else:
                self.ovi_in_20_years.setEnabled(False)


class AbilityToPayDialog(BaseCriminalDialog, Ui_AbilityToPayDialog):
    def __init__(self, case_information, parent=None):
        super().__init__(parent)
        self.case_information = case_information
        self.set_case_information_banner()
        # self.offense_1.setText(self.sentencing_dict["offense_1"])


class SentencingDialog(BaseCriminalDialog, Ui_SentencingDialog):
    def __init__(self, case_information, parent=None):
        super().__init__(parent)
        self.case_information = case_information
        self.set_case_information_banner()
        self.offense_count = 0

    def add_offense(self):
        """TODO: make fines and fine the same throughout app and labels regardless of
        whether it should be plural or singular."""
        """TODO: have charge information populate onto UI"""
        self.case_information.add_charge(self.offense_choice_box.currentText())
        self.case_information.charges_list[
            self.offense_count
        ].plea = self.plea_choice_box.currentText()
        self.case_information.charges_list[
            self.offense_count
        ].finding = self.finding_choice_box.currentText()
        self.case_information.charges_list[
            self.offense_count
        ].fines = self.fine_amount.text()
        self.case_information.charges_list[
            self.offense_count
        ].fines_suspended = self.fines_suspended.text()
        self.case_information.charges_list[
            self.offense_count
        ].jail_days = self.jail_days.text()
        self.case_information.charges_list[
            self.offense_count
        ].jail_days_suspended = self.jail_days_suspended.text()
        self.offense_count += 1
