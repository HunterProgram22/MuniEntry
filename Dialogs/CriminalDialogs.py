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
from pyuifiles.case_information_dialog_ui import Ui_CaseInformationDialog
from pyuifiles.amend_offense_dialog_ui import Ui_AmendOffenseDialog
from Dialogs.CaseInformation import (
    CaseInformation, CriminalCharge, CommunityControlTerms,
    OviDetails, AbilityToPayDetails
    )

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

    def proceed_to_sentencing(self):
        SentencingDialog(self.case_information).exec()

    def proceed_to_ovi(self):
        OviDialog(self.case_information).exec()

    def proceed_to_ability_to_pay(self):
        AbilityToPayDialog(self.case_information).exec()

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
        """This slot is tied to the signal 'pressed()', which has precedence over
        released() and clicked()."""
        self.case_information.case_number = self.case_number.text()
        self.case_information.defendant_name = self.defendant_name.text()
        self.case_information.defendant_attorney_name = self.defendant_attorney_name.text()
        self.case_information.plea_trial_date = self.plea_trial_date.date().toString("MMMM dd yyyy")
        self.case_information.case_number = self.case_number.text()
        self.case_information.defendant_name = self.defendant_name.text()
        self.case_information.defendant_attorney_name = (
            self.defendant_attorney_name.text()
        )
        if self.is_citizen_checkbox.isChecked():
            self.case_information.is_citizen = True
        if self.citizen_deportation_checkbox.isChecked():
            self.case_information.citizen_deportation = True
        if self.waived_counsel_checkbox.isChecked():
            self.case_information.waived_counsel = True


class OviDialog(BaseCriminalDialog, Ui_OviDialog):
    def __init__(self, case_information, parent=None):
        super().__init__(parent)
        self.case_information = case_information
        self.set_case_information_banner()

    def update_case_information(self):
        self.ovi_details = OviDetails()
        self.ovi_details.ovi_offenses_within_ten_years = self.ovi_offenses_within_ten_years_box.currentText()
        if self.high_bac_test_checkbox.isChecked():
            self.ovi_details.ovi_high_bac_test = True
        if self.refused_breathylizer_checkbox.isChecked():
            self.ovi_details.ovi_refused_breathylizer = True
            self.ovi_details.ovi_offenses_within_twenty_years = self.ovi_offenses_within_twenty_years_box.currentText()
        self.case_information.ovi_details = self.ovi_details

    def set_dialog(self, bool):
        if self.sender().objectName() == "refused_breathylizer_checkbox":
            if bool == True:
                self.ovi_offenses_within_twenty_years_box.setEnabled(True)
            else:
                self.ovi_offenses_within_twenty_years_box.setEnabled(False)


class AmendOffenseDialog(BaseCriminalDialog, Ui_AmendOffenseDialog):
    def __init__(self, case_information, parent=None):
        super().__init__(parent)
        self.case_information = case_information
        self.set_case_information_banner()


class AbilityToPayDialog(BaseCriminalDialog, Ui_AbilityToPayDialog):
    def __init__(self, case_information, parent=None):
        super().__init__(parent)
        self.case_information = case_information
        self.set_case_information_banner()

    def proceed_to_community_control(self):
        self.ability_to_pay_details = AbilityToPayDetails()
        if self.ability_to_pay_checkbox.isChecked():
            self.ability_to_pay_details.ability_to_pay_time = self.ability_to_pay_box.currentText()
        if self.pretrial_jail_days_credit_checkbox.isChecked():
            self.ability_to_pay_details.pretrial_jail_days_credit = True
        else:
            self.ability_to_pay_details.pretrial_jail_days_credit = False
        if self.community_service_for_fines_checkbox.isChecked():
            self.ability_to_pay_details.community_service_for_fines = True
        else:
            self.ability_to_pay_details.community_service_for_fines = False
        """Judge H and AB said fines suspended upon showing license is not used by them,
        just by KP, so maybe don't include this on UI - not currently wired up."""
        self.case_information.ability_to_pay_details = self.ability_to_pay_details
        dialog = CommunityControlDialog(self.case_information)
        dialog.exec()


class CommunityControlDialog(BaseCriminalDialog, Ui_CommunityControlDialog):
    def __init__(self, case_information, parent=None):
        super().__init__(parent)
        self.case_information = case_information
        self.set_case_information_banner()

    def add_community_control(self):
        self.community_control_terms = CommunityControlTerms()
        if self.community_control_required_checkbox.isChecked():
            self.community_control_terms.community_control_required = True
            self.community_control_terms.term_of_community_control = self.term_of_community_control_box.currentText()
            self.community_control_terms.type_of_community_control = self.type_of_community_control_box.currentText()
        else:
            self.community_control_terms.community_control_required = False
        self.case_information.community_control_terms = self.community_control_terms


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

    def amend_offense(self):
        dialog = AmendOffenseDialog(self.case_information)
        dialog.exec()
