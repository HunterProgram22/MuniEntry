import sys, os
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docxtpl import DocxTemplate
from PyQt5.uic import loadUi

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)

from omnibus_motion_dialog_ui import Ui_OmnibusMotionDialog
from jury_instructions_dialog_ui import Ui_JuryInstructionsDialog

#PATH = "C:\\Users\\Justin Kudela\\AppData\\Local\\Programs\\Python\\Python39\\MuniEntry\\"

class OmnibusMotionDialog(QDialog, Ui_OmnibusMotionDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def createEntry(self):
        doc = DocxTemplate("demo_template.docx")
        defendantName = self.DefendantName_lineEdit.text()
        caseNo = self.CaseNo_lineEdit.text()
        context = { 'defendant_name' : defendantName,
                    'case_no' : caseNo
                    }
        doc.render(context)
        doc.save("Demo_actual_document.docx")
        os.startfile("Demo_actual_document.docx")


class JuryInstructionsDialog(QDialog, Ui_JuryInstructionsDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def createEntry(self):
        doc = DocxTemplate("JuryInstructionsMaster.docx")
        defendantName = self.DefendantName_lineEdit.text()
        caseNo = self.CaseNo_lineEdit.text()
        firstCharge = self.firstCharge_comboBox.currentText()
        secondCharge = self.secondCharge_comboBox.currentText()
        context = { 'defendant_name' : defendantName,
                    'case_no' : caseNo,
                    'first_charge' : firstCharge,
                    'second_charge' : secondCharge,
                    }
        doc.render(context)
        doc.save("Jury_Instructions_Test.docx")
        os.startfile("Jury_Instructions_Test.docx")
