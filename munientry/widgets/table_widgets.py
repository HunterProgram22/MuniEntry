"""Module containing custom Table Widgets.

If using QtDesigner for creation of the Ui file you must promote the widget to one of the custom
widgets that is used. The header file for this module must then be added in QtDesigner so that
when the file is converted using 'pyuic6 -o {python_view_file.py} {qt_ui_file.ui}' this
module will be imported as part of the python_view_file.py.
"""
from PyQt6 import QtGui, QtPrintSupport
from PyQt6.QtWidgets import QWidget, QTableWidget, QAbstractScrollArea, QSizePolicy, QHeaderView, QPushButton, QGridLayout, QDialog
from loguru import logger
from munientry.paths import ICON_PATH


class ReportWindow(QWidget):
    def __init__(self, rows, cols, report_name):
        QWidget.__init__(self)
        self.report_name = report_name
        self.setWindowTitle(self.tr(self.report_name))
        self.setWindowIcon(QtGui.QIcon(ICON_PATH + 'gavel.ico'))
        self.table = ReportTable(rows, cols, self.report_name, self)
        self.buttonPrint = QPushButton('Print', self)
        self.buttonPrint.clicked.connect(self.handlePrint)
        self.buttonPreview = QPushButton('Preview', self)
        self.buttonPreview.clicked.connect(self.handlePreview)
        layout = QGridLayout(self)
        layout.addWidget(self.table, 0, 0, 1, 2)
        layout.addWidget(self.buttonPrint, 1, 0)
        layout.addWidget(self.buttonPreview, 1, 1)
        self.resize(1000, 800)

    def handlePrint(self):
        printer = QtPrintSupport.QPrinter()
        dialog = QtPrintSupport.QPrintDialog(printer)
        if dialog.exec() == 1:
            self.handlePaintRequest(dialog.printer())

    def handlePreview(self):
        dialog = QtPrintSupport.QPrintPreviewDialog()
        dialog.setWindowIcon(QtGui.QIcon(ICON_PATH + 'gavel.ico'))
        dialog.resize(1000, 800)
        dialog.paintRequested.connect(self.handlePaintRequest)
        dialog.exec()

    def handlePaintRequest(self, printer):
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


class ReportTable(QTableWidget):
    def __init__(self, rows, cols, title, parent=None):
        super(QTableWidget, self).__init__(rows, cols, parent)
        self.title = title
        self.set_up_widget()
        logger.info(self.title)

    def set_up_widget(self):
        self.setWindowIcon(QtGui.QIcon(ICON_PATH + 'gavel.ico'))
        self.setWindowTitle(self.title)
        self.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        header = self.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.setSortingEnabled(False)
        self.setAlternatingRowColors(True)
        self.resize(1000, 800)
