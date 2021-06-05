import sys, os
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docxtpl import DocxTemplate
from PyQt5.uic import loadUi

from PyQt5.QtCore import QDate, Qt, QDateTime
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
    )

from pyuifiles.ovi_entry_dialog_ui import Ui_OviEntryDialog
from pyuifiles.sentencing_entry_dialog_ui import Ui_SentencingDialog
from pyuifiles.failure_to_appear_dialog_ui import Ui_FailureToAppearDialog

#Home Paths
PATH = "C:\\Users\\Justin Kudela\\appdata\\local\\programs\\python\\python39\\MuniEntry\\"
TEMPLATE_PATH = "C:\\Users\\Justin Kudela\\appdata\\local\\programs\\python\\python39\\MuniEntry\\"
SAVE_PATH = "C:\\Users\\Justin Kudela\\appdata\\local\\programs\\python\\python39\\MuniEntry\\Saved\\"

#Work Paths
#PATH = "C:\\Users\\jkudela\\AppData\\Local\\Programs\\Python\\Python39\\MuniEntry\\"
#TEMPLATE_PATH = "C:\\Users\\jkudela\\appdata\\local\\programs\\python\\python39\\MuniEntry\\Templates\\"


class BaseDialog(QDialog):
    """Base class that creates all the methods commonly used by all
    dialogs for forms. The template for each form is a class variable
    for that specific class used for each dialog."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.template = self.__class__.template
        self.template_name = self.__class__.template_name
        self.setupUi(self)

    def createEntry(self):
        self.fields_dict = self.getDialogFields()
        doc = DocxTemplate(self.getTemplate())
        doc.render(self.fields_dict)
        for para in doc.paragraphs:
            para.alignment = WD_ALIGN_PARAGRAPH.LEFT
        self.docname = self.fields_dict['case_no'] + '_' + self.template_name + '.docx'
        doc.save(SAVE_PATH + self.docname)
        #Need to use OS to get system Path
        os.startfile(SAVE_PATH + self.docname)

    def getDialogFields(self):
        defendant_name = self.defendant_name.text()
        case_no = self.case_no.text()
        try:
            defendant_address = self.defendant_address.text()
            defendant_city = self.defendant_city.text()
            defendant_state = self.defendant_state.currentText()
            defendant_zipcode = self.defendant_zipcode.text()
        except AttributeError:
            """This may need to be modified to address if user leaves fields
            blank but the data is required."""
            defendant_address = None
            defendant_city = None
            defendant_state = None
            defendant_zipcode = None
        self.fields_dict = {
            'defendant_name' : defendant_name,
            'case_no' : case_no,
            'defendant_address' : defendant_address,
            'defendant_city' : defendant_city,
            'defendant_state' : defendant_state,
            'defendant_zipcode' : defendant_zipcode,
            }
        return self.fields_dict

    def getTemplate(self):
        return self.template

    def proceedToSentencing(self):
        dialog = SentencingDialog()
        dialog.exec()


class OviEntryDialog(BaseDialog, Ui_OviEntryDialog):
    template = "Templates/Ovi_Entry.docx"
    template_name = "Ovi_Entry"

    def __init__(self, parent=None):
        super().__init__(parent)

    def setDialog(self, bool):
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


class SentencingDialog(BaseDialog, Ui_SentencingDialog):
    template = "Templates/Sentencing_Entry.docx"
    template_name = "Sentencing_Entry"

    def __init__(self, parent=None):
        super().__init__(parent)


class FailureToAppearDialog(BaseDialog, Ui_FailureToAppearDialog):
    template = "Templates/Failure_To_Appear_Entry.docx"
    template_name = "Failure_To_Appear_Entry"

    def __init__(self, parent=None):
        super().__init__(parent)
