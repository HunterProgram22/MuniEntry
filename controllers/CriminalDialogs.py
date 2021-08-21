import sys, os, pathlib
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docxtpl import DocxTemplate
from PyQt5.uic import loadUi

from PyQt5.QtCore import QDate, Qt, QDateTime
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QLabel

from views.ovi_dialog_ui import Ui_OviDialog
from views.sentencing_dialog_ui import Ui_SentencingDialog
from views.ability_to_pay_dialog_ui import Ui_AbilityToPayDialog
from views.community_control_dialog_ui import Ui_CommunityControlDialog
from views.case_information_dialog_ui import Ui_CaseInformationDialog

from views.amend_offense_dialog_ui import Ui_AmendOffenseDialog
from models.CaseInformation import (
    CaseInformation,
    CriminalCharge,
    CommunityControlTerms,
    OviDetails,
    AbilityToPayDetails,
    AmendOffenseDetails,
)

PATH = str(pathlib.Path().absolute())
TEMPLATE_PATH = PATH + "\\resources\\Templates\\"
SAVE_PATH = PATH + "\\resources\\Saved\\"

"""TODO: Need to add maximize and minimize buttons for controllers."""


class BaseCriminalDialog(QDialog):
    """This class is a base class to provide methods that are used by some or all
    class controllers that are used in the application. This class is never instantiated
    as its own dialog, but the init contains the setup for all inherited class controllers."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def close_window(self):
        self.close()

    def create_entry(self):
        self.doc = DocxTemplate(self.template)
        self.doc.render(self.case_information.get_case_information())
        self.set_document_name()
        self.doc.save(SAVE_PATH + self.docname)
        os.startfile(SAVE_PATH + self.docname)

    def set_document_name(self):
        self.docname = (
            self.case_information.case_number + "_" + self.template_name + ".docx"
        )

    def proceed_to_sentencing(self):
        SentencingDialog(self.case_information).exec()

    def proceed_to_ovi(self):
        OviDialog(self.case_information).exec()

    def proceed_to_ability_to_pay(self):
        AbilityToPayDialog(self.case_information).exec()

    def set_case_information_banner(self):
        self.defendant_name_label.setText(self.case_information.defendant_name)
        self.case_number_label.setText(self.case_information.case_number)
        if self.case_information.defendant_attorney_name is not None:
            self.defendant_attorney_name_label.setText(
                "Attorney: " + self.case_information.defendant_attorney_name
            )

    def set_charges_grid(self):
        """TODO: the criminal charge is a list in case information so need to
        account for that when setting charges grid to get it to work."""
        total_charges = self.case_information.total_charges
        for charge in range(total_charges):
            self.charges_gridLayout.addWidget(
                QLabel(self.case_information.criminal_charge.offense), 0, charge
            )
            self.charges_gridLayout.addWidget(
                QLabel(self.case_information.criminal_charge.plea), 1, charge
            )
            self.charges_gridLayout.addWidget(
                QLabel(self.case_information.criminal_charge.finding), 2, charge
            )
            self.charges_gridLayout.addWidget(
                QLabel(self.case_information.criminal_charge.fines_amount), 3, charge
            )
            self.charges_gridLayout.addWidget(
                QLabel(self.case_information.criminal_charge.fines_suspended), 4, charge
            )
            self.charges_gridLayout.addWidget(
                QLabel(self.case_information.criminal_charge.jail_days), 5, charge
            )
            self.charges_gridLayout.addWidget(
                QLabel(self.case_information.criminal_charge.jail_days_suspended),
                6,
                charge,
            )
            total_charges -= 1

    def update_case_information(self):
        pass


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
        self.case_information.defendant_attorney_name = (
            self.defendant_attorney_name.text()
        )
        self.case_information.plea_trial_date = self.plea_trial_date.date().toString(
            "MMMM dd, yyyy"
        )
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
        if self.understood_plea_checkbox.isChecked():
            self.case_information.understood_plea = True
        else:
            self.case_information.understood_plea = False


class OviDialog(BaseCriminalDialog, Ui_OviDialog):
    def __init__(self, case_information, parent=None):
        super().__init__(parent)
        self.case_information = case_information
        self.set_case_information_banner()

    def update_case_information(self):
        self.ovi_details = OviDetails()
        self.ovi_details.ovi_offenses_within_ten_years = (
            self.ovi_offenses_within_ten_years_box.currentText()
        )
        if self.high_bac_test_checkbox.isChecked():
            self.ovi_details.ovi_high_bac_test = True
        if self.refused_breathylizer_checkbox.isChecked():
            self.ovi_details.ovi_refused_breathylizer = True
            self.ovi_details.ovi_offenses_within_twenty_years = (
                self.ovi_offenses_within_twenty_years_box.currentText()
            )
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

    def amend_offense(self):
        self.amend_offense_details = AmendOffenseDetails()
        self.amend_offense_details.original_charge = (
            self.original_charge_box.currentText()
        )
        self.amend_offense_details.amended_charge = (
            self.amended_charge_box.currentText()
        )
        self.amend_offense_details.amending_procedure = (
            self.pursuant_to_box.currentText()
        )
        self.amend_offense_details.motion_disposition = (
            self.motion_decision_box.currentText()
        )
        self.case_information.amend_offense_details = self.amend_offense_details


class AbilityToPayDialog(BaseCriminalDialog, Ui_AbilityToPayDialog):
    def __init__(self, case_information, parent=None):
        super().__init__(parent)
        self.case_information = case_information
        self.set_case_information_banner()
        # self.set_charges_grid()

    def proceed_to_community_control(self):
        self.ability_to_pay_details = AbilityToPayDetails()
        if self.ability_to_pay_checkbox.isChecked():
            self.ability_to_pay_details.ability_to_pay_time = (
                self.ability_to_pay_box.currentText()
            )
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
        # self.set_charges_grid()

    def update_community_control(self):
        self.community_control_terms = CommunityControlTerms()
        if self.community_control_required_checkbox.isChecked():
            self.community_control_terms.community_control_required = True
            self.community_control_terms.term_of_community_control = (
                self.term_of_community_control_box.currentText()
            )
            self.community_control_terms.type_of_community_control = (
                self.type_of_community_control_box.currentText()
            )
        else:
            self.community_control_terms.community_control_required = False
        if self.not_consume_checkbox.isChecked():
            self.community_control_terms.not_consume = True
        if self.not_refuse_checkbox.isChecked():
            self.community_control_terms.not_refuse = True
        self.case_information.community_control_terms = self.community_control_terms


class SentencingDialog(BaseCriminalDialog, Ui_SentencingDialog):
    def __init__(self, case_information, parent=None):
        super().__init__(parent)
        self.case_information = case_information
        self.set_case_information_banner()
        self.offense_count = 0

    def add_offense(self):
        """TODO: Shrink text as charges are added."""
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
        """CHECK: Should I be adding the charges to case information after GUI, and make
        sure that I clean up and don't potentially have two versions - I do right now,
        need to fix. The charge is added to case information above and then to GUI."""
        self.offense_count += 1
        self.charges_gridLayout.addWidget(
            QLabel(self.criminal_charge.offense), 0, self.offense_count
        )
        self.charges_gridLayout.addWidget(
            QLabel(self.criminal_charge.plea), 1, self.offense_count
        )
        self.charges_gridLayout.addWidget(
            QLabel(self.criminal_charge.finding), 2, self.offense_count
        )
        self.charges_gridLayout.addWidget(
            QLabel(self.criminal_charge.fines_amount), 3, self.offense_count
        )
        self.charges_gridLayout.addWidget(
            QLabel(self.criminal_charge.fines_suspended), 4, self.offense_count
        )
        self.charges_gridLayout.addWidget(
            QLabel(self.criminal_charge.jail_days), 5, self.offense_count
        )
        self.charges_gridLayout.addWidget(
            QLabel(self.criminal_charge.jail_days_suspended), 6, self.offense_count
        )
        self.case_information.total_charges = self.offense_count

    def delete_offense(self):
        """TODO: Currently this just deletes labels 'at random' but need to figure out
        how it is indexing and modify to delete last added offense."""
        self.charges_gridLayout.itemAt(self.offense_count).widget().deleteLater()

    def amend_offense(self):
        AmendOffenseDialog(self.case_information).exec()
