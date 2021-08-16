import sys, pathlib
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets

PATH = str(pathlib.Path().absolute())


def create_offense_list():
    conn = sqlite3.connect(PATH + "\\charges.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT offense, statute FROM charges")
    offense_list = cursor.fetchall()
    clean_offense_list = []
    clean_statute_list = []
    for i in offense_list:
        clean_offense_list.append(i[0])
        clean_statute_list.append(i[1])
    conn.close()
    return clean_offense_list, clean_statute_list


def get_dialog_fields(self):
    self.fields_dict = {
        "defendant_name": self.defendant_name.text(),
        "case_no": self.case_no.text(),
        "defendant_address": defendant_address,
        "defendant_city": defendant_city,
        "defendant_state": defendant_state,
        "defendant_zipcode": defendant_zipcode,
    }
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

    return self.fields_dict


class FailureToAppearDialog(BaseCriminalDialog, Ui_FailureToAppearDialog):
    template = TEMPLATE_PATH + "Failure_To_Appear_Entry.docx"
    template_name = "Failure_To_Appear_Entry"

    def __init__(self, parent=None):
        super().__init__(parent)


class TransferEntryDialog(BaseDialog, Ui_TransferEntryDialog):
    template = TEMPLATE_PATH + "Transfer_Judgment_Entry.docx"
    template_name = "Transfer_Entry"

    def __init__(self, parent=None):
        super().__init__(parent)

    def get_dialog_fields(self):
        super(TransferEntryDialog, self).get_dialog_fields()
        self.fields_dict["assigned_date"] = self.assigned_date.date().toString(
            "MMMM d, yyyy"
        )
        self.fields_dict["assigned_judge"] = self.assigned_judge.currentText()
        self.fields_dict["transferred_judge"] = self.transferred_judge.currentText()
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

    def set_dialog(self, bool):
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

    def get_dialog_fields(self):
        """This gets the data and populates fields even if the box for the item
        is not checked. Need to fix to ignore date if box not checked."""
        super(YellowFormDialog, self).get_dialog_fields()
        self.fields_dict["case_set_date"] = self.case_set_date.date().toString(
            "MMMM d, yyyy"
        )
        self.fields_dict["case_set_time"] = self.case_set_time.time().toString(
            "h:mm AP"
        )
        self.fields_dict[
            "case_set_for_choices"
        ] = self.case_set_for_choices.currentText()
        return self.fields_dict


class MotionEntryDialog(BaseDialog, Ui_MotionEntryDialog):
    template = TEMPLATE_PATH + "Motion_Judgment_Entry.docx"
    template_name = "Motion_Form"

    def __init__(self, parent=None):
        super().__init__(parent)

    def get_dialog_fields(self):
        super(MotionEntryDialog, self).get_dialog_fields()
        self.fields_dict["motion_filed_date"] = self.motion_filed_date.date().toString(
            "MMMM d, yyyy"
        )
        self.fields_dict["motion_filed_by"] = self.motion_filed_by.currentText()
        self.fields_dict["motion_description"] = self.motion_description.toPlainText()
        self.fields_dict["motion_decision"] = self.motion_decision.currentText()
        self.fields_dict["assigned_judge"] = self.assigned_judge.currentText()
        return self.fields_dict


class BaseDialog(QDialog):
    """Base class that creates all the methods commonly used by all
    dialogs for forms. The template for each form is a class variable
    for that specific class used for each dialog."""

    template = None
    template_name = None

    def __init__(self, parent=None):
        """TODO: Need to set default to None for templates and template names."""
        super().__init__(parent)
        self.template = self.__class__.template
        self.template_name = self.__class__.template_name
        self.setupUi(self)

    def align_entry_left(self):
        for para in self.doc.paragraphs:
            para.alignment = WD_ALIGN_PARAGRAPH.LEFT

    def create_entry(self):
        self.fields_dict = self.get_dialog_fields()
        self.doc = DocxTemplate(self.get_template())
        self.doc.render(self.fields_dict)
        self.align_entry_left()
        self.set_document_name()
        self.doc.save(SAVE_PATH + self.docname)
        os.startfile(SAVE_PATH + self.docname)

    def set_document_name(self):
        self.docname = self.fields_dict["case_no"] + "_" + self.template_name + ".docx"

    def get_dialog_fields(self):
        self.fields_dict = {
            "defendant_name": self.defendant_name.text(),
            "case_number": self.case_number.text(),
            "defendant_attorney_name": self.defendant_attorney_name.text(),
        }
        return self.fields_dict

    def get_template(self):
        return self.template


self.offense_1 = None
self.plea_1 = None
self.finding_1 = None
self.fines_1 = None
self.fines_suspended_1 = None
self.jail_days_1 = None
self.jail_days_suspended_1 = None
self.offense_2 = None
self.plea_2 = None
self.finding_2 = None
self.fines_2 = None
self.fines_suspended_2 = None
self.jail_days_2 = None
self.jail_days_suspended_2 = None
self.offense_3 = None
self.plea_3 = None
self.finding_3 = None
self.fines_3 = None
self.fines_suspended_3 = None
self.jail_days_3 = None
self.jail_days_suspended_3 = None
