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
from pyuifiles.community_control_dialog_ui import Ui_CommunityControlDialog
from pyuifiles.case_information_ui import Ui_CaseInformationDialog
from Dialogs.CaseInformation import CaseInformation, CriminalCharge, CommunityControlTerms

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
        self.template = TEMPLATE_PATH + "Judgment_Entry_Green_Sheet.docx"
        self.template_name = "Judgment Entry"

    def close_window(self):
        self.close()

    def create_entry(self):
        self.doc = DocxTemplate(self.template)
        self.doc.render(self.case_information.get_case_information())
        self.align_entry_left()
        self.set_document_name()
        self.doc.save(SAVE_PATH + self.docname)
        os.startfile(SAVE_PATH + self.docname)

    def get_context(self):
        return {
            'defendant_name': self.case_information.defendant_name,
            'case_number': self.case_information.case_number,
            'plea_trial_date': self.case_information.plea_trial_date,
        }

    def align_entry_left(self):
        for para in self.doc.paragraphs:
            para.alignment = WD_ALIGN_PARAGRAPH.LEFT

    def set_document_name(self):
        self.docname = self.case_information.case_number + "_" + self.template_name + ".docx"

        self.docname = (
            self.case_information.case_number + "_" + self.template_name + ".docx"
        )

    def proceed_to_sentencing(self):
        dialog = SentencingDialog(self.case_information)
        dialog.exec()

    def proceed_to_ability_to_pay(self):
        dialog = AbilityToPayDialog(self.case_information)
        dialog.exec()

    def proceed_to_community_control(self):
        dialog = CommunityControlDialog(self.case_information)
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
        print(self.case_number.text())
        self.case_information.case_number = self.case_number.text()
        self.case_information.defendant_name = self.defendant_name.text()
        self.case_information.defendant_attorney_name = self.defendant_attorney_name.text()
        self.case_information.plea_trial_date = self.plea_trial_date.date().toString("MMMM dd yyyy")
        print(self.case_information.defendant_name)

        """This slot is tied to the signal 'pressed()', but when I switch
        this to clicked with continue_dialog() not all data passes tests. Need to figure
        out why both slots can't work properly with the same signal."""
        self.case_information.case_number = self.case_number.text()
        self.case_information.defendant_name = self.defendant_name.text()
        self.case_information.defendant_attorney_name = (
            self.defendant_attorney_name.text()
        )

    def continue_dialog(self):
        """This slot is tied to the signal 'clicked()'"""
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


class CommunityControlDialog(BaseCriminalDialog, Ui_CommunityControlDialog):
    def __init__(self, case_information, parent=None):
        super().__init__(parent)
        self.case_information = case_information
        self.set_case_information_banner()

    def add_community_control(self):
        self.community_control_terms = CommunityControlTerms()
        self.community_control_terms.term_of_community_control = self.term_of_community_control_box.currentText()
        self.case_information.add_community_control(self.community_control_terms)
        print(self.case_information.community_control_terms)



class SentencingDialog(BaseCriminalDialog, Ui_SentencingDialog):
    def __init__(self, case_information, parent=None):
        super().__init__(parent)
        self.case_information = case_information
        self.set_case_information_banner()
        self.offense_count = 0

    def add_offense(self):
        """TODO: have charge information populate onto UI.
        Perhaps switch to loadUi for dialogs to load XML then
        I can use Jinja tags in the UI display."""
        self.criminal_charge = CriminalCharge()
        self.criminal_charge.offense = self.offense_choice_box.currentText()
        self.criminal_charge.degree = self.degree_choice_box.currentText()
        self.criminal_charge.plea = self.plea_choice_box.currentText()
        self.criminal_charge.finding = self.finding_choice_box.currentText()
        self.criminal_charge.fines_amount = self.fines_amount.text()
        self.criminal_charge.fines_suspended = self.fines_suspended.text()
        self.criminal_charge.jail_days = self.jail_days.text()
        self.criminal_charge.jail_days_suspended = self.jail_days_suspended.text()
        self.case_information.add_charge(self.criminal_charge)
        #print(self.case_information.charges_list[self.offense_count].offense)
        self.offense_count += 1
