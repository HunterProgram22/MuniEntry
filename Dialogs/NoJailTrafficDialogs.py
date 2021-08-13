import sys, os, pathlib
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docxtpl import DocxTemplate
from PyQt5.uic import loadUi

from PyQt5.QtCore import QDate, Qt, QDateTime
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QLabel

from pyuifiles.traffic_case_information_dialog_ui import Ui_TrafficCaseInformationDialog

from Dialogs.CaseInformation import CaseInformation
from Dialogs.CriminalDialogs import BaseCriminalDialog

PATH = str(pathlib.Path().absolute())
TEMPLATE_PATH = PATH + "\\Templates\\"
SAVE_PATH = PATH + "\\Saved\\"




class TrafficCaseInformationDialog(BaseCriminalDialog, Ui_TrafficCaseInformationDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.case_information = CaseInformation()
