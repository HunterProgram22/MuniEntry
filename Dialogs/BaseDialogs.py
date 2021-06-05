import sys, os, pathlib
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docxtpl import DocxTemplate
from PyQt5.uic import loadUi

from PyQt5.QtCore import QDate, Qt, QDateTime
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
    )

from pyuifiles.motion_entry_dialog_ui import Ui_MotionEntryDialog
from pyuifiles.transfer_entry_dialog_ui import Ui_TransferEntryDialog
from pyuifiles.verdict_form_dialog_ui import Ui_VerdictFormDialog
from pyuifiles.yellow_form_dialog_ui import Ui_YellowFormDialog

from HelperFunctions import getText

PATH = str(pathlib.Path().absolute())
TEMPLATE_PATH = PATH + "\\Templates\\"
SAVE_PATH = PATH + "\\Saved\\"


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
        self.doc = DocxTemplate(self.getTemplate())
        self.doc.render(self.fields_dict)
        for para in self.doc.paragraphs:
            para.alignment = WD_ALIGN_PARAGRAPH.LEFT
        self.docname = self.fields_dict['case_no'] + '_' + self.template_name + '.docx'
        self.doc.save(SAVE_PATH + self.docname)
        #Need to us os to get system Path
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

class TransferEntryDialog(BaseDialog, Ui_TransferEntryDialog):
    template = TEMPLATE_PATH + "Transfer_Judgment_Entry.docx"
    template_name = "Transfer_Entry"

    def __init__(self, parent=None):
        super().__init__(parent)

    def getDialogFields(self):
        super(TransferEntryDialog, self).getDialogFields()
        self.fields_dict['assigned_date'] = self.assigned_date.date().toString('MMMM d, yyyy')
        self.fields_dict['assigned_judge'] = self.assigned_judge.currentText()
        self.fields_dict['transferred_judge'] = self.transferred_judge.currentText()
        return self.fields_dict


class VerdictFormDialog(BaseDialog, Ui_VerdictFormDialog):
    template = TEMPLATE_PATH + "Verdict_Form.docx"
    template_name = "Verdict_Form"

    def __init__(self, parent=None):
        super().__init__(parent)


class YellowFormDialog(BaseDialog, Ui_YellowFormDialog):
    template = TEMPLATE_PATH + "Yellow_Form.docx"
    template_name = "Yellow_Form"

    def __init__(self, parent=None):
        super().__init__(parent)

    def setDialog(self, bool):
        if self.sender().objectName() == "set_hearing_checkbox":
            if bool == True:
                self.case_set_date.setEnabled(True)
                self.case_set_time.setEnabled(True)
                self.case_set_for_choices.setEnabled(True)
                self.hearing_date_label.setEnabled(True)
                self.hearing_time_label.setEnabled(True)
            else:
                self.case_set_date.setEnabled(False)
                self.case_set_time.setEnabled(False)
                self.case_set_for_choices.setEnabled(False)
                self.hearing_date_label.setEnabled(False)
                self.hearing_time_label.setEnabled(False)
        if self.sender().objectName() == "extradition_checkbox":
            if bool == True:
                self.extradition_choices.setEnabled(True)
            else:
                self.extradition_choices.setEnabled(False)
        if self.sender().objectName() == "case_dismissed_checkbox":
            if bool == True:
                self.dismissed_choices.setEnabled(True)
            else:
                self.dismissed_choices.setEnabled(False)
        if self.sender().objectName() == "plea_pending_checkbox":
            if bool == True:
                self.plea_pending_choices.setEnabled(True)
            else:
                self.plea_pending_choices.setEnabled(False)

    def getDialogFields(self):
        """This gets the data and populates fields even if the box for the item
        is not checked. Need to fix to ignore date if box not checked."""
        super(YellowFormDialog, self).getDialogFields()
        self.fields_dict['case_set_date'] = self.case_set_date.date().toString('MMMM d, yyyy')
        self.fields_dict['case_set_time'] = self.case_set_time.time().toString('h:mm AP')
        self.fields_dict['case_set_for_choices'] = self.case_set_for_choices.currentText()
        return self.fields_dict


class MotionEntryDialog(BaseDialog, Ui_MotionEntryDialog):
    template = TEMPLATE_PATH + "Motion_Judgment_Entry.docx"
    template_name = "Motion_Form"

    def __init__(self, parent=None):
        super().__init__(parent)

    def getDialogFields(self):
        super(MotionEntryDialog, self).getDialogFields()
        self.fields_dict['motion_filed_date'] = self.motion_filed_date.date().toString('MMMM d, yyyy')
        self.fields_dict['motion_filed_by'] = self.motion_filed_by.currentText()
        self.fields_dict['motion_description'] = self.motion_description.toPlainText()
        self.fields_dict['motion_decision'] = self.motion_decision.currentText()
        self.fields_dict['assigned_judge'] = self.assigned_judge.currentText()
        return self.fields_dict
