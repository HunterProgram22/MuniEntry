import sys, os
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docxtpl import DocxTemplate
from PyQt5.uic import loadUi

from PyQt5.QtCore import QDate, Qt, QDateTime
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
    )

from Dialogs.BaseDialogs import BaseDialog, PATH, TEMPLATE_PATH, SAVE_PATH

from pyuifiles.ovi_entry_dialog_ui import Ui_OviEntryDialog
from pyuifiles.sentencing_entry_dialog_ui import Ui_SentencingDialog
from pyuifiles.failure_to_appear_dialog_ui import Ui_FailureToAppearDialog


class BaseCriminalDialog(BaseDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

    def proceedToSentencing(self):
        dialog = SentencingDialog()
        dialog.exec()


class OviEntryDialog(BaseCriminalDialog, Ui_OviEntryDialog):
    template = TEMPLATE_PATH + "Ovi_Entry.docx"
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


class SentencingDialog(BaseCriminalDialog, Ui_SentencingDialog):
    template = TEMPLATE_PATH + "Sentencing_Entry.docx"
    template_name = "Sentencing_Entry"

    def __init__(self, parent=None):
        super().__init__(parent)


class FailureToAppearDialog(BaseCriminalDialog, Ui_FailureToAppearDialog):
    template = TEMPLATE_PATH + "Failure_To_Appear_Entry.docx"
    template_name = "Failure_To_Appear_Entry"

    def __init__(self, parent=None):
        super().__init__(parent)
