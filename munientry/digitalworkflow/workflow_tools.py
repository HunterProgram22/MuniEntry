"""Module for PDF Viewers and tools used by Viewers."""
import os
import webbrowser

import fitz
from loguru import logger
from PyQt6 import QtGui, QtPrintSupport
from PyQt6.QtCore import QUrl
# from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QHBoxLayout, QMainWindow, QToolBar, QToolButton

from munientry.settings import DW_APPROVED_DIR, ICON_PATH, TIMENOW


def add_approved_stamp(file):
    """Move this to a TextWriter box for centering."""
    img_rect = fitz.Rect(475, 50, 555, 130)
    img_filename = fr'{ICON_PATH}\approved_stamp.png'
    text_start_point = fitz.Point(465, 65)
    file_time = TIMENOW.toString('MMM dd, yyyy hh:mm')
    filestamp_text = \
        f'FILED\nDELAWARE\nMUNICIPAL COURT\n'\
        + f'{file_time}\nCindy Dinovo\nClerk of Court'
    document = fitz.open(file)
    page = document[0]
    page.insert_image(img_rect, filename=img_filename)
    page.insert_text(text_start_point, filestamp_text, color=(0.7, 0.0, 0.1))
    document.save(f'{DW_APPROVED_DIR}/Test.pdf')
    document.close()


class ToolButton(QToolButton):
    """Custom tool button for PDF Viewers."""

    def __init__(self, button_text, button_color, slot_function, parent=None):
        super().__init__(parent)
        self.button_text = button_text
        self.button_color = button_color
        self.slot_function = slot_function
        self._set_up_button()

    def _set_up_button(self):
        self.setText(self.button_text)
        self.setStyleSheet(f'background-color: {self.button_color}; padding: 10px;')
        self.setFixedSize(150, 50)
        self.clicked.connect(self.slot_function)


class BasePdfViewer(QMainWindow):

    def __init__(self, document, entry_widget, widget_list, dialog, parent=None):
        super().__init__(parent)
        self.document = document
        self.entry_widget = entry_widget
        self.widget_list = widget_list
        self.dialog = dialog
        # self.initUI()
        self.add_viewer_buttons()
        self.show()

    def initUI(self):
        self.toolBar = QToolBar(self)
        self.toolBar.setStyleSheet('spacing: 10px; padding: 10px;')
        self.addToolBar(self.toolBar)

        # self.webEngineView = QWebEngineView(self)
        # settings = self.webEngineView.settings()
        # settings.setAttribute(settings.WebAttribute.PluginsEnabled, True)
        # settings.setAttribute(settings.WebAttribute.PdfViewerEnabled, True)
        # self.setCentralWidget(self.webEngineView)
        #
        # self.setGeometry(600, 600, 1000, 800)
        # self.setWindowTitle('Digital Workflow Viewer')
        # self.setWindowIcon(QtGui.QIcon(f'{ICON_PATH}gavel.ico'))

        # self.webEngineView.load(QUrl.fromLocalFile(self.document))

    def print_entry(self):
        webbrowser.open_new(self.document)

class PdfViewer(BasePdfViewer):

    def __init__(self, document, entry_widget, dialog, parent=None):
        super().__init__(document, entry_widget, dialog, parent)

    def add_viewer_buttons(self):
        self.reject_Button = ToolButton('REJECT', 'red', self.reject_entry)
        self.toolBar.addWidget(self.reject_Button)

        self.print_Button = ToolButton('OPEN TO PRINT', 'gray', self.print_entry)
        self.toolBar.addWidget(self.print_Button)

        self.approve_Button = ToolButton('APPROVE', 'green', self.approve_entry)
        self.toolBar.addWidget(self.approve_Button)

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


class MattoxPdfViewer(BasePdfViewer):

    def __init__(self, document, entry_widget, widget_list, dialog, parent=None):
        super().__init__(document, entry_widget, widget_list, dialog, parent)

    def add_viewer_buttons(self):
        self.print_Button = ToolButton('OPEN TO PRINT', 'gray', self.print_entry)
        self.toolBar.addWidget(self.print_Button)

        self.complete_Button = ToolButton('COMPLETE', 'green', self.complete_entry)
        self.toolBar.addWidget(self.complete_Button)

    def complete_entry(self):
        row = self.widget_list.row(self.entry_widget)
        self.widget_list.takeItem(row)
        os.remove(self.document)
        self.close()
