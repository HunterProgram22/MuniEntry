import sys
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docxtpl import DocxTemplate

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)

from omnibus_motion_dialog_ui import Ui_OmnibusMotionDialog


class OmnibusMotionDialog(QDialog, Ui_OmnibusMotionDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def createEntry(self):
        doc = DocxTemplate("demo_template.docx")
        context = { 'defendant_name' : 'Justin Kudela',
                    'case_no' : '21TRD1234'
                    }
        doc.render(context)
        doc.save("Demo_actual_document.docx")
