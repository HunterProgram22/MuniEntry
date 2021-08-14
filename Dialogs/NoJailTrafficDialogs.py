import pathlib
from docx import Document
from docxtpl import DocxTemplate

from PyQt5.QtWidgets import QDialog, QLabel

from pyuifiles.traffic_case_information_dialog_ui import Ui_TrafficCaseInformationDialog
from Dialogs.CaseInformation import CaseInformation, CriminalCharge
from Dialogs.CriminalDialogs import BaseCriminalDialog

PATH = str(pathlib.Path().absolute())
TEMPLATE_PATH = PATH + "\\Templates\\"
SAVE_PATH = PATH + "\\Saved\\"


class TrafficCaseInformationDialog(BaseCriminalDialog, Ui_TrafficCaseInformationDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.case_information = CaseInformation()
        self.offense_count = 0
        self.template = TEMPLATE_PATH + "No_Jail_Traffic_Template.docx"
        self.template_name = "Traffic Judgment Entry"

    def add_offense(self):
        self.criminal_charge = CriminalCharge()
        self.criminal_charge.offense = self.offense_choice_box.currentText()
        self.criminal_charge.statute = self.statute_choice_box.currentText()
        self.criminal_charge.degree = self.degree_choice_box.currentText()
        self.criminal_charge.plea = self.plea_choice_box.currentText()
        self.criminal_charge.finding = self.finding_choice_box.currentText()
        self.criminal_charge.fines_amount = self.fines_amount.text()
        self.criminal_charge.fines_suspended = self.fines_suspended.text()
        self.criminal_charge.court_costs = self.court_costs_box.currentText()
        self.case_information.add_charge(self.criminal_charge)
        """CHECK: Should I be adding the charges to case information after GUI, and make
        sure that I clean up and don't potentially have two versions - I do right now,
        need to fix. The charge is added to case information above and then to GUI."""
        self.offense_count += 1
        self.charges_gridLayout.addWidget(
            QLabel(self.criminal_charge.offense), 0, self.offense_count
        )
        self.charges_gridLayout.addWidget(
            QLabel(self.criminal_charge.statute), 1, self.offense_count
        )
        self.charges_gridLayout.addWidget(
            QLabel(self.criminal_charge.degree), 2, self.offense_count
        )
        self.charges_gridLayout.addWidget(
            QLabel(self.criminal_charge.plea), 3, self.offense_count
        )
        self.charges_gridLayout.addWidget(
            QLabel(self.criminal_charge.finding), 4, self.offense_count
        )
        self.charges_gridLayout.addWidget(
            QLabel(self.criminal_charge.fines_amount), 5, self.offense_count
        )
        self.charges_gridLayout.addWidget(
            QLabel(self.criminal_charge.fines_suspended), 6, self.offense_count
        )
        self.charges_gridLayout.addWidget(
            QLabel(self.criminal_charge.court_costs), 7, self.offense_count
        )
        self.case_information.total_charges = self.offense_count

    def update_case_information(self):
        """This slot is tied to the signal 'pressed()', which has precedence over
        released() and clicked()."""
        self.case_information.case_number = self.case_number.text()
        self.case_information.defendant_name = self.defendant_name.text()
        self.case_information.plea_trial_date = self.plea_trial_date.date().toString("MMMM dd, yyyy")
        self.case_information.ability_to_pay_time = self.ability_to_pay_box.currentText()

    def set_statute(self):
        data = {"":"",
                "Speeding - School Zone":"R.C. 4511.21(B)(1)",
                "Speeding > 25 mph":"R.C. 4511.21(B)(2)",
                "Speeding > 35 mph": "R.C. 4511.21(B)(3)",
                "Driving in Marked Lanes": "R.C. 4511.33"
                }
        key = self.offense_choice_box.currentText()
        value = data[key]
        self.statute_choice_box.setCurrentText(value)
