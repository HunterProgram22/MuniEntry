"""Module for custom table widgets used for reports.

**muninetry.widgets.table_widgets**

If using QtDesigner for creation of the Ui file you must promote the widget to one of the custom
widgets that is used. The header file for this module must then be added in QtDesigner so that
when the file is converted using 'pyuic6 -o {python_view_file.py} {qt_ui_file.ui}' this
module will be imported as part of the python_view_file.py.

Classes:

    ReportWindow(QWidget)

    ReportTable(QTableWidget)

"""
from loguru import logger
from PyQt6 import QtGui, QtPrintSupport
from PyQt6.QtWidgets import (
    QAbstractScrollArea,
    QGridLayout,
    QHeaderView,
    QPushButton,
    QSizePolicy,
    QTableWidget,
    QWidget,
)

from munientry.appsettings.paths import ICON_PATH


class ReportTable(QTableWidget):
    def __init__(self, rows, cols, title, parent=None):
        super().__init__(rows, cols, parent)
        self.title = title
        self.set_up_widget()
        logger.info(self.title)

    def set_up_widget(self):
        self.setWindowIcon(QtGui.QIcon(ICON_PATH + 'gavel.ico'))
        self.setWindowTitle(self.title)
        self.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.header = self.horizontalHeader()
        self.header.setStretchLastSection(True)
        self.header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.setSortingEnabled(False)
        self.setAlternatingRowColors(True)
        self.resize(1000, 800)


class ReportWindow(QWidget):
    """A Window object separate from the MainWindow used for displaying reports.

    Args:
        report_name (str): The name of the report shown in the window.

    Attrs:
        report_name (str): The name of the report shown in the window.
    """

    def __init__(self, report_name):
        super().__init__()
        self.report_name = report_name
        self.setWindowTitle(self.tr(self.report_name))
        self.setWindowIcon(QtGui.QIcon(ICON_PATH + 'gavel.ico'))


class TableReportWindow(ReportWindow):
    """A Window object separate from the MainWindow used for displaying reports with tables.

    Args:
        report_name (str): The name of the report shown in the window.

    Attrs:
        report_name (str): The name of the report shown in the window.
    """

    def __init__(self, report_name):
        super().__init__(report_name)
        self.table = None
        self.print_button = QPushButton('Print', self)
        self.print_button.clicked.connect(self.handle_print)
        self.preview_button = QPushButton('Preview', self)
        self.preview_button.clicked.connect(self.handle_preview)
        self.copy_button = QPushButton('Copy', self)
        self.copy_button.clicked.connect(self.handle_copy)
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.print_button, 1, 0)
        self.layout.addWidget(self.preview_button, 1, 1)
        self.layout.addWidget(self.copy_button, 1, 2)
        self.resize(1000, 800)

    def add_table(self, rows: int, cols: int, report_name: str, parent: object) -> ReportTable:
        table = ReportTable(rows, cols, report_name, parent)
        self.layout.addWidget(table, 0, 0, 1, 3)
        return table

    def handle_copy(self):
        self.clipboard = QtGui.QGuiApplication.clipboard()
        selected = self.table.selectedRanges()
        copied_text = ''
        for row in range(selected[0].topRow(), selected[0].bottomRow() + 1):
            for col in range(selected[0].leftColumn(), selected[0].rightColumn() + 1):
                try:
                    copied_text += str(self.table.item(row, col).text()) + "\t"
                except AttributeError:
                    copied_text += "\t"
            copied_text = copied_text[:-1] + "\n"  # eliminate last '\t'
        logger.info(copied_text)
        self.clipboard.setText(copied_text)

    def handle_print(self):
        printer = QtPrintSupport.QPrinter()
        dialog = QtPrintSupport.QPrintDialog(printer)
        if dialog.exec() == 1:
            self.handle_paint_request(dialog.printer())

    def handle_preview(self):
        dialog = QtPrintSupport.QPrintPreviewDialog()
        dialog.setWindowIcon(QtGui.QIcon(ICON_PATH + 'gavel.ico'))
        dialog.resize(1000, 800)
        dialog.paintRequested.connect(self.handle_paint_request)
        dialog.exec()

    def handle_paint_request(self, printer):
        document = QtGui.QTextDocument()
        cursor = QtGui.QTextCursor(document)
        h1_style = '{text-align: center; font-family: "Palatino Linotype", Palatino, serif;}'
        title = cursor.insertHtml(f'''
            <style>
                h1 {h1_style}
            </style>
            <h1>DELAWARE MUNICIPAL COURT</h1>
            <br>
            <h3>{self.report_name}</h3>
           <hr> 
            ''')
        if self.table.rowCount() > 0:
            table = cursor.insertTable(self.table.rowCount(), self.table.columnCount())
            for row in range(table.rows()):
                for col in range(table.columns()):
                    cursor.insertText(self.table.item(row, col).text())
                    cursor.movePosition(QtGui.QTextCursor.MoveOperation.NextCell)
        document.print(printer)
