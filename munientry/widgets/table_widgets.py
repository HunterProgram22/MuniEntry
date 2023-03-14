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
from collections import namedtuple

from loguru import logger
from PyQt6 import QtGui, QtPrintSupport
from PyQt6.QtWidgets import (
    QAbstractScrollArea,
    QGridLayout,
    QHeaderView,
    QPushButton,
    QSizePolicy,
    QTableWidget,
    QWidget, )

from munientry.appsettings.paths import GAVEL_PATH
from munientry.widgets.message_boxes import RequiredBox

TABLE_HEIGHT = 1000
TABLE_WIDTH = 800
WINDOW_HEIGHT = 1000
WINDOW_WIDTH = 800


class ReportTable(QTableWidget):
    """Custom table widget for displaying information.

    Args:
        rows (int): The number of rows for the table.

        cols (int): The number of columns for the table.

        title (str): The name of the table.

        parent (obj): The parent widget.

    Attrs:
        rows (int): The number of rows for the table.

        cols (int): The number of columns for the table.

        title (str): The name of the table.

        parent (obj): The parent widget.

        header (obj): The header row that contains column names.
    """

    def __init__(self, rows, cols, title, parent=None):
        super().__init__(rows, cols, parent)
        self.title = title
        self.set_up_widget()
        logger.info(self.title)

    def set_up_widget(self):
        self.setWindowIcon(QtGui.QIcon(GAVEL_PATH))
        self.setWindowTitle(self.title)
        self.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.header = self.horizontalHeader()
        self.header.setStretchLastSection(True)
        self.header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.setSortingEnabled(False)
        self.setAlternatingRowColors(True)
        self.resize(TABLE_HEIGHT, TABLE_WIDTH)


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
        self.setWindowIcon(QtGui.QIcon(GAVEL_PATH))


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
        self.clipboard = QtGui.QGuiApplication.clipboard()
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
        self.resize(WINDOW_HEIGHT, WINDOW_WIDTH)

    def add_table(self, rows: int, cols: int, report_name: str, parent: object) -> ReportTable:
        table = ReportTable(rows, cols, report_name, parent)
        self.layout.addWidget(table, 0, 0, 1, 3)
        return table

    def handle_copy(self):
        try:
            selected = self.get_selected_text()
        except IndexError as error:
            RequiredBox('You must select text to be copied before pressing the Copy button.').exec()
            return None
        copied_text = ''
        for row in range(selected.start_row, selected.end_row):
            for col in range(selected.start_col, selected.end_col):
                try:
                    text = str(self.table.item(row, col).text())
                except AttributeError:
                    text = ''
                copied_text = f'{copied_text} {text}\t'
            copied_text = copied_text[:-1]  # Removes last tab
            copied_text = f'{copied_text}\n'
        logger.info(copied_text)
        self.clipboard.setText(copied_text)

    def get_selected_text(self) -> namedtuple:
        """Returns row and column ranges for selected text in a namedtuple."""
        selected = self.table.selectedRanges()
        start_row = selected[0].topRow()
        end_row = selected[0].bottomRow() + 1
        start_col = selected[0].leftColumn()
        end_col = selected[0].rightColumn() + 1
        Selection = namedtuple('Selection', 'start_row end_row start_col end_col')
        return Selection(start_row, end_row, start_col, end_col)

    def handle_print(self):
        printer = QtPrintSupport.QPrinter()
        dialog = QtPrintSupport.QPrintDialog(printer)
        if dialog.exec() == 1:
            self.handle_paint_request(dialog.printer())

    def handle_preview(self):
        dialog = QtPrintSupport.QPrintPreviewDialog()
        dialog.setWindowIcon(QtGui.QIcon(GAVEL_PATH))
        dialog.resize(WINDOW_HEIGHT, WINDOW_WIDTH)
        dialog.paintRequested.connect(self.handle_paint_request)
        dialog.exec()

    def handle_paint_request(self, printer):
        document = QtGui.QTextDocument()
        cursor = QtGui.QTextCursor(document)
        h1_style = '{text-align: center; font-family: "Palatino Linotype", Palatino, serif;}'
        cursor.insertHtml(
            f"""
            <style>h1 {h1_style}</style>
            <h1>DELAWARE MUNICIPAL COURT</h1>
            <br><h3>{self.report_name}</h3><hr>
            """,
        )
        if self.table.rowCount() > 0:
            table = cursor.insertTable(self.table.rowCount(), self.table.columnCount())
            for row in range(table.rows()):
                for col in range(table.columns()):
                    cursor.insertText(self.table.item(row, col).text())
                    cursor.movePosition(QtGui.QTextCursor.MoveOperation.NextCell)
        document.print(printer)
