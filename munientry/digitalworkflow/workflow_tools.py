import fitz
from PyQt6 import QtGui
from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QMainWindow, QToolBar, QPushButton
from loguru import logger
from munientry.settings import ICON_PATH, TIMENOW, DW_APPROVED_DIR


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


class PdfViewer(QMainWindow):

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
