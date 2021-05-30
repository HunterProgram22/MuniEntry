import sys, os
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docxtpl import DocxTemplate
from PyQt5.uic import loadUi

from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)

from omnibus_motion_dialog_ui import Ui_OmnibusMotionDialog
from jury_instructions_dialog_ui import Ui_JuryInstructionsDialog
from transfer_entry_dialog_ui import Ui_TransferEntryDialog
from verdict_form_dialog_ui import Ui_VerdictFormDialog
from HelperFunctions import getText

#Home Paths
PATH = "C:\\Users\\Justin Kudela\\appdata\\local\\programs\\python\\python39\\MuniEntry\\"
TEMPLATE_PATH = "C:\\Users\\Justin Kudela\\appdata\\local\\programs\\python\\python39\\MuniEntry\\"
SAVE_PATH = "C:\\Users\\Justin Kudela\\appdata\\local\\programs\\python\\python39\\MuniEntry\\Saved\\"

#Work Paths
#PATH = "C:\\Users\\jkudela\\AppData\\Local\\Programs\\Python\\Python39\\MuniEntry\\"
#TEMPLATE_PATH = "C:\\Users\\jkudela\\appdata\\local\\programs\\python\\python39\\MuniEntry\\Templates\\"

JURY_INSTRUCTIONS_TEMPLATE = TEMPLATE_PATH + "JuryInstructionsMaster.docx"
JURY_INSTRUCTIONS_SAVED_DOC = PATH + "Saved/Jury_Instructions_Test.docx"

class BaseDialog(QDialog):
    """Base class that creates all the methods commonly used by all
    dialogs for forms. The template for each form is a class variable
    for that specific class used for each dialog."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.template = self.__class__.template
        self.template_name = self.__class__.template_name
        self.setupUi(self)

    def getTemplate(self):
        return self.template

    def createEntry(self):
        self.fields_dict = self.getDialogFields()
        doc = DocxTemplate(self.getTemplate())
        doc.render(self.fields_dict)
        for para in doc.paragraphs:
            para.alignment = WD_ALIGN_PARAGRAPH.LEFT
        self.docname = self.fields_dict['case_no'] + '_' + self.template_name + '.docx'
        doc.save(SAVE_PATH + self.docname)
        #Need to us os to get system Path
        os.startfile(SAVE_PATH + self.docname)

    def getDialogFields(self):
        defendant_name = self.defendant_name.text()
        case_no = self.case_no.text()
        defendant_address = self.defendant_address.text()
        defendant_city = self.defendant_city.text()
        defendant_state = self.defendant_state.currentText()
        defendant_zipcode = self.defendant_zipcode.text()
        self.fields_dict = {
            'defendant_name' : defendant_name,
            'case_no' : case_no,
            'defendant_address' : defendant_address,
            'defendant_city' : defendant_city,
            'defendant_state' : defendant_state,
            'defendant_zipcode' : defendant_zipcode,
            }
        return self.fields_dict


class TransferEntryDialog(BaseDialog, Ui_TransferEntryDialog):
    template = "Templates/Transfer_Judgment_Entry.docx"
    template_name = "Transfer_Entry"

    def __init__(self, parent=None):
        super().__init__(parent)

    def getDialogFields(self):
        super(TransferEntryDialog, self).getDialogFields()
        assigned_date = self.assigned_date.date().toString('MMMM d, yyyy')
        assigned_judge = self.assigned_judge.currentText()
        transferred_judge = self.transferred_judge.currentText()
        self.fields_dict['assigned_date'] = assigned_date
        self.fields_dict['assigned_judge'] = assigned_judge
        self.fields_dict['transferred_judge'] = transferred_judge
        return self.fields_dict


class VerdictFormDialog(BaseDialog, Ui_VerdictFormDialog):
    template = "Templates/Verdict_Form.docx"
    template_name = "Verdict_Form"

    def __init__(self, parent=None):
        super().__init__(parent)


class OmnibusMotionDialog(QDialog, Ui_OmnibusMotionDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


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
        fields_dict = { 'defendant_name' : defendant_name,
                    'case_no' : case_no,
                    'first_charge' : first_charge,
                    'second_charge' : second_charge,
                    'complaint_date' : complaint_date,
                    'count_one_instructions' : count_one_instructions,
                    }
        return fields_dict

    def populateInstructions(self, instructions):
        defendant_name = self.DefendantName_lineEdit.text()
        fields_dict = { 'defendant_name' : defendant_name,
                    }
        doc = DocxTemplate(instructions)
        doc.render(fields_dict)
        doc.save("Saved/Jury_Instructions_Test.docx")


class JuryInstructionTemplate(object):
    """A class for the specific jury instructions for each different type of charge."""

    def __init__(self, template=None):
        self.template = template
