import os
import shutil
import fitz

from loguru import logger
from PyQt6 import QtGui
from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineCore import QWebEngineSettings
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QMainWindow, QToolBar, QPushButton

from munientry.settings import DW_APPROVED_DIR, DW_HEMMETER, DW_ROHRER, ICON_PATH
from munientry.builders import base_builders as base


def add_approved_stamp(file):
    img_rect = fitz.Rect(55, 30, 150, 390)
    img_filename = fr'{ICON_PATH}\approved_stamp.png'
    document = fitz.open(file)
    logger.debug(document)
    page = document[0]
    logger.debug(page)
    page.insert_image(img_rect, filename=img_filename)
    document.save(f'{DW_HEMMETER}/Test.pdf')
    document.close()


class RohrerWorkflowDialog(base.BaseDialogBuilder):

    build_dict = {
        'dialog_name': 'Rohrer Digital Workflow',
        'view': None,
        'slots': None,
        'signals': None,
    }


class DigitalWorkflow(object):

    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        self.load_digital_workflow_counts()

    def load_digital_workflow_counts(self):
        hemmeter_file_count = self.get_file_count(DW_HEMMETER)
        rohrer_file_count = self.get_file_count(DW_ROHRER)
        self.mainwindow.jour_count_jh_label.setText(str(hemmeter_file_count))
        self.mainwindow.jour_count_jr_label.setText(str(rohrer_file_count))

    def get_file_count(self, directory):
        try:
            return len(os.listdir(directory))
        except FileNotFoundError as error:
            logger.warning(error)

    def open(self, entry):
        self.mainwindow.webview = self.create_pdf_view(entry)

    def create_pdf_view(self, entry):
        webview = PdfDialogView(entry)
        return webview


class PdfDialogView(QMainWindow):

    def __init__(self, document, entry_widget, dialog, parent=None):
        super().__init__(parent)
        self.document = document
        self.entry_widget = entry_widget
        self.dialog = dialog
        self.initUI()

    def initUI(self):
        self.toolBar = QToolBar(self)
        self.addToolBar(self.toolBar)

        self.reject_Button = QPushButton(self)
        self.reject_Button.setText('REJECT')
        self.reject_Button.setStyleSheet('background-color : red')
        self.reject_Button.clicked.connect(self.reject_entry)
        self.toolBar.addWidget(self.reject_Button)

        self.approve_Button = QPushButton(self)
        self.approve_Button.setText('APPROVE')
        self.approve_Button.setStyleSheet('background-color : green')
        self.approve_Button.clicked.connect(self.approve_entry)
        self.toolBar.addWidget(self.approve_Button)

        self.webEngineView = QWebEngineView(self)
        logger.debug(self.webEngineView.settings())
        settings = self.webEngineView.settings()
        settings.setAttribute(settings.WebAttribute.PluginsEnabled, True)
        settings.setAttribute(settings.WebAttribute.PdfViewerEnabled, True)
        self.setCentralWidget(self.webEngineView)

        self.setGeometry(600, 600, 1000, 800)
        self.setWindowTitle('Digital Workflow Viewer')
        self.setWindowIcon(QtGui.QIcon(f'{ICON_PATH}gavel.ico'))
        self.show()

        self.webEngineView.load(QUrl.fromLocalFile(self.document))

    def reject_entry(self):
        row = self.dialog.pending_entries_listWidget.row(self.entry_widget)
        entry = self.dialog.pending_entries_listWidget.takeItem(row)
        self.dialog.rejected_entries_listWidget.addItem(entry)
        self.close()

    def approve_entry(self):
        row = self.dialog.pending_entries_listWidget.row(self.entry_widget)
        entry = self.dialog.pending_entries_listWidget.takeItem(row)
        self.dialog.approved_entries_listWidget.addItem(entry)
        self.close()
