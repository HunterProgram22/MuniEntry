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
from HelperFunctions import getText

PATH = "C:\\Users\\Justin Kudela\\appdata\\local\\programs\\python\\python39\\MuniEntry\\"

class OmnibusMotionDialog(QDialog, Ui_OmnibusMotionDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def createEntry(self):
        doc = DocxTemplate("Templates/demo_template.docx")
        defendantName = self.DefendantName_lineEdit.text()
        caseNo = self.CaseNo_lineEdit.text()
        context = { 'defendant_name' : defendantName,
                    'case_no' : caseNo
                    }
        doc.render(context)
        doc.save("Saved/Demo_actual_document.docx")
        #Need to us os to get system Path
        os.startfile(PATH + "Saved/Demo_actual_document.docx")


class JuryInstructionsDialog(QDialog, Ui_JuryInstructionsDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def createEntry(self):
        context = self.getDialogFields()
        doc = DocxTemplate("Templates/JuryInstructionsMaster.docx")
        doc.render(context)
        for para in doc.paragraphs:
            para.alignment = WD_ALIGN_PARAGRAPH.LEFT
        doc.save("Saved/Jury_Instructions_Test.docx")
        #Need to us os to get system Path
        os.startfile(PATH + "Saved/Jury_Instructions_Test.docx")

    def getDialogFields(self):
        defendantName = self.DefendantName_lineEdit.text()
        caseNo = self.CaseNo_lineEdit.text()
        firstCharge = self.firstCharge_comboBox.currentText()
        secondCharge = self.secondCharge_comboBox.currentText()
        self.populateInstructions("Templates/OVI_Instructions_Template.docx")
        countOneInstructions = getText("Saved/Populated_Jury_Instructions.docx")
        context = { 'defendant_name' : defendantName,
                    'case_no' : caseNo,
                    'first_charge' : firstCharge,
                    'second_charge' : secondCharge,
                    'count_one_instructions' : countOneInstructions,
                    }
        return context

    def populateInstructions(self, instructions):
        defendantName = self.DefendantName_lineEdit.text()
        context = { 'defendant_name' : defendantName,
                    }
        doc = DocxTemplate(instructions)
        doc.render(context)
        doc.save("Saved/Populated_Jury_Instructions.docx")
