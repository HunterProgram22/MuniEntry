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

#Home Paths
PATH = "C:\\Users\\Justin Kudela\\appdata\\local\\programs\\python\\python39\\MuniEntry\\"
TEMPLATE_PATH = "C:\\Users\\Justin Kudela\\appdata\\local\\programs\\python\\python39\\MuniEntry\\"

#Work Paths
#PATH = "C:\\Users\\jkudela\\AppData\\Local\\Programs\\Python\\Python39\\MuniEntry\\"
#TEMPLATE_PATH = "C:\\Users\\jkudela\\appdata\\local\\programs\\python\\python39\\MuniEntry\\Templates\\"



JURY_INSTRUCTIONS_TEMPLATE = TEMPLATE_PATH + "JuryInstructionsMaster.docx"
JURY_INSTRUCTIONS_SAVED_DOC = PATH + "Saved/Jury_Instructions_Test.docx"

class BaseDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def createEntry(self):
        #This needs to be refactored to be a true base class method
        context = self.getDialogFields()
        doc = DocxTemplate("Templates/JuryInstructionsMaster.docx")
        doc.render(context)
        for para in doc.paragraphs:
            para.alignment = WD_ALIGN_PARAGRAPH.LEFT
        doc.save("Saved/Jury_Instructions_Test.docx")
        #Need to us os to get system Path
        os.startfile(PATH + "Saved/Jury_Instructions_Test.docx")



class OmnibusMotionDialog(QDialog, Ui_OmnibusMotionDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def createEntry(self):
        doc = DocxTemplate("Templates/demo_template.docx")
        defendant_name = self.DefendantName_lineEdit.text()
        case_no = self.CaseNo_lineEdit.text()
        context = { 'defendant_name' : defendant_name,
                    'case_no' : case_no,
                    }
        doc.render(context)
        doc.save("Saved/Demo_actual_document.docx")
        #Need to us os to get system Path
        os.startfile(PATH + "Saved/Demo_actual_document.docx")


class JuryInstructionsDialog(BaseDialog, Ui_JuryInstructionsDialog):
    template = JURY_INSTRUCTIONS_TEMPLATE
    #saved_doc = JURY_INSTRUCTIONS_SAVED_DOC

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def getDialogFields(self):
        defendant_name = self.DefendantName_lineEdit.text()
        case_no = self.CaseNo_lineEdit.text()
        complaint_date = self.ComplaintDate_lineEdit.text()
        first_charge = self.FirstCharge_comboBox.currentText()
        second_charge = self.SecondCharge_comboBox.currentText()
        self.populateInstructions(JuryInstructionsDialog.template)
        count_one_instructions = getText("Saved/Populated_Jury_Instructions.docx")
        context = { 'defendant_name' : defendant_name,
                    'case_no' : case_no,
                    'first_charge' : first_charge,
                    'second_charge' : second_charge,
                    'complaint_date' : complaint_date,
                    'count_one_instructions' : count_one_instructions,
                    }
        return context

    def populateInstructions(self, instructions):
        defendant_name = self.DefendantName_lineEdit.text()
        context = { 'defendant_name' : defendant_name,
                    }
        doc = DocxTemplate(instructions)
        doc.render(context)
        doc.save("Saved/Jury_Instructions_Test.docx")
